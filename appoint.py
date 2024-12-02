class Appointment:
    def __init__(self,day_of_week, start_time_hour,client_name = None, client_phone = None, appt_type = None,):
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
    
    def get_appt_type_desc(self):
        descriptions = {
            0: "Available",
            1: "Men’s Cut",
            2: "Ladies’ Cut",
            3: "Men’s Colouring",
            4: "Ladies’ Colouring",}
        return descriptions.get(self.appt_type,"invalid Input")
    

    def get_end_time_hour(self): 
        return self.start_time_hour + 1
    
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
    
    def schedule(self,name,phone,type):
        self.client_name = name
        self.client_phone = phone
        self.appt_type = type

    def cancel(self,name,phone,type):
        self.client_name = None
        self.client_phone = None
        self.appt_type = None
            
        
     

                   