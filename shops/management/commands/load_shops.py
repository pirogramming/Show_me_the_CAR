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
            for row in reader:
                shop = shop_models.Shop.objects.create(
                    name=row[0],
                    phone_number=row[1],
                    address=row[2],
                    city=row[3],
                    region=row[4],
                )
                shop.save()
