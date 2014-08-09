create database golang_mysql_demo;
use golang_mysql_demo;
drop table userinfo;
create table userinfo (
    uid int(10) NOT NULL AUTO_INCREMENT,
    username varchar(64) NULL DEFAULT NULL,
    departname varchar(64) NULL DEFAULT NULL,
    created DATE NULL DEFAULT NULL,
    primary key (uid)
);

drop table userdetail;
create table userdetail (
    uid int(10) NOT NULL DEFAULT 0,
    intro text NULL,
    profile text NULL,
    primary key (uid)
)
