def find_appointments_by_time(object_list,day_of_week,start_time):
           for object in object_list:
                   if day_of_week in object and start_time in object:
                           return object
                   print(f"Appointment: {object.day_of_week_getter()} {object.start_time_getter()} - {object.end_time_getter()} for {object.client_name_getter()} Has been Cancelled!")
                      
           else: print("That time slot isn't booked and doesn't need to be cancelled")        