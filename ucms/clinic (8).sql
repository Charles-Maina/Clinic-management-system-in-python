-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2024 at 04:55 AM
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
-- Database: `clinic`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(30) NOT NULL,
  `designation` enum('Medical Admin','General Admin') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `designation`) VALUES
('ADM001', 'General Admin'),
('ADMIN001', 'Medical Admin'),
('ADMOO1', 'General Admin');

-- --------------------------------------------------------

--
-- Table structure for table `archive`
--

CREATE TABLE `archive` (
  `username` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `medical_records` text DEFAULT NULL,
  `blood_group` enum('A','B','AB','O') NOT NULL,
  `health_condition` enum('Respiratory','Mental','Reproductive','STI','Injuries','Allergic','ENT','No','Other') NOT NULL,
  `allergies` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `username` varchar(30) NOT NULL,
  `designation` enum('Surgeon','Gynecologist','Allergist','General Practitioner') DEFAULT NULL,
  `schedule` text DEFAULT NULL,
  `years_0f_experience` int(11) NOT NULL,
  `available` enum('Yes','No') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`username`, `designation`, `schedule`, `years_0f_experience`, `available`) VALUES
('DOC/01/2020', 'Surgeon', 'Dayshift from 1st March to 1st April', 12, 'Yes'),
('DOC/01/2021', 'Allergist', 'DayShift from 1st March to 1st April', 3, 'Yes'),
('DOC/02/2020', 'Gynecologist', 'DayShift as from 1st March to 1st April', 13, 'Yes'),
('DOC/02/2024', 'Gynecologist', 'NightShift from 1st March to 1st April.', 3, 'Yes'),
('DOC/03/2017', 'General Practitioner', 'Dayshift from 1st March to 1st April', 8, 'Yes'),
('DOC/04/2020', 'Allergist', 'DayShift from 1st March to 1st April.', 12, 'Yes'),
('DOC/05/2020', 'Allergist', 'Nightshift from 1st March to 1st April', 7, 'Yes'),
('DOC/08/2020', 'Surgeon', 'Dayshift from 1st March to 1st April', 7, 'Yes'),
('DOC/09/2019', 'General Practitioner', 'DayShift from 1st March to 1st April', 10, 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `username` varchar(30) NOT NULL,
  `year_0f_employment` int(11) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`username`, `year_0f_employment`, `designation`) VALUES
('EMP/01/2020', 2020, 'Senior Lecturer Department of Engineering and Built environment.'),
('EMP/02/2020', 2020, 'Junior Lecturer Accounting Department.'),
('EMP/03/2020', 2020, 'Accountant.'),
('EMP/04/2015', 2015, 'Library Attendant'),
('EMP/05/2020', 2020, 'Chief Security'),
('EMP/06/2020', 2020, 'Lab Technician');

-- --------------------------------------------------------

--
-- Table structure for table `nurse`
--

CREATE TABLE `nurse` (
  `username` varchar(30) NOT NULL,
  `designation` enum('Surgical Nurse','Audiologist','Orthopedic','Emergency Room Nurse','General Nurse','Allergy Specialist') NOT NULL,
  `schedule` text DEFAULT NULL,
  `available` enum('Yes','No') DEFAULT 'Yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nurse`
--

INSERT INTO `nurse` (`username`, `designation`, `schedule`, `available`) VALUES
('NUR/01/2020', 'Surgical Nurse', 'Dayshift from 1st March to 1st April', 'Yes'),
('NUR/01/2021', 'Allergy Specialist', 'DayShift from 1st March to 1st April', 'Yes'),
('NUR/01/2024', 'Emergency Room Nurse', 'DayShift from 1st April to 1st March]]]]]', 'Yes'),
('NUR/02/2021', 'Emergency Room Nurse', 'NightShift from 1st February to 1st May', 'Yes'),
('NUR/04/2019', 'Surgical Nurse', 'NightShift from 1st March to 1st April.', 'Yes'),
('NUR/04/2020', 'Allergy Specialist', 'DayShift from 1st March to 1st April', 'Yes'),
('NUR/05/2020', 'Allergy Specialist', 'NightShift from 1st March to 1st April.', 'Yes'),
('NUR/05/2023', 'Audiologist', 'Dayshift from 1st March to 1st April', 'Yes'),
('NUR/05/2024', 'General Nurse', 'NightShift from 1st March to 1st April', 'Yes'),
('NUR/06/2020', 'Emergency Room Nurse', 'DayShift from 1st March to 1st April', 'Yes'),
('NUR/07/2018', 'Surgical Nurse', 'Dayshift from 1st March to 1st April', 'Yes'),
('NUR/08/2021', 'General Nurse', 'Dayshift from 1st March to 1st April.', 'Yes'),
('NUR/09/2024', 'Emergency Room Nurse', 'DayShift from 1st March to 1st April', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `username` varchar(30) NOT NULL,
  `password` varchar(300) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `medical_history` text DEFAULT NULL,
  `location` varchar(30) NOT NULL,
  `allergies` text DEFAULT NULL,
  `blood_group` enum('A','B','AB','O') NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `role` enum('doctor','nurse','receptionist','employee','student','patient') NOT NULL,
  `health_condition` enum('Respiratory','Mental','Reproductive','STI','Injuries','Allergic','ENT','No','Other') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `username` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `procedure_type` enum('medical examination','check-up','result analysis') NOT NULL,
  `visit` enum('Yes','No') NOT NULL,
  `department` enum('General','Neurology','Cardiology','Gynecology','Pediatrics','ENT') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `receptionist`
--

CREATE TABLE `receptionist` (
  `username` varchar(30) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `schedule` text DEFAULT NULL,
  `available` enum('Yes','No') DEFAULT 'Yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `receptionist`
--

INSERT INTO `receptionist` (`username`, `designation`, `schedule`, `available`) VALUES
('REC/01/2020', 'General Receptionist ', 'DayShift from 1st March to 1st April', 'Yes'),
('REC/02/2021', 'Data entry clerk.', 'Overnight schedule from 1st March to 1st April.', 'Yes'),
('REC/03/2020', 'General Receptionist ', 'Dayshift from 1st March to 1st April', 'Yes'),
('REC/04/2019', 'Data entry clerk', 'Dayshift from 1st March to 1st April', 'Yes'),
('REC/04/2020', 'General Receptionist ', 'NightShift from 1st March to 1st April.', 'Yes'),
('REC/05/2022', 'Data entry clerk', 'DayShift from 1st March to 1st April.', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `username` varchar(30) NOT NULL,
  `year_0f_study` int(11) NOT NULL,
  `department` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`username`, `year_0f_study`, `department`) VALUES
('BAC/B/01-01813/2020', 4, 'Bachelor of Accounting'),
('BAC/B/01-01813/2021', 3, 'Bachelor of Accounting'),
('BCB/01-01938/2023', 1, 'Bachelor of Commerce'),
('BCM/B/01-01813/2020', 4, 'Bachelor of Commerce'),
('COM/B/01-01813/2020', 4, 'Computer Science'),
('CSE/B/01-01012/2019', 5, 'Civil and Structural Engineering'),
('EDA/B/01-01813/2020', 4, 'Education Arts'),
('EDA/B/01-01813/2021', 4, 'Education Arts'),
('EDA/B/01-01814/2022', 2, 'Education Arts'),
('EDS/B/01-01813/2020', 4, 'Education Science'),
('EDS/B/01-02813/2023', 1, 'Education Science'),
('ETS/B/01-01813/2019', 4, 'Education Technology'),
('MED/B/01-01813/2019', 5, 'Medicine'),
('SIT/B/01-01713/2020', 4, 'Information Technology'),
('SIT/B/01-01813/2019', 4, 'Information Technology'),
('SIT/B/01-01813/2020', 4, 'Information Technology'),
('SIT/B/01-01813/2024', 1, 'Information Technology');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(300) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `medical_history` text DEFAULT NULL,
  `location` varchar(30) NOT NULL,
  `allergies` text DEFAULT NULL,
  `blood_group` enum('A','B','AB','O') DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `role` enum('admin','doctor','nurse','receptionist','employee','student') NOT NULL,
  `health_condition` enum('Respiratory','Mental','Reproductive','STI','Injuries','Allergic','ENT','No','Other') DEFAULT NULL,
  `weight` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `name`, `email`, `phone`, `gender`, `age`, `medical_history`, `location`, `allergies`, `blood_group`, `image`, `role`, `health_condition`, `weight`) VALUES
('ADM001', 'admin1', 'CHARLES MAINA', 'chm@gmail.com', 796303832, 'Male', 30, '1. Last visit on 01/01/2024 with symptoms of malaria.Laboratory tests revealed the presence of Plasmodium falciparum parasites in the patient\'s blood smear, confirming the diagnosis of malaria. Treated by anti-malarial medication  ', 'Kakamega Town', 'No allergies recorded ', 'A', '', 'admin', 'No', 87.00),
('ADMIN001', 'admin1', 'Phelistus Wambo', 'wambo@gmail.com', 796303832, 'Female', 46, '1. Annual breast cancer screening conducted on 11/7/2023. Mammogram revealed benign calcifications, and subsequent biopsy confirmed benign pathology.', '0768909876', 'No allergies recorded', 'B', '', 'admin', 'No', 89.00),
('ADMOO1', 'admin1', 'Charles Maina', 'maina21@gmail.com', 796303832, 'Male', 32, 'No severe medical condition', 'Shweywe.', 'Dust', 'AB', 'C:\\Users\\USER\\PycharmProjects\\ucms\\static\\logo.png', 'admin', NULL, 92.00),
('BAC/B/01-01813/2020', 'pbkdf2:sha256:600000$JVJAlS3S5ZYbothf$685cb5a3f6a7a46395b07b7335b1d79ae2e3e0c894821264fb24a8990f9b5933', 'Catherine Oburo', 'oburo@gmail.com', 798231209, 'Female', 23, '1. Last visit on 10/03/2024 for physical therapy and casting 2. Fractured right wrist in a skateboarding accident on 28/02/2024, undergoing casting and physical therapy for rehabilitation.', 'Milimani', 'No allergies recorded', 'A', NULL, 'student', 'Injuries', 68.22),
('BAC/B/01-01813/2021', 'pbkdf2:sha256:600000$qPtfAvZPJGHj4Rob$9833e0489eaf626260716005b05f4d77c47c611cde29d5f2d8a27a39eeecbf22', 'Philip Andenga', 'philipe@gmail.com', 118875432, 'Male', 19, '1. Last visit on 11/03/2023 for medical checkup and evaluation. 2. Chronic cough and dyspnea on exertion, currently undergoing evaluation for possible interstitial lung disease.', 'Shikambi', 'Dyspea allergy', 'B', NULL, 'student', 'Allergic', 63.00),
('BCB/01-01938/2023', '123456789', 'Elizabeth Waeni', 'waenie@gmail.com', 756389021, 'Male', 18, '1. Last visit on 06/03/2024 experiencing wheezing and difficult in breathing. Treated with epinephrine auto-injector \r\n\r\n2. Experienced allergic reaction to bee sting in February, 2024, that caused throat swelling and shortness of breath.', 'Hall 1', 'Insect Sting Allergies (Bees,Wasps and fire ants)', 'O', NULL, 'student', 'Allergic', 55.00),
('BCB/B/01-01813/2020', '123456789', 'Fidel Kuya', 'fidelk@gmail.com', 110087650, 'Male', 20, '1. Last visit on 01/01/2024 for routine prostate cancer screening with digital rectal examination (DRE). DRE findings were normal, and prostate gland felt smooth and non-enlarged, suggesting no signs of prostate cancer.', 'StageMandazi ', 'No allergies recorded', '', NULL, 'student', 'No', 56.40),
('BCM/B/01-01813/2020', 'pbkdf2:sha256:600000$R5oJt048IgzYOSPo$6c424e1f221bff422bd8c7f12dd6aab71ebc19e2e40a4fba7f4bbc5aaf1108f6', 'Juliet Stasha', 'stasha@gmai.com', 779123091, 'Female', 23, '1. Last visit on 25/02/2024 to collect ARV dosage.\r\n2. Tested positive for HIV in February, 2024 currently receiving antiretroviral therapy.\r\n', 'Kefinco', 'No allergies recorded', 'A', NULL, 'student', 'STI', 68.00),
('COM/B/01-01813/2020', 'pbkdf2:sha256:600000$knjhWFyHb75lgKjx$7420945b6917583fd123fa6b5ed18ab88c552972e4feb9b5cf04c0b9ff51b085', 'Austine Asembo', 'sema@gmail.com', 734537892, 'Male', 21, '2. Last visit on 01/01/2021\r\n1. No serious medical history', 'Amalemba', 'No allergies recorded', 'AB', NULL, 'student', 'No', 69.00),
('CSE/B/01-01012/2019', 'pbkdf2:sha256:600000$aiMnDcIft6dESDC5$06eb3ae6aecd741842ed324fbe851ae2fdc3ca3cf7b7fd28c6dcd488bb7bccce', 'Egnicious Keino', 'keino@gmail.com', 718054673, 'Male', 26, '1. Last visit on 28/02/2024 for outpatient prevention therapy.\r\n2. Substance abuse disorder(bhang) history. Completed rehabilitation in 2023 and currently engaged in out-patient prevention therapy.', 'Koromatangi ', 'No allergies recorded', 'AB', NULL, 'student', 'Respiratory', 59.00),
('DOC/01/2020', 'doc123', 'Alfred Tom', 'alfredo@gmail.com', 110053971, 'Male', 34, '1. Received Pfizer Corona virus vaccine in August, 2020', 'Lurambi', 'No allergic reactions recorded.\r\n', 'O', NULL, 'doctor', 'No', 98.00),
('DOC/01/2021', 'pbkdf2:sha256:600000$MqfyovnEhJQg0hCX$2c35a0a54c367acb406f05927e38e95d519667482cd40165c2f4a478f6aea46f', 'Solomon Mutinda', 'mutinda@gmail.com', 789436765, 'Male', 32, '1. Last visit on 01/01/2024 for cancer screening. No cancer cells detected.', 'Kakamega Town', 'No allergies recorded', 'AB', NULL, 'doctor', 'No', NULL),
('DOC/02/2020', 'pbkdf2:sha256:600000$qwsXRDBrp0ooFtCG$d7ef50886eef5d6824426473158800a48d92460717e2205cb3009d0d8bbb9f4c', 'Linus Njoroge', 'njoro@gmail.com', 745378900, 'Male', 54, '1. Experienced anaphylaxis in 2019 that led to rapid pulses and loss of consciousness', 'Kakamega', 'Allergic to pet dander.', 'O', NULL, 'doctor', 'Allergic', 70.00),
('DOC/02/2024', 'pbkdf2:sha256:600000$q5kXZskf04LMcXrB$8402e2b15f21c5efbc9286213e44306c825ce9a2887d3938f2482ebdf7dd60e3', 'Joseph Kosgey', 'kos@gmail.com', 723899870, 'Male', 29, '1. No serious medical history', 'Kakamega Town', 'No recorded allergies', 'AB', NULL, 'doctor', 'No', 69.00),
('DOC/03/2017', 'pbkdf2:sha256:600000$XJLB8ayOeNRYoJTj$c3ca75763d55b58be39bf3e7b8d01320452cc9d26a3d3f50435fa6183297537e', 'Lilian Nafula', 'nafula@gmail.com', 745378909, 'Female', 36, '1. No serious medical history', 'Kakamega Town', 'No allergies recorded', 'AB', NULL, 'doctor', 'No', 78.00),
('DOC/04/2020', 'pbkdf2:sha256:600000$CVQPYjERpCYXgV5d$7a55654e933125bcfc333c1b8118a06cffffae9b4a1e265aafa5937007fdff4c', 'Pius Mworia', 'mwor@gmail.com', 734890765, 'Male', 41, 'No serious medical history.', 'Kakamega Town', 'No.', 'A', NULL, 'doctor', 'No', 74.00),
('DOC/05/2020', 'pbkdf2:sha256:600000$G45ZlMXNEpxENqII$e577d44fdcf4f6c00066f1631ea1547da11f77cc0893a400d3dcf43822c75d49', 'Elizabeth Achieng ', 'achieg@gmail.com', 745190876, 'Female', 30, 'No serious medical history', 'Kakamega Town', 'No allergies recorded.', 'B', NULL, 'doctor', 'No', 89.00),
('DOC/08/2020', 'pbkdf2:sha256:600000$q8gV1qj1I25w3mJD$e3fa620d075f12bc29ac9c83b606767a3c0fe49fc909f6c6b98198d8a07acd40', 'Philis Moraa', 'moraa@gmail.com', 743789302, 'Male', 38, '1. Diagnosed with polycystic ovary syndrome (PCOS) at age 36, managed with lifestyle modifications and metformin.', 'Kisumu', 'No allergies recorded', 'O', NULL, 'doctor', 'Reproductive', 80.00),
('DOC/09/2019', 'pbkdf2:sha256:600000$XnyY2h8mOSWZKTYW$cb5b71d70f9c7da184e37b78c7040c9f1263e23e623053c538a394ba7ecc6299', 'James Njuguna', 'jemon@gmail.com', 743563278, 'Male', 39, '1. Received the Moderna COVID-19 vaccine, an mRNA vaccine, in March 2021.', 'Kakamega Town.', 'No allergies recorded', 'B', NULL, 'doctor', 'No', 99.00),
('EDA/B/01-01813/2020', 'pbkdf2:sha256:600000$ZGQf4CnU4OrqVT9f$16c9b19adf3eb32c287949a7f29f3fdab29e49971406322caf402e0eb3414088', 'Joyce Awinja', 'joy@gmail.com', 745678909, 'Female', 23, '1. Last visit on 07/03/2024 for regular follow up.\r\n2. Experienced recurrent episodes of wheezing, coughing, chest tightness, and shortness of breath in Jan, 2020. Signifying an asmatic ailment.', 'Hall 4', 'No allergies recorded', 'O', NULL, 'student', 'Allergic', 60.00),
('EDA/B/01-01813/2021', 'pbkdf2:sha256:600000$4Rjo1yMt9Tni8zNz$b35450d571e3e9012908af4d268f79d7b6a54f2df49b73434eeb611604b2cf6b', 'Esther Wahome', 'wahome@gmail.com', 789876543, 'Female', 20, '1. Last visit on 11/03/2024 for checkup and picking medication.\r\n2. History of allergic rhinitis and sinusitis, experiencing seasonal exacerbations of nasal congestion and post-nasal drip. ', 'Maraba', 'Allergic rhinitis and sinusitis', 'AB', NULL, 'student', 'Allergic', 57.60),
('EDA/B/01-01814/2022', '123456789', 'Suzzanne Maria', 'suzz@gmail.com', 110098765, 'Female', 19, '1. History of genital herpes outbreaks since 2018, managed with antiviral medication.\r\n', 'Kefinco', 'No allergies recorded', 'A', NULL, 'student', 'STI', 63.00),
('EDS/B/01-01813/2020', 'pbkdf2:sha256:600000$ILs6wvnZQMOJQCeJ$a8ae3b98ee6a5aa0d3b2ff2f2339a010dc13be3b3ab1a9625f644f0b8b19c263', 'Aggrey Mukwambo', 'mukwamboa@gmail', 732890765, 'Male', 24, '1. Last visit on 08/03/2024 for checkup and examination.\r\n2. Involved in a road accident on 01/03/2024 that left him with a fractured leg.', 'Lupe', 'No allergies recorded\r\n', 'AB', NULL, 'student', 'Injuries', 54.00),
('EDS/B/01-02813/2023', 'pbkdf2:sha256:600000$hU9WWOqcfmnakojT$d36a6adb3d1ceaeaca0b21b0171508242ad5238eddbc71e7372acc66b587b57d', 'Angela Wairimu', 'wairimu@gmail.com', 120078932, 'Female', 17, '1. History of Asthma: Diagnosed with asthma in 2012. Currently managed with Leukotriene Modifiers medication.\r\n', 'Hall 4.', 'No allergies recorded ', 'O', NULL, 'student', 'Respiratory', 50.00),
('EMP/01/2020', 'employee1', 'Julius Juma', 'jumaj@gmail.com', 768098743, 'Male', 53, '1.  Experienced allergic reaction to penicillin antibiotics, characterized by skin rashes , confirmed by allergy testing in January, 2021.', 'Bungoma.', 'Penicillin ', 'AB', NULL, 'employee', 'No', 101.00),
('EMP/02/2020', 'employee2', 'Sussan Mwendwa', 'mwend@gmail.com', 734219087, 'Female', 39, '1. Follow-up visit on 11/03/2024 after breast biopsy revealed a typical ductal hyperplasia. Patient counseled on increased risk of breast cancer and recommended for regular surveillance and lifestyle modifications.', 'Kisumu', 'No recorded allergies.', 'B', NULL, 'employee', 'No', 90.00),
('EMP/03/2020', 'employee3', 'Victorine Wambugu', 'wambuv@gmail.com', 725095678, 'Male', 34, '1. Last visit on 01/0/2023, underwent a casting and physiotherapy treatment after sustaining a fracture of the right arm after falling on a slippery floor.', 'Kakamega Town', 'No allergies recorded', 'O', NULL, 'employee', 'Injuries', 89.00),
('EMP/04/2015', 'pbkdf2:sha256:600000$B8Z2cFekckEOMLDE$f2794251f942126b0063781ff2a9326b3880b951caaaa1c28f3daff935aebf77', 'Patrice Lumumba', 'patl@gmail.com', 756545654, 'Male', 50, '1. No serious medical history ', 'Kakamega Town', 'No allergies recorded', 'AB', NULL, 'employee', 'No', 81.00),
('EMP/05/2020', 'pbkdf2:sha256:600000$ASrZnV3qiyX9is9Q$0d890b4a53b94edac328e914ed4e531f4d1daf4318022b75162752b0e74b5b43', 'Joel Muasia', 'joel@gmail.com', 734565456, 'Male', 43, '1. No serious medical history', 'Kakamega Town.', 'No allergies recorded.', 'AB', NULL, 'employee', 'No', 77.00),
('EMP/06/2020', 'pbkdf2:sha256:600000$MlHnffS5K9hKr6o6$d7afed0f0713c2d09d8fbd0cbc62ffbc77f7235dae36733ba4ff7bbd8785263b', 'Christabel Kipkurere', 'kip@gmail.com', 768904536, 'Female', 41, '1. Miscariage in 2023', 'Eldoret', 'No', 'A', NULL, 'employee', 'Reproductive', 73.00),
('ETS/B/01-01813/2019', 'pbkdf2:sha256:600000$nigazD8dOnEsnFop$b8294debf8b40e122619865e34eff52cf37cac183eee57127ebb6cc5e8e5780e', 'Titus Omondi', 'omondi@gmail.com', 790653421, 'Male', 27, '1. Last visit on 04/03/2024 for scheduled follow up.\r\n2. Injured right shoulder in a car accident in January, 2024. Underwent surgery for a torn rotator cuff and currently undergoing physical therapy.', 'Hall 2', 'No allergies recorded', 'O', NULL, 'student', 'Injuries', 50.00),
('MED/B/01-01813/2019', 'pbkdf2:sha256:600000$lU7BQnnyyhzjtoEo$3b5f88ffa3d5e50accf9b0a361bb276b9cd2abc67c20f38ab5916684f91dbadd', 'Maureen Mwema', 'mwem@gmail.com', 739043223, 'Female', 24, '1. Bipolar disorder diagnosed in 2020, receiving mood stabilizers and regular psychiatric monitoring.', 'Hall 1', 'No allergies recorded', 'AB', NULL, 'student', 'Mental', 58.00),
('NUR/01/2020', 'nurse1', 'Philice Wanga', 'phil@gmail.com', 710053970, 'Female', 32, '1. On 09/03/2024 underwent cancer screening. No cancer cells detected.\r\n\r\n2. Received the Johnson & Johnson\'s Janssen COVID-19 vaccine in May 2021, a viral vector vaccine. ', 'Amalemba', 'No allergies recorded.', 'O', NULL, 'nurse', 'No', 78.00),
('NUR/01/2021', 'pbkdf2:sha256:600000$6dcJV7HkbFCNdRSj$2c7aa70de3117c53f3f5eaf83785be303f9f1e03ed566c4586c206698dcd27ac', 'Susan Mutinda', 'sus@gmail.com', 789432387, 'Female', 29, '1. No serious medical record', 'Kakamega Town', 'No allergies recorded.', 'AB', NULL, 'nurse', 'No', 77.00),
('NUR/01/2024', 'pbkdf2:sha256:600000$ZBIpImI6TR405uhg$0fb36b9ab70ab6264460f9b7e6f4c4bbf04695fe1e166f8ad8e0264e577be8ba', 'Josephine Jumwa', 'jjpne@gmail.com', 796303832, 'Female', 36, '1. Last Visit on 02/03/2024 for routine surveillance. \r\n2. History of ovarian cysts diagnosed during routine pelvic ultrasound in 2023, currently asymptomatic and under surveillance. ', 'Kakamega Town', 'No allergies recorded', 'B', NULL, 'nurse', 'No', 73.00),
('NUR/02/2021', 'nurse123', 'Fredrick Ochieng', 'ochie@gmail.com', 743567897, 'Male', 37, '1. Exercise-induced bronchoconstriction (EIB) diagnosed during adolescence, requiring pre-exercise bronchodilator use', 'Lurambi', 'No allergies recorded.', 'A', NULL, 'nurse', 'No', 80.00),
('NUR/04/2019', 'pbkdf2:sha256:600000$OaTK1Cd5XWKwz7fX$4d298542d9094270f3756074213ca97fcb13a117598a46185557b9cd419e01e4', 'Johnstone Muruge', 'mge@gmail.com', 734909009, 'Male', 46, '1. Attended clinic on 6/19/2022 for lung cancer screening with low-dose computed tomography (CT) scan. CT scan showed no evidence of pulmonary nodules or masses, suggesting no lung cancer.', 'Kakamega Town', 'No allergies recorded', 'AB', NULL, 'nurse', 'No', 92.00),
('NUR/04/2020', 'pbkdf2:sha256:600000$4vndSpTbedKg1hzM$b2e301d0d79caf49ef4703e8d7a7c7fa4fa9a46d5a27c68fa1b6128664d75913', 'Jackson Waweru', 'jack@gmail.com', 754637282, 'Male', 42, '1. Received the Pfizer-BioNTech COVID-19 vaccine, an mRNA vaccine, in January 2021.', 'Kakamega Town', 'No allergies recorded', 'A', NULL, 'nurse', 'No', 97.00),
('NUR/05/2020', 'pbkdf2:sha256:600000$sPspquuuNYk2BggZ$d38aafb981ad689cee93f1ccaa978c9387f8c3c904ee1681b9b8041a549e0c3c', 'Justus Kangethe', 'justo@gmail.com', 745454545, 'Male', 49, '1. Developed tennis elbow from repetitive strain at work, treated with rest, anti-inflammatory medication, and ergonomic adjustments.', 'Kakamega Town', 'No allergies recorded', 'B', NULL, 'nurse', 'No', 78.00),
('NUR/05/2023', 'pbkdf2:sha256:600000$jPUo1avWIFsBKpIU$09024c65b53f513886b24cc28d97a98273e867688d682947507a09942c071762', 'Eunice Aisha', 'aisha@gmail.com', 789432123, 'Female', 29, '1. No serious medical history.', 'Kisumu', 'No allergies recorded', 'O', NULL, 'nurse', 'No', 77.00),
('NUR/05/2024', 'pbkdf2:sha256:600000$tK8b6Etr2IUpIhTf$5f87e3bb053b12f5eaa669e1b61dc17f2bb42c97a6ae44ceacbd2c8e1ce01850', 'John Ochieng', 'och@gmail.com', 784564738, 'Male', 27, '1. Treated for Anemia, Received iron supplementation and dietary counseling for iron-deficiency anemia in 2020', 'Kisumu', 'No allergies recorded', 'AB', NULL, 'nurse', 'Other', 70.00),
('NUR/06/2020', 'pbkdf2:sha256:600000$fd5069OyRiLSxPCo$630e0207a6a1652dac9ef813dc52c6afa830e22b41fc9ae05a91b1de854cf79a', 'Phanice Atieno', 'ati@gmail.com', 723908752, 'Female', 32, '1. Last visit on 12/03/2024 for allergic evaluation.\r\n2. Presented with a history of recurrent skin rashes, itching, and hives following contact with latex-containing products. Symptoms exacerbated during medical procedures involving latex gloves. Uses Vynil gloves.', 'Kakamega Town', 'Allergic to Latext, Uses Vynil gloves.', 'B', NULL, 'nurse', 'Allergic', 67.00),
('NUR/07/2018', 'pbkdf2:sha256:600000$PjX0YPITxS5qjnw1$25a4db14c13fcaecfcfeab1903e469e796aa3f2fd7de3c9b6562794a12b21948', 'Edith Keino', 'key@gmail.com', 732909090, 'Female', 38, '1. Family history of breast cancer, maternal grandmother diagnosed at age 37 and mother at 45 undergoing regular mammography screening from 2022.', 'Kakamega Town', 'No allergies recorded', 'A', NULL, 'nurse', 'Reproductive', 81.00),
('NUR/08/2021', 'pbkdf2:sha256:600000$MnPe2pituZ5HE7Ac$b400f1b249cc75d6f1146fd0c32d4a823dd51f3098d4d7c3c588b5388d3641de', 'Getrude Awinja', 'gety@gmail.com', 789432778, 'Female', 32, '1. No serious medical history.', 'Kakamega Town.', 'No allergies recorded', 'B', NULL, 'nurse', 'No', 84.00),
('NUR/09/2024', 'pbkdf2:sha256:600000$0eWVRsVhX723Di7H$c5b510202e27bc5136a308b7d052b9a1a0c860ef74ed25ad20a18e62ccef7c40', 'Mourice Odhiambo', 'odhis@gmail.com', 745372890, 'Male', 34, '1. Received the Johnson & Johnson\'s Janssen COVID-19 vaccine in May 2021', 'Kisumu.', 'No allergies recorded.', 'AB', NULL, 'nurse', 'No', 75.00),
('REC/01/2020', 'receptionist1', 'Emmanuel Kibet', 'kibet@gmail.com', 754633226, 'Male', 42, '1. Diagnosed and treated  with small pox in 2010', 'Kisumu.', 'No allergies recorded.', 'A', NULL, 'receptionist', 'Other', 72.00),
('REC/02/2021', 'receptionist2', 'Andrew Wechuli', 'wechulia@gmail.com', 723456712, 'Male', 29, '1. No serious medical treatment so far', 'Bungoma', 'No recorded allergies.', 'O', NULL, 'receptionist', 'No', 69.00),
('REC/03/2020', 'pbkdf2:sha256:600000$wyG2QNaDkemnZuhk$f14df6a9260ce6faf40a6b52deed7b5f53e92d28bebcd579d8c5348400db2fa3', 'Philemon Kipngetich', 'kip@gmail.com', 712980876, 'Male', 32, '1. No serious medical history', 'Kakamega Town', 'No', 'AB', NULL, 'receptionist', 'No', 69.00),
('REC/04/2019', 'pbkdf2:sha256:600000$6g8HoajRaXH2ndhn$a5ca2a97b691fe2a6d8e92345cd74921ceede27272ef3d9bc79009038374b3c9', 'Mary Wairimu', 'mary@gmail.com', 734261789, 'Female', 37, '1. Attended clinic on 5/03/2023 for routine breast examination and screening mammography. Results indicated benign findings with no evidence of malignancy.', 'Kakamega Town', 'No allergies recorded', 'B', NULL, 'receptionist', 'No', 74.00),
('REC/04/2020', 'pbkdf2:sha256:600000$Jx3OkrAqD5ANpKgL$3ac551a1ce66d3d0ab9df33a28883c473c74db6d172346b2265db26aabd48b4b', 'Emanuel Ngeno', 'ngeno@gmail.com', 765676567, 'Male', 28, '1. No serious medical history.', 'Amalemba.', 'No allergies recorded', 'O', NULL, 'receptionist', 'No', 70.00),
('REC/05/2022', 'pbkdf2:sha256:600000$qwi1ktnFqB58L8mC$1b42bc07102e117e067f4e000823b666a5797b00b7e1ac815773a0683be07d4a', 'Catherine Vishi', 'vyshy@gmail.com', 745673092, 'Female', 44, '1. Received corona virus vaccine in 2022', 'Kisumu.', 'No allergies recorded ', 'O', NULL, 'receptionist', 'No', 69.00),
('SIT/B/01-01713/2020', 'pbkdf2:sha256:600000$VyGDQh0NplpMaiY3$35978388c00c19cab043cdb12ae414a8b910225fd17fe092170638dc20f184d7', 'Hellen Chepkuony', 'chep@yahoo.com', 745672901, 'Female', 20, '1. Last Visit on 02/03/2024 for routine surveillance. \r\n2. History of ovarian cysts diagnosed during routine pelvic ultrasound in 2023, currently asymptomatic and under surveillance.', 'Lurambi.', 'No recorded allergies', 'AB', NULL, 'student', 'Respiratory', 50.00),
('SIT/B/01-01813/2019', 'pbkdf2:sha256:600000$QiocwL5IfiWbizt0$bcc2fa86a6269839bb07a636d059e0c46591f9b26816bc55f5d160ed19f2bac1', 'Florence Wambo', 'wam@gmail.com', 789097809, 'Female', 24, '1. Last visit on 01/03/2023, received malaria treatment.\r\n2. Cut left hand while cooking, received stitches at the emergency room and underwent a course of antibiotics to prevent infection. ', 'Lurambi', 'No allergies recorded', 'AB', NULL, 'student', 'Injuries', 67.00),
('SIT/B/01-01813/2020', 'pbkdf2:sha256:600000$vTgHJc0O5r9dygvB$6a73022bb96fbbae6c138e48f42af8e92bb920a413978913b0d80f1c5f6c357a', 'CHARLES MAINA', 'mca@gmail.com', 796303832, 'Male', 20, '1. Last visit on 01/01/2024 for cancer screening. No cancer cells detected.\r\n', 'Sichirai.', 'No allergies recorded', 'B', NULL, 'student', 'No', 56.00),
('SIT/B/01-01813/2024', 'pbkdf2:sha256:600000$yAlyznF1llozMt4A$86528c6d78d3a157cad5f5350712bb23b990f90a129cb7a6b0b51b0dce478325', 'Joseph Kirui', 'josk@gmail.com', 700009054, 'Male', 18, '1. Last visit on 08/03/2024 for TB Screening, No infections detected.\r\n2. Received the Moderna COVID-19 vaccine, an mRNA vaccine, in July 2021', 'Hall 2.', 'No recorded allergies', 'B', NULL, 'student', 'No', 54.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `archive`
--
ALTER TABLE `archive`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `nurse`
--
ALTER TABLE `nurse`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `receptionist`
--
ALTER TABLE `receptionist`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `nurse`
--
ALTER TABLE `nurse`
  ADD CONSTRAINT `nurse_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `prescription`
--
ALTER TABLE `prescription`
  ADD CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`);

--
-- Constraints for table `receptionist`
--
ALTER TABLE `receptionist`
  ADD CONSTRAINT `receptionist_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  ADD CONSTRAINT `student_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
