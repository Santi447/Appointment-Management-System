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

def show_appointments_by_day(appointments_list,day):
     
    for appointments in appointments_list:
        if appointments.get_day_of_week() == day:
            print(appointments.__str__())

def change_appointment_by_day_time(appointments_list):
    day = str(input("Enter a day: ")).strip().title()
    start_hour = int(input("Enter a satrting hour (24 hour clock): "))
    if day in DAY_OF_WEEK and start_hour in START_TIME_HOUR:
        for appointments in appointments_list:
            result = appointments.find_appointments_by_time(appointments_list, day, start_hour)
            appt_type = appointments.get_appointment_type()
            name = appointments.get_client_name()
            phone_number = appointments.get_client_phone()
            
            if result.get_appointment_type() != 0:
                new_day = input("Enter new day: ")
                new_start_hour = input("Enter new start hour (24 hour clock): ")
                if new_day in DAY_OF_WEEK and new_start_hour in START_TIME_HOUR:
                    for appointments in appointments_list:
                        new_result = appointments.find_appointments_by_time(appointments_list, new_day, new_start_hour)
                        if new_result.get_appointment_type() == 0:
                            new_result.schedule(name, phone_number, appt_type)
                            result.cancel()
                            print(f"Appointment for {name} has been changed to :\nDay = {new_day}\nTime = {new_start_hour}")
            else:
                print("That time slot isn't booked and doesn't need to be changed")
    pass

def calculate_fees_per_day():
    pass

def calculate_weekly_fees():
    pass

def save_scheduled_appointments():
    pass

def schedule_appointment():
    pass

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
            pass
        elif selection == 3:
            day = str(input("Enter a day: ")).strip().title()
            show_appointments_by_day(appointments_list, day)
            


        elif selection == 4:
            pass
        elif selection == 5:
            change_appointment_by_day_time()


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