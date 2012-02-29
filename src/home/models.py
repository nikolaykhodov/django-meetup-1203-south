# -* -coding: utf-8 -*-

from django.db import models
from home.fields import BaseDictField
from south.modelsinspector import add_introspection_rules

class Account(models.Model):
    """
    Модель аккаунта, от которого будет размещен комментарий
    """
    pass

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    headers = BaseDictField()
    who = models.ForeignKey(Account)
    text = models.CharField(max_length=4096)

add_introspection_rules([], ["^home\.fields\.BaseDictField"])
