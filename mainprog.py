from Handlefile import add_patient, view_patients, search_patient
from doctor_manage import add_doctor, view_doctors, search_doctor

patients = []
doctors = []

print("=" * 45)
print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
print("=" * 45)

while True:
    print("\nMain Menu")
    print("1. Patient Management")
    print("2. Visit Management")
    print("3. Doctor Management")
    print("4. Billing")
    print("5. Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n--- Patient Management ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Back to Main Menu")

        patient_choice = input("\nEnter your choice: ")

        if patient_choice == "1":
            add_patient(patients)

        elif patient_choice == "2":
            view_patients(patients)

        elif patient_choice == "3":
            search_patient(patients)

        elif patient_choice == "4":
            continue

        else:
            print("\nInvalid choice.")

    elif choice == "2":
        print("\nVisit Management selected.")

    elif choice == "3":
        print("\n--- Doctor Management ---")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Search Doctor")
        print("4. Back to Main Menu")

        doctor_choice = input("\nEnter your choice: ")

        if doctor_choice == "1":
            add_doctor(doctors)

        elif doctor_choice == "2":
            view_doctors(doctors)

        elif doctor_choice == "3":
            search_doctor(doctors)

        elif doctor_choice == "4":
            continue

        else:
            print("\nInvalid choice.")

    elif choice == "4":
        print("\nBilling selected.")

    elif choice == "5":
        print("\nStatistics selected.")

    elif choice == "6":
        print("\nThank you for using the Hospital Patient Management System.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
