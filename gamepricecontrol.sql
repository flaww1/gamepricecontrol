-- --------------------------------------------------------
-- Anfitrião:                    127.0.0.1
-- Versão do servidor:           10.4.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versão:              11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for gamepricecontrol
CREATE DATABASE IF NOT EXISTS `gamepricecontrol` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `gamepricecontrol`;

-- Dumping structure for table gamepricecontrol.alembic_version
CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.alembic_version: ~0 rows (approximately)
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.calendar
CREATE TABLE IF NOT EXISTS `calendar` (
  `id_cal` int(11) NOT NULL AUTO_INCREMENT,
  `cal_date` date DEFAULT NULL,
  `cal_week` int(11) DEFAULT NULL,
  `cal_month` int(11) DEFAULT NULL,
  `cal_quarter` int(11) DEFAULT NULL,
  `cal_half` int(11) DEFAULT NULL,
  `cal_year` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cal`),
  KEY `ix_calendar_cal_year` (`cal_year`),
  KEY `ix_calendar_cal_week` (`cal_week`),
  KEY `ix_calendar_cal_month` (`cal_month`),
  KEY `ix_calendar_cal_quarter` (`cal_quarter`),
  KEY `ix_calendar_cal_half` (`cal_half`),
  KEY `ix_calendar_cal_date` (`cal_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.calendar: ~0 rows (approximately)
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.games
CREATE TABLE IF NOT EXISTS `games` (
  `id_game` int(11) NOT NULL AUTO_INCREMENT,
  `game_name` varchar(100) DEFAULT NULL,
  `game_image` varchar(120) DEFAULT NULL,
  `game_preview1` varchar(120) DEFAULT NULL,
  `game_preview2` varchar(120) DEFAULT NULL,
  `game_preview3` varchar(120) DEFAULT NULL,
  `game_description` varchar(200) DEFAULT NULL,
  `game_rating` int(11) DEFAULT NULL,
  `game_date` date DEFAULT NULL,
  PRIMARY KEY (`id_game`),
  KEY `ix_games_game_preview1` (`game_preview1`),
  KEY `ix_games_game_rating` (`game_rating`),
  KEY `ix_games_game_preview2` (`game_preview2`),
  KEY `ix_games_game_date` (`game_date`),
  KEY `ix_games_game_preview3` (`game_preview3`),
  KEY `ix_games_game_name` (`game_name`),
  KEY `ix_games_game_description` (`game_description`),
  KEY `ix_games_game_image` (`game_image`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.games: ~0 rows (approximately)
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
REPLACE INTO `games` (`id_game`, `game_name`, `game_image`, `game_preview1`, `game_preview2`, `game_preview3`, `game_description`, `game_rating`, `game_date`) VALUES
	(29, 'tomas', 'godofwarpreview1.jpg', 'godofwarpreview2.png', 'godofwarpreview3.png', 'godofwarpreview1.jpg', 'sdfzfghterdshg', 100, '2020-05-05');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.game_cost_calendar
CREATE TABLE IF NOT EXISTS `game_cost_calendar` (
  `id_cal` int(11) DEFAULT NULL,
  `id_gcc` int(11) DEFAULT NULL,
  KEY `id_cal` (`id_cal`),
  KEY `id_gcc` (`id_gcc`),
  CONSTRAINT `game_cost_calendar_ibfk_1` FOREIGN KEY (`id_cal`) REFERENCES `calendar` (`id_cal`),
  CONSTRAINT `game_cost_calendar_ibfk_2` FOREIGN KEY (`id_gcc`) REFERENCES `game_cost_control` (`id_gcc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.game_cost_calendar: ~0 rows (approximately)
/*!40000 ALTER TABLE `game_cost_calendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_cost_calendar` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.game_cost_control
CREATE TABLE IF NOT EXISTS `game_cost_control` (
  `id_gcc` int(11) NOT NULL AUTO_INCREMENT,
  `gcc_period` varchar(50) DEFAULT NULL,
  `gcc_date` date DEFAULT NULL,
  `id_game` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_gcc`),
  KEY `id_game` (`id_game`),
  KEY `ix_game_cost_control_gcc_date` (`gcc_date`),
  KEY `ix_game_cost_control_gcc_period` (`gcc_period`),
  CONSTRAINT `game_cost_control_ibfk_1` FOREIGN KEY (`id_game`) REFERENCES `games` (`id_game`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.game_cost_control: ~0 rows (approximately)
/*!40000 ALTER TABLE `game_cost_control` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_cost_control` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.game_genre
CREATE TABLE IF NOT EXISTS `game_genre` (
  `id_games` int(11) DEFAULT NULL,
  `id_gen` int(11) DEFAULT NULL,
  KEY `id_games` (`id_games`),
  KEY `id_gen` (`id_gen`),
  CONSTRAINT `game_genre_ibfk_1` FOREIGN KEY (`id_games`) REFERENCES `games` (`id_game`),
  CONSTRAINT `game_genre_ibfk_2` FOREIGN KEY (`id_gen`) REFERENCES `genres` (`id_gen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.game_genre: ~4 rows (approximately)
/*!40000 ALTER TABLE `game_genre` DISABLE KEYS */;
REPLACE INTO `game_genre` (`id_games`, `id_gen`) VALUES
	(29, 1),
	(29, 4),
	(29, 11),
	(29, 12);
/*!40000 ALTER TABLE `game_genre` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.game_subplatform
CREATE TABLE IF NOT EXISTS `game_subplatform` (
  `id_games` int(11) DEFAULT NULL,
  `id_subplat` int(11) DEFAULT NULL,
  KEY `id_games` (`id_games`),
  KEY `id_subplat` (`id_subplat`),
  CONSTRAINT `game_subplatform_ibfk_1` FOREIGN KEY (`id_games`) REFERENCES `games` (`id_game`),
  CONSTRAINT `game_subplatform_ibfk_2` FOREIGN KEY (`id_subplat`) REFERENCES `subplatforms` (`id_subplat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.game_subplatform: ~3 rows (approximately)
/*!40000 ALTER TABLE `game_subplatform` DISABLE KEYS */;
REPLACE INTO `game_subplatform` (`id_games`, `id_subplat`) VALUES
	(29, 1),
	(29, 10),
	(29, 13);
/*!40000 ALTER TABLE `game_subplatform` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.genres
CREATE TABLE IF NOT EXISTS `genres` (
  `id_gen` int(11) NOT NULL AUTO_INCREMENT,
  `name_gen` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_gen`),
  UNIQUE KEY `ix_genres_name_gen` (`name_gen`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.genres: ~11 rows (approximately)
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
REPLACE INTO `genres` (`id_gen`, `name_gen`) VALUES
	(3, 'Action'),
	(2, 'Adventure'),
	(1, 'Arcade'),
	(9, 'Fighting'),
	(7, 'FPS'),
	(8, 'Indie'),
	(10, 'MMO'),
	(4, 'Racing'),
	(11, 'RPG'),
	(12, 'Simulation'),
	(5, 'Sports'),
	(6, 'Strategy');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.platforms
CREATE TABLE IF NOT EXISTS `platforms` (
  `id_plat` int(11) NOT NULL AUTO_INCREMENT,
  `name_plat` varchar(40) DEFAULT NULL,
  `icon_plat` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id_plat`),
  UNIQUE KEY `ix_platforms_name_plat` (`name_plat`),
  KEY `ix_platforms_icon_plat` (`icon_plat`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.platforms: ~4 rows (approximately)
/*!40000 ALTER TABLE `platforms` DISABLE KEYS */;
REPLACE INTO `platforms` (`id_plat`, `name_plat`, `icon_plat`) VALUES
	(1, 'Playstation', NULL),
	(2, 'XBOX', NULL),
	(3, 'Nintendo', NULL),
	(4, 'PC', NULL);
/*!40000 ALTER TABLE `platforms` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.price_per_period
CREATE TABLE IF NOT EXISTS `price_per_period` (
  `price` decimal(10,0) NOT NULL,
  PRIMARY KEY (`price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.price_per_period: ~0 rows (approximately)
/*!40000 ALTER TABLE `price_per_period` DISABLE KEYS */;
/*!40000 ALTER TABLE `price_per_period` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.subplatforms
CREATE TABLE IF NOT EXISTS `subplatforms` (
  `id_subplat` int(11) NOT NULL AUTO_INCREMENT,
  `name_subplat` varchar(40) DEFAULT NULL,
  `icon_subplat` varchar(120) DEFAULT NULL,
  `id_plat` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_subplat`),
  UNIQUE KEY `ix_subplatforms_name_subplat` (`name_subplat`),
  KEY `id_plat` (`id_plat`),
  KEY `ix_subplatforms_icon_subplat` (`icon_subplat`),
  CONSTRAINT `subplatforms_ibfk_1` FOREIGN KEY (`id_plat`) REFERENCES `platforms` (`id_plat`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.subplatforms: ~17 rows (approximately)
/*!40000 ALTER TABLE `subplatforms` DISABLE KEYS */;
REPLACE INTO `subplatforms` (`id_subplat`, `name_subplat`, `icon_subplat`, `id_plat`) VALUES
	(1, 'Playstation 4', NULL, 1),
	(2, 'Playstation 3', NULL, 1),
	(3, 'PSP', NULL, 1),
	(4, 'XBOX ONE', NULL, 2),
	(5, 'XBOX 360', NULL, 2),
	(6, 'Wii', NULL, 3),
	(7, 'Nintendo DS', NULL, 3),
	(8, 'Nintendo 3DS', NULL, 3),
	(9, 'Nintendo Switch', NULL, 3),
	(10, 'Steam', NULL, 4),
	(11, 'GOG Galaxy', NULL, 4),
	(12, 'Epic Games Store', NULL, 4),
	(13, 'Origin', NULL, 4),
	(14, 'Battle.net', NULL, 4),
	(15, 'Uplay', NULL, 4),
	(16, 'Betsheda', NULL, 4),
	(17, 'XBOX Store', NULL, 4);
/*!40000 ALTER TABLE `subplatforms` ENABLE KEYS */;

-- Dumping structure for table gamepricecontrol.user
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(24) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password_hash` tinyblob NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `remember_me` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `ix_user_email` (`email`),
  UNIQUE KEY `ix_user_username` (`username`),
  CONSTRAINT `CONSTRAINT_1` CHECK (`is_admin` in (0,1)),
  CONSTRAINT `CONSTRAINT_2` CHECK (`remember_me` in (0,1))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table gamepricecontrol.user: ~0 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
REPLACE INTO `user` (`id_user`, `username`, `email`, `password_hash`, `is_admin`, `remember_me`) VALUES
	(1, 'teste1234', 'teste@gmail.com', _binary 0x243262243132246F685945542F5558344130692F6A316F553862416F7572522F74494A584D73752F756562505564536A327664437051375841564379, 1, 0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
