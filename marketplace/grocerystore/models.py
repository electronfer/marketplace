from email.policy import default
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Exito(models.Model):
    exito_code = models.CharField(max_length=20, unique=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    class TypeOfFood(models.TextChoices):
        FOOD = 'FOOD', _('FOOD')
        CLEANING = 'CLEANING', _('CLEANING')
        VEGETABLES = 'VEGETABLES', _('VEGETABLES')

    element_group = models.CharField(max_length=10, choices=TypeOfFood.choices, default=TypeOfFood.FOOD)

    product_name = models.CharField(max_length=200, null=False)
    unit_price = models.IntegerField(default=0, null=False)
    date_price_updated = models.DateTimeField(verbose_name='date published', null=False, default=datetime(2022, 10, 29, 14,42,0))

    def __str__(self):
        return 'Product number = (%s) | Product name = (%s) | Unit price = (%d)'%(self.exito_code, self.product_name, self.unit_price)

class Marketday(models.Model):
    product = models.ForeignKey(Exito, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False)
    total_purchased = models.IntegerField(default=0, null=False)
    purchase_date = models.DateTimeField(verbose_name='purchase date', null=False)