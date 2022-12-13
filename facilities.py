class Facility:
    def __init__(self):
        self.menu = int(input(''' Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu '''))
        if self.menu == 1: 
            self.displayFacilities()
        if self.menu == 2:
            self.addFacility()

    def addFacility(self):
        facility = input("Enter Facility name:\n")
        with open ("facilities.txt", "a")as file:
            file.write(f"\n{facility}")
        print("\n Back to previous menu")

    def displayFacilities(self):
        with open ("facilities.txt", "r")as file:
           print(file.read())         
        print("\n Back to previous menu")   

while True:
    facility_object = Facility()
    if facility_object.menu == 3:
        break
