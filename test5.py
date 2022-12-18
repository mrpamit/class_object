class person:
    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        print("take emailid form the person:", email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell your dob")
        return dob


amit = person()
sonu = person()
gargi = person()
krish = person()
hitesh = person()
amit.email_id_input("amit@gmail.com")
print(amit.age(2022, 1998))
print("the date of birth:{}".format(hitesh.ask_dob()))
# print("the date of birth:%d",(hitesh.ask_dob()))


"""Task 1 - in a past whatever questions i have given to your with respect to list ,
tuple , dic , set , string try to create a separate class for each and everyting and
    restructure your code for all the segment and submit .

instruction number 1 -
    always use exception handling
instruction number 2 :
    use logging as well

Reformat your code and submit it to me before tomorrow's' class 3 PM IST to my mail id
sudhanshu@ineuron.ai
sunny.savita@ineuron.ai

i am only looking for your separate python file in your github link"""
