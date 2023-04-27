class Shipping_Address:
    def __init__(self, name_surname, phone_number, address, sub_district, district, province, postal_code):
        self.__name_surname = name_surname
        self.__phone_number = phone_number
        self.__address = address
        self.__sub_district = sub_district
        self.__district = district
        self.__province = province
        self.__postal_code = postal_code
        
    def set_shipping_address(self,new_name_surname,new_phone_number,new_address,new_sub_district,new_district,new_provine,new_postal_code):
        self.__name_surname= new_name_surname
        self.__phone_number = new_phone_number
        self.__address= new_address
        self.__sub_district= new_sub_district
        self.__district= new_district
        self.__province = new_provine
        self.__postal_code = new_postal_code
        
    def get_name_surname(self):
        return self.__name_surname
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    def get_sub_district(self):
        return self.__sub_district
    
    def get_district(self):
        return self.__district
    
    def get_province(self):
        return self.__province
    
    def get_postal_code(self):
        return self.__postal_code
        
        
    