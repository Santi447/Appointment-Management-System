class Appointment:
    def __init__(self, day_of_week, start_time_hour, client_name = "", client_phone = "", appt_type = 0):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour
    
    def get_client_name(self):
        return self.__client_name
    def get_client_phone(self):
        return self.__client_phone
    
    def get_appointment_type(self):
        return self.__appt_type
    def get_day_of_week(self):
        return self.__day_of_week
    
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_appt_type_desc(self):
        if self.__appt_type == 0:
            description = "Available"
        elif self.__appt_type == 1:
            description = "Mens Cut"
        elif self.__appt_type == 2:
            description = "Ladies Cut"
        elif self.__appt_type == 3:
            description = "Mens Colouring"
        elif self.__appt_type == 4:
            description = "Ladies Colouring"
        return description
    def get_end_time_hour(self):
        end_time = self.__start_time_hour + 1
        return end_time
    def set_client_name(self, name):
        self.__client_name = name
    
    def set_client_phone(self, phone):
        self.__client_phone = phone
    
    def set_appt_type(self, type):
        self.__appt_type = type
    def schedule(self, name, phone, type):
        self.__client_name = name
        self.__client_phone = phone
        self.__appt_type = type
    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
    
    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}"
    def __str__(self):
        end_time = self.get_end_time_hour()
        appt_type = self.get_appt_type_desc()
        return (
            f"{self.__client_name:<20}{self.__client_phone:<15}{self.__day_of_week:<10}"
            f"{self.__start_time_hour:<2}:00  -  {end_time:<2}:00     {appt_type:<20}"
            )
    



def find_appointments_by_time(object_list,day_of_week,start_time):
        #    print("*"*2,"Cancel an appointment","*"*2)
        #    day_of_week = input("What day: ").strip().capitalize()
        #    start_time = int(input("Enter start hour (24 hour clock): ").strip())
           for object in object_list:
                if object.get_day_of_week() == day_of_week and object.get_start_time_hour() == start_time:
                    print(f"Appointment: {object.get_day_of_week()} {object.get_start_time_hour()}:00 - {object.get_end_time_hour()}:00 for {object.get_client_name()} has been cancelled!")
                               
                    return object
                   
           if object != object_list:
            print("That time slot isn't booked and doesn't need to be cancelled")
            return None 


def show_appointments_by_name(object_list,name):
          found = False
          for objects in object_list:
              if objects.get_client_name() == name:
                print(objects.__str__())
                found = True
          if not found:
            print("no appointments found.")

def main():
    appt = Appointment("Thursday", 11, "Steven","403-600-6000",1)
    appt2 = Appointment("Thursday", 13, "Gabriela", "368-111-9999", 4)
    object_list = [appt,appt2]
    print("Client Name         Phone          Day       Start     End       Type")
    print(f"{"-" * 85}")
    print(appt)
    print(appt2)
    name = input("Enter Client Name: ").capitalize()
    show_appointments_by_name(object_list,name)
    # print("*"*2,"Cancel an appointment","*"*2)
    # day_of_week = input("What day: ").strip().capitalize()
    # start_time = int(input("Enter start hour (24 hour clock): ").strip())
    # find_appointments_by_time(object_list,day_of_week,start_time)
    
          
    
 
main()                   
               