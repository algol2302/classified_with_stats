from infi.clickhouse_orm import migrations
from clicks import models

operations = [
    migrations.CreateTable(models.Clicks),
]
