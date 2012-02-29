# -* -coding: utf-8 -*-

from django.db import models
from home.fields import BaseDictField

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
