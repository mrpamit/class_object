class Person :
    # constructor
    # in method eveerytime we   self is working as pointer

    def __init__(self, name: object, surname: object, emailid: object, yob: object) -> object:
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.yob=yob
var_Amit = Person("amit","prakash","amit@gmail.com",1998)
var_saif = Person("saif","ali","saif@gmail",1996)
print(var_saif.name)
print(var_saif.emailid)
print(var_Amit.name)
print(var_Amit.surname)
print(var_Amit.emailid)
print(var_Amit.yob)

