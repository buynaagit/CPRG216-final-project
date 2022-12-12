import os


#My change --->>>>>>>> GIT HUB!!!!
class Doctor:
    doctors = []
    
    doctors_test = []
   
    """
    Formats each doctor’s information (properties) in the same format 
    used in the .txt file (i.e., has underscores between values)
    """
    # cant do this cuz it will miss arguments on every call
    def __init__(self,  id = 0, name = "", specialist = "", timing = "", qualification = "", room_no = ""):
        #Instance variable
        self.id = id
        self.name = name 
        self.specialist = specialist
        self.timing = timing
        self.qualification = qualification
        self.room_no =  room_no
        
        
    
    def format_dr_info(self, doctor):
        # 1: format this doctor's information in this format: 66_Dr. Mike_Heart_9am-5pm_MS_2
        # 2: return the formatted string: 66_Dr. Mike_Heart_9am-5pm_MS_2
         return str(doctor.id + "_" + doctor.name + "_" + doctor.specialist + "_"+doctor.timing + "_" + doctor.qualification + "_"+ doctor.room_no )
        
       
  
    # Asks the user to enter doctor properties (listed in the Properties point)
    def enter_dr_info(self):
        # ask user to enter doctor's data and use variables to receive it.
        # todo: declare variables accordingly
        print('called enter dr info')
        id = input("Enter the doctor’s ID:\n")
        name = input("Enter the doctor’s name\n")
        specialist = input("Enter the doctor’s specilaity\n")
        timing = input("Enter the doctor’s timing (e.g., 7am-10pm)\n")
        qual = input("Enter the doctor’s qualification\n")
        room_no = input("Enter the doctor’s room number\n")
        # create a Doctor object and return the object
        entered_info = Doctor(id, name, specialist, timing, qual, room_no)
        
        return entered_info
        
      
    # Reads from “doctors.txt” file and fills the doctor objects in a list1
    
    def read_doctors_file(self):
        # doctors = []
        # checking if txt file is empty or not and do operation if its not empty 
       if os.path.getsize('doctors.txt') > 0:   
          with open("doctors.txt") as file_in:
            for line in file_in:
              splitted = line.split("_")
              doctor = Doctor(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4], splitted[5])
              self.doctors.append(doctor)
       else:
           return print('data is empty')
    
        # Doctor(doctors)
        
        
    # Searches whether the doctor is in the list of doctors
    # using the doctor ID that the user enters
    def search_doctor_by_id(self):
        print(str('\n Enter the doctor Id: ')) 
        id = input()
        # # loop the doctor list to check if there is a a matched one
        found = False
        for doctor in self.doctors:
          if id == doctor.id:
            found = True 
            print ("{:<4} {:<22} {:<15} {:<15} {:<15} {:<10}"
                    .format(doctor.id, doctor.name, doctor.specialist , doctor.timing, doctor.qualification, doctor.room_no))
        if found == False:
             print(f"Patient with ID {id} not in Doctor file.")



        """
        Searches whether the doctor is in the list of doctors
        using the doctor name that the user enters
        """
    def search_doctor_by_name(self):
        print(str('\n Enter the doctor name: ')) 
        name = input()
        found = False
        for doctor in self.doctors:
            if name == doctor.name:
                found = True
                print("{:<4} {:<22} {:<15} {:<15} {:<15} {:<10}"
                .format(doctor.id, doctor.name, doctor.specialist , doctor.timing, doctor.qualification, doctor.room_no))
         
        if found == False:
            print(f"Patient with ID {name} not in Doctor file.")
                   
    


    # Asks the user to enter the ID of the doctor to change their information, 
    # and then the user can enter the new doctor information

    def edit_doctor_info(self):
        print("Please enter the id of the doctor that you want to edit their information: ")
        id = input()
        found = False
        #loop the doctor list to find the doctor that will be updated
        #enter the new doctor information and and update the doctor information in the list
        for doctor in self.doctors:
            if id == doctor.id:
                found = True
                #enter the new doctor information
                print('\nEnter new Name: ')
                name = input()
                print('\nEnter new Specilist in:')
                specialist = input()
                print('\nEnter new Timing: ')
                timing = input()
                print('\nEnter new Qualification: ')
                qualification = input()
                print('\nEnter new Room number: ')
                room_no = input()
                # update the doctor information in the list
                # doctor object is mutable
                doctor.name = name
                doctor.specilist = specialist
                doctor.timing = timing
                doctor.qualification = qualification
                #Put new \n at the end of line to fix formatting
                doctor.room_no = room_no + "\n"
                
                #   call write_list_of_doctors_to_file()
                self.write_list_of_doctors_to_file()
                #   call display_doctors_list()
                self.display_doctors_list()
            
                # stop the loop iteration when the doctor is updated. 
                break
              
        if found == False:
            print("Can't find the doctor with the same id on the system")
        

    # Displays all the doctors’ information, read from the file, as a report/table
    def display_doctors_list(self):
        # loop the doctor list to print out each doctor's information correctly
        if len(self.doctors) > 0:
          for doctor in self.doctors:
        #    print('line -->_>__>_>>__>>_>>__>_>_>>_', line)
           print("{:<5} {:30} {:<20} {:<20} {:<20} {:<20}".format(doctor.id, doctor.name, doctor.specialist,doctor.timing,doctor.qualification,doctor.room_no))
        #Clear list after displaying becuase it would add duplicate values to list on each loop
            
            
    # Writes the list of doctors to the doctors.txt file after formatting it correctly  
    def write_list_of_doctors_to_file(self):
        #  loop the doctor list
        # call format_dr_info() for each doctor
        formatted_list = []
        for line in self.doctors:
           formatted_list.append(self.format_dr_info(line)) 
        # then write the formatted data to doctors.txt
        print('formmmm', formatted_list)
        with open('doctors.txt', 'w') as file:
         file.writelines(formatted_list)
     
        
    # Writes doctors to the doctors.txt file after formatting it correctly
    def add_dr_to_file(self):
        # call enter_dr_info() to get new data from the user
        with open("doctors.txt", "a") as file:
         new_doctor = self.enter_dr_info()
         self.doctors.append(new_doctor)
        # call format_dr_info() to format new data
        # then write the formatted data to doctors.txt
         formatted_doc = self.format_dr_info(new_doctor)
         file.write(f"\n{formatted_doc}")
         


class Management:

    print("Welcome to the Hospital Managment system ")

    option = -1
    # The program should continue until the user enters 0.
    while(option != 0):
        print("\nSelect an option from the following options or 0 to stop: ")
        print("1 - 	Doctors")
        print("2 - 	Facilities")
        print("3 - 	Laboratories")
        print("4 - 	Patients ")

        option = int(input())
        if (option == 1):
            # as long as the user chooe this doctor category,
            # we are going to create a doctor object and load the data from the doctor.txt file to a doctors list 
            doctor_obj = Doctor()
            doctor_obj.read_doctors_file()
            
            doctor_option = -1
            # a dictionary to store the user option and the corresponding action
            doctor_methods = {
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
                doctor_methods.get(doctor_option)()
                
                print("\nBack to the prevoius Menu")
