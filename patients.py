class Patient:
    patients = []

    def __init__(self, id = 0, name = "", disease = "", gender = "", age = ""):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def format_patient_info(self, patient):
        return str(patient.id + "_" + patient.name + "_" + patient.disease + "_" + patient.gender + "_" + patient.age + "_")

    def enter_patient_info(self):
        id = input(int("Enter Patient's id: \n"))
        name = input("Enter Patient's name:\n")
        disease = input("Enter Patient's disease: \n")
        gender = input("Enter Patient's gender: \n")
        age = input("Enter Patient's age: \n")
        patient = Patient(id, name, disease, gender, age)
        return patient
    ##this is the format of entering new patient info
    
    def read_patients_file(self):
        with open("files/patients.txt", "r") as patient_file:####Change the directory if necessary
            file_content = patient_file.readlines()
            for line in file_content:
                content = line.split("_")
                patient = Patient(content[0], content[1], content[2], content[3], content[4])
                self.patients.append(patient)
        print("Loading patients.txt to the list: Completed")
    
    def search_patient_by_id(self):
        found = False
        name = input("Enter the patient's name: \n")
        for patient in self.patients:
            if name == patient.name:
                found = True
                print("{:<4} {:<22} {:<15} {:<15} {:<10}"
                .format(patient.id, patient.name, patient.disease, patient.gender, patient.age))
            
        if found == False:
            print("Patient name can't be found in the system")
        ##If the ID is not found. Print this^
    def display_patient_info(self):
        pass
    ##this function should be in management
    
    def edit_patient_info(self):
        found = False
        id = input("Enter the id of the patient that you want to edit: \n")
        for patient in self.patients:
            if id == patient.id:
                found = True
                name = input("Enter the new name: \n")
                disease = input("Enter the new disease: \n")
                gender = input("Enter the new gender: \n")
                age = input("Enter the new age: \n")

                patient.id = id
                patient.name = name
                patient.disease = disease
                patient.gender = gender
                patient.age = age

                self.write_list_of_patients_to_file()
                self.display_patient_list()
                ##Format for editing the existing patient info
                break
        if found == False:
            print("id can't be found in the patient's info")
        ##Print this if the id is not found^

    def display_patient_list(self):
        for patient in self.patients:
            print("{:<4} {:<22} {:<15} {:<15} {:<10}"
            .format(patient.id, patient.name, patient.disease, patient.gender, patient.age))
    
    def write_list_of_patients_to_file(self):
        with open("files/patients.txt", "w") as patient_file:####Change the directory if necessary
            for patient in self.patients:
                format_patient = self.format_patient_info(patient)
                patient_file.write(format_patient)
        print("Writing data from the list to file: Complete")
    
    def add_patient_to_file(self):
        with open("files/patients.txt", "w") as patient_file:####Change the directory if necessary
            new_patient = self.enter_patient_info()
            self.patients.append(new_patient)
            format_patient = self.format_patient_info(new_patient)
            patient_file.write(f"\n{format_patient}")
        print("Adding a new patient in the file: Complete")
    