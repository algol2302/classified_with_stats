from infi.clickhouse_orm import Database

Database('demo').migrate('clicks.migrations')
