from appoint import Appointment
import os

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
    file_object.close()

                                                                      
                            


def print_menu():
    selection_invalid = True
    while selection_invalid:
        print(
            f"\n{"=" * 38}\n"
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
            print("\nInvalid option")
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
              if objects.get_client_name().lower().startswith(name.lower()):
                print(objects.__str__())
                found = True
          if not found:
            print("no appointments found.")

def show_appointments_by_day(appointments_list,day):
    for appointments in appointments_list:
     if appointments.get_day_of_week() == day:
         print(appointments.__str__())    
    

def change_appointment_by_day_time(appointments_list):
    # Input current appointment details
    
    print("\nChange appointment for:")
    day = input("What day: ").strip().title()
    start_hour = int(input("Enter start hour (24-hour clock): ").strip())

    # Validate and find the current appointment
    result = find_appointments_by_time(appointments_list, day, start_hour)
    if not result or result.get_appointment_type() == 0:
        print("That time slot isnt booked and doesnt need to be changed")
        return

    # Display the current appointment details
    name = result.get_client_name()
    phone_number = result.get_client_phone()
    appt_type = result.get_appointment_type()


    
    

    # Prompt for new appointment details
    new_day = input("Enter a new day: ").strip().title()
    new_start_hour = int(input("Enter starting hour (24-hour clock): ").strip())

    # Validate new input
    if new_day not in DAY_OF_WEEK or new_start_hour not in START_TIME_HOUR:
        print("That time slot isn't booked and doesn't need to be changed")
        return

    # Check if the new time slot is available
    new_result = find_appointments_by_time(appointments_list, new_day, new_start_hour)
    if new_result and new_result.get_appointment_type() == 0:
        # Schedule the new appointment
        new_result.schedule(name, phone_number, appt_type)
        print(f"Appointment for {name} has been changed to:\nDay = {new_day}\nTime = {new_start_hour}")
        result.cancel()
    else:
        print("The new time slot is already booked")



def calculate_fees_per_day(appointments_list):
    print("Fees calculation per day....")
    day = str(input("What day: ")).strip().title()
    
    total_fees = 0 
    if day in DAY_OF_WEEK:

        for appointments in appointments_list:
            
            if appointments.get_day_of_week() == day:
              match appointments.get_appointment_type():


                    case 1:
                        total_fees += 40

                    case 2:
                        total_fees += 60

                    case 3:
                        total_fees += 40

                    case 4:
                        total_fees += 80
        print(f"Total fees for {day} is ${(total_fees)}")
    else:
        print(f"{day} is invalid day or the salon is closed")
        
                          
    
            
              


def calculate_weekly_fees(appointment_list):
    total = 0
    for appt in appointment_list:
        type = appt.get_appointment_type()
        match type:
          case 1:
           total += 40
          case 2:
           total += 60
          case 3:
           total += 40
          case 4:
            total += 80 
    print(f"Total weekly fees is ${total}")    
    

def save_scheduled_appointments(appointments_list):
  running = True
  while running:
    created_file = input("Enter apointment filename: ").strip()
    if os.path.exists(created_file):
         overwrite = input("File already exist. would you like to overwrite it y/n: ")
         if overwrite == "N":
                continue
         elif overwrite !="Y":
                continue        
          
         
    with open(created_file, "w") as file_object:
           for appointment in appointments_list:
             if appointment.get_appointment_type() != 0:
                line = appointment.format_record()          
                file_object.write(line + "\n")
                
    with open(created_file, "r") as file_appointments_count:
                 content = file_appointments_count.readlines()
                 appointments_saved = len(content)
    print(f"{appointments_saved} scheduled appointments have been successfully saved")
    running = False

           
                      

def schedule_appointment():
    print("\n** Schedule an appointment **")
    # asks the user for the day and start hour
    day = input("What day: ").strip().title()
    start_hour = int(input("Enter start hour (24 hour clock): "))
    # if day and start hour is both in the day of week and start hour lists respectively, looks through the appointments list
    if (day in DAY_OF_WEEK and start_hour in START_TIME_HOUR): 
        i = 0
        # goes through all the elements in the appointments list
        for appt in appointments_list:
            # gets the appt's start time hour
            time = appt.get_start_time_hour()
            # gets the appt's day of the week
            appt_day = appt.get_day_of_week()
            # if the time and appt_day is the same as the inputted day and start hour by user,
            # looks at what the appointment type is for that element
            if time == start_hour and appt_day == day:
                # gets the appointment type for appt
                type = appt.get_appointment_type()
                # if the type is 0(available), asks the user more information for their appointment
                if type == 0:
                    # asks for user's name and phone number
                    client_name = input("Client Name: ").strip().title()
                    client_phone = input("Client Phone: ").strip()
                    print("Appointment types")
                    print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")
                    # asks for the appointment type the user wants to schedule
                    appt_type = int(input("Type of Appointment: "))
                    # creates the appointment object using the values given by the user
                    # overwrites the available slot in the appointments list
                    appointments_list[i].schedule(client_name,client_phone,appt_type)
                    print(f"Ok, {client_name}'s appointment is scheduled!")
                else:
                    print("Sorry that time slot is booked already!")
            # increments the i/index value by 1 each elements passed
            i += 1
    else:
        print("Sorry that time slot is not in the weekkly calendar!")    
    

def cancel_appointment():
    print("\n**","Cancel an appointment","**")
    day_of_week = input("What day: ").strip().title()
    start_time = int(input("Enter start hour (24 hour clock): ").strip())
    result = find_appointments_by_time(appointments_list,day_of_week,start_time)
    if result:
        if result.get_appointment_type() == 0:
            print("That time slot isnt booked and doesnt need to be cancelled")
        else:    
         print(f"Appointment: {result.get_day_of_week()} {result.get_start_time_hour()}:00 - {result.get_end_time_hour()}:00 for {result.get_client_name()} has been cancelled!")
        result.cancel()
    else:
        print("That time slot isnt booked and doesnt need to be cancelled")

def find_appointments_by_name():
        print("\n**","Find appointment by name","**")
        name = input("Enter Client Name: ").title()
        print()
        print_info_table()
        show_appointments_by_name(appointments_list,name)
def exit_program():
        print("\n** Exit the system **")
        save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").strip().lower()
        if save == "y":
            save_scheduled_appointments(appointments_list)
        print("Good Bye!")            
def print_calendar_for_a_specific_day():
            print("\n**","Print calendar for a specific day","**")
            day = str(input("Enter day of week: ")).strip().title()
            print(f"Appointments for {day}\n")
            print_info_table()
            show_appointments_by_day(appointments_list,day)    
    

def main():
    global DAY_OF_WEEK, START_TIME_HOUR,appointments_list
    DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    START_TIME_HOUR = [9, 10, 11, 12, 13, 14, 15, 16]
    appointments_list = []
    print("Starting the Appointment Manager System")
    create_weekly_calendar(appointments_list)
    print("Weekly calendar created")
    prev_sched_appt = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").strip().lower()
    if prev_sched_appt == "y":
        load_scheduled_appointments()
        
        
    
    selection = 0
    while selection != 9:

        selection = print_menu()
        match selection:

          case 1:
            schedule_appointment()

          case 2:
            find_appointments_by_name()
        
          case 3:
            print_calendar_for_a_specific_day()

          case 4:
            cancel_appointment()
            
          case 5:
            change_appointment_by_day_time(appointments_list)
            
          case 6:
            calculate_fees_per_day(appointments_list)
            
          case 7:
            calculate_weekly_fees(appointments_list)
          case 9:
             exit_program()
          case _:
           print("\nInvalid option")        
main()
