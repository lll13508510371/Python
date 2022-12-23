use 0115_01_15107916;
show tables;
show create table user;
CREATE TABLE `user`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(3)  DEFAULT NULL,
    `job`         varchar(20) DEFAULT NULL,
    `company`     varchar(50) DEFAULT NULL,
    `residence`   varchar(50) DEFAULT NULL,
    `blood_group` varchar(3)  DEFAULT NULL,
    `username`    varchar(20) DEFAULT NULL,
    `sex`         varchar(1)  DEFAULT NULL,
    `address`     varchar(50) DEFAULT NULL,
    `mail`        varchar(50) DEFAULT NULL,
    `birthdate`   varchar(20) DEFAULT NULL,
    `id_card`     varchar(18) DEFAULT NULL,
    `phone`       varchar(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 101
  DEFAULT CHARSET = utf8mb4;
select *
from user;

select * from user where name=%s;
select * from user where phone like '%%s%';

insert into user() values ();

insert into user(id,name,job,company,residence,blood_group,username,sex,address,mail,birthdate,id_card,phone) values ('0','正心','设备主管','精芯传媒有限公司','澳门特别行政区荆门县清浦西宁路D座 779711','A-','min34','F','吉林省惠州县和平樊路h座 406759','yang70@yahoo.com','1979-05-26','61092819490407596X',14722525948);

show create table user;  /*显示创建 user 表的 sql 语句*/
show create database python;

CREATE DATABASE `python` /*!40100 DEFAULT CHARACTER SET utf8mb4 */