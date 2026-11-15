
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")



patient1 = Patient("Juan Dela Cruz", 5000)
patient2 = PhilhealthPatient("Maria Santos", 5000)
patient3 = SeniorPatient("Pedro Reyes", 5000)


patients = [patient1, patient2, patient3]

for patient in patients:
    print("\nPatient Name:", patient.get_name())
    patient.display_patient_type()
    print("Total Bill: PHP", patient.calculate_bill())
