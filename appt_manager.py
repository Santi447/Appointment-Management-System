# date 2024/12/10 created by Gianna,Cauy,Santiago
# This program was created for a hair salon company to managed their appointments and calculate total fees for days and weeks as well it also allows you to load previous weeks or save current weeks with the option to overwrite the file if it already exist
# import appointments class and os
from appoint import Appointment
import os
# function for info table
def print_info_table():
    print("Client Name         Phone          Day       Start     End       Type")
    print(f"{"-" * 85}")   

#function to create weekly calander  
def create_weekly_calendar(appointment_list):
    # clear appointments list
    appointment_list.clear()
    for day in DAY_OF_WEEK:
        for hour in START_TIME_HOUR:
            # append day and hour appintment to appointments list tocreated weekly calendar
            appt = Appointment(day,hour)
            appointments_list.append(appt)

# function to load previous schedules
def load_scheduled_appointments():
    # user input file name
    file_name = input("Enter appointment filename: ").strip()
    # while file exist false
    while not os.path.exists(file_name):
        #   if user enters a that isnt found reprompt input
          file_name = input("File not found. Re-enter appointment filename: ").strip()
        #   open a file in moode read
    file_object = open(file_name, "r")
    # stores lines in list 
    content = file_object.readlines()
    # takes amount of items in the list as appointments loaded
    appointments_loaded = len(content)          
          
    # iterate line in content
    for line in content:
        # split in line into list ","
        items = line.rstrip().split(",")
        # parse itemlist indexs into corresponding variable that match appointments class attributes   
        day_of_week = str(items[3])
        start_time = int(items[4])
        client_name = str(items[0])
        client_phone = str(items[1])
        appt_type = int(items[2])
        # store loaded appointments to appointments list 
        result = find_appointments_by_time(appointments_list,day_of_week,start_time)
        result.schedule(client_name,client_phone,appt_type)
      
    print(f"{appointments_loaded} previously scheduled appointments have been loaded")
    file_object.close()

                                                                      
                            

# menu function
def print_menu():
    # flag
    selection_invalid = True
    while selection_invalid:
        # print menu
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
        # slection input
        selection = int(input("Enter your selection: "))
        # if selection is invalid
        if selection < 10 :
            selection_invalid = False
        else:
            print("\nInvalid option")
    return selection

# find appointments by time function
def find_appointments_by_time(object_list,day_of_week,start_time):
           #iterate through appointments in appointments list 
           for object in object_list:
                # validate that a object was recived 
                if object.get_day_of_week() == day_of_week and object.get_start_time_hour() == start_time:
                #returns object if found in objects list   
                       return object
            # returns nothing if no appointent is found  
           return None                                          
               
# show appointments by time function
def show_appointments_by_name(object_list,name):
        #   flag for if name is found 
          found = False
        #   iterate through the appointnments in appointments list
          for objects in object_list:
            #   allows for partial matches when searching for name
              if objects.get_client_name().lower().startswith(name.lower()):
                # print the object attributes in __str__() method
                print(objects.__str__())
                # if found break the loop
                found = True
         # if not found print no appointments found
          if not found:
            print("no appointments found.")

# show appointments by day function
def show_appointments_by_day(appointments_list,day):
    # iterate through appointments in appointments list
    for appointments in appointments_list:
    #  if the appointments found matches the paramater day recived in the function print out the appointments in .__str__() method format
     if appointments.get_day_of_week() == day:
         print(appointments.__str__())    
    
# change appointments by day and time
def change_appointment_by_day_time(appointments_list):
    
    # ask for orginial appointments dates
    print("\nChange appointment for:")
    day = input("What day: ").strip().title()
    start_hour = int(input("Enter start hour (24-hour clock): ").strip())

    # checks if it valid and find the current appointment
    result = find_appointments_by_time(appointments_list, day, start_hour)
    if not result or result.get_appointment_type() == 0:
        print("That time slot isnt booked and doesnt need to be changed")
        return

    # saves current appointment details
    name = result.get_client_name()
    phone_number = result.get_client_phone()
    appt_type = result.get_appointment_type()


    
    

    # Prompt for new appointment details
    new_day = input("Enter a new day: ").strip().title()
    new_start_hour = int(input("Enter starting hour (24-hour clock): ").strip())

    # make sure new day and new hour are valid new input within the salon hours of operation
    if new_day not in DAY_OF_WEEK or new_start_hour not in START_TIME_HOUR:
        print("That time slot isn't booked and doesn't need to be changed")
        return

    # Check if the new time slot is available
    new_result = find_appointments_by_time(appointments_list, new_day, new_start_hour)
    if new_result and new_result.get_appointment_type() == 0:
        # Schedule the new appointment
        new_result.schedule(name, phone_number, appt_type)
        print(f"Appointment for {name} has been changed to:\nDay = {new_day}\nTime = {new_start_hour}")
        # cancel the old appointments on if appointments is available 
        result.cancel()
    else:
        # print if new timeslot is already booked
        print("The new time slot is already booked")


# calculate fee for the day function
def calculate_fees_per_day(appointments_list):
    print("\nFees calculation per day....")
    # ask the user for day
    day = str(input("What day: ")).strip().title()
    # set total to 0
    total_fees = 0 
    # validate if the dau from user input is valid for salon operating days
    if day in DAY_OF_WEEK:
        #  iterate appointments in appointments list
        for appointments in appointments_list:
            # if appointments day booked matches the user input
            if appointments.get_day_of_week() == day:
            # match the cases based on the appoitments type of the appointmnts in appointments list
              match appointments.get_appointment_type():

                    # if mens hair cut add $40
                    case 1:
                        total_fees += 40
                    # if womans haircut add $60
                    case 2:
                        total_fees += 60
                    #  if mens coloring add $40
                    case 3:
                        total_fees += 40
                    # if womans coloring add $80
                    case 4:
                        total_fees += 80
        # print total
        print(f"Total fees for {day} is ${(total_fees)}")
 # print message if user enters a day that is not valid
    else:
        print(f"{day} is invalid day or the salon is closed")
        
                          
    
            
              
# calculate fee for week function

def calculate_weekly_fees(appointment_list):
    # set total = 0
    total = 0
    # iterate through appointments in appoitments list
    for appt in appointment_list:
        # get the type of  appointments 
        
        type = appt.get_appointment_type()
        # match the corresponding appointment type with the cost of each service
        match type:
          case 1:
           total += 40
          case 2:
           total += 60
          case 3:
           total += 40
          case 4:
            total += 80 
    #print total 
    print(f"Total weekly fees is ${total}")    
    
# save schedule for appointments for that week function
def save_scheduled_appointments(appointments_list):
#   set flag to true
  running = True
#   while the condtition remains true run the loop
  while running:
    # ask user for file name
    created_file = input("Enter appointment filename: ").strip()
    # checks if file already exist using os 
    if os.path.exists(created_file):
        #  if it is ask if the user want to they want to overwrite
         overwrite = input("File already exist. would you like to overwrite it (Y/N)? ")
        #  if the user selects no bring them back to the loop
         if overwrite == "N":
                continue
        #  if the user selects anything other then yes bring them back to the loop as to avoid invalid inputs 
         elif overwrite !="Y":
                continue        
          
     #if the user enters a file name that doesnt exist or if they want to overwrite the file then open the file  
    with open(created_file, "w") as file_object:
        # iterate through appointments in appointments list 
           for appointment in appointments_list:
            #  if appointments type isnt availble then format appointments attributes in csv format and write it into the file 
             if appointment.get_appointment_type() != 0:
                line = appointment.format_record()          
                file_object.write(line + "\n")
     #once the file is created open the file and count the amount of lines and print out the amount if line and use that as the appointments saved 
    with open(created_file, "r") as file_appointments_count:
                 content = file_appointments_count.readlines()
                 appointments_saved = len(content)
    print(f"{appointments_saved} scheduled appointments have been successfully saved")
    # set flag back to false once proccess is done
    running = False

           
                      
# schedule appointments function
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
    
# cancel appointments function
def cancel_appointment():
    print("\n**","Cancel an appointment","**")
    # ask the user for the day and start time of the appointments they want to cancel
    day_of_week = input("What day: ").strip().title()
    start_time = int(input("Enter start hour (24 hour clock): ").strip())
    # store the result of the function find appointment by time in a variable
    result = find_appointments_by_time(appointments_list,day_of_week,start_time)
    # if a result is found
    if result:
        # if the appointment found, appointment type is is available then print a error message
        if result.get_appointment_type() == 0:
            print("That time slot isn't booked and doesn't need to be cancelled")
        #else print out the appointment canceled message 
        else:    
         print(f"Appointment: {result.get_day_of_week()} {result.get_start_time_hour()}:00 - {result.get_end_time_hour()}:00 for {result.get_client_name()} has been cancelled!")
        result.cancel()
    #in case of error print error message 
    else:
        print("That time slot isn't booked and doesn't need to be cancelled")

# find appointments by name for main function
def find_appointments_by_name():
        print("\n**","Find appointment by name","**")
        # ask the user for name input for the paramater in the show appointments by name function
        name = input("Enter Client Name: ").title()
        print()
        # prints table headings
        print_info_table()
        # prints appointments attributes 
        show_appointments_by_name(appointments_list,name)

 # exit program for main function 
def exit_program():
        print("\n** Exit the system **")
        # aks the user if they want to save
        save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").strip().lower()
        # if user select yes
        if save == "y":
            # save appointment schedule
            save_scheduled_appointments(appointments_list)
       #print goodbye 
        print("Good Bye!")
# print appointments for the day 
def print_calendar_for_a_specific_day():
            
            print("\n**","Print calendar for a specific day","**")
            # ask the user to enter day of week they want to see
            day = str(input("Enter day of week: ")).strip().title()
            print(f"Appointments for {day}\n")
            print_info_table()
            # use user input as paramater and shoe the appointments for that day
            show_appointments_by_day(appointments_list,day)    
    
# main function to run the program
def main():
    # make the following constant and list as global variables
    global DAY_OF_WEEK, START_TIME_HOUR,appointments_list
    DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    START_TIME_HOUR = [9, 10, 11, 12, 13, 14, 15, 16]
    appointments_list = []
    # print start message
    print("Starting the Appointment Manager System")
    # create weekly calendar
    create_weekly_calendar(appointments_list)
    # confirmation that weekly calendar was created
    print("Weekly calendar created")
    # ask if user want to load perivous saved schedule
    prev_sched_appt = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").strip().lower()
    #  if yes call load appointments schedule 
    if prev_sched_appt == "y":
        load_scheduled_appointments()
        
        
    # set selection as 0
    selection = 0
    # runs program loop as long as selections is not exit program
    while selection != 9:
        # while program rinning  call the print menu function
        selection = print_menu()
        # match the slection cases to call function depending on what slectin is enter
        match selection:
        #  case if selection is 1 call schedule appointments 
          case 1:
            schedule_appointment()
        # case if selection is 2 call find appoitments by name
          case 2:
            find_appointments_by_name()
        #  case if selection is 3 call print calendar for a specific day
          case 3:
            print_calendar_for_a_specific_day()
        # case if selection is 4 call cancel appointments
          case 4:
            cancel_appointment()
        # case if selection is 5 call change appointments by day and time 
          case 5:
            change_appointment_by_day_time(appointments_list)
        # case if selection is 6 call calculate fee per day 
          case 6:
            calculate_fees_per_day(appointments_list)
        # case if selection is 7 call calculate weekly fees 
          case 7:
            calculate_weekly_fees(appointments_list)
        # case of selection is 9 calls exit program 
          case 9:
             exit_program()
         # case of selection does not match the other cases print a error message while not calling a function but allow for another selection to be made  
          case _:
           print("\nInvalid option")
#program 
main()
