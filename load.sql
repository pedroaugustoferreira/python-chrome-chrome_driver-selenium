DELETE FROM torre_unix;
LOAD DATA LOCAL INFILE '/var/lib/mysql-files/upload.csv'
INTO TABLE torre_unix
FIELDS TERMINATED BY ';'
