def add_visit(visits):
    visit_id = input("Enter visit ID: ")
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    visit_date = input("Enter visit date: ")
    reason = input("Enter reason for visit: ")

    visit = {
        "visit_id": visit_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "visit_date": visit_date,
        "reason": reason
    }

    visits.append(visit)

    print("\nVisit added successfully!")


def view_visits(visits):
    if len(visits) == 0:
        print("\nNo visits found.")
        return

    print("\n" + "=" * 45)
    print("HOSPITAL VISITS")
    print("=" * 45)

    for visit in visits:
        print("\nVisit ID:", visit["visit_id"])
        print("Patient ID:", visit["patient_id"])
        print("Doctor ID:", visit["doctor_id"])
        print("Visit Date:", visit["visit_date"])
        print("Reason:", visit["reason"])
        print("-" * 45)


def search_visit(visits):
    visit_id = input("Enter visit ID to search: ")

    for visit in visits:
        if visit["visit_id"] == visit_id:
            print("\nVisit Found!")
            print("-" * 30)
            print("Visit ID:", visit["visit_id"])
            print("Patient ID:", visit["patient_id"])
            print("Doctor ID:", visit["doctor_id"])
            print("Visit Date:", visit["visit_date"])
            print("Reason:", visit["reason"])
            print("-" * 30)
            return

    print("\nVisit not found.")
