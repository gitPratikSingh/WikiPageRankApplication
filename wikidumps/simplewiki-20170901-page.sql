--
-- Table structure for table `page`
--

DROP TABLE IF EXISTS `page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `page` (
  `page_id` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `page_namespace` int(11) NOT NULL DEFAULT '0',
  `page_title` varbinary(255) NOT NULL DEFAULT '',
  `page_restrictions` tinyblob NOT NULL,
  `page_counter` bigint(20) unsigned NOT NULL DEFAULT '0',
  `page_is_redirect` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `page_is_new` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `page_random` double unsigned NOT NULL DEFAULT '0',
  `page_touched` varbinary(14) NOT NULL DEFAULT '',
  `page_links_updated` varbinary(14) DEFAULT NULL,
  `page_latest` int(8) unsigned NOT NULL DEFAULT '0',
  `page_len` int(8) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`page_id`),
  UNIQUE KEY `name_title` (`page_namespace`,`page_title`),
  KEY `page_random` (`page_random`),
  KEY `page_len` (`page_len`),
  KEY `page_redirect_namespace_len` (`page_is_redirect`,`page_namespace`,`page_len`)
) ENGINE=InnoDB AUTO_INCREMENT=41532769 DEFAULT CHARSET=binary;
/*!40101 SET character_set_client = @saved_cs_client */;


INSERT INTO `page` VALUES (10,0,'AccessibleComputing','',0,1,0,0.33167112649574004,'20131223211334',NULL,381202555,57),(12,0,'Anarchism','',5252,0,0,0.786172332974311,'20140102071601',NULL,588758487,173521),(13,0,'AfghanistanHistory','',5,1,0,0.0621502865684687,'20140101120449',NULL,74466652,57),(14,0,'AfghanistanGeography','',0,1,0,0.952234464653055,'20140101143540',NULL,407008307,59),(15,0,'AfghanistanPeople','',4,1,0,0.574721494293512,'20140101073926',NULL,135089040,60),(18,0,'AfghanistanCommunications','',8,1,0,0.7510681513241201,'20131219163648',NULL,74466499,64),(19,0,'AfghanistanTransportations','',2,1,0,0.674272520164282,'20140101210650',NULL,409266982,79),(20,0,'AfghanistanMilitary','',7,1,0,0.118158177582694,'20131218234416',NULL,558328133,54),(21,0,'AfghanistanTransnationalIssues','',2,1,0,0.567973358154272,'20140101163532',NULL,46448859,67),(23,0,'AssistiveTechnology','',0,1,0,0.72304140005544,'20131127140227',NULL,74466798,55), ... ;
