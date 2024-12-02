class Appointment:
    def __init__(self,client_name, client_phone, appt_type, day_of_week, start_time_hour):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

    #  getter methods
    def client_name_getter(self):
        return self.client_name
    
    def client_phone_getter(self):
        return self.client_phone

    def appt_type_getter(self):
        return self.appt_type


    def day_of_week_getter(self):
        return self.day_of_week

    def start_time_hour_getter(self):
        return self.start_time_hour
    
    # setter methods for client name, client phone, client appointment type
    def client_name_setter(self,client_name_value):
        self.client_name = client_name_value
        return self.client_name
    
    def client_phone_setter(self,client_phone_value):
        self.client_phone = client_phone_value
        return self.client_phone

    def appt_type_setter(self,appt_type_value):
        self.appt_type = appt_type_value
        return self.appt_type
    
     

                   