-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2024 at 01:55 AM
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
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `medical_history` text DEFAULT NULL,
  `location` varchar(30) NOT NULL,
  `allergies` text DEFAULT NULL,
  `blood_group` varchar(10) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `role` enum('admin','doctor','nurse','receptionist','employee','student') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `name`, `email`, `phone`, `gender`, `age`, `medical_history`, `location`, `allergies`, `blood_group`, `image`, `role`) VALUES
('ADMOO1', 'admin1', 'Charles Maina', 'maina21@gmail.com', 796303832, 'Male', 32, 'No severe medical condition', 'Shweywe', 'Dust', 'AB', 'C:\\Users\\USER\\PycharmProjects\\ucms\\static\\logo.png', 'admin'),
('BCB/01-01938/2023', '123456789', 'Elizabeth Waeni', 'waenie@gmail.com', 756389021, 'Male', 18, 'No special medical history', 'Hall 1', 'No', 'A', NULL, 'student'),
('BCB/B/01-01813/2020', '123456789', 'Fidel Kuya', 'fidelk@gmail.com', 110087650, 'Male', 20, 'No applicable medical history\r\n', 'StageMandazi ', 'No', 'AO', NULL, 'student'),
('DOC/01/2020', 'doc123', 'Alfred Tom', 'alfredo@gmail.com', 110053971, 'Male', 34, 'Anaemic', 'Lurambi', 'No allergic reactions\r\n', 'O', NULL, 'doctor'),
('DOC/02/2020', 'scrypt:32768:8:1$C0LYo5D2KDqQE', 'Norah Iminza', 'inorah@gmail.com', 795565431, 'Female', 28, 'No', 'Mumias', 'No', 'AB', NULL, 'doctor'),
('EMP/01/2020', 'employee1', 'Jacob Bakari', 'jbakarii@gmail.com', 789654329, 'Male', 42, 'Treated with level one cancer condition\r\n at Kenyata', 'Carlifonia', 'Allergic to smoke', 'AB', NULL, 'employee'),
('EMP/02/2019', 'employee2', 'Juliet Kerubo', 'jkerubo@gmail.com', 789098909, 'Female', 42, 'No', 'Kisumu', 'No', 'A', NULL, 'employee'),
('NUR/01/2020', 'nurse1', 'Philice Wanga', 'wangaphi@gmail.com', 710053970, 'Female', 32, 'Survived Corona attack for two months.', 'Amalemba', 'No allergies recorded..', 'O', NULL, 'nurse'),
('NUR/03/2021', 'nurse3', 'Fredrick Ochieng', 'ochiengf@gmail.com', 789435678, 'Male', 37, 'No', 'Kisumu', 'No', 'A', NULL, 'nurse'),
('REC/01/2020', 'receptionist1', 'Faith Atieno', 'atieno1@gmail.com', 75463322, 'Female', 42, 'Treated my small pox in 2010', 'Kisumu', 'Cold condition', 'A', NULL, 'receptionist'),
('REC/02/2021', 'receptionist2', 'Andrew Wechuli', 'wechulia@gmail.com', 723456712, 'Male', 29, 'No serious medical treatment so far', 'Bungoma', 'No recorded allergies.', 'O', NULL, 'receptionist'),
('SIT/B/01-01813/2020', '123456789', 'Charles Maina', 'mainacharlesmca@gmail.com', 796303832, 'Male', 22, 'No serious medical procedure recorded.', 'California ', 'Dust.', 'AB', NULL, 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
