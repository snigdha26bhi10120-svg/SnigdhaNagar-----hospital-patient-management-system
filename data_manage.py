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
