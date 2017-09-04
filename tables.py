import MySQLdb


conn = MySQLdb.connect("ipaddress_of_database","user","password" )
c = conn.cursor()
d=c.execute("CREATE DATABASE linux_traffic_shaping")
d=c.execute("USE linux_traffic_shaping")
d=c.execute("CREATE TABLE ipkeys (sno INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, keyval VARCHAR(10) NOT NULL )")
d=c.execute("CREATE TABLE hislog (sno INT(225) NOT NULL AUTO_INCREMENT PRIMARY KEY, shaper VARCHAR(225) NOT NULL, interfaces VARCHAR(225) NOT NULL, action VARCHAR(225) NOT NULL, IPadd VARCHAR(225) NOT NULL, tim TIMESTAMP DEFAULT CURRENT_TIMESTAMP )")
d= c.execute("insert into ipkeys (keyval) values (11), (22)")

