from flask import render_template, session, redirect, url_for, flash
from models import db, User, Doctor, Student, Nurse, Receptionist, Employee
from flask import Flask
from flask import Blueprint

manage_bp = Blueprint('manage', __name__)


app = Flask(__name__)


# Route for managing users by general admin
@app.route('/manage_user')
def manage_user():
    return render_template('manageuser.html')


# Route for managing students
@app.route('/manage_students')
def manage_student():
    if 'username' in session and session['user_type'] == 'admin':
        students = db.session.query(Student, User.name, User.email, User.phone, User.location, Student.department,
                                    Student.year_0f_study, User.medical_history, User.blood_group, User.health_condition,
                                    User.allergies, User.weight).join(User).all()
        return render_template('managestudents.html', students=students)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for managing doctors
@app.route('/manage_doctors')
def manage_doctor():
    if 'username' in session and session['user_type'] == 'admin':
        doctor = db.session.query(Doctor, User.name, User.email, User.phone, User.location, Doctor.designation,
                                  Doctor.schedule, Doctor.years_0f_experience, User.medical_history, User.blood_group,
                                  User.health_condition, User.allergies, Doctor.available,  User.weight).join(User).all()
        return render_template('managedoctors.html', doctor=doctor)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for managing nurses
@app.route('/manage_nurses')
def manage_nurse():
    if 'username' in session and session['user_type'] == 'admin':
        nurse = db.session.query(Nurse, User.name, User.email, User.phone, User.location, Nurse.designation,
                                 Nurse.schedule, User.medical_history, User.blood_group, User.health_condition,
                                 User.allergies, Nurse.available,  User.weight).join(User).all()
        return render_template('managenurses.html', nurse=nurse)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for managing employees
@app.route('/manage_employees')
def manage_employees():
    if 'username' in session and session['user_type'] == 'admin':
        employee = db.session.query(Employee, User.name, User.email, User.phone, User.location, Employee.designation,
                                    Employee.year_0f_employment, User.blood_group, User.medical_history,
                                    User.health_condition, User.allergies,  User.weight).join(User).all()
        return render_template('manageemployees.html', employee=employee)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for managing receptionists
@app.route('/manage_receptionists')
def manage_receptionist():
    if 'username' in session and session['user_type'] == 'admin':
        receptionist = db.session.query(Receptionist, User.name, User.email, User.phone, User.location,
                                        Receptionist.designation, Receptionist.schedule,  User.medical_history,
                                        User.blood_group, User.health_condition, User.allergies,
                                        Receptionist.available,  User.weight).join(User).all()
        return render_template('managereceptionists.html', receptionist=receptionist)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))

