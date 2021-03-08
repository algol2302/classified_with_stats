from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import caches

from . import City
from .user import CustomUser


class Advert(models.Model):
    header = models.CharField(max_length=255, blank=False)

    description = models.TextField(blank=False)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='owners'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _('Advert')
        verbose_name_plural = _('Adverts')

    def __str__(self):
        return "{}".format(self.header)

    # def save(self, *args, **kwargs):
    #     caches['advert'].clear()
    #     super(Advert, self).save(*args, **kwargs)

    @property
    def click_count(self):
        return 0

    def clicks(self):
        return None
