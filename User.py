class User:
    def __init__(self, name ,email,id ):
        self.name= name 
        self.email=email
        self.id=id



    # def given_info(self):
    #     return (f" name: {self.name}"
    #             f" email:{self.id}"
    #             f" id :{self.id}")    
    def __str__(self):
         return (f" name: {self.name}"
                f" email:{self.id}"
                f" id :{self.id}")  
        
    
user1=User("brat","leoncorporation@gmail.com","151487340")

print(user1)
           

    