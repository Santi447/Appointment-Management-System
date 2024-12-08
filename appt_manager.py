from appoint import Appointment
import os
client_name = ""
client_phone = ""
appt_type = 0
DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
START_TIME_HOUR = [9, 10, 11, 12, 13, 14, 15, 16]
appointments_list = []



def print_info_table():
    print("Client Name         Phone          Day       Start     End       Type")
    print(f"{"-" * 85}")            
         

def create_weekly_calendar(appointment_list):
    appointment_list.clear()
    for day in DAY_OF_WEEK:
        for hour in START_TIME_HOUR:
            appt = Appointment(day,hour)
            appointments_list.append(appt)

def load_scheduled_appointments():
    # user input file name
    file_name = input("Enter appointment filename: ").strip()
    # while file exist false
    while not os.path.exists(file_name):
          file_name = input("File not found. Re-enter appointment filename: ").strip()
    file_object = open(file_name, "r")
    content = file_object.readlines()
    appointments_loaded = len(content)          
          

    for line in content:
                  
        items = line.rstrip().split(",")
        day_of_week = str(items[3])
        start_time = int(items[4])
        client_name = str(items[0])
        client_phone = str(items[1])
        appt_type = int(items[2])

        result = find_appointments_by_time(appointments_list,day_of_week,start_time)
        result.schedule(client_name,client_phone,appt_type)
          
    print(f"{appointments_loaded} previously scheduled appointments have been loaded")

                                                                      
                            


def print_menu():
    selection_invalid = True
    while selection_invalid:
        print(
            f"{"=" * 38}\n"
            f"{"Hair Salon Appointment Manager":^38}\n"
            f"{"=" * 38}\n"
            " 1) Schedule an appointment\n"
            " 2) Find appointment by name\n"
            " 3) Print calendar for a specific day\n"
            " 4) Cancel an appointment\n"
            " 5) Change an appointment\n"
            " 6) Calculate total fees for a day\n"
            " 7) Calculate total weekly fees\n"
            " 9) Exit the system"
        )
        selection = int(input("Enter your selection: "))
        
        if selection < 10 :
            selection_invalid = False
        else:
            print("\nInvalid option\n")
    return selection

def find_appointments_by_time(object_list,day_of_week,start_time):
           for object in object_list:
                if object.get_day_of_week() == day_of_week and object.get_start_time_hour() == start_time:
                #returns object if found in objects list   
                       return object
                    
           return None                                          
               

def show_appointments_by_name(object_list,name):
          found = False
          for objects in object_list:
              if objects.get_client_name() == name:
                print(objects.__str__())
                found = True
          if not found:
            print("no appointments found.")

def show_appointments_by_day():
    pass

def change_appointment_by_day_time():
    pass

def calculate_fees_per_day():
    pass

def calculate_weekly_fees():
    pass

def save_scheduled_appointments():
    pass

def schedule_appointment():
    pass
def cancel_appointment():
    print("*"*2,"Cancel an appointment","*"*2)
    day_of_week = input("What day: ").strip()
    start_time = int(input("Enter start hour (24 hour clock): ").strip())
    result = find_appointments_by_time(appointments_list,day_of_week,start_time)
    if result:
        if result.get_appointment_type() == 0:
            print("That time slot isnt booked and doesnt need to be cancelled")
        else:    
         print(f"Appintment: {result.get_day_of_week()} {result.get_start_time_hour()}:00 - {result.get_end_time_hour()}:00 for {result.get_client_name()} has been cancelled!")
        result.cancel()
    else:
        print("That time slot isnt booked and doesnt need to be cancelled")    

    

def main():
    print("Starting the Appointment Manager System")
    create_weekly_calendar(appointments_list)
    prev_sched_appt = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").strip().lower()
    if prev_sched_appt == "y":
        load_scheduled_appointments()
        
    
    selection = 0
    while selection != 9:
        print()
        selection = print_menu()
        if selection == 1:
            print("\n** Schedule an appointment **")
            day = input("What day: ").strip().title()
            start_hour = int(input("Enter start hour (24 hour clock): "))

            if (day in DAY_OF_WEEK and start_hour in START_TIME_HOUR): 
                i = 0
                for appt in appointments_list:
                    time = appt.get_start_time_hour()
                    appt_day = appt.get_day_of_week()
                    if time == start_hour and appt_day == day:
                        type = appt.get_appointment_type()
                        if type == 0:
                            client_name = input("Client Name: ").strip()
                            client_phone = input("Client Phone: ").strip()
                            print("Appointment types")
                            print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")
                            appt_type = int(input("Type of Appointment: "))
                            appointments_list[i] = Appointment(day, time, client_name, client_phone, appt_type)
                            print(f"Ok, {client_name}'s appointment is scheduled!")
                        else:
                            print("Sorry that time slot is booked already!")
                    i += 1

            else:
                print("Sorry that time slot is not in the weekkly calendar!")
        elif selection == 2:
            print("*"*2,"Find appointment by name","*"*2)
            name = input("Enter Client Name: ").title()
            print_info_table()
            show_appointments_by_name(appointments_list,name)
        elif selection == 3:
            pass
        elif selection == 4:
            cancel_appointment()
            pass
        elif selection == 5:
            pass
        elif selection == 6:
            pass
        elif selection == 7:
            pass
        elif selection == 9:
            print("\n** Exit the system **")
            save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").strip().lower()
            if save == "y":
                save_scheduled_appointments()
            print("Good Bye!")
main()
