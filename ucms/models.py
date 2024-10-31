from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

db = SQLAlchemy()


# models.py

class User(db.Model):
    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum('Male', 'Female', 'Other'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text)
    location = db.Column(db.String(30), nullable=False)
    allergies = db.Column(db.Text)
    blood_group = db.Column(db.Enum('A', 'B', 'AB', 'O'), nullable=False)
    image = db.Column(db.String(255))
    weight = db.Column(db.Numeric(precision=5, scale=2))  # Add this line to include the weight column
    role = db.Column(db.Enum('admin', 'doctor', 'nurse', 'receptionist', 'employee', 'student'), nullable=False)
    health_condition = db.Column(
        Enum('Respiratory', 'Mental', 'Reproductive', 'STI', 'Injuries', 'Allergic', 'ENT', 'No', 'Other'),
        nullable=False)  # Add health_condition field

    student = relationship("Student", back_populates="user")
    doctor = relationship("Doctor", back_populates="user")
    nurse = relationship("Nurse", back_populates="user")
    employee = relationship("Employee", back_populates="user")
    receptionist = relationship("Receptionist", back_populates="user")
    appointment = relationship("Appointment", back_populates="user")
    archive = relationship("Archive", back_populates="user")
    # patient = relationship("Patient", back_populates="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Student(db.Model):
    __tablename__ = 'student'
    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)
    year_0f_study = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)

    user = relationship("User", back_populates="student")

    def __repr__(self):
        return f"<Student {self.username}>"


class Admin(db.Model):
    __tablename__ = 'admin'

    username = db.Column(db.String(30), primary_key=True)
    designation = db.Column(Enum('Medical Admin', 'General Admin'), nullable=False)


    def __repr__(self):
        return f"<Admin {self.username}>"


class Doctor(db.Model):
    __tablename__ = 'doctor'

    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)
    designation = db.Column(Enum('Surgeon', '', 'Gynecologist', 'Allergist', 'General Practitioner'), nullable=False)
    schedule = db.Column(db.Text)
    years_0f_experience = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Enum('Yes', 'No'), nullable=False)

    user = relationship("User", back_populates="doctor")

    def __rep__(self):
        return f"<Doctor {self.username}>"


class Nurse(db.Model):
    __tablename__ = "nurse"

    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)
    designation = db.Column(Enum('Surgical Nurse', 'Audiologist', 'Orthopedic', 'Emergency Room Nurse',
                                 'General Nurse', 'Allergy Specialist','Field Nurse'), nullable=False)
    schedule = db.Column(db.Text)
    # prescription = db.Column(db.Text)
    available = db.Column(db.Enum('Yes', 'No'), nullable=False)

    user = relationship("User", back_populates="nurse")

    def __repr__(self):
        return f"<Nurse {self.username}>"


class Employee(db.Model):
    __tablename__ = "employee"
    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)
    year_0f_employment = db.Column(db.Integer, nullable=False)
    designation = db.Column(db.String(100), nullable=False)

    user = relationship("User", back_populates="employee")

    def __repr__(self):
        return f"<Employee {self.username}>"


class Receptionist(db.Model):
    __tablename__ = "receptionist"
    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)
    designation = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.Text)
    available = db.Column(db.Enum('Yes', 'No'), nullable=False)

    user = relationship("User", back_populates="receptionist")


def __repr__(self):
    return f"<Receptionist {self.username}>"


class Appointment(db.Model):
    __tablename__ = "appointment"

    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)  # Primary key as username
    date = db.Column(db.Date, nullable=False)  # Date field
    time = db.Column(db.Time, nullable=False)  # Time field
    procedure_type = db.Column(Enum('medical examination', 'check-up', 'result analysis'),
                               nullable=False)  # Procedure dropdown list
    visit = db.Column(Enum('Yes', 'No'), nullable=False)  # Visit option
    department = db.Column(Enum('General', 'Neurology', 'Cardiology', 'Gynecology', 'Pediatrics', 'ENT'),
                           nullable=False)  # Department enum

    user = db.relationship("User", back_populates="appointment")

    def __repr__(self):
        return f"<appointment {self.username}>"


# Define the Archive model
class Archive(db.Model):
    __tablename__ = 'archive'

    username = db.Column(db.String(30), db.ForeignKey('user.username'), primary_key=True)

    user = db.relationship("User", back_populates="archive")

    def __repr__(self):
        return f"<Archive {self.username}>"

