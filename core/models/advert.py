from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.cache import caches


from . import City


class Advert(models.Model):
    header = models.CharField(verbose_name=_('Заголовок'))

    description = models.TextField(verbose_name=_('Описание'))

    city = models.ForeignKey(
        City, verbose_name=_('Город'),
        on_delete=models.CASCADE
    )

    owner = models.ForeignKey(
        User, verbose_name=_('Владелец'),
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')

    def __str__(self):
        return "{}".format(self.header)

    def save(self, *args, **kwargs):
        caches['advert'].clear()
        super(Advert, self).save(*args, **kwargs)

    @property
    def click_count(self):
        return 0

    def clicks(self):
        return None
