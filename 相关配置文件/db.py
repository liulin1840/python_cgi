create table message
(
	id       INT NOT NULL AUTO_INCREMENT,
	subject  VARCHAR(100) NOT NULL,
	sender   VARCHAR(20) NOT NULL,
	reply_to INT,
	text     MEDIUMTEXT NOT NULL,
	PRIMARY  KEY(id)
	)

# 少写了个e
