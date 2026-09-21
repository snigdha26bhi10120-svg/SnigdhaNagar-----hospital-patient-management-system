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
