# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee(models.Model):

    #__Employee_FIELDS__
    firstname = models.TextField(max_length=255, null=True, blank=True)
    lastname = models.TextField(max_length=255, null=True, blank=True)
    id = models.TextField(max_length=255, null=True, blank=True)
    allocatedoffice = models.ForeignKey(Office, on_delete=models.CASCADE)
    allocationdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Office(models.Model):

    #__Office_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)
    floor = models.TextField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)

    #__Office_FIELDS__END

    class Meta:
        verbose_name        = _("Office")
        verbose_name_plural = _("Office")



#__MODELS__END
