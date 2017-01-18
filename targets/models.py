from __future__ import unicode_literals

from django.db import models


class Counter(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)
    value = models.IntegerField(default=1)
