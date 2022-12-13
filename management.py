#from doctor import Doctor / from facility import Facility / from patient import Patient / from laboratory import Laboratory
from doctor import Doctor
from patients import Patient
from lab import Laboratory
# from facility import Facility

     
class Management:

    print("Welcome to the Hospital Managment system ")

    display_options = -1
    # The following program should keep on running until individual enters 0. 
    # ! bot equal to 0
    while(display_options != 0):
        print(""" Select an option from the following options or 0 to stop: 
        1 - 	Doctors
        2 - 	Facilities 
        3 - 	Laboratories 
        4 - 	Patients """)

        display_options = int(input())
        if (display_options == 1):
            # as long as the user chooe this doctor category,
            # we are going to create a doctor object and load the data from the doctor.txt file to a doctors list 
            doctor_obj = Doctor()
            doctor_obj.read_doctors_file()
            
            doctor_option = -1
            # a dictionary to store the user option and the corresponding action
            doctor_system = {
                1: doctor_obj.display_doctors_list,
                2: doctor_obj.search_doctor_by_id,
                3: doctor_obj.search_doctor_by_name,
                4: doctor_obj.add_dr_to_file,
                5: doctor_obj.edit_doctor_info
            }
            while(doctor_option != 6):
                print("\n1 - Display Doctors list")
                print("2 - Search for doctor by id")
                print("3 - Search for doctor by name")
                print("4 - Add doctor")
                print("5 - Edit doctor info")
                print("6 - Back to the Main Menu")
                doctor_option = int(input())
                if(doctor_option == 6):
                    break
                doctor_system.get(doctor_option)()
                
                print("\nBack to the prevoius Menu")
     
        if (display_options == 3):
            # as long as the user chooe this doctor category,
            # we are going to create a doctor object and load the data from the doctor.txt file to a doctors list 
            lab_obj = Laboratory()
            lab_obj.read_laboratory_file()
            
            lab_option = -1
            # a dictionary to store the user option and the corresponding action
            lab_system = {
                1: lab_obj.display_labs_list,
                2: lab_obj.add_lab_to_file,
            }
            while(lab_option != 3):
                print("\n1 - Display laboratories list")
                print("2 - Add laboratory")
                print("3 - Back to the Main Menu")
                lab_option = int(input())
                if(lab_option == 3):
                    break
                lab_system.get(lab_option)()
                print("\nBack to the prevoius Menu")
        
        
        if (display_options == 4):
            # as long as the user chooe this doctor category,
            # we are going to create a doctor object and load the data from the doctor.txt file to a doctors list 
            patients_obj = Patient()
            patients_obj.read_patients_file()
            
            patient_option = -1
            # a dictionary to store the user option and the corresponding action
            patients_system = {
                1: patients_obj.display_patient_list,
                2: patients_obj.search_patient_by_id,
                3: patients_obj.add_patient_to_file,
                4: patients_obj.edit_patient_info
            }
            while(patient_option != 5):
                print("\n1 - Display Patient list")
                print("2 - Search for patient by id")
                print("3 - Add patient")
                print("4 - Edit patient info")
                print("5 - Back to the Main Menu")
                patient_option = int(input())
                if(patient_option == 5):
                    break
                patients_system.get(patient_option)()
                print("\nBack to the prevoius Menu")
        
