class Person:
    # constructor
    # in method eveerytime we   self is working as pointer

    def __init__(self, name: object, surname: object, email_id: object, yob: object) -> object:
        self.name1 = name
        self.surname = surname
        self.email_id = email_id
        self.yob = yob


var_Amit = Person("amit", "prakash", "amit@gmail.com", 1998)
var_saif = Person("saif", "ali", "saif@gmail", 1996)
print(var_saif.name1)
print(var_saif.email_id)
print(var_Amit.name1)
print(var_Amit.surname)
print(var_Amit.email_id)
print(var_Amit.yob)
