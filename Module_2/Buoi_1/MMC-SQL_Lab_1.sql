DROP DATABASE IF EXISTS Testing_System_Db;
CREATE DATABASE Testing_System_Db;
USE Testing_System_Db;

CREATE TABLE Department (
    DepartmentID    INT,
    DepartmentName  VARCHAR(50)
);


CREATE TABLE `Position` (
    PositionID      INT,
    PositionName    VARCHAR(50)
);

CREATE TABLE `Account` (
    AccountID       INT,
    Email           VARCHAR(50),
    Username        VARCHAR(50),
    FullName        CHAR(50),
    DepartmentID    INT,
    PositionID      INT,
    CreateDate      DATETIME
);

CREATE TABLE `Group` (
    GroupID         INT,
    GroupName       VARCHAR(50),
    CreatorID       INT,
    CreateDate      DATETIME
);

CREATE TABLE GroupAccount (
    GroupID         INT,
    AccountID       VARCHAR(50),
    JoinDate        DATE
);

CREATE TABLE TypeQuestion (
    TypeID          INT,
    TypeName        VARCHAR(50)
);

CREATE TABLE CategoryQuestion (
    CategoryID      INT,
    CategoryName    VARCHAR(50)
);

CREATE TABLE Question (
    QuestionID      INT,
    Content         VARCHAR(255),
    CategoryID      INT,
    TypeID          INT,
    CreatorID       INT,
    CreateDate      DATE
);

CREATE TABLE Answer (
    AnswerID        INT,
    Content         VARCHAR(255),
    QuestionID      INT,
    IsCorrect       BIT
);

CREATE TABLE Exam (
    ExamID          INT,
    Code            VARCHAR(50),
    Title           VARCHAR(50),
    CategoryID      INT,
    Duration        INT,
    CreatorID       INT,
    CreateDate      DATETIME
);

CREATE TABLE ExamQuestion (
    ExamID          INT,
    QuestionID      INT
);