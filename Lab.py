class Laboratory:
    name = ""
    cost = 0
    laboratory_list = []

    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
        self.laboratory_list.append(self)


    # Formats the Laboratory object similar to the laboratories.txt file 
    def format_lab_info(self):
        return self.name + "_" + str(self.cost)
    
    #  Asks the user to enter lab name and cost and forms a Laboratory object
    def enter_laboratory_info(self):
        name = input( " Enter the name of the libratory: ")
        cost = int(input("Enter the cost of the labratory: "))
        self.laboratory_list.append(Laboratory(name,cost))
        
        
    #  Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def read_laboratory_file(self):
        x = open("Laboratory_Cost.txt", "r")
        lines = x.readlines()
        for line in lines:
            name, cost = line.split ('_')
            self.laboratory_list.append (Laboratory(name,cost))
            x.close()
            

    # Displays the list of laboratories
    def display_labs_list(self):
        x = open("Laboratory_Cost.txt", "r")
        lines = x.readlines()
        for line in lines:
            name, cost = line.split('_')
            print("{:<20} {:<15}".format(name,cost))
            x.close()
        # loop the lab list and print each lab in the correct format.
        
            

    #  Writes the list of labs into the file laboratories.txt
    def write_list_of_labs_to_file(self):
        x = open("laboratory_Cost.txt", "w")
        x.write("Laboratory List: ")
        for lab in self.laboratory_list:
            x.write("\n" + lab.format_lab_info())
        x.close()
        # loop the lab list
        # call format_lab_info() for each lab and write it to the file
        
        
    #    Adds and writes the lab name to the file in the format of the data 
    #    that is in the file       
    def add_lab_to_file(self):
        name = input("Enter the name of the Laboratory: ")
        cost = int(input("Enter the cost of the Laboratory: "))
        self.laboratory_list.append(Laboratory(name,cost))
        x = open("Laboratory_Cost.txt", "a")
        x.write("\n" + name + "_" + str(cost))
        x.close()

        # call enter_laboratory_info() to ask for new lab data
        # call format_lab_info() to format new data
        # write the new data to the file

    def laboratory_menu(self):
        while 1:
            print("Laboratory Menu")
            print("1 - Display Laboratory List")
            print("2 - Add Laboratory")
            print("3 Go back to the  Main Menu")
            choice = int(input("Enter your choice"))
            if choice == 1:
                self.display_labs_list()
            elif choice == 2:
                self.add_lab_to_file()
            elif choice == 3:
                Management.DisplayMenu()
            else:
                print("Invalid option")
                self.laboratory_menu()
