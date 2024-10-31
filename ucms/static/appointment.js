<script>
    document.getElementById('staff_type').addEventListener('change', function() {
        var staffType = this.value;
        var designationSelect = document.getElementById('designation');

        // Clear previous options
        designationSelect.innerHTML = '';

        // Populate options based on staff type
        if (staffType === 'Doctor') {
            // Options for doctor designation
            var doctorOptions = ['Surgeon', 'Gynecologist', 'Allergist', 'General Practitioner'];
            doctorOptions.forEach(function(option) {
                var opt = document.createElement('option');
                opt.value = option;
                opt.textContent = option;
                designationSelect.appendChild(opt);
            });
        } else if (staffType === 'Nurse') {
            // Options for nurse designation
            var nurseOptions = ['Surgical Nurse', 'Audiologist', 'Orthopedic', 'Emergency Room Nurse', 'General Nurse', 'Allergy Specialist'];
            nurseOptions.forEach(function(option) {
                var opt = document.createElement('option');
                opt.value = option;
                opt.textContent = option;
                designationSelect.appendChild(opt);
            });
        }
    });
</script>
