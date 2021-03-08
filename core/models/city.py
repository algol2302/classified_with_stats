from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import caches


class City(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return "{}".format(self.name)
    
    # def save(self, *args, **kwargs):
    #     caches['city'].clear()
    #     super(City, self).save(*args, **kwargs)
