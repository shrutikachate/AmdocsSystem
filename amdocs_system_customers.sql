-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: amdocs_system
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `Account_Number` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Mobile_Number` bigint NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Adhaar_Card` bigint NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Account_Type` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Pan_Card` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Account_Number`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `Adhaar_Card` (`Adhaar_Card`),
  CONSTRAINT `customers_chk_1` CHECK ((`Account_Type` in (_utf8mb4'Current Account',_utf8mb4'Saving Account')))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Himal',9908087271,'himal@gmail.com',345543456654,'Hyderabad','Saving Account','ji','2021-08-06','jkui8765tg'),(3,'Harshini',9390576820,'harshini@gmail.com',454378654389,'Bidar','Current account','ohhmy','2012-08-16','hgy67895tf'),(4,'Yogesh',8786905467,'yogesh@gmail.com',786890987654,'Raichur','Current account','yogi','2023-01-04','hyu765thju'),(5,'Kruthika',8088642253,'kruthika@gmail.com',667588907765,'Tumkur','Saving Account','kruthi','2015-08-13','jji78yy567'),(6,'Ritu',7788889075,'ritu@gmail.com',223333556776,'Gulbarga','Current account','risti','1994-02-18','cvb112nnma'),(7,'koushik',9988754345,'koushik@gmail.com',778866554433,'Kalburgi','Saving Account','koushi','2005-12-01','bhg54rf3d2'),(8,'Parikshith',7655679900,'parikshith@gmail.com',445566778899,'Chennai','Current account','pari','1986-11-04','9900ppoo88'),(9,'preethi',8989767654,'preethi@gmail.com',656543432121,'pune','Current account','pri','2023-08-08','jhuy6543rf');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dummy`@`%`*/ /*!50003 TRIGGER `pan_card` BEFORE INSERT ON `customers` FOR EACH ROW IF length (new.Pan_Card) <> 10 THEN

SIGNAL SQLSTATE '45000'

SET MESSAGE_TEXT ="PLEASE ENTER A VALID PAN CARD NUMBER";

END IF */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-30  9:35:54
