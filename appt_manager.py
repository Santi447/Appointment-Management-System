from appoint import Appointment



def print_info_table():
    print("Client Name         Phone          Day       Start     End       Type")
    print(f"{"-" * 85}")            
    



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
    print_info_table()
    print(appt)
    print(appt2)
    

    name = input("Enter Client Name: ").capitalize()
    print_info_table()
    show_appointments_by_name(object_list,name)
    # print("*"*2,"Cancel an appointment","*"*2)
    # day_of_week = input("What day: ").strip().capitalize()
    # start_time = int(input("Enter start hour (24 hour clock): ").strip())
    # find_appointments_by_time(object_list,day_of_week,start_time)
    
          
    
 
main()                   
               