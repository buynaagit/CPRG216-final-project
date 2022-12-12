#Laboratory class
class Laboratory:
    name = ""
    cost = 0
    laboratory_list = []
    def __init__(self,name = "",cost = ""):
        self.name = name
        self.cost = cost
        
    # Formats the Laboratory object similar to the laboratories.txt file 
    def format_lab_info(self, lab):
         return str(lab.name + "_" + lab.cost)
        
    #  Asks the user to enter lab name and cost and forms a Laboratory object
    def enter_laboratory_info(self):
        name = input( " Enter the name of the laboratory: ")
        cost = input("Enter the cost of the labratory: ")
        entered_info = Laboratory(name,cost)
        return entered_info
    
    #  Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def read_laboratory_file(self):
         with open("Laboratory_Cost.txt") as file_in:
            for line in file_in:
              splitted = line.split("_")
              lab = Laboratory(splitted[0], splitted[1])
              self.laboratory_list.append(lab)
    # Displays the list of laboratories
    # loops the lab list and prints each lab in the correct format.
    
    def display_labs_list(self):
       # loop the doctor list to print out each doctor's information correctly
        if len(self.laboratory_list) > 0:
          for lab in self.laboratory_list:
        #    print('line -->_>__>_>>__>>_>>__>_>_>>_', line)
           print("{:<5} {:30}".format(lab.name, lab.cost))
        #Clear list after displaying becuase it would add duplicate values to list on each loop
    #  Writes the list of labs into the file laboratories.txt
    
    def write_list_of_labs_to_file(self):
        formatted_list = []
        for lab in self.laboratory_list:
           formatted_list.append(self.format_lab_info(lab)) 
        # then write the formatted data to doctors.txt
        print('formmmm', formatted_list)
        with open('Laboratory_Cost.txt', 'w') as file:
         file.writelines(formatted_list)
    #    Adds and writes the lab name to the file in the format of the data 
    #    that is in the file       
    
    def add_lab_to_file(self):
        with open("Laboratory_Cost.txt", "a") as file:
         new_lab = self.enter_laboratory_info()
         self.laboratory_list.append(new_lab)
        # call format_dr_info() to format new data
        # then write the formatted data to doctors.txt
         formatted_doc = self.format_lab_info(new_lab)
         file.write(f"\n{formatted_doc}")
      # while loop, this is where the choices are made      
