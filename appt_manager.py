from appoint import Appointment

client_name = ""
client_phone = ""
appt_type = 0
DAY_OF_WEEK = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
START_TIME_HOUR = [9, 10, 11, 12, 13, 14, 15, 16]
appointments_list = []

def create_weekly_calendar(appointment_list):
    appointment_list.clear()
    for day in DAY_OF_WEEK:
        for hour in START_TIME_HOUR:
            appt = Appointment(day,hour)
            appointments_list.append(appt)

def load_scheduled_appointments():
    pass

def print_menu():
    selection_invalid = True
    while(selection_invalid):
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
        
        if (selection == 1 or selection == 2 or selection ==3 or selection == 4 or 
            selection == 5 or selection == 6 or selection == 7 or selection == 9):
            selection_invalid = False
        else:
            print("\nInvalid option\n")
    return selection

def find_appointment_by_time():
    pass

def show_appointments_by_name():
    pass

def show_appointments_by_day():
    pass

def change_appointment_by_day_time():
    pass

def calculate_fees_per_day():
    pass

def calculate_weekly_fees(appointment_list):
    total = 0
    for appt in appointment_list:
        match appt.get_appointment_type():
            case 1:
                total += 40
            case 2:
                total += 60
            case 3:
                total += 40
            case 4:
                total += 80
    print(f"Total weekly fees is ${total}")

def save_scheduled_appointments():
    pass

def schedule_appointment():
    pass

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
                    client_name = input("Client Name: ").strip()
                    client_phone = input("Client Phone: ").strip()
                    print("Appointment types")
                    print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")
                    # asks for the appointment type the user wants to schedule
                    appt_type = int(input("Type of Appointment: "))
                    # overwrites the available slot in the appointments list
                    appointments_list[i].schedule(client_name, client_phone, appt_type)
                    print(f"Ok, {client_name}'s appointment is scheduled!")
                else:
                    print("Sorry that time slot is booked already!")
            # increments the i/index value by 1 each elements passed
            i += 1
    else:
        print("Sorry that time slot is not in the weekkly calendar!")

def print_info_table():
    print("Client Name         Phone          Day       Start     End       Type")
    print(f"{"-" * 85}")

def main():
    print("Starting the Appointment Manager System")
    create_weekly_calendar(appointments_list)
    prev_sched_appt = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").strip().lower()
    if prev_sched_appt == "y":
        load_scheduled_appointments()
        print("loaded")
    
    selection = 0
    while selection != 9:
        print()
        # calls on the print_menu()
        selection = print_menu()
        if selection == 1:
            # calls on the schedule_appointment method
            schedule_appointment()
        elif selection == 2:
            print("\n** Find appointment by name **")
            client_name = input("Enter Client Name: ").strip()
            # calls on the show_appointments_by_name method
            show_appointments_by_name(appointments_list, client_name)
        elif selection == 3:
            print("\n** Print calendar for a specific day **")
        elif selection == 4:
            pass
            # calls on the cancel_appointment method
            # cancel_appointment()
        elif selection == 5:
            print("\nChange an appointment for:")
            change_appointment_by_day_time()
        elif selection == 6:
            print("\nFees calculation per day....")
            calculate_fees_per_day()
        elif selection == 7:
            calculate_weekly_fees()
        elif selection == 9:
            print("\n** Exit the system **")
            save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").strip().lower()
            if save == "y":
                save_scheduled_appointments()
            print("Good Bye!")
main()