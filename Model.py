class nishan:
    def __init__(self,cname,pho):
        self.__customer_name=cname
        self.__phone=pho

    def set_customer_name(self,cname):
        self.__customer_name=cname

    def get_customer_name(self):
        return self.__customer_name
    def set_phone(self,pho):
        self.__phone=pho

    def get_phone(self):
        return self.__phone