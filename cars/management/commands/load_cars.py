# -*- coding: utf-8 -*-
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
            reader = csv.reader(f, dialect="excel")
            for row in reader:
                try:
                    car = car_models.Car.objects.get(model_name=row[5], color=row[6])
                except car_models.Car.DoesNotExist:
                    brand = car_models.Brand.objects.get(name=row[7])
                    car = car_models.Car.objects.create(
                        model_name=row[5], color=row[6], brand=brand
                    )
                    car.save()
                try:
                    shop = shop_models.Shop.objects.get(name=row[0])
                except shop_models.Shop.DoesNotExist:
                    car.delete()
                    continue
                car.shop.add(shop)

