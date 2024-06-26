-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for rama_adrian_expi1a_i164
DROP DATABASE IF EXISTS `rama_adrian_expi1a_i164`;
CREATE DATABASE IF NOT EXISTS `rama_adrian_expi1a_i164` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `rama_adrian_expi1a_i164`;

-- Dumping structure for table rama_adrian_expi1a_i164.applications
DROP TABLE IF EXISTS `applications`;
CREATE TABLE IF NOT EXISTS `applications` (
  `id_application` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `icon_url` varchar(500) NOT NULL,
  `description` text,
  `lien_telechargement` varchar(500) NOT NULL,
  `date_upload` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_categorie` int DEFAULT NULL,
  PRIMARY KEY (`id_application`) USING BTREE,
  KEY `fk_applications_categories` (`id_categorie`),
  CONSTRAINT `fk_applications_categories` FOREIGN KEY (`id_categorie`) REFERENCES `categories` (`id_categorie`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.applications: ~13 rows (approximately)
INSERT INTO `applications` (`id_application`, `nom`, `icon_url`, `description`, `lien_telechargement`, `date_upload`, `id_categorie`) VALUES
	(1, 'Discord', 'https://static-00.iconduck.com/assets.00/discord-icon-2048x2048-o5mluhz2.png', 'Discord est une plateforme de VoIP et de messagerie instantanée.', 'https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64', '2024-04-23 18:50:34', 5),
	(2, 'paint.net', 'https://www.techspot.com/images2/downloads/topdownload/2014/06/paint.net.png', 'paint.net (anciennement Paint.NET) est un logiciel de retouche photo gratuit.', 'https://github.com/paintdotnet/release/releases/download/v5.0.13/paint.net.5.0.13.install.anycpu.web.zip', '2024-04-23 18:52:52', 7),
	(3, 'Office 365', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Microsoft_365_%282022%29.svg/1862px-Microsoft_365_%282022%29.svg.png', 'Microsoft 365, anciennement Office 365, est la marque désignant un abonnement à la dernière version de Microsoft Office et à un ensemble de services Cloud', 'https://c2rsetup.officeapps.live.com/c2r/download.aspx?productReleaseID=O365ProPlusRetail&platform=Def&language=fr-fr&TaxRegion=db&correlationId=c0df8d44-2cc5-4ac9-bd03-0703d5d14c1a&token=0505445d-bf0d-4afa-8c93-918be9296d39&version=O16GA&source=O15OLSO365&Br=2', '2024-04-23 18:56:13', 4),
	(4, 'Steam', 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Steam_Logo.png', 'Steam est une plateforme de distribution de contenu en ligne, de gestion des droits et de communication développée par Valve et disponible depuis le 12 septembre 2003.', 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe', '2024-04-23 18:57:42', 3),
	(5, 'Pycharm Community', 'https://static-00.iconduck.com/assets.00/pycharm-icon-2048x2048-50p1jq6b.png', 'PyCharm est un environnement de développement intégré utilisé pour programmer en Python.', 'https://www.jetbrains.com/fr-fr/pycharm/download/download-thanks.html?platform=windows&code=PCC', '2024-04-23 18:58:52', 2),
	(6, 'VS Code', 'https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_vscode_icon_130084.png', 'Visual Studio Code est un éditeur de code extensible développé par Microsoft pour Windows, Linux et macOS.', 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user', '2024-04-23 19:00:04', 2),
	(7, 'Python 3.12.3', 'https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png', 'Python est un langage de programmation interprété, multiparadigme et multiplateformes.', 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe', '2024-04-23 19:01:18', 2),
	(8, 'Apache Netbeans 21', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Apache_NetBeans_Logo.svg/888px-Apache_NetBeans_Logo.svg.png', 'NetBeans est un environnement de développement intégré, placé en open source par Sun en juin 2000 sous licence CDDL et GPLv2.', 'https://www.apache.org/dyn/closer.lua/netbeans/netbeans-installers/21/Apache-NetBeans-21-bin-windows-x64.exe', '2024-04-23 19:02:10', 2),
	(9, 'Jave JRE', 'https://static-00.iconduck.com/assets.00/java-icon-1511x2048-6ikx8301.png', 'Java est un langage de programmation de haut niveau orienté objet créé par James Gosling et Patrick Naughton, employés de Sun Microsystems, avec le soutien de Bill Joy, présenté officiellement le 23 mai 1995 au SunWorld.', 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=249851_43d62d619be4e416215729597d70b8ac', '2024-04-23 19:03:10', 4),
	(10, 'Jave JDK 22', 'https://static-00.iconduck.com/assets.00/java-icon-1511x2048-6ikx8301.png', 'Le Java Development Kit désigne un ensemble de bibliothèques logicielles de base du langage de programmation Java, ainsi que les outils avec lesquels le code Java peut être compilé, transformé en bytecode destiné à la machine virtuelle Java.', 'https://download.oracle.com/java/22/latest/jdk-22_windows-x64_bin.exe', '2024-04-23 19:03:10', 2),
	(11, 'ShareX', 'https://upload.wikimedia.org/wikipedia/commons/d/d1/ShareX_Logo.png', 'ShareX est un logiciel libre et open source de capture d\'écran pour Microsoft Windows.', 'https://github.com/ShareX/ShareX/releases/download/v16.0.1/ShareX-16.0.1-setup.exe', '2024-04-23 19:05:22', 4),
	(12, 'Laragon Full', 'https://i.pinimg.com/originals/a6/31/32/a631321da408385e13a803084482d05b.png', 'Laragon est un environnement de développement universel portable, isolé, rapide et puissant pour Windows.', 'https://github.com/leokhoa/laragon/releases/download/6.0.0/laragon-wamp.exe', '2024-04-23 19:06:17', 2),
	(13, 'Virtualbox', 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Virtualbox_logo.png', 'Oracle VM VirtualBox (anciennement VirtualBox) est un logiciel libre de virtualisation créé par la société Innotek rachetée par Sun Microsystems et aujourd\'hui publié par Oracle.', 'https://download.virtualbox.org/virtualbox/7.0.18/VirtualBox-7.0.18-162988-Win.exe', '2024-05-29 18:19:26', 1);

-- Dumping structure for table rama_adrian_expi1a_i164.categories
DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `icon_url` varchar(500) DEFAULT NULL,
  `id_categorie` int NOT NULL AUTO_INCREMENT,
  `nom_categorie` varchar(50) NOT NULL,
  PRIMARY KEY (`id_categorie`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.categories: ~7 rows (approximately)
INSERT INTO `categories` (`icon_url`, `id_categorie`, `nom_categorie`) VALUES
	('https://cdn-icons-png.flaticon.com/512/3211/3211307.png', 1, 'Virtualization'),
	('https://cdn-icons-png.flaticon.com/512/1197/1197409.png', 2, 'Programmation'),
	('https://cdn-icons-png.flaticon.com/512/3655/3655555.png', 3, 'Gaming'),
	('https://cdn-icons-png.flaticon.com/512/4149/4149648.png', 4, 'Productivité'),
	('https://cdn-icons-png.flaticon.com/512/543/543089.png', 5, 'Communication'),
	('https://cdn-icons-png.flaticon.com/512/705/705062.png', 6, 'Divertissement'),
	('https://cdn-icons-png.flaticon.com/512/2400/2400603.png', 7, 'Art');

-- Dumping structure for table rama_adrian_expi1a_i164.commentaires
DROP TABLE IF EXISTS `commentaires`;
CREATE TABLE IF NOT EXISTS `commentaires` (
  `id_commentaire` int NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int DEFAULT NULL,
  `id_application` int DEFAULT NULL,
  `commentaire` text,
  `note` int DEFAULT NULL,
  `date_commentaire` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_commentaire`) USING BTREE,
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_application` (`id_application`),
  CONSTRAINT `commentaires_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  CONSTRAINT `commentaires_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.commentaires: ~0 rows (approximately)

-- Dumping structure for table rama_adrian_expi1a_i164.roles
DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `icon_url` varchar(500) DEFAULT NULL,
  `id_role` int NOT NULL AUTO_INCREMENT,
  `nom_role` varchar(50) NOT NULL,
  PRIMARY KEY (`id_role`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.roles: ~3 rows (approximately)
INSERT INTO `roles` (`icon_url`, `id_role`, `nom_role`) VALUES
	('https://images.freeimages.com/fic/images/icons/573/must_have/256/user.png?fmt=webp&w=500', 1, 'Utilisateur'),
	('https://cdn-icons-png.flaticon.com/512/2206/2206368.png', 2, 'Admin'),
	('https://cdn-icons-png.flaticon.com/512/9028/9028075.png', 3, 'Owner');

-- Dumping structure for table rama_adrian_expi1a_i164.signalements
DROP TABLE IF EXISTS `signalements`;
CREATE TABLE IF NOT EXISTS `signalements` (
  `id_signalement` int NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int DEFAULT NULL,
  `id_application` int DEFAULT NULL,
  `soucis` text,
  `date_signalement` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_signalement`) USING BTREE,
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_application` (`id_application`),
  CONSTRAINT `signalements_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  CONSTRAINT `signalements_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.signalements: ~0 rows (approximately)

-- Dumping structure for table rama_adrian_expi1a_i164.telechargements
DROP TABLE IF EXISTS `telechargements`;
CREATE TABLE IF NOT EXISTS `telechargements` (
  `id_telechargement` int NOT NULL AUTO_INCREMENT,
  `id_utilisateur` int DEFAULT NULL,
  `id_application` int DEFAULT NULL,
  `date_telechargement` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_telechargement`) USING BTREE,
  KEY `id_utilisateur` (`id_utilisateur`),
  KEY `id_application` (`id_application`),
  CONSTRAINT `telechargements_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  CONSTRAINT `telechargements_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.telechargements: ~0 rows (approximately)

-- Dumping structure for table rama_adrian_expi1a_i164.utilisateurs
DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE IF NOT EXISTS `utilisateurs` (
  `icon_url` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  `id_role` int DEFAULT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `date_naiss` date DEFAULT NULL,
  `nom_utilisateur` varchar(50) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `date_enregistrement` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_utilisateur`) USING BTREE,
  KEY `id_role` (`id_role`),
  CONSTRAINT `FK_utilisateurs_roles` FOREIGN KEY (`id_role`) REFERENCES `roles` (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Dumping data for table rama_adrian_expi1a_i164.utilisateurs: ~4 rows (approximately)
INSERT INTO `utilisateurs` (`icon_url`, `id_utilisateur`, `id_role`, `nom`, `prenom`, `date_naiss`, `nom_utilisateur`, `mot_de_passe`, `mail`, `date_enregistrement`) VALUES
	('https://cdn-icons-png.flaticon.com/512/9028/9028075.png', 1, 3, 'Rama', 'Adrian', '2006-11-15', 'DarkVoltz', 'gogogaga69420', 'rama@blader.com', '2024-06-06 15:19:03'),
	('https://cdn-icons-png.flaticon.com/512/2206/2206368.png', 2, 2, 'Ecuyer', 'Gregory', '2003-05-09', 'Hikari', 'jaimelescrotesdenez123', 'gregory.ecuyer@eduvaud.ch', '2024-06-06 15:22:08'),
	('https://images.freeimages.com/fic/images/icons/573/must_have/256/user.png?fmt=webp&w=500', 5, 1, 'Leni', 'Vithurshan', '1997-07-18', 'Leni', 'jaimeutilisergrindr69', 'leni.moras@merckgroup.com', '2024-06-06 19:10:36'),
	('https://images.freeimages.com/fic/images/icons/573/must_have/256/user.png?fmt=webp&w=500', 6, 1, 'Matin', 'Matin', '2000-06-16', 'Matinnn', 'matinlebg', 'matin@matin.matin', '2024-06-06 21:09:21');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
