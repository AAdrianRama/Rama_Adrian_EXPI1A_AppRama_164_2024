-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 05, 2024 at 09:05 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rama_adrian_expi1a_i164`
--

-- --------------------------------------------------------

--
-- Table structure for table `applications`
--

CREATE TABLE `applications` (
  `id_application` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `icon_url` varchar(500) NOT NULL,
  `description` text DEFAULT NULL,
  `lien_telechargement` varchar(500) NOT NULL,
  `date_upload` timestamp NULL DEFAULT current_timestamp(),
  `id_categorie` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `applications`
--

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

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id_categorie` int(11) NOT NULL,
  `nom_categorie` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id_categorie`, `nom_categorie`) VALUES
(1, 'Virtualization'),
(2, 'Programmation'),
(3, 'Gaming'),
(4, 'Productivité'),
(5, 'Communication'),
(6, 'Divertissement'),
(7, 'Art');

-- --------------------------------------------------------

--
-- Table structure for table `commentaires`
--

CREATE TABLE `commentaires` (
  `id_commentaire` int(11) NOT NULL,
  `id_utilisateur` int(11) DEFAULT NULL,
  `id_application` int(11) DEFAULT NULL,
  `commentaire` text DEFAULT NULL,
  `note` int(11) DEFAULT NULL,
  `date_commentaire` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id_role` int(11) NOT NULL,
  `nom_role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `signalements`
--

CREATE TABLE `signalements` (
  `id_signalement` int(11) NOT NULL,
  `id_utilisateur` int(11) DEFAULT NULL,
  `id_application` int(11) DEFAULT NULL,
  `soucis` text DEFAULT NULL,
  `date_signalement` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `telechargements`
--

CREATE TABLE `telechargements` (
  `id_telechargement` int(11) NOT NULL,
  `id_utilisateur` int(11) DEFAULT NULL,
  `id_application` int(11) DEFAULT NULL,
  `date_telechargement` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id_utilisateur` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `nom_utilisateur` varchar(50) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `date_enregistrement` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `utilisateursroles`
--

CREATE TABLE `utilisateursroles` (
  `id_utilisateur` int(11) NOT NULL,
  `id_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applications`
--
ALTER TABLE `applications`
  ADD PRIMARY KEY (`id_application`) USING BTREE,
  ADD KEY `fk_applications_categories` (`id_categorie`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id_categorie`) USING BTREE;

--
-- Indexes for table `commentaires`
--
ALTER TABLE `commentaires`
  ADD PRIMARY KEY (`id_commentaire`) USING BTREE,
  ADD KEY `id_utilisateur` (`id_utilisateur`),
  ADD KEY `id_application` (`id_application`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_role`) USING BTREE;

--
-- Indexes for table `signalements`
--
ALTER TABLE `signalements`
  ADD PRIMARY KEY (`id_signalement`) USING BTREE,
  ADD KEY `id_utilisateur` (`id_utilisateur`),
  ADD KEY `id_application` (`id_application`);

--
-- Indexes for table `telechargements`
--
ALTER TABLE `telechargements`
  ADD PRIMARY KEY (`id_telechargement`) USING BTREE,
  ADD KEY `id_utilisateur` (`id_utilisateur`),
  ADD KEY `id_application` (`id_application`);

--
-- Indexes for table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id_utilisateur`) USING BTREE;

--
-- Indexes for table `utilisateursroles`
--
ALTER TABLE `utilisateursroles`
  ADD PRIMARY KEY (`id_utilisateur`,`id_role`),
  ADD KEY `id_role` (`id_role`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applications`
--
ALTER TABLE `applications`
  MODIFY `id_application` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id_categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `commentaires`
--
ALTER TABLE `commentaires`
  MODIFY `id_commentaire` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id_role` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `signalements`
--
ALTER TABLE `signalements`
  MODIFY `id_signalement` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `telechargements`
--
ALTER TABLE `telechargements`
  MODIFY `id_telechargement` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  MODIFY `id_utilisateur` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `applications`
--
ALTER TABLE `applications`
  ADD CONSTRAINT `fk_applications_categories` FOREIGN KEY (`id_categorie`) REFERENCES `categories` (`id_categorie`);

--
-- Constraints for table `commentaires`
--
ALTER TABLE `commentaires`
  ADD CONSTRAINT `commentaires_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  ADD CONSTRAINT `commentaires_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`);

--
-- Constraints for table `signalements`
--
ALTER TABLE `signalements`
  ADD CONSTRAINT `signalements_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  ADD CONSTRAINT `signalements_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`);

--
-- Constraints for table `telechargements`
--
ALTER TABLE `telechargements`
  ADD CONSTRAINT `telechargements_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  ADD CONSTRAINT `telechargements_ibfk_2` FOREIGN KEY (`id_application`) REFERENCES `applications` (`id_application`);

--
-- Constraints for table `utilisateursroles`
--
ALTER TABLE `utilisateursroles`
  ADD CONSTRAINT `utilisateursroles_ibfk_1` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateurs` (`id_utilisateur`),
  ADD CONSTRAINT `utilisateursroles_ibfk_2` FOREIGN KEY (`id_role`) REFERENCES `roles` (`id_role`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
