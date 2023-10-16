-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: Movie_Database
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Actor`
--

DROP TABLE IF EXISTS `Actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor` (
  `Actor_ID` smallint NOT NULL,
  `ActorName` varchar(20) DEFAULT NULL,
  `BirthDate` date DEFAULT NULL,
  `Height_Inches` tinyint DEFAULT NULL,
  PRIMARY KEY (`Actor_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor`
--

LOCK TABLES `Actor` WRITE;
/*!40000 ALTER TABLE `Actor` DISABLE KEYS */;
INSERT INTO `Actor` VALUES (10101,'Jake Johnson','1978-05-28',70),(10102,'Hailee Steinfeld','1996-12-11',68),(10103,'Tom Cruise','1962-07-03',67),(10104,'Miles Teller','1987-02-20',73),(10105,'Kevin Hart','1979-07-06',62),(10106,'Bryan Cranston','1956-03-07',71);
/*!40000 ALTER TABLE `Actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Favorite_Role`
--

DROP TABLE IF EXISTS `Favorite_Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Favorite_Role` (
  `Actor_ID` smallint NOT NULL,
  `RoleNumber` tinyint NOT NULL,
  `Role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Actor_ID`,`RoleNumber`),
  CONSTRAINT `Favorite_Role_ibfk_1` FOREIGN KEY (`Actor_ID`) REFERENCES `Actor` (`Actor_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Favorite_Role`
--

LOCK TABLES `Favorite_Role` WRITE;
/*!40000 ALTER TABLE `Favorite_Role` DISABLE KEYS */;
INSERT INTO `Favorite_Role` VALUES (10101,1,'Nick Miller'),(10101,2,'Randy Cilliano'),(10102,1,'Gwen Stacy'),(10102,2,'Mattie'),(10103,1,'Pete Mitchell'),(10104,1,'Bradley Bradshaw'),(10104,2,'Andrew'),(10105,1,'Franklin Finbar'),(10106,1,'Walter White'),(10106,2,'Hal');
/*!40000 ALTER TABLE `Favorite_Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie`
--

DROP TABLE IF EXISTS `Movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie` (
  `Movie_ID` smallint NOT NULL,
  `MoveTitle` varchar(20) DEFAULT NULL,
  `Genre` varchar(20) DEFAULT NULL,
  `Runtime` smallint DEFAULT NULL,
  `ReleaseDate` date DEFAULT NULL,
  `Rating` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie`
--

LOCK TABLES `Movie` WRITE;
/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
INSERT INTO `Movie` VALUES (20101,'The Upside','Drama/Comedy',125,'2019-01-19','PG-13'),(20102,'Into The Spiderverse','Action/Adventure',116,'2018-12-14','PG'),(20103,'Top Gun Maverick','Action/Adventure',131,'2022-05-27','PG-13');
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie_Actor`
--

DROP TABLE IF EXISTS `Movie_Actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie_Actor` (
  `Movie_ID` smallint NOT NULL,
  `Actor_ID` smallint NOT NULL,
  PRIMARY KEY (`Movie_ID`,`Actor_ID`),
  KEY `Actor_ID` (`Actor_ID`),
  CONSTRAINT `Movie_Actor_ibfk_1` FOREIGN KEY (`Actor_ID`) REFERENCES `Actor` (`Actor_ID`),
  CONSTRAINT `Movie_Actor_ibfk_2` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie_Actor`
--

LOCK TABLES `Movie_Actor` WRITE;
/*!40000 ALTER TABLE `Movie_Actor` DISABLE KEYS */;
INSERT INTO `Movie_Actor` VALUES (20103,10101),(20103,10102),(20102,10103),(20102,10104),(20101,10105),(20101,10106);
/*!40000 ALTER TABLE `Movie_Actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Showing`
--

DROP TABLE IF EXISTS `Showing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Showing` (
  `Theater_ID` smallint NOT NULL,
  `TheaterRoom` char(2) NOT NULL,
  `ShowingDate_Time` datetime NOT NULL,
  `NumberSeats` tinyint DEFAULT NULL,
  `Movie_ID` smallint DEFAULT NULL,
  PRIMARY KEY (`Theater_ID`,`TheaterRoom`,`ShowingDate_Time`),
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `Showing_ibfk_1` FOREIGN KEY (`Theater_ID`) REFERENCES `Theater` (`Theater_ID`),
  CONSTRAINT `Showing_ibfk_2` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Showing`
--

LOCK TABLES `Showing` WRITE;
/*!40000 ALTER TABLE `Showing` DISABLE KEYS */;
INSERT INTO `Showing` VALUES (30101,'A1','2022-10-04 13:00:00',24,20101),(30101,'B1','2022-10-03 20:00:00',30,20103),(30102,'C1','2023-10-05 23:00:00',40,20101),(30102,'C2','2022-10-04 19:00:00',60,20102),(30103,'A1','2023-10-03 14:00:00',20,20103);
/*!40000 ALTER TABLE `Showing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Snack_Option`
--

DROP TABLE IF EXISTS `Snack_Option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Snack_Option` (
  `Theater_ID` smallint NOT NULL,
  `SnackNumber` tinyint NOT NULL,
  `Snack` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Theater_ID`,`SnackNumber`),
  CONSTRAINT `Snack_Option_ibfk_1` FOREIGN KEY (`Theater_ID`) REFERENCES `Theater` (`Theater_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Snack_Option`
--

LOCK TABLES `Snack_Option` WRITE;
/*!40000 ALTER TABLE `Snack_Option` DISABLE KEYS */;
INSERT INTO `Snack_Option` VALUES (30101,1,'Skittles'),(30101,2,'Popcorn'),(30101,3,'Lemon Heads'),(30102,1,'Popcorn'),(30102,2,'Licorice'),(30102,3,'Cotton Candy'),(30103,1,'Popcorn'),(30103,2,'Cheetos');
/*!40000 ALTER TABLE `Snack_Option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Theater`
--

DROP TABLE IF EXISTS `Theater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Theater` (
  `Theater_ID` smallint NOT NULL,
  `TheaterName` varchar(25) DEFAULT NULL,
  `OperatingHours` varchar(40) DEFAULT NULL,
  `Location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Theater_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Theater`
--

LOCK TABLES `Theater` WRITE;
/*!40000 ALTER TABLE `Theater` DISABLE KEYS */;
INSERT INTO `Theater` VALUES (30101,'Roxy','12:00 am - 11:30 pm','1258 Show Lane'),(30102,'AMC','11:00 am - 1:00 am','2548 First Street'),(30103,'Big Theater','1:00 pm - 10:00 pm','126 Broadway');
/*!40000 ALTER TABLE `Theater` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 16:23:39
