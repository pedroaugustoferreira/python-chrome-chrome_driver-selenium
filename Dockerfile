# Usa uma imagem base do python
FROM python
# Instala algumas dependencias necessárias
RUN apt-get update &&\
      apt-get -y install wget gnupg2 unzip vim
# ADD Google Chrome Repo
RUN wget https://dl.google.com/linux/linux_signing_key.pub &&\
      apt-key add linux_signing_key.pub &&\
      echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list
# Install Chrome
RUN apt-get update &&\
      apt install -y google-chrome-stable
# Install chrome driver
RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip &&\
      unzip chromedriver_linux64.zip &&\
      cp chromedriver /usr/sbin/
# Install Selenium and Behave
RUN pip install selenium configparser
CMD [ "python3", "/app/main.py" ]
