CREATE DATABASE PROJECT; 
USE PROJECT;

CREATE TABLE TEACHER (
    NO INT(2) PRIMARY KEY,             
    NAME VARCHAR(40),               
    AGE INT(2),                        
    DEPARTMENT VARCHAR(15),         
    DATEOFJOIN DATE,                
    SALARY INT(6),          
    GENDER CHAR(1)                  
);

INSERT INTO TEACHER VALUES
(1, 'ROHIT', 34, 'COMPUTER', '2018-10-01', 12000, 'M'),
(2, 'SHARMILA', 31, 'HISTORY', '2012-03-25', 10000, 'F'),
(3, 'SANDEEP', 32, 'MATHS', '2011-06-08', 30000, 'M'),
(4, 'SANGEETA', 35, 'HISTORY', '2011-11-23', 10000, 'F'),
(5, 'RAKESH', 42, 'MATHS', '2017-09-12', 15000, 'M'),
(6, 'SHYAMA', 50, 'HISTORY', '2009-06-12', NULL, 'M'),
(7, 'SHIV', 44, 'COMPUTER', '2015-09-18', 21000, 'M'),
(8, 'SADHVI', 33, 'MATHS', '2015-11-21', 20000, 'F');

SELECT NAME FROM TEACHER WHERE GENDER = 'F' AND DEPARTMENT = 'MATHS';

SELECT * FROM TEACHER ORDER BY AGE;

SELECT * FROM TEACHER WHERE GENDER = 'M' AND SALARY<=12000;

SELECT DEPARTMENT, NAME FROM TEACHER WHERE DATEOFJOIN LIKE '2015%';

UPDATE TEACHER
SET SALARY = SALARY + 2000;
COMMIT;

ALTER TABLE TEACHER
ADD EmailId VARCHAR(20);
COMMIT;

DELETE FROM TEACHER WHERE DEPARTMENT = 'HISTORY';

SELECT DISTINCT DEPARTMENT FROM TEACHER;

SELECT * FROM TEACHER WHERE NAME LIKE 'SA%';

SELECT * FROM TEACHER WHERE SALARY BETWEEN 20000 AND 35000;

SELECT MAX(SALARY), MIN(SALARY) FROM TEACHER;

/*
 source C:\Users\Panav Gupta\Desktop\codes\class 12\sql\sheet.sql
Query OK, 1 row affected (0.01 sec)

Database changed
Query OK, 0 rows affected, 3 warnings (0.02 sec)

Query OK, 8 rows affected (0.00 sec)
Records: 8  Duplicates: 0  Warnings: 0

+--------+
| NAME   |
+--------+
| SADHVI |
+--------+
1 row in set (0.00 sec)

+----+----------+------+------------+------------+--------+--------+
| NO | NAME     | AGE  | DEPARTMENT | DATEOFJOIN | SALARY | GENDER |
+----+----------+------+------------+------------+--------+--------+
|  2 | SHARMILA |   31 | HISTORY    | 2012-03-25 |  10000 | F      |
|  3 | SANDEEP  |   32 | MATHS      | 2011-06-08 |  30000 | M      |
|  8 | SADHVI   |   33 | MATHS      | 2015-11-21 |  20000 | F      |
|  1 | ROHIT    |   34 | COMPUTER   | 2018-10-01 |  12000 | M      |
|  4 | SANGEETA |   35 | HISTORY    | 2011-11-23 |  10000 | F      |
|  5 | RAKESH   |   42 | MATHS      | 2017-09-12 |  15000 | M      |
|  7 | SHIV     |   44 | COMPUTER   | 2015-09-18 |  21000 | M      |
|  6 | SHYAMA   |   50 | HISTORY    | 2009-06-12 |   NULL | M      |
+----+----------+------+------------+------------+--------+--------+
8 rows in set (0.00 sec)

+----+-------+------+------------+------------+--------+--------+
| NO | NAME  | AGE  | DEPARTMENT | DATEOFJOIN | SALARY | GENDER |
+----+-------+------+------------+------------+--------+--------+
|  1 | ROHIT |   34 | COMPUTER   | 2018-10-01 |  12000 | M      |
+----+-------+------+------------+------------+--------+--------+
1 row in set (0.00 sec)

+------------+--------+
| DEPARTMENT | NAME   |
+------------+--------+
| COMPUTER   | SHIV   |
| MATHS      | SADHVI |
+------------+--------+
2 rows in set (0.00 sec)

Query OK, 7 rows affected (0.00 sec)
Rows matched: 8  Changed: 7  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 3 rows affected (0.00 sec)

+------------+
| DEPARTMENT |
+------------+
| COMPUTER   |
| MATHS      |
+------------+
2 rows in set (0.00 sec)

+----+---------+------+------------+------------+--------+--------+---------+
| NO | NAME    | AGE  | DEPARTMENT | DATEOFJOIN | SALARY | GENDER | EmailId |
+----+---------+------+------------+------------+--------+--------+---------+
|  3 | SANDEEP |   32 | MATHS      | 2011-06-08 |  32000 | M      | NULL    |
|  8 | SADHVI  |   33 | MATHS      | 2015-11-21 |  22000 | F      | NULL    |
+----+---------+------+------------+------------+--------+--------+---------+
2 rows in set (0.00 sec)

+----+---------+------+------------+------------+--------+--------+---------+
| NO | NAME    | AGE  | DEPARTMENT | DATEOFJOIN | SALARY | GENDER | EmailId |
+----+---------+------+------------+------------+--------+--------+---------+
|  3 | SANDEEP |   32 | MATHS      | 2011-06-08 |  32000 | M      | NULL    |
|  7 | SHIV    |   44 | COMPUTER   | 2015-09-18 |  23000 | M      | NULL    |
|  8 | SADHVI  |   33 | MATHS      | 2015-11-21 |  22000 | F      | NULL    |
+----+---------+------+------------+------------+--------+--------+---------+
3 rows in set (0.00 sec)

+-------------+-------------+
| MAX(SALARY) | MIN(SALARY) |
+-------------+-------------+
|       32000 |       14000 |
+-------------+-------------+
1 row in set (0.00 sec)
*/