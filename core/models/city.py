# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import caches


class City(models.Model):
    name = models.TextField(verbose_name=_('Название города'))

    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')

    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        caches['city'].clear()
        super(City, self).save(*args, **kwargs)
