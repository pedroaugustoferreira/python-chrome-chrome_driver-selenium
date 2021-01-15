#! /bin/bash
#id="-431237191"
id="-324783358"

cd /chamados/python-chrome-chrome_driver-selenium/python_selenium
docker run --rm --name my-running-script -v /chamados/python-chrome-chrome_driver-selenium/python_selenium:/app -w /app python-chrome-chrome_driver-selenium python screenshot.py 

cp -rp img.png /home/file_upload/img/img.${id}.png
cp -rp upload.csv /home/file_upload/img/img.${id}.csv


