from careAll import CareALL

class Young(CareALL):
    young_list = []

    @classmethod
    def add_young_per(cls,obj):
        cls.young_list.append(obj)

    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.care_list_confirmed = []
        self.care_list_chosen = []
        self.caring_num = 0
        Young.add_young_per(self)
    
    def add_old(self,name):
        if len(self.care_list_confirmed) < 4:
            self.care_list_confirmed.append(name)
            return True
        else:
            return False
    
    def get_care_list(self):
        for old in self.care_list_confirmed:
            print(old.name)
    
    def income(self):
        total = 0
        for a in self.care_list_confirmed:
            total+=a.get_funds()
            return total
    
    def number(self):
        return len(self.care_list_chosen)
    
    def select(self,care_list_confirmed):
        for people in care_list_confirmed:
            if people.status:
                print("would you like to take care of {} name{} age {}".format(people.gender,people.name,people.age))
                i=input("enter response")
                if i=='YES':
                    self.care_list_chosen.append(people)
                elif i=='NO':
                    pass
                else:
                    print("enter yes or no")
                    return self.select(care_list_confirmed)