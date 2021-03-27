from main.models import Offer as OfferModel
from main.models import *
from django.core.exceptions import ObjectDoesNotExist
from main.models.save_dir.base import BasePattern


class Offer:
    """Класс внутри которого находятся классы нужные для сохранения данных"""

    """Нужен для общей категории"""
    class Base:
        """ для простых данных"""
        def __init__(self, data, offer, name=''):
            self.data = data
            self.offer = offer
            self.name = name

        def save(self) -> None:
            """
            Сохранить данные
            """
            setattr(self.offer, self.name, self.data)

        def exist(self, item):
            return self.data.get(item, None)

    """Все последующие классы для сложных данных"""
    class Price(Base):
        def save(self) -> None:
            Price.objects.update_or_create(
                offer=self.offer,
                defaults={
                    "value": self.exist("value"),
                    "vat": self.exist('vat'),
                    "discountBase": self.exist('discountBase')
                }
            )

    class Barcodes(Base):
        def save(self) -> None:
            for item in self.data:
                Barcode.objects.update_or_create(offer=self.offer, barcode=item)

    class Urls(Base):
        def save(self) -> None:
            for item in self.data:
                Url.objects.update_or_create(offer=self.offer, url=item)

    class ManufacturerCountries(Base):
        def save(self) -> None:
            for item in self.data:
                ManufacturerCountry.objects.update_or_create(offer=self.offer, name=item)

    class WeightDimensions(Base):
        def save(self) -> None:
            WeightDimension.objects.update_or_create(
                offer=self.offer,
                length=float(self.data['length']),
                width=float(self.data['width']),
                height=float(self.data['height']),
                weight=float(self.data['weight'])
            )

    class SupplyScheduleDays(Base):
        def save(self) -> None:
            SupplyScheduleDays.objects.update_or_create(offer=self.offer, supplyScheduleDay=self.data)

    class ProcessingState(Base):
        def save(self) -> None:
            ProcessingState.objects.update_or_create(offer=self.offer, status=self.data['status'])

    class Mapping(Base):
        def save(self) -> None:
            Mapping.objects.update_or_create(
                offer=self.offer,
                marketSku=self.data["marketSku"],
                categoryId=self.data["categoryId"],
            )

    class LifeTime(Base):
        def save(self):
            print(self.data)
            LifeTime.objects.update_or_create(
                offer=self.offer,
                timePeriod=self.exist("timePeriod"),
                timeUnit=self.exist('timeUnit'),
                comment=self.exist("comment"),
            )

    class ShelfLife(Base):
        def save(self):
            print(self.data)
            ShelfLife.objects.update_or_create(
                offer=self.offer,
                timePeriod=self.exist("timePeriod"),
                timeUnit=self.exist('timeUnit'),
                comment=self.exist("comment"),
            )

    class GuaranteePeriod(Base):
        def save(self):
            GuaranteePeriod.objects.update_or_create(
                offer=self.offer,
                timePeriod=self.exist("timePeriod"),
                timeUnit=self.exist('timeUnit'),
                comment=self.exist("comment"),
            )


class OfferPattern(BasePattern):
    """Класс сохраняющий данные offer из json в БД"""

    attrs = {
        'simple': [
            'name',
            'shopSku',
            'category',
            'vendor',
            'vendorCode',
            'description',
            'manufacturer',
            'minShipment',
            'transportUnitSize',
            'quantumOfSupply',
            'deliveryDurationDays',
            'availability',
        ],
        'diff': [
            "barcodes",
            "urls",
            "weightDimensions",
            "supplyScheduleDays",
            "processingState",
            "manufacturerCountries",
            "mapping",
            "lifeTime",
            "guaranteePeriod",
            "shelfLife"
        ]
    }

    def save(self, user) -> None:
        """Сохраняет данные в БД"""
        for item in self.json:
            try:
                offer = OfferModel.objects.get(shopSku=item['offer'].get('shopSku'), user=user)
            except ObjectDoesNotExist:
                offer = OfferModel.objects.create(user=user)
            json_offer = item['offer']
            if 'mapping' in item:
                json_offer['mapping'] = item['mapping']
            self.parse_attrs(json_offer, offer)
            offer.save()

    def parse_attrs(self, json_offer, offer) -> None:
        """Парсит данные из json на простые и сложные"""
        for key, data in json_offer.items():
            if key in self.attrs['simple']:
                Offer.Base(data=data, offer=offer, name=key).save()
            elif key in self.attrs['diff']:
                getattr(Offer, key[0].title() + key[1::])(data=data, offer=offer).save()
