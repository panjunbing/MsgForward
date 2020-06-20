# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Msg(models.Model):
    message = models.CharField(max_length=255)
    role = models.IntegerField()
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'msg'


class User(models.Model):
    username = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    role = models.ForeignKey(Msg, models.DO_NOTHING, db_column='role')
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'user'