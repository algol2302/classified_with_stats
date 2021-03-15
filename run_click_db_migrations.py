from infi.clickhouse_orm import Database

Database('default').migrate('clicks.migrations')
