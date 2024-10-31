from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from models import db, User, Admin, Doctor, Student, Nurse, Receptionist, Employee, Archive
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import event

app = Flask(__name__)
app.secret_key = "charles"  # Secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/clinicdb'
db.init_app(app)
app.app_context().push()


# Route for home page
@app.route('/')
def home():
    return render_template('login.html')


# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if user.password.startswith('pbkdf2'):
                if check_password_hash(user.password, password):
                    session['username'] = username
                    session['user_type'] = user.role

                    if user.role == 'admin':
                        admin_admin = Admin.query.filter_by(username=username).first()
                        if admin_admin:
                            if admin_admin.designation == 'Medical Admin':
                                return redirect(url_for('admins_dashboard'))  # Redirect to medical admin dashboard
                            elif admin_admin.designation == 'General Admin':
                                return redirect(url_for('admin_dashboard'))  # Redirect to general admin dashboard
                            else:
                                flash('You are not authorized to access this dashboard.', 'error')
                                return redirect(url_for('login'))
                    else:
                        return redirect(url_for(user.role + '_dashboard'))  # Redirect to other users' dashboards
            else:
                if user.password == password:
                    session['username'] = username
                    session['user_type'] = user.role

                    if user.role == 'admin':
                        admin_admin = Admin.query.filter_by(username=username).first()
                        if admin_admin:
                            if admin_admin.designation == 'Medical Admin':
                                return redirect(url_for('admins_dashboard'))  # Redirect to medical admin dashboard
                            elif admin_admin.designation == 'General Admin':
                                return redirect(url_for('admin_dashboard'))  # Redirect to general admin dashboard
                            else:
                                flash('You are not authorized to access this dashboard.', 'error')
                                return redirect(url_for('login'))
                    else:
                        return redirect(url_for(user.role + '_dashboard'))  # Redirect to other users' dashboards

        flash('Invalid username or password', 'error')

    return render_template('login.html')


# signup route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Extract the form data
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        age = request.form.get('age')
        medical_history = request.form.get('medical_history')
        location = request.form.get('location')
        allergies = request.form.get('allergies')
        blood_group = request.form.get('blood_group')
        image = request.form.get('image')
        role = 'admin'  # Set role to admin
        designation = request.form.get('designation')
        health_condition = request.form.get('health_condition')

        # Perform validation if necessary

        # Hash the password
        # hashed_password = generate_password_hash(password)

        # Create a new user object with the form data
        new_user = User(username=username, password=password, name=name, email=email, phone=phone, gender=gender,
                          age=age, medical_history=medical_history, location=location, allergies=allergies,
                          blood_group=blood_group, image=image, role=role, health_condition=health_condition)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Create a new admin object with the form data
        new_admin = Admin(username=username, designation=designation)

        # Add the new admin to the database
        db.session.add(new_admin)
        db.session.commit()

        # Redirect to the login page after successful signup
        return redirect(url_for('login'))
    else:
        # Render the signup.html template for GET requests
        return render_template('signup.html')


# Route for general admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_user = User.query.filter_by(username=username).first()
        admin_admin = Admin.query.filter_by(username=username).first()
        if admin_user and admin_admin:
            # Check if the designation is 'General Admin'
            if admin_admin.designation == 'General Admin':
                return render_template('admindashboard.html', admin_user=admin_user, admin_admin=admin_admin)
            else:
                flash('You are not authorized to access this dashboard.', 'error')
                return redirect(url_for('login'))
        else:
            flash('No admin details found.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Route for medical admin dashboard
@app.route('/admins_dashboard')
def admins_dashboard():
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_user = User.query.filter_by(username=username).first()
        admin_admin = Admin.query.filter_by(username=username).first()
        if admin_user and admin_admin:
            # Check if the designation is 'Medical Admin'
            if admin_admin.designation == 'Medical Admin':
                return render_template('adminsdashboard.html', admin_user=admin_user, admin_admin=admin_admin)
            else:
                flash('You are not authorized to access this dashboard.', 'error')
                return redirect(url_for('login'))
        else:
            flash('No admin details found.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Route for student dashboard
@app.route('/student_dashboard')
def student_dashboard():
    if 'username' in session and session['user_type'] == 'student':
        username = session['username']
        student_user = User.query.filter_by(username=username).first()
        student_student = Student.query.filter_by(username=username).first()
        if student_user and student_student:
            return render_template('studentdashboard.html', student_user=student_user, student_student=student_student)
        else:
            flash('No student details found.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Route for doctor dashboard
@app.route('/doctor_dashboard')
def doctor_dashboard():
    if 'username' in session and session['user_type'] == 'doctor':
        username = session['username']
        doctor_user = User.query.filter_by(username=username).first()
        doctor_doctor = Doctor.query.filter_by(username=username).first()
        if doctor_user and doctor_doctor:
            return render_template('doctordashboard.html', doctor_user=doctor_user, doctor_doctor=doctor_doctor)
        else:
            flash('No Doctors details found.', 'error')
            return redirect(url_for('login'))
    return redirect(url_for('login'))


# Route for nurse dashboard
@app.route('/nurse_dashboard')
def nurse_dashboard():
    if 'username' in session and session['user_type'] == 'nurse':
        username = session['username']
        nurse_user = User.query.filter_by(username=username).first()
        nurse_nurse = Nurse.query.filter_by(username=username).first()
        if nurse_user and nurse_nurse:
            return render_template('nursedashboard.html', nurse_user=nurse_user, nurse_nurse=nurse_nurse)
        else:
            flash('No Nurse details found.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Route for receptionist dashboard
@app.route('/receptionist_dashboard')
def receptionist_dashboard():
    if 'username' in session and session['user_type'] == 'receptionist':
        username = session['username']
        receptionist_user = User.query.filter_by(username=username).first()
        receptionist_receptionist = Receptionist.query.filter_by(username=username).first()
        if receptionist_user and receptionist_receptionist:
            return render_template('receptionistdashboard.html', receptionist_user=receptionist_user,
                                   receptionist_receptionist=receptionist_receptionist)
        else:
            flash('No Receptionist details found.', 'error')
            return redirect(url_for('login'))
    return redirect(url_for('login'))


# Route for employee dashboard
@app.route('/employee_dashboard')
def employee_dashboard():
    if 'username' in session and session['user_type'] == 'employee':
        username = session['username']
        employee_user = User.query.filter_by(username=username).first()
        employee_employee = Employee.query.filter_by(username=username).first()
        if employee_user and employee_employee:
            return render_template('employeedashboard.html', employee_user=employee_user,
                                   employee_employee=employee_employee)
        else:
            flash('No Employee details found.', 'error')
            return redirect(url_for('login'))
    return redirect(url_for('login'))


# Route for managing users by medical admin
@app.route('/manage_users')
def manage_users():
    return render_template('manageusers.html')


# Route for managing patients (users) accessible only to the medical admin
@app.route('/manage_patients')
def manage_patients():
    # Check if the user is logged in and is a medical admin
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_admin = Admin.query.filter_by(username=username).first()

        # Check if the logged-in admin is a medical admin
        if admin_admin and admin_admin.designation == 'Medical Admin':
            # Query all users from the database
            users = User.query.all()
            return render_template('managepatients.html', users=users)
        else:
            flash('Unauthorized access', 'error')
            return redirect(url_for('login'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for editing patient details
@app.route('/edit_patient', methods=['GET', 'POST'])
def edit_patient():
    # Check if the user is logged in
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the patient from the query parameters
        username = request.args.get('username')

        # Query the database to find the patient by username
        user = User.query.filter_by(username=username).first()

        # If the patient is found
        if user:
            # Render the edit_patient.html template with patient details
            return render_template('edit_patient.html', user=user)
        else:
            flash('No patient details found.', 'error')
            return redirect(url_for('manage_patients'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for updating patient details
@app.route('/update_patient', methods=['POST'])
def update_patient():
    # Check if the user is logged in
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the patient from the form data
        username = request.form['username']

        # Query the database to find the patient by username
        user = User.query.filter_by(username=username).first()

        # If the patient is found
        if user:
            # Update the patient's information with the data from the form
            # user.email = request.form['email']
            # user.phone = request.form['phone']
            # user.gender = request.form['gender']
            # user.age = request.form['age']
            user.medical_history = request.form['medical_history']
            user.health_condition = request.form['health_condition']

            user.allergies = request.form['allergies']
            user.weight = request.form['weight']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('Patient information updated successfully!', 'success')

            # Redirect to the manage_patients route
            return redirect(url_for('manage_patients'))
        else:
            flash('No patient details found.', 'error')
            return redirect(url_for('manage_patients'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


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


# Route for editing admin details
@app.route('/edit_admin')
def edit_admin():
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_user = User.query.filter_by(username=username).first()
        admin_admin = Admin.query.filter_by(username=username).first()
        if admin_user and admin_admin:
            return render_template('edit_admin.html', admin_user=admin_user, admin_admin=admin_admin)
        else:
            flash('No admin details found.', 'error')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Route for updating admin details
@app.route('/update_admin', methods=['POST'])
def update_admin():
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_user = User.query.filter_by(username=username).first()
        if admin_user:
            admin_user.email = request.form['email']
            admin_user.phone = request.form['phone']
            admin_user.location = request.form['location']
            admin_user.medical_history = request.form['medical_history']
            admin_user.allergies = request.form['allergies']
            # admin_user.location = request.form['location']

            db.session.commit()
            flash('Admin information updated successfully.', 'success')
        else:
            flash('No admin details found.', 'error')
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('login'))


# Route for adding a new student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        # Extract weight from form data
        weight = request.form['weight']
        # Convert weight to float
        weight_decimal = float(weight)
        medical_history = request.form['medical_history']
        location = request.form['location']
        allergies = request.form['allergies']
        blood_group = request.form['blood_group']
        health_condition = request.form['health_condition']
        year_of_study = request.form['year_of_study']
        department = request.form['department']

        # Create a new User instance with weight included
        new_user = User(username=username, password=hashed_password, name=name, email=email, phone=phone, gender=gender,
                        age=age, weight=weight_decimal, medical_history=medical_history, location=location, allergies=allergies,
                        blood_group=blood_group, health_condition=health_condition, role='student')

        # Create a new Student instance
        new_student = Student(username=username, year_0f_study=year_of_study, department=department)

        # Add the new user and student to the database session
        db.session.add(new_user)
        db.session.add(new_student)
        db.session.commit()

        flash('New student added successfully.', 'success')
        return redirect(url_for('manage_student'))  # Redirect to the manage students page
    else:
        return render_template('add_student.html')  # Render the form template for adding a new student


# Route for adding a new doctor
@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        medical_history = request.form['medical_history']
        location = request.form['location']
        allergies = request.form['allergies']
        blood_group = request.form['blood_group']
        health_condition = request.form['health_condition']
        designation = request.form['designation']
        schedule = request.form['schedule']
        available = request.form['available']

        years_of_experience = request.form['years_of_experience']

        # Create a new User instance. with hashed password
        new_user = User(
            username=username,
            password=hashed_password,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            medical_history=medical_history,
            location=location,
            allergies=allergies,
            blood_group=blood_group,
            health_condition=health_condition,

            role='doctor'
        )

        # Create a new Doctor instance
        new_doctor = Doctor(
            username=username,
            designation=designation,
            schedule=schedule,
            years_0f_experience=years_of_experience,
            available=available

        )

        # Add the new user and doctor to the database session
        db.session.add(new_user)
        db.session.add(new_doctor)
        db.session.commit()

        flash('New doctor added successfully.', 'success')
        return redirect(url_for('manage_doctor'))  # Redirect to the manage doctors page
    else:
        return render_template('add_doctor.html')  # Render the form template for adding a new doctor.


# Route for adding a new employee
@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        medical_history = request.form['medical_history']
        location = request.form['location']
        allergies = request.form['allergies']
        blood_group = request.form['blood_group']
        health_condition = request.form['health_condition']
        year_of_employment = request.form['year_of_employment']
        designation = request.form['designation']

        # Create a new User instance
        new_user = User(
            username=username,
            password=hashed_password,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            medical_history=medical_history,
            location=location,
            allergies=allergies,
            blood_group=blood_group,
            health_condition=health_condition,
            role='employee'
        )

        # Create a new Employee instance
        new_employee = Employee(
            username=username,
            year_0f_employment=year_of_employment,
            designation=designation
        )

        # Add the new user and employee to the database session
        db.session.add(new_user)
        db.session.add(new_employee)
        db.session.commit()

        flash('New employee added successfully.', 'success')
        return redirect(url_for('manage_employees'))  # Redirect to the manage employees page
    else:
        return render_template('add_employee.html')  # Render the form template for adding a new employee


# Route for adding a new nurse
@app.route('/add_nurse', methods=['GET', 'POST'])
def add_nurse():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        medical_history = request.form['medical_history']
        location = request.form['location']
        allergies = request.form['allergies']
        blood_group = request.form['blood_group']
        health_condition = request.form['health_condition']
        designation = request.form['designation']
        schedule = request.form['schedule']
        available = request.form['available']
        # prescription = request.form['prescription']

        # Create a new User instance for nurse
        new_user = User(
            username=username,
            password=hashed_password,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            medical_history=medical_history,
            location=location,
            allergies=allergies,
            blood_group=blood_group,
            health_condition=health_condition,
            role='nurse'
        )

        # Create a new Nurse instance
        new_nurse = Nurse(
            username=username,
            designation=designation,
            schedule=schedule,
            available=available,
            # prescription=prescription
        )

        # Add the new user and nurse to the database session
        db.session.add(new_user)
        db.session.add(new_nurse)
        db.session.commit()

        flash('New nurse added successfully.', 'success')
        return redirect(url_for('manage_nurse'))  # Redirect to the manage nurses page
    else:
        return render_template('add_nurse.html')  # Render the form template for adding a new nurse.


# Route for adding a new receptionist
@app.route('/add_receptionist', methods=['GET', 'POST'])
def add_receptionist():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        medical_history = request.form['medical_history']
        location = request.form['location']
        allergies = request.form['allergies']
        blood_group = request.form['blood_group']
        health_condition = request.form['health_condition']
        designation = request.form['designation']
        schedule = request.form['schedule']
        available = request.form['available']

        # Create a new receptionist instance
        # Create a new User instance
        new_user = User(
            username=username,
            password=hashed_password,

            name=name,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            medical_history=medical_history,
            location=location,
            allergies=allergies,
            blood_group=blood_group,
            health_condition=health_condition,
            role='receptionist'
        )
        new_receptionist = Receptionist(
            username=username,
            designation=designation,
            schedule=schedule,
            available=available
        )

        # Add the new user and nurse to the database session
        db.session.add(new_user)
        db.session.add(new_receptionist)
        db.session.commit()

        flash('New receptionist added successfully.', 'success')
        return redirect(url_for('manage_receptionist'))  # Redirect to the manage nurses page
    else:
        return render_template('add_receptionist.html')  # Render the form template for adding a new nurse.


# Route for editing student details
@app.route('/edit_student', methods=['GET', 'POST'])
def edit_student():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the student from the session or query parameters
        username = request.args.get('username') if 'username' in request.args else session['username']

        # Query the database to find the student by username
        student = Student.query.filter_by(username=username).first()

        # If the doctor is found
        if student:
            # Check if the user is authorized to edit student details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'student' and session['username'] == username):
                # Render the edit_student.html template with doctor details
                return render_template('edit_student.html', student=student, user_type=session['user_type'])
            else:
                flash('You do not have permission to edit this student\'s details.', 'error')
        else:
            flash('No student details found.', 'error')

        # Redirect to the appropriate page
    return redirect(url_for('manage_student' if session['user_type'] == 'admin' else 'student_dashboard'))


# Route for updating student details
@app.route('/update_student', methods=['POST'])
def update_student():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the student from the form data
        username = request.form['username']

        # Query the database to find the student by username
        student = Student.query.filter_by(username=username).first()

        # If the student is found
        if student:
            # Check if the user is authorized to update student details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'student' and session['username'] == username):

                # Update the student's information with the data from the form
                student.user.email = request.form['email']
                student.user.phone = request.form['phone']
                student.user.location = request.form['location']
                # student.user.medical_history = request.form['medical_history']
                # student.user.allergies = request.form['allergies']
                # student.user.weight = request.form['weight']
                # student.user.health_condition = request.form['health_condition']

                # Commit the changes to the database
                db.session.commit()

                # Flash a success message
                flash('Student information updated successfully!', 'success')

                # Redirect to the appropriate page based on user type
                return redirect(url_for('manage_student') if session['user_type'] == 'admin' else url_for('student_dashboard'))
            else:
                flash('You do not have permission to update this student\'s details.', 'error')
        else:
            flash('No student details found.', 'error')

            # Redirect to the appropriate page based on user type
        return redirect(url_for('manage_student' if session['user_type'] == 'admin' else 'student_dashboard'))
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))


# Route for editing and updating doctor details
@app.route('/edit_doctor', methods=['GET', 'POST'])
def edit_doctor():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the doctor from the query parameters or session
        username = request.args.get('username') if 'username' in request.args else session['username']

        # Query the database to find the doctor by username
        doctor = Doctor.query.filter_by(username=username).first()

        # If the doctor is found
        if doctor:
            # Check if the user is authorized to edit doctor details
            if session['user_type'] == 'admin' or (session['user_type'] == 'doctor' and session['username'] == username):
                # Render the edit_doctor.html template with doctor details
                return render_template('edit_doctor.html', doctor=doctor, user_type=session['user_type'])
            else:
                flash('You do not have permission to edit this doctor\'s details.', 'error')
        else:
            flash('No doctor details found.', 'error')

    # Redirect to the appropriate page
    return redirect(url_for('manage_doctor' if session['user_type'] == 'admin' else 'doctor_dashboard'))


# Route for updating doctor details
@app.route('/update_doctor', methods=['POST'])
def update_doctor():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the doctor from the form data
        username = request.form['username']

        # Query the database to find the doctor by username
        doctor = Doctor.query.filter_by(username=username).first()

        # If the doctor is found
        if doctor:
            # Check if the user is authorized to update doctor details
            if session['user_type'] == 'admin' or (session['user_type'] == 'doctor' and session['username'] == username):
                # Update the doctor's information with the data from the form

                doctor.user.email = request.form['email']
                doctor.user.phone = request.form['phone']
                doctor.user.location = request.form['location']
                doctor.schedule = request.form['schedule']
                # doctor.user.medical_history = request.form['medical_history']
                # doctor.user.allergies = request.form['allergies']
                # doctor.user.health_condition = request.form['health_condition']
                doctor.available = request.form['available']

                # Commit the changes to the database
                db.session.commit()

                # Flash a success message
                flash('Doctor information updated successfully!', 'success')

                # Redirect to the appropriate page based on user type
                return redirect(url_for('manage_doctor' if session['user_type'] == 'admin' else 'doctor_dashboard'))
            else:
                flash('You do not have permission to update this doctor\'s details.', 'error')
        else:
            flash('No doctor details found.', 'error')

    # Redirect to the appropriate page
    return redirect(url_for('manage_doctor' if session['user_type'] == 'admin' else 'doctor_dashboard'))


# Route for editing receptionist details
@app.route('/edit_receptionist', methods=['GET', 'POST'])
def edit_receptionist():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the receptionist from the session or query parameters
        username = request.args.get('username') if 'username' in request.args else session['username']

        # Query the database to find the receptionist by username
        receptionist = Receptionist.query.filter_by(username=username).first()

        # If the receptionist is found
        if receptionist:
            # Check if the user is authorized to edit receptionist details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'receptionist' and session['username'] == username):
                # Render the edit_receptionist.html template with receptionist details
                return render_template('edit_receptionist.html',
                                       receptionist=receptionist, user_type=session['user_type'])
            else:
                flash('You do not have permission to edit this receptionist\'s details.', 'error')
        else:
            flash('No receptionist details found.', 'error')

        # Redirect to the appropriate page
    return redirect(url_for('manage_receptionist' if session['user_type'] == 'admin' else 'receptionist_dashboard'))


# Route for updating receptionist details
@app.route('/update_receptionist', methods=['POST'])
def update_receptionist():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the receptionist from the form data
        username = request.form['username']

        # Query the database to find the nurse by username
        receptionist = Receptionist.query.filter_by(username=username).first()

        # If the receptionist is found
        if receptionist:
            # Check if the user is authorized to update receptionist details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'receptionist' and session['username'] == username):

                # Update the receptionist information with the data from the form
                receptionist.user.email = request.form['email']
                receptionist.user.phone = request.form['phone']
                receptionist.user.location = request.form['location']
                # receptionist.user.medical_history = request.form['medical_history']
                # receptionist.user.allergies = request.form['allergies']
                # receptionist.user.health_condition = request.form['health_condition']
                receptionist.schedule = request.form['schedule']
                receptionist.available = request.form['available']

                # Commit the changes to the database
                db.session.commit()

                # Flash a success message
                flash('receptionist information updated successfully!', 'success')

                # Redirect to the appropriate page based on user type
                return redirect(url_for('manage_receptionist') if session['user_type'] == 'admin'
                                else url_for('receptionist_dashboard'))
            else:
                flash('You do not have permission to update this receptionist\'s details.', 'error')
        else:
            flash('No receptionist details found.', 'error')

            # Redirect to the appropriate page based on user type
        return redirect(url_for('manage_receptionist' if session['user_type'] == 'admin' else 'receptionist_dashboard'))
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))


# Route for editing nurse details
@app.route('/edit_nurse', methods=['GET', 'POST'])
def edit_nurse():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the nurse from the session or query parameters
        username = request.args.get('username') if 'username' in request.args else session['username']

        # Query the database to find the nurse by username
        nurse = Nurse.query.filter_by(username=username).first()

        # If the nurse is found
        if nurse:
            # Check if the user is authorized to edit nurse details, either admin or nurse
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'nurse' and session['username'] == username):
                # Render the edit_nurse.html template with nurse details
                return render_template('edit_nurse.html', nurse=nurse, user_type=session['user_type'])
            else:
                flash('You do not have permission to edit this nurse\'s details.', 'error')
        else:
            flash('No nurse details found.', 'error')

        # Redirect to the appropriate page
    return redirect(url_for('manage_nurse' if session['user_type'] == 'admin' else 'nurse_dashboard'))


# Route for updating nurse details
@app.route('/update_nurse', methods=['POST'])
def update_nurse():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the nurse from the form data
        username = request.form['username']

        # Query the database to find the nurse by username
        nurse = Nurse.query.filter_by(username=username).first()

        # If the nurse is found
        if nurse:
            # Check if the user is authorized to update nurse details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'nurse' and session['username'] == username):

                # Update the nurse information with the data from the form
                nurse.user.email = request.form['email']
                nurse.user.phone = request.form['phone']
                nurse.user.location = request.form['location']
                # nurse.user.medical_history = request.form['medical_history']
                # nurse.user.allergies = request.form['allergies']
                # nurse.user.health_condition = request.form['health_condition']
                nurse.schedule = request.form['schedule']
                nurse.available = request.form['available']

                # Commit the changes to the database
                db.session.commit()

                # Flash a success message
                flash('nurse information updated successfully!', 'success')

                # Redirect to the appropriate page based on user type
                return redirect(url_for('manage_nurse') if session['user_type'] == 'admin'
                                else url_for('nurse_dashboard'))
            else:
                flash('You do not have permission to update this nurse\'s details.', 'error')
        else:
            flash('No nurse details found.', 'error')

            # Redirect to the appropriate page based on user type
        return redirect(url_for('manage_nurse' if session['user_type'] == 'admin' else 'nurse_dashboard'))
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))


# Route for editing employee details
@app.route('/edit_employee', methods=['GET', 'POST'])
def edit_employee():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the employee from the session or query parameters
        username = request.args.get('username') if 'username' in request.args else session['username']

        # Query the database to find the employee by username
        employee = Employee.query.filter_by(username=username).first()

        # If the employee is found
        if employee:
            # Check if the user is authorized to edit employee details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'employee' and session['username'] == username):
                # Render the edit_employee.html template with doctor details
                return render_template('edit_employee.html', employee=employee, user_type=session['user_type'])
            else:
                flash('You do not have permission to edit this employee\'s details.', 'error')
        else:
            flash('No employee details found.', 'error')

        # Redirect to the appropriate page
    return redirect(url_for('manage_employees' if session['user_type'] == 'admin' else 'employee_dashboard'))


# Route for updating employee details
@app.route('/update_employee', methods=['POST'])
def update_employee():
    # Check if the user is logged in
    if 'username' in session:
        # Get the username of the employee from the form data
        username = request.form['username']

        # Query the database to find the employee by username
        employee = Employee.query.filter_by(username=username).first()

        # If the employee is found
        if employee:
            # Check if the user is authorized to update employee details
            if session['user_type'] == 'admin' or (
                    session['user_type'] == 'employee' and session['username'] == username):

                # Update the employee information with the data from the form
                employee.user.email = request.form['email']
                employee.user.phone = request.form['phone']
                employee.user.location = request.form['location']
                # employee.user.medical_history = request.form['medical_history']
                # employee.user.allergies = request.form['allergies']
                # employee.user.health_condition = request.form['health_condition']

                # Commit the changes to the database
                db.session.commit()

                # Flash a success message
                flash('employee information updated successfully!', 'success')

                # Redirect to the appropriate page based on user type
                return redirect(url_for('manage_employees') if session['user_type'] == 'admin'
                                else url_for('employee_dashboard'))
            else:
                flash('You do not have permission to update this employee\'s details.', 'error')
        else:
            flash('No employee details found.', 'error')

            # Redirect to the appropriate page based on user type
        return redirect(url_for('manage_employee' if session['user_type'] == 'admin' else 'employee_dashboard'))
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))


# Route for deleting a student (confirmation page)
@app.route('/confirm_delete_student')
def confirm_delete_student():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.args.get('username')

        student = Student.query.filter_by(username=username).first()
        if student:
            return render_template('delete_student.html', student_username=username,
                                   student_name=student.user.name,
                                   student_department=student.department)
        else:
            flash('Student not found.', 'error')
            return redirect(url_for('manage_student'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting student
@app.route('/delete_student', methods=['POST'])
def delete_student():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        student = Student.query.filter_by(username=username).first()
        if student:
            try:
                # Perform cascading delete by first deleting related data
                # Assuming there's a User model related to the student
                User.query.filter_by(username=username).delete()
                # Now delete the student from the student table
                db.session.delete(student)
                db.session.commit()
                flash('Student account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash('Error deleting student account: {}'.format(str(e)), 'error')
        else:
            flash('student not found.', 'error')
        return redirect(url_for('manage_student'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting a receptionist (confirmation page)
@app.route('/confirm_delete_receptionist')
def confirm_delete_receptionist():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.args.get('username')

        receptionist = Receptionist.query.filter_by(username=username).first()
        if receptionist:
            return render_template('delete_receptionist.html', receptionist_username=username,
                                   receptionist_name=receptionist.user.name,
                                   receptionist_designation=receptionist.designation)
        else:
            flash('Receptionist not found.', 'error')
            return redirect(url_for('manage_receptionist'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting receptionist
@app.route('/delete_receptionist', methods=['POST'])
def delete_receptionist():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        receptionist = Receptionist.query.filter_by(username=username).first()
        if receptionist:
            try:
                # Perform cascading delete by first deleting related data
                # Assuming there's a User model related to the Receptionist
                User.query.filter_by(username=username).delete()
                # Now delete the receptionist from the Receptionist table
                db.session.delete(receptionist)
                db.session.commit()
                flash('Receptionist account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash('Error deleting receptionist account: {}'.format(str(e)), 'error')
        else:
            flash('Receptionist not found.', 'error')
        return redirect(url_for('manage_receptionist'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting a doctor (confirmation page)
@app.route('/confirm_delete_doctor')
def confirm_delete_doctor():
    # check if the logged-in user has admin privileges
    if 'username' in session and session['user_type'] == 'admin':

        # RETRIEVING USER USERNAME FROM URL ARGUMENT
        username = request.args.get('username')

        # FINDING THE USER
        doctor = Doctor.query.filter_by(username=username).first()
        if doctor:
            # render the user confirmation template and pass user data to template
            return render_template('delete_doctor.html', doctor_username=username,
                                   doctor_name=doctor.user.name,
                                   doctor_designation=doctor.designation)
        else:
            flash('Doctor not found.', 'error')
            return redirect(url_for('manage_doctor'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting doctor
@app.route('/delete_doctor', methods=['POST'])
def delete_doctor():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        doctor = Doctor.query.filter_by(username=username).first()
        if doctor:
            try:
                # Perform cascading delete by first deleting related data
                # Assuming there's a User model related to the Doctor
                User.query.filter_by(username=username).delete()
                # Now delete the doctor from the Receptionist table
                db.session.delete(doctor)
                db.session.commit()
                flash('Doctor account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash('Error deleting doctor account: {}'.format(str(e)), 'error')
        else:
            flash('Doctor not found.', 'error')
        return redirect(url_for('manage_doctor'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting a nurse (confirmation page)
@app.route('/confirm_delete_nurse')
def confirm_delete_nurse():
    # check if the logged-in user has admin privileges
    if 'username' in session and session['user_type'] == 'admin':

        # RETRIEVING USER USERNAME FROM URL ARGUMENT
        username = request.args.get('username')

        # FINDING THE USER
        nurse = Nurse.query.filter_by(username=username).first()
        if nurse:
            # render the user confirmation template and pass user data to template
            return render_template('delete_nurse.html', nurse_username=username,
                                   nurse_name=nurse.user.name,
                                   nurse_designation=nurse.designation)
        else:
            flash('Nurse not found.', 'error')
            return redirect(url_for('manage_nurse'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting nurse
@app.route('/delete_nurse', methods=['POST'])
def delete_nurse():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        nurse = Nurse.query.filter_by(username=username).first()
        if nurse:
            try:
                # Perform cascading delete by first deleting related data
                # Assuming there's a User model related to the Nurse
                User.query.filter_by(username=username).delete()
                # Now delete the doctor from the Receptionist table
                db.session.delete(nurse)
                db.session.commit()
                flash(' Nurse account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash('Error deleting doctor account: {}'.format(str(e)), 'error')
        else:
            flash('Nurse not found.', 'error')
        return redirect(url_for('manage_nurse'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting an employee (confirmation page)
@app.route('/confirm_delete_employee')
def confirm_delete_employee():
    # check if the logged-in user has admin privileges
    if 'username' in session and session['user_type'] == 'admin':

        # RETRIEVING USER USERNAME FROM URL ARGUMENT
        username = request.args.get('username')

        # FINDING THE USER
        employee = Employee.query.filter_by(username=username).first()
        if employee:
            # render the user confirmation template and pass user data to template
            return render_template('delete_employee.html', employee_username=username,
                                   employee_name=employee.user.name,
                                   employee_designation=employee.designation)
        else:
            flash('Employee not found.', 'error')
            return redirect(url_for('manage_employees'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for deleting employee
@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        employee = Employee.query.filter_by(username=username).first()
        if employee:
            try:
                # Perform cascading delete by first deleting related data
                # Assuming there's a User model related to the Doctor
                User.query.filter_by(username=username).delete()
                # Now delete the doctor from the Receptionist table
                db.session.delete(employee)
                db.session.commit()
                flash(' Employee account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash('Error deleting employee account: {}'.format(str(e)), 'error')
        else:
            flash('Employee not found.', 'error')
        return redirect(url_for('manage_employees'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Function to archive user details before deletion
def archive_user(user):
    if user:
        # Create an archive entry with user details
        archive_entry = Archive(
            username=user.username,
            name=user.name,
            email=user.email,
            phone=user.phone,
            location=user.location,
            # Add other user details as needed
        )
        # Add the archive entry to the database session
        db.session.add(archive_entry)
        db.session.commit()


# Routes for confirming and deleting users
@app.route('/confirm_delete_user/<user_type>')
def confirm_delete_user(user_type):
    if 'username' in session and session['user_type'] == 'admin':
        username = request.args.get('username')

        # Determine the model based on the user type
        if user_type == 'student':
            user = Student.query.filter_by(username=username).first()
        elif user_type == 'receptionist':
            user = Receptionist.query.filter_by(username=username).first()
        elif user_type == 'doctor':
            user = Doctor.query.filter_by(username=username).first()
        elif user_type == 'nurse':
            user = Nurse.query.filter_by(username=username).first()
        elif user_type == 'employee':
            user = Employee.query.filter_by(username=username).first()
        else:
            flash('Invalid user type', 'error')
            return redirect(url_for('manage_users'))

        if user:
            return render_template('confirm_delete_user.html', user_type=user_type, username=username)
        else:
            flash('User not found.', 'error')
            return redirect(url_for('manage_users'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


@app.route('/delete_user/<user_type>', methods=['POST'])
def delete_user(user_type):
    if 'username' in session and session['user_type'] == 'admin':
        username = request.form.get('username')  # Retrieve username from the form data

        # Determine the model based on the user type
        if user_type == 'student':
            user = Student.query.filter_by(username=username).first()
        elif user_type == 'receptionist':
            user = Receptionist.query.filter_by(username=username).first()
        elif user_type == 'doctor':
            user = Doctor.query.filter_by(username=username).first()
        elif user_type == 'nurse':
            user = Nurse.query.filter_by(username=username).first()
        elif user_type == 'employee':
            user = Employee.query.filter_by(username=username).first()
        else:
            flash('Invalid user type', 'error')
            return redirect(url_for('manage_users'))

        if user:
            try:
                # Archive the user details
                archive_user(user)

                # Delete the user
                db.session.delete(user)
                db.session.commit()
                flash(f'{user_type.capitalize()} account deleted successfully.', 'success')
            except Exception as e:
                db.session.rollback()  # Rollback changes in case of error
                flash(f'Error deleting {user_type} account: {str(e)}', 'error')
        else:
            flash('User not found.', 'error')

        return redirect(url_for(f'manage_{user_type}s'))
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for appointment
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if 'username' in session:  # Check if user is logged in
        if request.method == 'POST':
            # Retrieve form data
            date = request.form['date']
            time = request.form['time']
            staff_type = request.form['staff_type']
            designation = request.form['designation']

            # Redirect to scheduleappointment with form data
            return redirect(url_for('scheduleappointment', date=date, time=time, staff_type=staff_type, designation=designation))
        else:
            return render_template('appointment.html')
    else:
        flash('Please log in to access this page', 'error')
        return redirect(url_for('login'))


# Route for scheduleappointment
@app.route('/scheduleappointment', methods=['GET', 'POST'])
def scheduleappointment():
    if 'username' in session:  # Check if user is logged in
        if request.method == 'GET':
            # Retrieve form data from URL parameters
            date = request.args.get('date')
            time = request.args.get('time')
            staff_type = request.args.get('staff_type')
            designation = request.args.get('designation')

            # Query the database to get available staff members with the specified designation
            if staff_type == 'Doctor':
                staff_members = User.query.join(Doctor).filter(Doctor.designation == designation, Doctor.available == 'Yes').all()
            elif staff_type == 'Nurse':
                staff_members = User.query.join(Nurse).filter(Nurse.designation == designation, Nurse.available == 'Yes').all()

            return render_template('scheduleappointment.html', date=date, time=time, staff_type=staff_type, designation=designation, staff_members=staff_members)
    else:
        flash('Please log in to access this page', 'error')
        return redirect(url_for('login'))


@app.route('/confirmappointment', methods=['POST'])
def confirm_appointment():
    if request.method == 'POST':
        # Retrieve the selected staff member's username, date, and time from the form submission
        selected_staff_username = request.form.get('confirm_staff')
        appointment_date = request.form.get('date')
        appointment_time = request.form.get('time')

        # Query the database to get details of the selected staff member
        selected_staff_member = User.query.filter_by(username=selected_staff_username).first()

        if selected_staff_member:
            # Render the confirmation page with details of the selected staff member and appointment
            return render_template('confirmappointment.html', staff_member=selected_staff_member, appointment_date=appointment_date, appointment_time=appointment_time)
        else:
            # If the selected staff member is not found, redirect to an error page or handle accordingly
            return render_template('error.html', message='Selected staff member not found')
    else:
        # If the request method is not POST, redirect to an error page or handle accordingly
        return render_template('error.html', message='Invalid request method')


# Flask route for helping receptionist search user by username
@app.route('/search_user', methods=['POST'])
def search_user():
    if request.method == 'POST':
        username = request.form.get('username')

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        if user:
            # Render a new template to display user details
            return render_template('user_details.html', user=user)
        else:
            flash('User not found.', 'error')
            return redirect(url_for('receptionist_dashboard'))


# Route for handling appointment requests
@app.route('/mission', methods=['GET'])
def mission():
    return render_template('mission.html')


# Route for handling appointment requests
@app.route('/vision', methods=['GET'])
def vision():
    return render_template('vision.html')


# Route for handling appointment requests
@app.route('/corevalues', methods=['GET'])
def corevalues():
    return render_template('corevalues.html')


# Route for handling appointment requests
@app.route('/contactus', methods=['GET'])
def contactus():
    return render_template('contactus.html')


# Flask route for surgeon dashboard to be viewed by surgeon doctors only
@app.route('/surgeon_dashboard')
def surgeon_dashboard():
    role = session.get('role', None)
    users_with_injuries = User.query.filter_by(health_condition='injuries').all()
    return render_template('surgeon_dashboard.html', users_with_injuries=users_with_injuries, role=role)


# Flask route for  allowing doctor to view surgical nurses
@app.route('/viewsurgicalnurse')
def viewsurgicalnurse():
    surgical_nurse = Nurse.query.filter(Nurse.designation.in_(['surgical nurse', 'orthopedic',
                                                               'emergency room nurse'])).all()

    return render_template('viewsurgicalnurse.html',  surgical_nurse=surgical_nurse)


# Flask route for  allergist_dashboard
@app.route('/allergist_dashboard')
def allergist_dashboard():
    users_with_allergies = User.query.filter_by(health_condition='allergic').all()
    return render_template('allergist_dashboard.html', users_with_allergies=users_with_allergies)


# Flask route for viewing nurses
@app.route('/viewallergyspecialist')
def viewallergyspecialist():
    allergy_specialist = Nurse.query.filter(Nurse.designation.in_(['allergy specialist'])).all()

    return render_template('viewallergyspecialist.html',  allergy_specialist=allergy_specialist)


# Flask route for  dashboard
@app.route('/gynecologist_dashboard')
def gynecologist_dashboard():
    users_with_reproduction_issues = User.query.filter_by(health_condition='reproductive').all()
    return render_template('gynecologist_dashboard.html', users_with_reproduction_issues=users_with_reproduction_issues)


# Flask route for  dashboard
@app.route('/gp_dashboard')
def gp_dashboard():
    users_with_other = User.query.filter_by(health_condition='other').all()
    return render_template('gp_dashboard.html', users_with_other=users_with_other)


# Flask route for surgical nurse dashboard
@app.route('/surgicalnurse_dashboard')
def surgicalnurse_dashboard():
    role = session.get('role', None)
    users_with_injuries = User.query.filter_by(health_condition='injuries').all()
    return render_template('surgicalnurse_dashboard.html', users_with_injuries=users_with_injuries, role=role)


# Flask route for viewing surgeon doctors
@app.route('/viewsurgeon')
def viewsurgeon():
    surgeon = Doctor.query.filter(Doctor.designation.in_(['surgeon'])).all()
    return render_template('viewsurgeon.html',  surgeon=surgeon)


# Flask route for  nurse allergist_dashboard
@app.route('/allergyspecialist_dashboard')
def allergyspecialist_dashboard():
    users_with_allergies = User.query.filter_by(health_condition='allergic').all()
    return render_template('allergyspecialist_dashboard.html', users_with_allergies=users_with_allergies)


# Flask route for viewing surgeon doctors
@app.route('/viewallergist')
def viewallergist():
    allergist = Doctor.query.filter(Doctor.designation.in_(['allergist'])).all()
    return render_template('viewallergist.html',  allergist=allergist)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Retrieve the username and email entered by the user
        username = request.form.get('username')
        email = request.form.get('email')

        # Check if the username and email exist in the database
        user = User.query.filter_by(username=username, email=email).first()

        if user:
            # Display a confirmation message with the user's name
            name = user.name
            return render_template('confirm_password_reset.html', name=name)
        else:
            flash('No account found with that username and email address.', 'error')
            return redirect(url_for('forgot_password'))

    return render_template('forgot_password.html')


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        # Extract the username, email, and new password from the form
        username = request.form.get('username')
        email = request.form.get('email')
        new_password = request.form.get('new_password')

        # Perform any necessary validation, such as checking if the username and email match

        # Query the user by username and email
        user = User.query.filter_by(username=username, email=email).first()
        if user:
            # Update the password for the user
            user.password = new_password
            db.session.commit()

            # Redirect to the login page after successful password reset
            flash('Password reset successful. Please log in with your new password.', 'success')
            return redirect(url_for('login'))
        else:
            # Handle the case where the username and email do not match any user
            flash('Invalid username or email. Please try again.', 'error')
            return redirect(url_for('forgot_password'))
    else:
        # Render the reset password form for GET requests
        return render_template('confirm_password_reset.html')


# Define route for adding a patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Extract user input from the form
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        age = request.form.get('age')
        medical_history = request.form.get('medical_history')
        location = request.form.get('location')
        allergies = request.form.get('allergies')
        blood_group = request.form.get('blood_group')
        image = request.form.get('image')
        role = 'patient'  # Assuming patients are added by receptionists
        health_condition = request.form.get('health_condition')

        # Create a new patient record in the database
        new_patient = User(username=username, password=password, name=name, email=email,
                           phone=phone, gender=gender, age=age, medical_history=medical_history,
                           location=location, allergies=allergies, blood_group=blood_group,
                           image=image, role=role, health_condition=health_condition)

        # Add the new patient to the database session and commit
        db.session.add(new_patient)
        db.session.commit()

        # Redirect to receptionist profile page or any other desired page
        return redirect(url_for('receptionist_dashboard'))

    # Render the form for adding a new patient
    return render_template('add_patient.html')


# Define the route to handle notifications
@app.route('/notifications')
def notifications():
    # Retrieve appointment information from the database
    appointment_info = get_appointment_info()  # Assuming you have a method to retrieve appointment info
    return render_template('notifications.html', appointment_info=appointment_info)


# Define a function to retrieve appointment information from the database
def get_appointment_info():
    # Write code here to query your database and retrieve appointment information
    # For example:
    appointment_info = {
        'date_and_time': '2024-03-01 09:00 AM',
        'doctor_name': 'Dr. John Doe',
        'doctor_email': 'john.doe@example.com',
        'doctor_phone': '123-456-7890'
    }
    return appointment_info


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
