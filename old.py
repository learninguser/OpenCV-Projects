from careAll import CareALL
from young import Young

class Old(CareALL):
    old_list =[]
    @classmethod

    def add_old_per(cls,obj):
        cls.old_list.append(obj)

    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Old.add_old_per(self)

    def set_funds(self,price):
        self.price = price

    def get_funds(self):
        return self.price

    def accept(self,young):
        if self.status:
            print("will you take care by {} named {} aged {} ?".format(young.gender,young.name,young.age))
            u=input("enter response")
            if u=='YES':
                self.set_status = False
                return True
            elif u=='NO':
                pass
            else:
                print('enter yes or no')
                return self.accept(young_list)
    def getting_cared_by(self):
        return the_log.get(self.name,-1)