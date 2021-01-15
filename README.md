# python-chrome-chrome_driver-selenium

```
git clone https://github.com/pedroaugustoferreira/python-chrome-chrome_driver-selenium.git
cd python-chrome-chrome_driver-selenium
docker build -t python-chrome-chrome_driver-selenium .
mkdir data
mkdir python_selenium
chmod 770 data
chmod 770 python_selenium
docker-compose -f docker-compose.yaml up -d
docker exec -i 4biz_db mysql -uroot -padmin chamados < create_table.sql
vi python_selenium/config.ini 


```
