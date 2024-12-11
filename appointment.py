class Appointment:
    def __init__(self, day_of_week, start_time_hour:int, client_name = "", client_phone = "", appt_type = 0):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
        self.__day_of_week = day_of_week
        self.__start_time_hour = int(start_time_hour)
    
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
        descriptions = {
            0: "Available",
            1: "Men’s Cut",
            2: "Ladies’ Cut",
            3: "Men’s Colouring",
            4: "Ladies’ Colouring",}
        if self.__appt_type in descriptions:
             return descriptions[self.__appt_type]
        else:
             return "invalid Input"

    def get_end_time_hour(self):
        return self.__start_time_hour + 1 

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
            f"{self.__start_time_hour:02}:00  -  {end_time:<2}:00     {appt_type:<20}"
            )