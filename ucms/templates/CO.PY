from flask import Flask, render_template, request, session, redirect, url_for, flash
from models import db, User, Admin, Doctor, Student, Nurse, Receptionist, Employee
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "charles"  # Secret key for session management
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/clinic'
db.init_app(app)
app.app_context().push()


# Route for home page
@app.route('/')
def home():
    return render_template('login.html')


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password), password):
            session['username'] = username
            session['user_type'] = user.role
            if user.role == 'admin':
                # Redirect to admin dashboard
                admin_user = user.query.filter_by(username=username).first()
                admin_admin = Admin.query.filter_by(username=username).first()
                return redirect(url_for('admin_dashboard', admin_user=admin_user, admin_admin=admin_admin))
            elif user.role == 'student':
                # Redirect to student dashboard
                student_user = user.query.filter_by(username=username).first()
                student_student = Student.query.filter_by(username=username).first()
                return redirect(
                    url_for('student_dashboard', student_user=student_user, student_student=student_student))
            elif user.role == 'doctor':
                # Redirect to doctor dashboard
                doctor_user = User.query.filter_by(username=username).first()
                doctor_doctor = Doctor.query.filter_by(username=username).first()
                return redirect(url_for('doctor_dashboard', doctor_user=doctor_user, doctor_doctor=doctor_doctor))
            elif user.role == 'nurse':
                # Redirect to nurse dashboard
                nurse_user = User.query.filter_by(username=username).first()
                nurse_nurse = Nurse.query.filter_by(username=username).first()
                return redirect(url_for('nurse_dashboard', nurse_user=nurse_user, nurse_nurse=nurse_nurse))
            elif user.role == 'receptionist':
                # Redirect to receptionist dashboard
                receptionist_user = User.query.filter_by(username=username).first()
                receptionist_receptionist = Receptionist.query.filter_by(username=username).first()
                return redirect(url_for('receptionist_dashboard', receptionist_user=receptionist_user,
                                        receptionist_receptionist=receptionist_receptionist))
            elif user.role == 'employee':
                # Redirect to employee dashboard
                employee_user = User.query.filter_by(username=username).first()
                employee_employee = Employee.query.filter_by(username=username).first()
                return redirect(
                    url_for('employee_dashboard', employee_user=employee_user, employee_employee=employee_employee))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


# Route for admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' in session and session['user_type'] == 'admin':
        username = session['username']
        admin_user = User.query.filter_by(username=username).first()
        admin_admin = Admin.query.filter_by(username=username).first()
        if admin_user and admin_admin:
            return render_template('admindashboard.html', admin_user=admin_user, admin_admin=admin_admin)
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


# Route for managing users
@app.route('/manage_users')
def manage_users():
    return render_template('manageusers.html')


# Route for managing students
@app.route('/manage_students')
def manage_student():
    if 'username' in session and session['user_type'] == 'admin':
        students = db.session.query(Student, User.name, User.email, User.phone, User.location, Student.department,
                                    Student.year_0f_study, User.medical_history, User.blood_group, User.health_condition,
                                    User.allergies).join(User).all()
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
                                  User.health_condition, User.allergies).join(User).all()
        return render_template('managedoctors.html', doctor=doctor)
    else:
        flash('Unauthorized access', 'error')
        return redirect(url_for('login'))


# Route for managing nurses
@app.route('/manage_nurses')
def manage_nurse():
    if 'username' in session and session['user_type'] == 'admin':
        nurse = db.session.query(Nurse, User.name, User.email, User.phone, User.location, Nurse.designation,
                                 Nurse.prescription, Nurse.schedule, User.medical_history,
                                 User.blood_group, User.health_condition, User.allergies).join(User).all()
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
                                    User.health_condition, User.allergies).join(User).all()
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
                                        User.blood_group, User.health_condition, User.allergies).join(User).all()
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
        year_of_study = request.form['year_of_study']
        department = request.form['department']

        # Create a new User instance
        new_user = User(username=username, password=password, name=name, email=email, phone=phone, gender=gender,
                        age=age, medical_history=medical_history, location=location, allergies=allergies,
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
        years_of_experience = request.form['years_of_experience']

        # Create a new User instance with hashed password
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
            years_0f_experience=years_of_experience
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
            password=password,
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
        prescription = request.form['prescription']

        # Create a new User instance
        new_user = User(
            username=username,
            password=password,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            age=age,
            medical_history=medical_history,
            location=location,
            allergies=allergies,
            blood_group=blood_group,
            health_condtion=health_condition,
            role='nurse'
        )

        # Create a new Nurse instance
        new_nurse = Nurse(
            username=username,
            designation=designation,
            schedule=schedule,
            prescription=prescription
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

        # Create a new receptionist instance
        # Create a new User instance
        new_user = User(
            username=username,
            password=password,
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
            schedule=schedule
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
@app.route('/edit_student')
def edit_student():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the student from the query parameters
        username = request.args.get('username')

        # Query the database to find the student by username
        student = Student.query.filter_by(username=username).first()

        # If the student is found
        if student:
            # Query the associated user details
            user = User.query.filter_by(username=username).first()

            # Render the edit_student.html template with student and user details
            return render_template('edit_student.html', student=student, user=user)
        else:
            # If no student is found, redirect to the manage student page with an error flash message
            flash('No student details found.', 'error')
            return redirect(url_for('manage_student'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for updating student details
@app.route('/update_student', methods=['POST'])
def update_student():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the student from the form data
        username = request.form['username']

        # Query the database to find the student by username
        student = Student.query.filter_by(username=username).first()

        # If the student is found
        if student:
            # Update the student's information with the data from the form
            student.department = request.form['department']

            # Update the associated user details with the data from the form
            student.user.email = request.form['email']
            student.user.phone = request.form['phone']
            student.user.location = request.form['location']
            student.user.medical_history = request.form['medical_history']
            # student.user.blood_group = request.form['blood_group']
            student.user.allergies = request.form['allergies']
            student.user.health_condition = request.form['health_condition']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('Student information updated successfully!', 'success')
        else:
            # If no student is found, flash an error message
            flash('No student details found.', 'error')

        # Redirect to the manage student page
        return redirect(url_for('manage_student'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for editing doctor details
@app.route('/edit_doctor')
def edit_doctor():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the doctor from the query parameters
        username = request.args.get('username')

        # Query the database to find the doctor by username
        doctor = Doctor.query.filter_by(username=username).first()

        # If the doctor is found
        if doctor:
            # Query the associated user details
            user = User.query.filter_by(username=username).first()

            # Render the edit_doctor.html template with doctor and user details
            return render_template('edit_doctor.html', doctor=doctor, user=user)
        else:
            # If no doctor is found, redirect to the manage doctor page with an error flash message
            flash('No doctor details found.', 'error')
            return redirect(url_for('manage_doctor'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for updating doctor details
@app.route('/update_doctor', methods=['POST'])
def update_doctor():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the doctor from the form data
        username = request.form['username']

        # Query the database to find the doctor by username
        doctor = Doctor.query.filter_by(username=username).first()

        # If the doctor is found
        if doctor:
            # Update the associated user details with the data from the form
            doctor.user.email = request.form['email']
            doctor.user.phone = request.form['phone']
            doctor.user.location = request.form['location']
            doctor.user.medical_history = request.form['medical_history']
            doctor.user.allergies = request.form['allergies']
            doctor.user.health_condition = request.form['health_condition']

            # doctor.doctor.schedule = request.form['schedule']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('Doctor information updated successfully!', 'success')
        else:
            # If no doctor is found, flash an error message
            flash('No doctor details found.', 'error')

        # Redirect to the manage doctor page
        return redirect(url_for('manage_doctor'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for editing receptionist details
@app.route('/edit_receptionist')
def edit_receptionist():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the receptionist from the query parameters
        username = request.args.get('username')

        # Query the database to find the receptionist by username
        receptionist = Receptionist.query.filter_by(username=username).first()

        # If the receptionist is found
        if receptionist:
            # Query the associated user details
            user = User.query.filter_by(username=username).first()

            # Render the edit_receptionist.html template with doctor and user details
            return render_template('edit_receptionist.html', receptionist=receptionist, user=user)
        else:
            # If no receptionist is found, redirect to the manage receptionist page with an error flash message
            flash('No receptionist details found.', 'error')
            return redirect(url_for('manage_receptionist'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for updating receptionist details
@app.route('/update_receptionist', methods=['POST'])
def update_receptionist():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the doctor from the form data
        username = request.form['username']

        # Query the database to find the receptionist by username
        receptionist = Receptionist.query.filter_by(username=username).first()

        # If the doctor is found
        if receptionist:
            # Update the associated user details with the data from the form
            receptionist.user.email = request.form['email']
            receptionist.user.phone = request.form['phone']
            receptionist.user.location = request.form['location']
            receptionist.user.medical_history = request.form['medical_history']
            receptionist.user.allergies = request.form['allergies']
            receptionist.user.health_condition = request.form['health_condition']

            receptionist.user.schedule = request.form['schedule']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('Receptionist information updated successfully!', 'success')
        else:
            # If no receptionist is found, flash an error message
            flash('No receptionist details found.', 'error')

        # Redirect to the manage receptionist page
        return redirect(url_for('manage_receptionist'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for editing nurse details
@app.route('/edit_nurse')
def edit_nurse():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the nurse from the query parameters
        username = request.args.get('username')

        # Query the database to find the nurse by username
        nurse = Nurse.query.filter_by(username=username).first()

        # If the doctor is found
        if nurse:
            # Query the associated user details
            user = User.query.filter_by(username=username).first()

            # Render the edit_nurse.html template with nurse and user details
            return render_template('edit_nurse.html', nurse=nurse, user=user)
        else:
            # If no nurse is found, redirect to the manage nurse page with an error flash message
            flash('No Nurse details found.', 'error')
            return redirect(url_for('manage_nurse'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for updating nurse details
@app.route('/update_nurse', methods=['POST'])
def update_nurse():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the nurse from the form data
        username = request.form['username']

        # Query the database to find the doctor by username
        nurse = Nurse.query.filter_by(username=username).first()

        # If the doctor is found
        if nurse:
            # Update the associated user details with the data from the form
            nurse.user.email = request.form['email']
            nurse.user.phone = request.form['phone']
            nurse.user.location = request.form['location']
            nurse.user.medical_history = request.form['medical_history']
            nurse.user.allergies = request.form['allergies']
            nurse.user.health_condition = request.form['health_condition']

            # nurse.user.schedule = request.form['schedule']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('nurse information updated successfully!', 'success')
        else:
            # If no nurse is found, flash an error message
            flash('No doctor details found.', 'error')

        # Redirect to the manage nurse page
        return redirect(url_for('manage_nurse'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for editing employee details
@app.route('/edit_employee')
def edit_employee():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the doctor from the query parameters
        username = request.args.get('username')

        # Query the database to find the employee by username
        employee = Employee.query.filter_by(username=username).first()

        # If the doctor is found
        if employee:
            # Query the associated user details
            user = User.query.filter_by(username=username).first()

            # Render the edit_employee.html template with employee and user details
            return render_template('edit_employee.html', employee=employee, user=user)
        else:
            # If no employee is found, redirect to the manage doctor page with an error flash message
            flash('No employee details found.', 'error')
            return redirect(url_for('manage_employee'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
        return redirect(url_for('login'))


# Route for updating employee details
@app.route('/update_employee', methods=['POST'])
def update_employee():
    # Check if the user is logged in and has admin privileges
    if 'username' in session and session['user_type'] == 'admin':
        # Get the username of the employee from the form data
        username = request.form['username']

        # Query the database to find the doctor by username
        employee = Employee.query.filter_by(username=username).first()

        # If the doctor is found
        if employee:
            # Update the associated user details with the data from the form
            employee.user.email = request.form['email']
            employee.user.phone = request.form['phone']
            employee.user.location = request.form['location']
            employee.user.medical_history = request.form['medical_history']
            employee.user.allergies = request.form['allergies']
            employee.user.health_condition = request.form['health_condition']

            # Commit the changes to the database
            db.session.commit()

            # Flash a success message
            flash('Employee information updated successfully!', 'success')
        else:
            # If no employee is found, flash an error message
            flash('No employee details found.', 'error')

        # Redirect to the manage employee page
        return redirect(url_for('manage_employees'))
    else:
        # If the user is not logged in or doesn't have admin privileges, redirect to the login page
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
                # Assuming there's a User model related to the Doctor
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


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


# Route for handling appointment requests
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Handle appointment form submission here
        date = request.form['date']
        time = request.form['time']
        staff_username = request.form['staff_username']  # Username of the selected staff member
        # Process the appointment and save it to the database
        flash('Appointment scheduled successfully.', 'success')
        return redirect(url_for('index'))  # Redirect to the home page or any other appropriate page
    else:
        # Fetch the list of available nurses and doctors from the database
        nurses = Nurse.query.all()
        doctors = Doctor.query.all()
        return render_template('appointment.html', nurses=nurses, doctors=doctors)


if __name__ == '__main__':
    app.run(debug=True)
