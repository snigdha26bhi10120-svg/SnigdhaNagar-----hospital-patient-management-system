def save_patients(patients):
    file = open("patient_data.txt", "w")

    for patient in patients:
        file.write(
            patient["patient_id"] + "|" +
            patient["name"] + "|" +
            patient["age"] + "|" +
            patient["gender"] + "|" +
            patient["disease"] + "\n"
        )

    file.close()


def load_patients(patients):
    try:
        file = open("patient_data.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 5:
                patient = {
                    "patient_id": data[0],
                    "name": data[1],
                    "age": data[2],
                    "gender": data[3],
                    "disease": data[4]
                }

                patients.append(patient)

        file.close()

    except FileNotFoundError:
        pass


def save_doctors(doctors):
    file = open("doctor_data.txt", "w")

    for doctor in doctors:
        file.write(
            doctor["doctor_id"] + "|" +
            doctor["name"] + "|" +
            doctor["specialization"] + "|" +
            doctor["phone"] + "\n"
        )

    file.close()


def load_doctors(doctors):
    try:
        file = open("doctor_data.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 4:
                doctor = {
                    "doctor_id": data[0],
                    "name": data[1],
                    "specialization": data[2],
                    "phone": data[3]
                }

                doctors.append(doctor)

        file.close()

    except FileNotFoundError:
        pass


def save_visits(visits):
    file = open("visit_data.txt", "w")

    for visit in visits:
        file.write(
            visit["visit_id"] + "|" +
            visit["patient_id"] + "|" +
            visit["doctor_id"] + "|" +
            visit["visit_date"] + "|" +
            visit["reason"] + "\n"
        )

    file.close()


def load_visits(visits):
    try:
        file = open("visit_data.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 5:
                visit = {
                    "visit_id": data[0],
                    "patient_id": data[1],
                    "doctor_id": data[2],
                    "visit_date": data[3],
                    "reason": data[4]
                }

                visits.append(visit)

        file.close()

    except FileNotFoundError:
        pass


def save_bills(bills):
    file = open("billing_data.txt", "w")

    for bill in bills:
        file.write(
            bill["bill_id"] + "|" +
            bill["patient_id"] + "|" +
            str(bill["consultation_fee"]) + "|" +
            str(bill["medicine_charge"]) + "|" +
            str(bill["other_charge"]) + "|" +
            str(bill["total"]) + "\n"
        )

    file.close()


def load_bills(bills):
    try:
        file = open("billing_data.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) == 6:
                bill = {
                    "bill_id": data[0],
                    "patient_id": data[1],
                    "consultation_fee": float(data[2]),
                    "medicine_charge": float(data[3]),
                    "other_charge": float(data[4]),
                    "total": float(data[5])
                }

                bills.append(bill)

        file.close()

    except FileNotFoundError:
        pass
