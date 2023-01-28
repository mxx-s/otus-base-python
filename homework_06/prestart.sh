#!/usr/bin/env sh

echo Run prestart script

flask db upgrade

echo Start init data to db

flask init_db_data