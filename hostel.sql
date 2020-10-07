-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: hostel_management
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.19.04.1

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
-- Table structure for table `Application_applications`
--

DROP TABLE IF EXISTS `Application_applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Application_applications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Registration_No` longtext NOT NULL,
  `Name` longtext NOT NULL,
  `Address_For_Communication` longtext NOT NULL,
  `Permanent_Address` longtext NOT NULL,
  `Pincode` int(11) NOT NULL,
  `State` varchar(255) NOT NULL,
  `District` longtext NOT NULL,
  `Mobile_Number` varchar(255) NOT NULL,
  `Name_of_Guardian` longtext NOT NULL,
  `PhoneNumber_of_Guardian` varchar(255) NOT NULL,
  `Year_of_Study` int(11) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `Category` varchar(255) NOT NULL,
  `Sub_Category` varchar(255) DEFAULT NULL,
  `Physically_Handicapped` int(11) NOT NULL,
  `Keralite` int(11) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Course_of_study` varchar(255) NOT NULL,
  `Admission_date` date NOT NULL,
  `Course_completion_date` date NOT NULL,
  `CAT_Rank` int(11) DEFAULT NULL,
  `Prime_Ministers_program` int(11) NOT NULL,
  `Photo_upload` varchar(100) NOT NULL,
  `isvalid` tinyint(1) DEFAULT NULL,
  `category_isvalid` tinyint(1) DEFAULT NULL,
  `distance` int(11) DEFAULT NULL,
  `attendance` tinyint(1) DEFAULT NULL,
  `year_back` tinyint(1) DEFAULT NULL,
  `admitted` tinyint(1) DEFAULT NULL,
  `Hostel_admitted` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `verified_department` tinyint(1),
  `Room_No` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Application_applicat_user_id_deedece5_fk_login_ver` FOREIGN KEY (`user_id`) REFERENCES `login_verifieduser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Application_applications`
--

LOCK TABLES `Application_applications` WRITE;
/*!40000 ALTER TABLE `Application_applications` DISABLE KEYS */;
INSERT INTO `Application_applications` VALUES (51,'1','sff','dwf f gwfwefw','dwf f gwfwefw',688001,'Kerala','Alappuzha','1234567890','ffwf','1234567890',3,'Female','SC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-12','2019-06-29',3535,0,'user_39.png',1,1,64,1,0,0,NULL,39,1,'0'),(38,'2','vfdguisu','gfufgkgfiufg','gfufgkgfiufg',671315,'Kerala','Kozhikode','9946885868','khff','9946885868',4,'Female','SC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-02','2019-06-20',32354,0,'user_40.png',1,0,321,1,0,0,NULL,40,1,'0'),(39,'53','kjghdo','kfgsgfskug','kfgsgfskug',673611,'Kerala','Ernakulam','7994203745','jgdfaahkfajkg','7994203734',2,'Female','SC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-10','2019-06-21',875,0,'user_41.png',1,1,25,1,1,0,NULL,41,1,'0'),(40,'875','kjwuyfwk','kjfwkjfskjggebhvjsfhhlh','kjfwkjfskjggebhvjsfhhlh',682028,'Kerala','Kasaragod','9946885868','sgwgagew','9446568227',5,'Male','SC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-24','2019-06-28',6542,0,'user_42.png',1,1,8,1,1,0,NULL,42,1,'0'),(41,'243','usteuogfsu','jhfdfiusgfksut','jhfdfiusgfksut',682023,'Arunachal Pradesh','Tawang','9556657847','bjfhksjgds','9446568227',3,'Male','OBC','OBX (LC,Anglo India)',0,1,'Department of Applied Chemistry','M.Sc','2019-06-25','2019-06-28',24,0,'user_43.png',1,1,10,1,0,1,'Sanathana Hostel for Boys',43,1,'69'),(42,'98242','jsvgsuoiftwgb','ljlsgfwkjvgwkgfs','ljlsgfwkjvgwkgfs',673611,'Assam','Baksa','9446568228','QKFWKEFJGJ','9446568227',2,'Male','OEC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-04','2019-06-28',8754,0,'user_44.png',1,1,179,1,1,0,NULL,44,1,'0'),(43,'2543','khsfgsgjgui','bjkfwguosg','bjkfwguosg',673611,'Himachal Pradesh','Bilaspur','9446568228','amjfsjfhj','9946885868',1,'Female','GEN',NULL,1,1,'Department of Applied Chemistry','M.Sc','2019-06-03','2019-06-28',5353,0,'user_45.png',1,1,179,1,0,0,NULL,45,1,'0'),(44,'56342','jkfgsiugfskug','vsfskgiusfus','vsfskgiusfus',675234,'Daman and Diu (UT)','Daman','9946885868','sjkfskjgk','9446568227',1,'Female','ST',NULL,0,0,'Department of Applied Chemistry','M.Sc','2019-06-02','2019-06-20',2352,0,'user_46.png',1,1,25,1,1,0,NULL,46,1,'0'),(45,'43','khfgsuifj','bjfwuikfwfitwug','bjfwuikfwfitwug',684356,'Mizoram','Aizawl','9946885868','vjjgiusfgiskg','9946885868',2,'Female','OEC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-10','2019-06-20',231,1,'user_47.png',1,1,25,1,0,0,NULL,47,0,'0'),(46,'987','kutaydui','jgaqydiudg','jgaqydiudg',403004,'Goa','North Goa','9446568228','kjjfgydkugkd','9446568227',2,'Female','OBC','OBH',1,0,'Department of Applied Chemistry','M.Sc','2019-06-19','2019-06-21',635,0,'user_48.png',1,1,25,1,0,0,NULL,48,0,'0'),(47,'43675','jkukvgukug','jkuegeiu','jkuegeiu',673611,'Meghalaya','East Garo Hills','9446568228','iufiugiud','9446568227',1,'Male','OBC','MS (Muslim)',0,1,'Department of Applied Chemistry','M.Sc','2019-06-03','2019-06-29',8748,0,'user_49.png',1,1,179,1,0,0,NULL,49,1,'0'),(48,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,50,0,'0'),(49,'457','sjkcgisukcg','gfiuegfuui','gfiuegfuui',691001,'Andhra Pradesh','Anantapur','9446568228','hdugdid','9446568227',2,'Male','GEN',NULL,1,1,'Department of Applied Chemistry','M.Sc','2019-06-25','2019-06-26',4562,0,'user_51.png',1,1,25,1,0,0,NULL,51,0,'0'),(50,'432','dfgdoig','hcsfuisgi','hcsfuisgi',673611,'Assam','Baksa','9446568228','uiufgsuig','9946885868',1,'Male','OEC',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-03','2019-06-27',235,0,'user_52.png',1,1,179,1,1,0,NULL,52,1,'0'),(51,'35','sgsgw','vsgfsjgsk','vsgfsjgsk',680503,'Andhra Pradesh','Anantapur','9446568228','tyrhrhr','9946885868',2,'Male','GEN',NULL,0,1,'Department of Applied Chemistry','M.Sc','2019-06-03','2019-06-27',3543,0,'user_53.png',1,1,92,1,0,0,NULL,53,1,'0'),(52,'2424','scgsui','jsvsuvsui','jsvsuvsui',673611,'Andhra Pradesh','Guntur','9446568228','hrasrds','9446568228',4,'Male','OBC','OBH',0,1,'Department of Applied Chemistry','Ph.D','2019-06-02','2019-06-04',3633,0,'user_54.png',1,1,179,1,0,0,NULL,54,1,'0'),(53,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,55,0,'0'),(54,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,56,0,'0'),(55,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,57,0,'0'),(56,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,58,0,'0'),(57,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,59,0,'0'),(58,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,60,0,'0'),(60,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,62,0,'0'),(61,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,63,0,'0'),(62,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,64,0,'0'),(63,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-08','2019-06-08',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,65,0,'0'),(64,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-09','2019-06-09',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,66,0,'0'),(65,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-10','2019-06-10',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,67,0,'0'),(66,'','','','',0,'0','0','0','','0',0,'0','0',NULL,0,0,'0','0','2019-06-10','2019-06-10',0,0,'settings.MEDIA_ROOT/anonymous.jpg',1,1,25,1,0,0,NULL,68,0,'0');
/*!40000 ALTER TABLE `Application_applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add application settings',6,'add_applicationsettings'),(22,'Can change application settings',6,'change_applicationsettings'),(23,'Can delete application settings',6,'delete_applicationsettings'),(24,'Can view application settings',6,'view_applicationsettings'),(25,'Can add user',7,'add_verifieduser'),(26,'Can change user',7,'change_verifieduser'),(27,'Can delete user',7,'delete_verifieduser'),(28,'Can view user',7,'view_verifieduser'),(29,'Can add applications',8,'add_applications'),(30,'Can change applications',8,'change_applications'),(31,'Can delete applications',8,'delete_applications'),(32,'Can view applications',8,'view_applications');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_login_verifieduser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_login_verifieduser_id` FOREIGN KEY (`user_id`) REFERENCES `login_verifieduser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'Application','applications'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'login','applicationsettings'),(7,'login','verifieduser'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-06-04 06:48:41.187276'),(2,'contenttypes','0002_remove_content_type_name','2019-06-04 06:48:42.294575'),(3,'auth','0001_initial','2019-06-04 06:48:43.889212'),(4,'auth','0002_alter_permission_name_max_length','2019-06-04 06:48:50.043817'),(5,'auth','0003_alter_user_email_max_length','2019-06-04 06:48:50.145704'),(6,'auth','0004_alter_user_username_opts','2019-06-04 06:48:50.237672'),(7,'auth','0005_alter_user_last_login_null','2019-06-04 06:48:50.341483'),(8,'auth','0006_require_contenttypes_0002','2019-06-04 06:48:50.413355'),(9,'auth','0007_alter_validators_add_error_messages','2019-06-04 06:48:50.525849'),(10,'auth','0008_alter_user_username_max_length','2019-06-04 06:48:50.605908'),(11,'auth','0009_alter_user_last_name_max_length','2019-06-04 06:48:50.729344'),(12,'auth','0010_alter_group_name_max_length','2019-06-04 06:48:50.990318'),(13,'auth','0011_update_proxy_permissions','2019-06-04 06:48:51.086530'),(14,'login','0001_initial','2019-06-04 06:48:54.205461'),(15,'Application','0001_initial','2019-06-04 06:49:03.167683'),(16,'Application','0002_applications_user','2019-06-04 06:49:04.115502'),(17,'Application','0003_applications_verified_department','2019-06-04 06:49:07.208011'),(18,'Application','0004_auto_20190604_0626','2019-06-04 06:49:07.338703'),(19,'admin','0001_initial','2019-06-04 06:49:08.050431'),(20,'admin','0002_logentry_remove_auto_add','2019-06-04 06:49:11.771067'),(21,'admin','0003_logentry_add_action_flag_choices','2019-06-04 06:49:11.885071'),(22,'sessions','0001_initial','2019-06-04 06:49:12.513530'),(23,'Application','0005_applications_department_portal','2019-06-04 08:52:21.422375'),(24,'Application','0006_remove_applications_department_portal','2019-06-04 08:54:52.948306'),(25,'login','0002_verifieduser_department_portal','2019-06-04 08:56:17.255427'),(26,'Application','0003_applications_room_no','2019-06-06 12:22:23.512389');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bn0atek88dwhifcthatpf283ywgrsnux','ODkzNzM1YmQwZmJlNWVkMTAwM2RkMjlhODU2ZGVjZDY0MDQzOWZhYzp7fQ==','2019-06-18 07:07:54.737980'),('ckx3y8zmgb35jy6k3rfy9me2ymig1nus','OGE3ZTk1MTQ4MjBlOTk1NjkyZjBiZTY4ZGNmYTMzYWUxZDEzZWFlZTp7Il9hdXRoX3VzZXJfaWQiOiIzOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYjYxMGQyZGExM2IzMDMzYjFiMjllZDc4ZTM0OTNkZWJkZjAyMDQ2MyJ9','2019-06-24 14:13:03.108988'),('nguv5j9k88gpaq8sv956r3fhtcztfqjg','ODkzNzM1YmQwZmJlNWVkMTAwM2RkMjlhODU2ZGVjZDY0MDQzOWZhYzp7fQ==','2019-06-21 09:18:18.614180');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dump`
--

DROP TABLE IF EXISTS `dump`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dump` (
  `C1` text,
  `C2` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dump`
--

LOCK TABLES `dump` WRITE;
/*!40000 ALTER TABLE `dump` DISABLE KEYS */;
INSERT INTO `dump` VALUES ('-- MySQL dump 10.13  Distrib 5.7.26',' for Linux (x86_64)'),('/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS',' UNIQUE_CHECKS=0 */;'),('/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS',' FOREIGN_KEY_CHECKS=0 */;'),('/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE',' SQL_MODE=\'NO_AUTO_VALUE_ON_ZERO\' */;'),('/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES',' SQL_NOTES=0 */;'),('  `id` int(11) NOT NULL AUTO_INCREMENT',NULL),('  `Registration_No` longtext NOT NULL',NULL),('  `Name` longtext NOT NULL',NULL),('  `Address_For_Communication` longtext NOT NULL',NULL),('  `Permanent_Address` longtext NOT NULL',NULL),('  `Pincode` int(11) NOT NULL',NULL),('  `State` varchar(255) NOT NULL',NULL),('  `District` longtext NOT NULL',NULL),('  `Mobile_Number` varchar(255) NOT NULL',NULL),('  `Name_of_Guardian` longtext NOT NULL',NULL),('  `PhoneNumber_of_Guardian` varchar(255) NOT NULL',NULL),('  `Year_of_Study` int(11) NOT NULL',NULL),('  `Gender` varchar(255) NOT NULL',NULL),('  `Category` varchar(255) NOT NULL',NULL),('  `Sub_Category` varchar(255) DEFAULT NULL',NULL),('  `Physically_Handicapped` int(11) NOT NULL',NULL),('  `Keralite` int(11) NOT NULL',NULL),('  `Department` varchar(255) NOT NULL',NULL),('  `Course_of_study` varchar(255) NOT NULL',NULL),('  `Admission_date` date NOT NULL',NULL),('  `Course_completion_date` date NOT NULL',NULL),('  `CAT_Rank` int(11) DEFAULT NULL',NULL),('  `Prime_Ministers_program` int(11) NOT NULL',NULL),('  `Photo_upload` varchar(100) NOT NULL',NULL),('  `isvalid` tinyint(1) DEFAULT NULL',NULL),('  `distance` int(11) DEFAULT NULL',NULL),('  `attendance` tinyint(1) DEFAULT NULL',NULL),('  `year_back` tinyint(1) DEFAULT NULL',NULL),('  `admitted` tinyint(1) DEFAULT NULL',NULL),('  `Hostel_admitted` varchar(255) DEFAULT NULL',NULL),('  `user_id` int(11) NOT NULL',NULL),('  `category_isvalid` tinyint(1)',NULL),('  `verified_department` tinyint(1)',NULL),('  `Room_No` varchar(255) NOT NULL',NULL),('  PRIMARY KEY (`id`)',NULL),('  UNIQUE KEY `user_id` (`user_id`)',NULL);
/*!40000 ALTER TABLE `dump` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_applicationsettings`
--

DROP TABLE IF EXISTS `login_applicationsettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_applicationsettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active_applications` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_applicationsettings`
--

LOCK TABLES `login_applicationsettings` WRITE;
/*!40000 ALTER TABLE `login_applicationsettings` DISABLE KEYS */;
INSERT INTO `login_applicationsettings` VALUES (1,1);
/*!40000 ALTER TABLE `login_applicationsettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_verifieduser`
--

DROP TABLE IF EXISTS `login_verifieduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_verifieduser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `userhash` longtext,
  `is_active` tinyint(1) NOT NULL,
  `department_portal` longtext NOT NULL,
  `Accessible` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_verifieduser`
--

LOCK TABLES `login_verifieduser` WRITE;
/*!40000 ALTER TABLE `login_verifieduser` DISABLE KEYS */;
INSERT INTO `login_verifieduser` VALUES (39,'pbkdf2_sha256$150000$wqfnBBR77kGc$3m8R2EwWc4Ve2i+B1bAVVaNkLPY/FAp5ZYZl+t2pIyQ=','2019-06-10 14:13:02.959933',0,'aaa@gmail.com','','','',0,'2019-06-08 08:26:16.109007','gub5azq+QEYuSqgYdlR6a0QBATqD+TsFphr/p0SguEw=',1,'student',NULL),(40,'pbkdf2_sha256$150000$k3EzdPRePKMa$4U5J3MDWVBeAlIQCP2sXibmvZBX+4U0sgkJocFfS200=','2019-06-08 08:49:34.610444',0,'abc@gmail.com','','','',0,'2019-06-08 08:48:43.638011','57PokcaFwDEb8T1jnqz9NuIvsiqj3h8jOjOsQd6HNE0=',1,'student',NULL),(41,'pbkdf2_sha256$150000$oEYb1cB7BHWY$HJj/mbO7r3Y5e8RuJ65aTB4cM2l+bKxk4qUL7IJVM28=','2019-06-08 09:00:56.963088',0,'abd@gmail.com','','','',0,'2019-06-08 08:58:38.880537','/ci8wvoTThc1K3tp6plqb4M25ILHR75VtmfxubecgGM=',1,'student',NULL),(42,'pbkdf2_sha256$150000$GcULj6nRDm34$qAuHUOoGLBuCyalJnk3JelqKZr77nBtLhrupWTbsHyM=','2019-06-08 09:04:01.963027',0,'a@gmail.com','','','',0,'2019-06-08 09:03:11.072024','5xE542ACs74dcM+VtmAyyr63fy6nMeRI8D6fOe661hM=',1,'student',NULL),(43,'pbkdf2_sha256$150000$XtuDlSwEuhC7$rWXASMSfOEs0So7FByKObkKMnPejYToYfEErHGplzds=','2019-06-08 09:06:34.516632',0,'b@gmail.com','','','',0,'2019-06-08 09:06:03.719614','7PWiXrJT0/u9J8MIGVlrtwSISI5GqK6Z4fDCXBHzuLM=',1,'student',NULL),(44,'pbkdf2_sha256$150000$JNrbxmJ7TAis$x//XpC7tgSHNdKzsZ2JR/XqXfV/n1+G6b+JisQzTvD0=','2019-06-08 09:08:50.561261',0,'c@gmail.com','','','',0,'2019-06-08 09:08:21.417444','iCcv8So+3nxZh2ex0uu/8rC59FsIWvT79AR0K2j+xTI=',1,'student',NULL),(45,'pbkdf2_sha256$150000$3w5vHzUxInAz$8L+bBVcw/D+MICCns82jH0zALtx9JJLz5cxmwrhCSCg=','2019-06-08 09:11:54.517087',0,'e@gmail.com','','','',0,'2019-06-08 09:10:39.543852','abBroLVcMgTa9sGrLDFo3gLVqfJHpGs7/r2lDKv3Q1M=',1,'student',NULL),(46,'pbkdf2_sha256$150000$SKG1EZfRPhRC$y2H3zxKIT90qAanPTuYFI1jqY4GtUF4BzadJHQL0CZk=','2019-06-08 09:14:01.851886',0,'f@gmail.com','','','',0,'2019-06-08 09:13:31.797471','R/idHSFZS9J2/1/+2ALmZyimgXB05JqQrEPd1mzyrGw=',1,'student',NULL),(47,'pbkdf2_sha256$150000$VoxCeBwSO5Yf$yYOV62kFfmhMoU0lWpneHYmYgp+sddtVz+GrP41eqrg=','2019-06-08 09:16:37.503956',0,'g@gmail.com','','','',0,'2019-06-08 09:16:04.045105','0sEvNRA822UVdYSDz+vaUp1Gv0tVV9YasLcng2tGN2A=',1,'student',NULL),(48,'pbkdf2_sha256$150000$RzAAdEZv2irC$RMqR3RxuFrmMYTud84rDLqjuPdW1zlWUkoxTSVzejY8=','2019-06-08 09:19:32.270554',0,'h@gmail.com','','','',0,'2019-06-08 09:18:11.230169','8zDI2c21h1RRgkC1+b2bcBuxKKGSNnV9Ugm+oHFFk64=',1,'student',NULL),(49,'pbkdf2_sha256$150000$3vLYtNF7HuPG$+bXrZJ1kgCB94qf3fg0wZarWiurmmJL7Q+zHW32ej6g=','2019-06-08 09:27:47.392772',0,'i@gmail.com','','','',0,'2019-06-08 09:27:19.866848','dCSyxS91W2dcePkBAebrHWH2CQ6wg/wa9U7SRRYc5kI=',1,'student',NULL),(50,'pbkdf2_sha256$150000$fRVFjs9fckYC$cD5TInCCvCMciQK9/Hyuiqk5GmM/5DLna0sxUjGBYOo=',NULL,0,'j@gmail.com','','','',0,'2019-06-08 09:30:00.752846','XhjUFaQy1jbAWuKJ+VWtH9WUvE+urF0p5BYLpCZQDJ0=',1,'student',NULL),(51,'pbkdf2_sha256$150000$06zZzrlSDxmJ$rCyQb5WEOaDAIfEqPwl3FmnK0Sq4bjrpx1rW3Pu0QYs=','2019-06-10 13:46:07.508368',0,'k@gmail.com','','','',0,'2019-06-08 09:31:37.118364','6xItlBuJPqAGkXci028pRpYB5qMif86hK7w7bIipSK8=',1,'student',NULL),(52,'pbkdf2_sha256$150000$umoUtCa67bWc$XLwi1CYMMe2TXiOWoHhUDzRJqB5KpiBoK91B2/OT6DA=','2019-06-08 09:38:35.352671',0,'l@gmail.com','','','',0,'2019-06-08 09:38:07.758076','Z9BBuBj7YnNB2PxfGfzyuLMzMxceBhoNO/XkV/LjXGg=',1,'student',NULL),(53,'pbkdf2_sha256$150000$iisSya8uIhGu$FqI0r2mePAj2tedLR+N4/AN6Egbj17VrqXF0zmGVF1k=','2019-06-08 09:45:49.379500',0,'m@gmail.com','','','',0,'2019-06-08 09:45:18.479670','CpYlPKoDicAR1uzKOfzxyeDkD4T+pGPIW1xYmqhkJbk=',1,'student',NULL),(54,'pbkdf2_sha256$150000$1hehP2S1gvKA$nlXBsyM2FHYTvU1CjnlUrADxS4XqN3sZ+SShop5h7D0=','2019-06-08 09:51:33.924138',0,'n@gmail.com','','','',0,'2019-06-08 09:47:53.488240','/dcn59w+taPvGCvCmqWLda59a+op4Up6HB1gAxcOl2Y=',1,'student',NULL),(55,'pbkdf2_sha256$150000$boNu3nuWDKUh$e8QGMDBcl9+vX29b6nLjfCnPHIGlChTToW2kboaBIBs=',NULL,0,'abin','','','abin',0,'2019-06-08 10:12:54.460081',NULL,1,'Department of Applied Chemistry','M.Sc,M.Sc,'),(56,'pbkdf2_sha256$150000$TGQVQhZUjv9u$tckSgedv+xFxJDuFgwMa9DgvvMYUXuEmL6gNZa6J7gI=',NULL,0,'abi','','','abi',0,'2019-06-08 10:13:52.464938',NULL,1,'Department of Applied Economics','M.A,M.A,M.A,'),(57,'pbkdf2_sha256$150000$LGDXgAOOJ3yQ$xbr/Jwq8AeIkR347uuCQofk9cG7DZOwM5rFzpFiULu4=','2019-06-08 10:15:26.255599',0,'asdf','','','asdf',0,'2019-06-08 10:14:48.094286',NULL,1,'Department of Applied Chemistry','M.Sc,M.A,'),(58,'pbkdf2_sha256$150000$r91FJot65WcB$cm490ewCdNjJXLXJcapFUzOwGaPB77LCOuA6WkVMCw8=',NULL,0,'arnkl','','','arnkl',0,'2019-06-08 10:18:26.736593',NULL,1,'Department of Computer Applications','Ph.D,M.Phil,'),(59,'pbkdf2_sha256$150000$tAwXWrDLbS5G$I/6HQSvK11bFmadPhDyKrcMlwyIUTrtbsyOCcK3n3PY=',NULL,0,'aaa','','','aaa',0,'2019-06-08 10:42:48.233623',NULL,1,'Department of Biotechnology','Ph.D,'),(60,'pbkdf2_sha256$150000$6q79zsIY9QwH$R2kFurxSEw5oe3SWwzSUd2zNmiHk9oHKsZNs01PcpjM=','2019-06-08 10:45:22.357566',0,'asdsa','','','asdsa',0,'2019-06-08 10:45:01.115937',NULL,1,'Department of Applied Chemistry','M.Sc,'),(62,'pbkdf2_sha256$150000$Ee7yJpWhGLQQ$wYQkkBtKSNWujS3XtsbAR/shWwHIiUtMiSUtnP/zzM4=','2019-06-08 11:06:51.200380',0,'arjunmkkm','','','arjunmkkm',0,'2019-06-08 11:06:01.432168',NULL,1,'Department of Computer Applications','MCA,'),(63,'pbkdf2_sha256$150000$36mEzWcL9Pyp$cAnWXNDbak0IzapF/Cu92DeHUaBVilg71Jas4Qwa/pg=','2019-06-10 14:10:56.724919',0,'arjunmk368@gmail.com','','','',0,'2019-06-08 17:24:14.968053','Oy0RzhahvWY52Xn2WXTrdbUc2uj/PDBVvfy54csrwu4=',1,'office',NULL),(64,'pbkdf2_sha256$150000$yFyqFJeydCii$XfrUONhYGslRCvFVpD0g1Uv8mKpa6EWBhBzjNOcPPws=','2019-06-08 17:47:39.439299',0,'arjunmk','','','arjunmk',0,'2019-06-08 17:31:36.184858',NULL,1,'Department of Applied Chemistry','M.Sc,'),(65,'pbkdf2_sha256$150000$6gtvMUPKYJnB$V83XpH43tSM3S2/YLpzLfCFVdmtNaci74eqZtxvBL4o=','2019-06-10 09:30:55.563367',0,'abin1231','','','abin1231',0,'2019-06-08 17:49:46.817084',NULL,1,'Department of Applied Chemistry','M.Sc,'),(66,'pbkdf2_sha256$150000$2BFLQgmXsmol$sWqYbVxe6J+esQTFBrIzrZv3w08uAeQscKDEPBxPebE=','2019-06-09 08:43:18.848080',0,'abbb','','','abbb',0,'2019-06-09 08:42:29.138346',NULL,1,'DDU Kaushal Kendras (DDUKK)','M.Voc,'),(67,'pbkdf2_sha256$150000$42zbM427Cj7x$XG4tL2y1BRigInLoqoda4QW+tvTJRKR98v/WqiZfJIU=','2019-06-10 13:31:14.470493',0,'babu','','','babu',0,'2019-06-10 09:52:15.623218',NULL,1,'Department of Applied Chemistry','Ph.D,M.Sc,'),(68,'pbkdf2_sha256$150000$ZW8HFqljy3Qe$5eb6zqtVYl62OPbppbdfPYJEVQlmQ5WMXD+S9jj1zoU=','2019-06-10 13:45:36.107532',0,'arjunmk36@gmail.com','','','',0,'2019-06-10 13:45:02.668377','B7HK04buQ8TBV/gbg5sL05z/b2PY5rgUhfXmjmZ6DS8=',1,'student',NULL);
/*!40000 ALTER TABLE `login_verifieduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_verifieduser_groups`
--

DROP TABLE IF EXISTS `login_verifieduser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_verifieduser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `verifieduser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_verifieduser_groups_verifieduser_id_group_id_410ee1f4_uniq` (`verifieduser_id`,`group_id`),
  KEY `login_verifieduser_groups_group_id_8fde0df8_fk_auth_group_id` (`group_id`),
  CONSTRAINT `login_verifieduser_g_verifieduser_id_8eb84e10_fk_login_ver` FOREIGN KEY (`verifieduser_id`) REFERENCES `login_verifieduser` (`id`),
  CONSTRAINT `login_verifieduser_groups_group_id_8fde0df8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_verifieduser_groups`
--

LOCK TABLES `login_verifieduser_groups` WRITE;
/*!40000 ALTER TABLE `login_verifieduser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_verifieduser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_verifieduser_user_permissions`
--

DROP TABLE IF EXISTS `login_verifieduser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login_verifieduser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `verifieduser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_verifieduser_user__verifieduser_id_permissi_2059016d_uniq` (`verifieduser_id`,`permission_id`),
  KEY `login_verifieduser_u_permission_id_7167280b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `login_verifieduser_u_permission_id_7167280b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `login_verifieduser_u_verifieduser_id_3eb1e4f7_fk_login_ver` FOREIGN KEY (`verifieduser_id`) REFERENCES `login_verifieduser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_verifieduser_user_permissions`
--

LOCK TABLES `login_verifieduser_user_permissions` WRITE;
/*!40000 ALTER TABLE `login_verifieduser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `login_verifieduser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

DROP TABLE IF EXISTS `dept_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(150) NOT NULL,
  `course` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department` (`department`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-10 19:49:22
