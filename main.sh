#!/bin/bash
docker start 4biz_python_selenium
sleep 60
iconv -f iso-8859-1 -t utf-8 $(ls -trh python_selenium/*.csv|grep -v upload|tail -1) | egrep "Em Anda|Suspensa|Reaberto" | tr -d '"' > python_selenium/upload.csv
docker exec -i 4biz_db mysql -uroot -padmin chamados < load.sql
