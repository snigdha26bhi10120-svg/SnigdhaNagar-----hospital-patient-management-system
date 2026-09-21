from patientmanage import add_patient
patients=[]
print("=" * 45)
print("\n")
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
    print("\nPatient Management selected.")
    add_patient(patients)
    
    elif choice == "2":
        print("\nVisit Management selected.")

    elif choice == "3":
        print("\nDoctor Management selected.")

    elif choice == "4":
        print("\nBilling selected.")

    elif choice == "5":
        print("\nStatistics selected.")

    elif choice == "6":
        print("\nThank you for using the Hospital Patient Management System.")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
