DELETE FROM torre_unix;
LOAD DATA INFILE '/var/lib/mysql-files/upload.csv'
INTO TABLE torre_unix
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;