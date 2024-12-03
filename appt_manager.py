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