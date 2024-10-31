
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
        if user and user.password == password:  # Assuming the password is stored as plaintext
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
        year_of_study = request.form['year_of_study']
        department = request.form['department']

        # Create a new User instance
        new_user = User(username=username, password=password, name=name, email=email, phone=phone, gender=gender,
                        age=age, medical_history=medical_history, location=location, allergies=allergies,
                        blood_group=blood_group, role='student'
                        )

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

