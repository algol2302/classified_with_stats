from infi.clickhouse_orm import (
    Model, DateTimeField, UInt32Field, Memory, F, UUIDField
)


class Clicks(Model):
    advert_id = UInt32Field()
    advert_owner_id = UUIDField()
    advert_city_id = UInt32Field()
    visitor_id = UUIDField()
    created_at = DateTimeField(default=F.now())

    engine = Memory()
