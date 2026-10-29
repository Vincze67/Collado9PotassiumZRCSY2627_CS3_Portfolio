class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter for bill amount
    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # Calculate the full bill
    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = 0.20
        return self.get_bill_amount() * (1 - discount)


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        discount = 0.15
        return self.get_bill_amount() * (1 - discount)


# Create patient objects
patient1 = Patient("Cyndel Malijao", 15000)
patient2 = PhilHealthPatient("Vince Collado", 15000)
patient3 = SeniorPatient("Dave Collado", 15000)

# Display billing information
print("Hospital Billing System")
print("-----------------------")

patients = [patient1, patient2, patient3]

for patient in patients:
    print(f"\nPatient Name:  {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
