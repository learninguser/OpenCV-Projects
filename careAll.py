class CareALL:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.status = True

    def get_status(self):
        return self.status
    
    def set_status(self,new_status):
        self.status =new_status
    
    def set_rating(self,new_rating):
        self.rating = new_rating
    
    def get_rating(self):
        return self.rating
    
    def set_review(self,new_review):
        self.review = new_review
    
    def get_review(self):
        return self.review