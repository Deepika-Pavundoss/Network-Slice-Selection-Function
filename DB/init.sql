SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nssf2`
--

-- --------------------------------------------------------

--
-- Table structure for table `amfrepo`
--
DROP DATABASE IF EXISTS nssf;
CREATE DATABASE nssf;
USE nssf;

CREATE TABLE `amfrepo` (
  `NSSAI` int(5) NOT NULL,
  `amfID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `amfrepo`
--

INSERT INTO `amfrepo` (`NSSAI`, `amfID`) VALUES
(1256, 1),
(1256, 3),
(2136, 1),
(3256, 1),
(3256, 2),
(4215, 1),
(4215, 2),
(4215, 3),
(4556, 1),
(4556, 2),
(7560, 1),
(7560, 2),
(8610, 1),
(8610, 3);

-- --------------------------------------------------------

--
-- Table structure for table `amftable`
--

CREATE TABLE `amftable` (
  `AMFId` varchar(10) NOT NULL,
  `SliceID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `amftable`
--

INSERT INTO `amftable` (`AMFId`, `SliceID`) VALUES
('AMF-1', 'S1-A'),
('AMF-2', 'S1-B'),
('AMF-3', 'S1-C'),
('AMF-3', 'S1-D'),
('AMF-1', 'S1-E'),
('AMF-1', 'S1-F'),
('AMF-2', 'S1-G'),
('AMF-3', 'S1-H'),
('AMF-2', 'S1-I'),
('AMF-2', 'S1-J'),
('AMF-3', 'S1-K'),
('AMF-2', 'S1-L'),
('AMF-1', 'S1-M'),
('AMF-2', 'S1-N'),
('AMF-1', 'S1-O'),
('AMF-1', 'S1-P'),
('AMF-1', 'S1-Q'),
('AMF-2', 'S1-R'),
('AMF-2', 'S1-S'),
('AMF-3', 'S1-T'),
('AMF-3', 'S1-U'),
('AMF-2', 'S1-V'),
('AMF-1', 'S1-W'),
('AMF-1', 'S1-X'),
('AMF-1', 'S1-Y');

-- --------------------------------------------------------

--
-- Table structure for table `slicerepo`
--

CREATE TABLE `slicerepo` (
  `NSSAI` int NOT NULL,
  `SNSSAI` int NOT NULL,
  `SST` int NOT NULL,
  `SSD` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `app` varchar(60) NOT NULL,
  `bwLower` float NOT NULL,
  `bwUpper` float NOT NULL,
  `latencyLower` float NOT NULL,
  `latencyUpper` float NOT NULL,
  `Jitter` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `slicerepo`
--

INSERT INTO `slicerepo` (`NSSAI`, `SNSSAI`, `SST`, `SSD`, `name`, `app`, `bwLower`, `bwUpper`, `latencyLower`, `latencyUpper`, `Jitter`) VALUES
(1, 1023, 1, 1, 'eMBB', 'AR Gaming', 5, 200, 10, 50, 'low'),
(6, 2136, 2, 1, 'mMTC', 'Smart City Monitoring', 0.1, 10, 50, 100, 'variable'),
(2, 3256, 1, 2, 'eMBB', 'VR Streaming', 10, 500, 10, 50, 'low'),
(1, 4215, 1, 3, 'eMBB', 'Video Conferencing', 2, 50, 50, 100, 'variable'),
(1, 4556, 3, 1, 'URLLC', 'Industrial Automation', 1, 10, 0.5, 1, 'very low'),
(6, 7560, 1, 4, 'eMBB', 'Live Streaming', 5, 200, 50, 100, 'variable'),
(2, 8610, 2, 2, 'mMTC', 'IoT Sensor', 0.01, 0.1, 500, 1000, 'variable'),
(1, 2855, 1, 5, 'eMBB', 'Fleet Management', 1, 10, 50, 100, 'low'),
(1, 5698, 1, 6, 'eMBB', 'Media Streaming', 5, 100, 50, 100, 'variable'),
(1, 4236, 3, 2, 'URLLC', 'Traffic Management', 0.1, 1, 1, 10, 'very low'),
(1, 7456, 2, 3, 'mMTC', 'Energy Grid Monitoring', 0.01, 0.1, 500, 1000, 'variable'),
(6, 7520, 2, 3, 'mMTC', 'Asset Tracking', 0.001, 0.01, 500, 1000, 'variable');

-- --------------------------------------------------------

--
-- Table structure for table `sliceresource`
--

CREATE TABLE `sliceresource` (
  `SliceID` varchar(10) NOT NULL,
  `NSSAI` int NOT NULL,
  `SNSSAI` int NOT NULL,
  `bandWidth` float NOT NULL,
  `latency` float NOT NULL,
  `Jitter` varchar(40) NOT NULL,
  `available` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sliceresource`
--

INSERT INTO `sliceresource` (`SliceID`, `NSSAI`, `SNSSAI`, `bandWidth`, `latency`, `Jitter`, `available`) VALUES
('S1-A', 1, 1023, 90, 40, 'low', 1),
('S1-H', 1, 1024, 150, 15, 'low', 1),
('S1-I', 1, 1025, 60, 35, 'low', 1),
('S1-B', 6, 2136, 5, 75, 'variable', 1),
('S1-L', 6, 2137, 9, 55, 'variable', 1),
('S1-C', 2, 3256, 300, 25, 'low', 1),
('S1-M', 2, 3257, 100, 40, 'low', 1),
('S1-D', 1, 4215, 10, 90, 'variable', 1),
('S1-N', 1, 4216, 40, 75, 'variable', 1),
('S1-E', 1, 4556, 8, 1, 'very low', 1),
('S1-O', 1, 4557, 3, 0.5, 'very low', 1),
('S1-F', 6, 7560, 130, 80, 'variable', 1),
('S1-Q', 6, 7561, 85, 70, 'variable', 1),
('S1-G', 2, 8610, 0.05, 800, 'variable', 1),
('S1-R', 2, 8611, 0.9, 900, 'variable', 1),
('S1-J', 1, 2855, 7, 60, 'low', 1),
('S1-T', 1, 2856, 4, 85, 'low', 1),
('S1-K', 1, 5698, 60, 85, 'variable', 1),
('S1-U', 1, 5699, 15, 95, 'variable', 1),
('S1-P', 1, 4236, 1, 4, 'very low', 1),
('S1-V', 1, 4237, 0.9, 6, 'very low', 1),
('S1-S', 1, 7456, 0.1, 600, 'variable', 1),
('S1-W', 1, 7457, 0.09, 850, 'variable', 1),
('S1-Y', 1, 7520, 0.01, 800, 'variable', 1),
('S1-X', 1, 7521, 0.07, 600, 'variable', 1);

-- --------------------------------------------------------

--
-- Table structure for table `subscriptions`
--

CREATE TABLE `subscriptions` (
  `userID` int(3) NOT NULL,
  `MCC` int(3) NOT NULL,
  `MNC` int(3) NOT NULL,
  `brand` varchar(40) NOT NULL,
  `area` varchar(40) NOT NULL,
  `subs_NSSAI` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subscriptions`
--
CREATE TABLE Network (datetime datetime NOT NUll,value int,PRIMARY KEY (datetime));

INSERT INTO `subscriptions` (`userID`, `MCC`, `MNC`, `brand`, `area`, `subs_NSSAI`) VALUES
(1, 404, 1, 'Vi India', 'Haryana', 1),
(2, 404, 2, 'airtel', 'Punjab', 1),
(2, 404, 2, 'airtel', 'Punjab', 2),
(2, 404, 2, 'airtel', 'Punjab', 3),
(3, 404, 10, 'airtel', 'Delhi NCR', 2),
(4, 404, 20, 'VI india', 'Mumbai', 1),
(5, 404, 40, 'airtel', 'Chennai', 2),
(6, 404, 46, 'airtel', 'Kerala', 6),
(7, 404, 43, 'VI india', 'Tamil Nadu', 3),
(8, 404, 43, 'VI india', 'Tamil Nadu', 6);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `amfrepo`
--
ALTER TABLE `amfrepo`
  ADD PRIMARY KEY (`NSSAI`,`amfID`);

--
-- Indexes for table `amftable`
--
ALTER TABLE `amftable`
  ADD PRIMARY KEY (`AMFId`,`SliceID`);

--
-- Indexes for table `slicerepo`
--
ALTER TABLE `slicerepo`
  ADD PRIMARY KEY (`SNSSAI`);

--
-- Indexes for table `sliceresource`
--
ALTER TABLE `sliceresource`
  ADD PRIMARY KEY (`SliceID`);

--
-- Indexes for table `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD PRIMARY KEY (`userID`,`subs_NSSAI`);