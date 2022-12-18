class Person:
    # constructor
    # in method every time we self is working as pointer

    def __init__(amit, name: object, surname: object, email_id: object, yob: object) -> object:
        amit.name1 = name
        amit.surname = surname
        amit.email_id = email_id
        amit.yob = yob

    def age(self, cur_year):
        return cur_year - self.yob


var_Amit = Person("amit", "prakash", "amit@gmail.com", 1998)
var_saif = Person("saif", "ali", "saif@gmail", 1996)
print(var_saif.name1)
print(var_saif.email_id)
print(var_Amit.name1)
print(var_Amit.surname)
print(var_Amit.email_id)
print(var_Amit.yob)
# to concatenate
print(var_Amit.name1 + " " + var_Amit.surname)
print(var_Amit.age(2020))
