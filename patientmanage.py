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

def view_patients(patients):
    if len(patients) == 0:
        print("\nNo patients found.")
        return

    print("\n" + "=" * 45)
    print("REGISTERED PATIENTS")
    print("=" * 45)

    for patient in patients:
        print("\nPatient ID:", patient["patient_id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Disease/Health Issue:", patient["disease"])
        print("-" * 45)


