DROP DATABASE IF EXISTS co227db3;
CREATE DATABASE co227db3;
USE co227db3;

CREATE TABLE `Department` (
  `Department_id` int,
  `Department_name` char(50),
  `Department_head_id` int,
  `Email_Address` char(50),
  `Telephone_number` char(15),
  PRIMARY KEY (`Department_id`)
);

CREATE TABLE `lecturer` (
  `Id` int,
  `Department_id` int REFERENCES Department(Department_id),
  `Name` char(50),
  `Title` char(10),
  `Email_address` char(50),
  `Telephone_number` char(15),
  `channel_id` char(100),
  PRIMARY KEY (`Id`)
);

CREATE TABLE `Phase` (
  `Phase_code` int,
  `Course_code` char(5) REFERENCES Paper(Course_id),
  `due_date` datetime,
  PRIMARY KEY (`Phase_code`,`Course_code`)
);

CREATE TABLE `Examination` (
  `Examination_id` int,
  `Examination_name` char(50),
  PRIMARY KEY (`Examination_id`)
);

CREATE TABLE `Paper` (
  `Course_code` char(5),
  `Examination_id` int REFERENCES Examination(Examination_id),
  `Coordinator_id` int REFERENCES lecturer(Id),
  `Sub_coordinator_id` int REFERENCES lecturer(Id),
  `Moderator_id` int REFERENCES lecturer(Id),
  `Sub_moderator_id` int REFERENCES lecturer(Id),
  PRIMARY KEY (`Course_code`,`Examination_id`)
);

INSERT INTO DEPARTMENT(Department_id,Department_name,Department_head_id,Email_Address,Telephone_number) VALUES(1,'Computer Engineering Department',1,'ce@eng.pdn.ac.lk','+94xxxxxxxxx');             
-- change the email address in here --

INSERT INTO LECTURER(Id,Department_id,Name,Title,Email_address,Telephone_number,channel_id) VALUES (1,1,'Kamalanath Samarakoon','Dr','sanjayagihandesilva@gmail.com','+94xxxxxxxxx','xxxxxxxxxxxxxxxxxx');
INSERT INTO LECTURER(Id,Department_id,Name,Title,Email_address,Telephone_number,channel_id) VALUES (2,1,'Sithumini Ekanayake','Dr','sanjayagihandesilva@gmail.com','+94xxxxxxxxx','xxxxxxxxxxxxxxxxxx');
INSERT INTO LECTURER(Id,Department_id,Name,Title,Email_address,Telephone_number,channel_id) VALUES (3,1,'Swarnalatha Radhakrishnan','Dr','sanjayagihandesilva@gmail.com','+94xxxxxxxxx','xxxxxxxxxxxxxxxxxx');
INSERT INTO LECTURER(Id,Department_id,Name,Title,Email_address,Telephone_number,channel_id) VALUES (4,1,'Manjula Sandirigama','Dr','sanjayagihandesilva@gmail.com','+94xxxxxxxxx','xxxxxxxxxxxxxxxxxx');

