def create_bill(bills):
    bill_id = input("Enter bill ID: ")
    patient_id = input("Enter patient ID: ")

    consultation_fee = float(input("Enter consultation fee: "))
    medicine_charge = float(input("Enter medicine charge: "))
    other_charge = float(input("Enter other charges: "))

    total = consultation_fee + medicine_charge + other_charge

    bill = {
        "bill_id": bill_id,
        "patient_id": patient_id,
        "consultation_fee": consultation_fee,
        "medicine_charge": medicine_charge,
        "other_charge": other_charge,
        "total": total
    }

    bills.append(bill)

    print("\nBill created successfully!")
    print("Total Amount: ₹", total)


def view_bills(bills):
    if len(bills) == 0:
        print("\nNo bills found.")
        return

    print("\n" + "=" * 45)
    print("HOSPITAL BILLS")
    print("=" * 45)

    for bill in bills:
        print("\nBill ID:", bill["bill_id"])
        print("Patient ID:", bill["patient_id"])
        print("Consultation Fee: ₹", bill["consultation_fee"])
        print("Medicine Charge: ₹", bill["medicine_charge"])
        print("Other Charges: ₹", bill["other_charge"])
        print("Total Amount: ₹", bill["total"])
        print("-" * 45)


def search_bill(bills):
    bill_id = input("Enter bill ID to search: ")

    for bill in bills:
        if bill["bill_id"] == bill_id:
            print("\nBill Found!")
            print("-" * 30)
            print("Bill ID:", bill["bill_id"])
            print("Patient ID:", bill["patient_id"])
            print("Consultation Fee: ₹", bill["consultation_fee"])
            print("Medicine Charge: ₹", bill["medicine_charge"])
            print("Other Charges: ₹", bill["other_charge"])
            print("Total Amount: ₹", bill["total"])
            print("-" * 30)
            return

    print("\nBill not found.")
