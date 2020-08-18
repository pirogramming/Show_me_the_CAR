import csv
from django.core.management import BaseCommand
from shops import models as shop_models
from cars import models as car_models


class Command(BaseCommand):
    help = "Load crawled csv file into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f, dialect={"encoding": "utf-8-sig"})
            orders = list(reader)
            for row in orders:
                if len(row) == 0:
                    continue
                try:
                    shop = shop_models.Shop.objects.get(name=row[0])
                    shop.phone_number = row[1]
                    shop.address = row[2]
                    shop.city = row[3]
                    shop.region = row[4]

                    shop.save()

                except shop_models.Shop.DoesNotExist:
                    shop_models.Shop.objects.create(
                        name=row[0],
                        phone_number=row[1],
                        address=row[2],
                        city=row[3],
                        region=row[4],
                    )

            for row in orders:
                if len(row) == 0:
                    continue
                shop = shop_models.Shop.objects.get(name=row[0])
                try:
                    car = car_models.Car.objects.get(model_name=row[5], color=row[6])
                except car_models.Car.DoesNotExist:
                    car = car_models.Car.objects.create(
                        model_name=row[5], color=row[6],
                    )
                    brand, success = car_models.Brand.objects.get_or_create(name=row[7])
                    print(brand)
                    brand.cars.add(car)
                    print(car)
                car.shop.add(shop)
                car.save()
