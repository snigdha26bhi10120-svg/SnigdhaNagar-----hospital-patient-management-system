def add_doctor(doctors):
    doctor_id = input("Enter doctor ID: ")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter doctor phone number: ")

    doctor = {
        "doctor_id": doctor_id,
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    doctors.append(doctor)

    print("\nAlright, Doctor added successfully!")


def view_doctors(doctors):
    if len(doctors) == 0:
        print("\nOops! No doctors found.")
        return

    print("\n" + "=" * 45)
    print("REGISTERED DOCTORS")
    print("=" * 45)

    for doctor in doctors:
        print("\nDoctor ID:", doctor["doctor_id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Phone:", doctor["phone"])
        print("-" * 45)


def search_doctor(doctors):
    doctor_id = input("Enter doctor ID to search: ")

    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            print("\nDoctor Found!")
            print("-" * 30)
            print("Doctor ID:", doctor["doctor_id"])
            print("Name:", doctor["name"])
            print("Specialization:", doctor["specialization"])
            print("Phone:", doctor["phone"])
            print("-" * 30)
            return

    print("\nDoctor not found.")
