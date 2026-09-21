def add_patient(patients):
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    disease = input("Enter disease/health issue: ")

    patient = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease
    }

    patients.append(patient)

    print("\nPatient added successfully!")
