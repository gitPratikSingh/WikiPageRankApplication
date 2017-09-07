--
-- Table structure for table `pagelinks`
--

DROP TABLE IF EXISTS `pagelinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagelinks` (
  `pl_from` int(8) unsigned NOT NULL DEFAULT '0',
  `pl_namespace` int(11) NOT NULL DEFAULT '0',
  `pl_title` varbinary(255) NOT NULL DEFAULT '',
  UNIQUE KEY `pl_from` (`pl_from`,`pl_namespace`,`pl_title`),
  KEY `pl_namespace` (`pl_namespace`,`pl_title`,`pl_from`)
) ENGINE=InnoDB DEFAULT CHARSET=binary;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagelinks`
--

/*!40000 ALTER TABLE `pagelinks` DISABLE KEYS */;
INSERT INTO `pagelinks` VALUES (10,0,'Computer_accessibility'),(12,0,'-ism'),(12,0,'1848_Revolution'),(12,0,'1917_October_Revolution'),(12,0,'1919_United_States_anarchist_bombings'),(12,0,'19th_century_philosophy'),(12,0,'6_February_1934_crisis'),(12,0,'A._K._Press'),(12,0,'A._S._Neill'),(12,0,'AK_Press'),(12,0,'A_Greek–English_Lexicon'),(12,0,'A_Language_Older_Than_Words'),(12,0,'A_Vindication_of_Natural_Society'),(12,0,'A_las_Barricadas'),(12,0,'Abbie_Hoffman'),(12,0,'Absolute_idealism'),(12,0,'Abstentionism'),(12,0,'Action_theory_(philosophy)'),(12,0,'Adam_Smith'),(12,0,'Adolf_Brand'),(12,0,'Adolf_Hitler'),(12,0,'Adolphe_Thiers'),(12,0,'Aesthetic_emotions'),(12,0,'Aesthetics'),(12,0,'Affinity_group'),(12,0,'Affinity_groups'),(12,0,'African_philosophy'),(12,0,'Against_Civilization:_Readings_and_Reflections'),(12,0,'Against_His-Story,_Against_Leviathan'),(12,0,'Age_of_Enlightenment'),(12,0,'Agriculturalism'),(12,0,'Agriculture'),(12,0,'Al-Ghazali'),(12,0,'Alain_Badiou'),(12,0,'Alain_de_Benoist'), ... ;
