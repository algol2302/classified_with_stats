from django.http import HttpRequest

from clicks.models import Clicks
from core.models import CustomUser, Advert


def click_handler(advert: Advert, request: HttpRequest) -> None:
    visitor_ip = request.META['REMOTE_ADDR']

    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        user = CustomUser.objects.get(email='anonymous@anonymous.an')

    # TODO it should move a click creation to message queue?
    #  What's a best practice for this?

    Clicks.create_instance(
        advert_id=advert.id, advert_owner_id=advert.owner_id,
        advert_city_id=advert.city_id, visitor_id=user.id,
        visitor_ip=visitor_ip
    )
