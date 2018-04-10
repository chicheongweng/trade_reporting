# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField(null=True)
    bio = models.TextField()
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)