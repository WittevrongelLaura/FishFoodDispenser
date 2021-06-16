-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: FishFooddispenserDB
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Action`
--

DROP TABLE IF EXISTS `Action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Action` (
  `action_id` int(11) NOT NULL AUTO_INCREMENT,
  `action` varchar(45) NOT NULL,
  PRIMARY KEY (`action_id`),
  UNIQUE KEY `idx_action` (`action`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Action`
--

LOCK TABLES `Action` WRITE;
/*!40000 ALTER TABLE `Action` DISABLE KEYS */;
INSERT INTO `Action` VALUES (4,'green led on'),(3,'measuring content of container'),(2,'measuring waterlevel'),(1,'measuring watertemperature'),(6,'red led on'),(9,'servo at startposition'),(10,'servo in progress'),(8,'speaker off'),(7,'speaker on'),(5,'yellow led on');
/*!40000 ALTER TABLE `Action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Component`
--

DROP TABLE IF EXISTS `Component`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Component` (
  `component_id` int(11) NOT NULL AUTO_INCREMENT,
  `component_name` varchar(45) NOT NULL,
  `measuring_unit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`component_id`),
  UNIQUE KEY `idx_component_name` (`component_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Component`
--

LOCK TABLES `Component` WRITE;
/*!40000 ALTER TABLE `Component` DISABLE KEYS */;
INSERT INTO `Component` VALUES (1,'watertemperature','°C'),(2,'waterlevel','%'),(3,'containercapacity','%'),(4,'led',NULL),(5,'speaker',NULL),(6,'servo',NULL);
/*!40000 ALTER TABLE `Component` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dispenser`
--

DROP TABLE IF EXISTS `Dispenser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dispenser` (
  `measuring_id` int(11) NOT NULL AUTO_INCREMENT,
  `component_id` int(11) NOT NULL,
  `datetime` datetime DEFAULT current_timestamp(),
  `status` tinyint(4) DEFAULT 0,
  `value` varchar(45) DEFAULT NULL,
  `action_id` int(11) NOT NULL,
  PRIMARY KEY (`measuring_id`),
  KEY `fk_Dispenser_Component1_idx` (`component_id`),
  KEY `fk_Dispenser_Action1_idx` (`action_id`),
  CONSTRAINT `fk_Dispenser_Action1` FOREIGN KEY (`action_id`) REFERENCES `Action` (`action_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dispenser_Component1` FOREIGN KEY (`component_id`) REFERENCES `Component` (`component_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dispenser`
--

LOCK TABLES `Dispenser` WRITE;
/*!40000 ALTER TABLE `Dispenser` DISABLE KEYS */;
INSERT INTO `Dispenser` VALUES (1,1,'2021-06-13 15:48:34',1,'24',1),(2,2,'2021-06-13 15:48:34',1,'0',2),(3,3,'2021-06-13 15:48:34',1,'7',3),(4,1,'2021-06-13 15:49:33',1,'24',1),(5,2,'2021-06-13 15:49:33',1,'0',2),(6,3,'2021-06-13 15:49:33',1,'10',3),(7,1,'2021-06-13 15:49:40',1,'24',1),(8,2,'2021-06-13 15:49:40',1,'10',2),(9,3,'2021-06-13 15:49:40',1,'15',3),(10,1,'2021-06-13 23:20:51',1,'25',1),(11,2,'2021-06-13 23:20:51',1,'5',2),(12,3,'2021-06-13 23:20:51',1,'82',3),(13,1,'2021-06-13 23:25:44',1,'25',1),(14,2,'2021-06-13 23:25:44',1,'5',2),(15,3,'2021-06-13 23:25:44',1,'78',3),(16,1,'2021-06-13 23:30:21',1,'25',1),(17,2,'2021-06-13 23:30:21',1,'5',2),(18,3,'2021-06-13 23:30:21',1,'82',3),(19,1,'2021-06-13 23:36:20',1,'25',1),(20,2,'2021-06-13 23:36:20',1,'5',2),(21,3,'2021-06-13 23:36:20',1,'76',3),(22,1,'2021-06-14 00:20:25',1,'25',1),(23,2,'2021-06-14 00:20:25',1,'0',2),(24,3,'2021-06-14 00:20:25',1,'93',3),(25,1,'2021-06-14 00:41:41',1,'25',1),(26,2,'2021-06-14 00:41:41',1,'5',2),(27,3,'2021-06-14 00:41:41',1,'87',3),(28,1,'2021-06-14 00:41:53',1,'25',1),(29,2,'2021-06-14 00:41:53',1,'5',2),(30,3,'2021-06-14 00:41:53',1,'93',3),(31,1,'2021-06-15 16:18:46',1,'26',1),(32,2,'2021-06-15 16:18:47',1,'0',2),(33,3,'2021-06-15 16:18:47',1,'34250',3);
/*!40000 ALTER TABLE `Dispenser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Settings`
--

DROP TABLE IF EXISTS `Settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Settings` (
  `idSettings` int(11) NOT NULL AUTO_INCREMENT,
  `numOfGrams` int(11) NOT NULL,
  `feedingTime` time NOT NULL,
  `stateSpeaker` tinyint(4) NOT NULL,
  PRIMARY KEY (`idSettings`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Settings`
--

LOCK TABLES `Settings` WRITE;
/*!40000 ALTER TABLE `Settings` DISABLE KEYS */;
INSERT INTO `Settings` VALUES (1,5,'10:00:00',1);
/*!40000 ALTER TABLE `Settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-16  8:09:26
