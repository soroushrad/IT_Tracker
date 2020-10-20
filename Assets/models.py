# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import PROTECT


class Laptops(models.Model):
    class Meta:
        verbose_name = 'Laptops'
        verbose_name_plural = 'Laptops'

    id = models.CharField(verbose_name='Laptop ID', null=False, primary_key=True, max_length=30)
    model = models.CharField(verbose_name='Model', null=False, max_length=20)
    ram = models.IntegerField(verbose_name='RAM', null=True)
    SSD_512 = 1
    SSD_256 = 2
    HDD_1T = 3
    HDD_512 = 4
    HDD = (
        (SSD_512, 'SSD 512'),
        (SSD_256, 'SSD_256'),
        (HDD_1T, 'HDD_1T'),
        (HDD_512, 'HDD_512'),
    )
    HDD_status = models.IntegerField(choices=HDD, verbose_name='Hard Model')

    Win_7_32 = 1
    Win_7_64 = 2
    Win_8 = 3
    Win_10 = 4
    Win = (
        (Win_7_32, 'Windows 7 32 bit'),
        (Win_7_64, 'Windows 7 64 bit'),
        (Win_8, 'Windows 8 '),
        (Win_10, 'Windows_10'),
    )
    Win_status = models.IntegerField(choices=Win, verbose_name='Windows Status')

    Laptop_stock = 1
    Laptop_inUsed = 2
    Laptop_fixing = 3
    Laptop_overUsed = 4
    Laptop = (
        (Laptop_stock, 'لپ تاپ در انبار'),
        (Laptop_inUsed, 'لپ تاپ نزد کاربر'),
        (Laptop_fixing, 'لپ تاپ در تعمیرگاه'),
        (Laptop_overUsed, ' اسقاط شده است'),
    )
    Laptop_status = models.IntegerField(choices=Laptop, verbose_name='Laptop Status')
    Laptop_Description = models.TextField(verbose_name='Description', null=True)
    laptop_check_labled = models.BooleanField(verbose_name='Labled', default=False)

    def __str__(self):
        return "%s : %s " % (self.id, self.model)


class Personals(models.Model):
    class Meta:
        verbose_name = 'Personals'
        verbose_name_plural = 'Personals'

    id = models.CharField(verbose_name='Personal ID', max_length=30, primary_key=True)
    firstname = models.CharField(verbose_name='First name', max_length=30)
    lastname = models.CharField(verbose_name='Last name', max_length=30)
    email = models.EmailField(verbose_name='Email')
    telphone = models.IntegerField(verbose_name='Telephone')
    photo = models.ImageField(verbose_name='Images', upload_to='staff_photo/', blank=True)
    Department = models.CharField(verbose_name='Department', max_length=30, null=True, blank=True)

    def __str__(self):
        return "%s : %s %s" % (self.id, self.firstname, self.lastname)


class Owner(models.Model):
    owner_id = models.IntegerField(default=0, editable=False, primary_key=True)

    def owner_id(self):
        """
        Counts the total number of live changes of this type and saves the result to the `change_count` field.
        """
        count = self.change_set.filter(is_public=True).count()
        self.change_count = count
        self.save()

    Personal_id = models.ForeignKey(Personals, verbose_name='Personal ID', on_delete=PROTECT)
    owner_asset_1 = models.ForeignKey(Laptops, related_name='Asset1', verbose_name='Asset 1', blank=True, null=True,
                                      on_delete=PROTECT)
    owner_asset_2 = models.ForeignKey(Laptops, related_name='Asset2', verbose_name='Asset 2', blank=True, null=True,
                                      on_delete=PROTECT)
    owner_asset_3 = models.ForeignKey(Laptops, related_name='Asset3', verbose_name='Asset 3', blank=False,
                                      on_delete=PROTECT)

    def __str__(self):
        return "%s" % self.Personal_id
