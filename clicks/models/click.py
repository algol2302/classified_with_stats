from infi.clickhouse_orm import (
    Model, DateTimeField, UInt32Field, MergeTree, F, UUIDField,
    IPv4Field, Database
)

db = Database('default')


class Clicks(Model):
    advert_id = UInt32Field()
    advert_owner_id = UUIDField()
    advert_city_id = UInt32Field()
    visitor_id = UUIDField()
    visitor_ip = IPv4Field()
    created_at = DateTimeField(default=F.now())

    engine = MergeTree(
        date_col='created_at',
        order_by=(created_at, advert_id, visitor_ip)
    )

    @classmethod
    def create_instance(cls, **kwargs):
        db.insert([Clicks(**kwargs)])
