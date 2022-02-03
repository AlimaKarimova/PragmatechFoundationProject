# def outer_fun(a,b):
#    def inner_fun(c,d):
#       return c+d
#    return inner_fun(a,b)
#    return(a)
  

# result=outer_fun(5,10)
# print(result)      


# def display (**kwargs):
#    for i in kwargs:
#       print(i)

# display(emp="Kelly", salary="9000")      


   # def fun1(name, age=20):
   #    print(name, age)

   # fun1("emma",25)   


# print(2*3**3*4)


# a=[20,40]
# b=a
# b+=[30,40]
# print(a)
# print(b)



# x=75
# def myfunc():
#    x=x+1
#    print(x)

# myfunc()
# print(x)


# def func():
#    x=50
#    return x
# func()
# print(x)

# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# print(type([]) is list)
# print(bool(""), bool(3.14159), bool(-3), bool(1.0+1j)) 

# def func():
#    x=50
#    return x
# func()
# print(x)   

# print(type({}) is set)
# print(type(10))

# class User:
#     def __init__(self,f_name,l_name,age,login_attempts=0):
#       self.first_name=f_name
#       self.last_name=l_name
#       self.age=age
#       self.login_attempts=login_attempts

#     def describe(self):
#          print('user haqqinda melumatlar:',self.first_name,self.last_name,self.age)


class Istifadeci:
   def __init__(self, _userName,_parol):
     self.userName=_userName
     self.parol=_parol

user_1=Istifadeci('Alima','123456')     
user_1=Istifadeci('Cavad','123')     
user_1=Istifadeci('Murad','456')  

secimler=input('qeydiiyatdan kecmek ucun [1] yazin\n sisteme daxil olmaq ucun [2] yazin \n ana menyuya qayitmaq ucun [3] yazin\n sistemden cixmaq ucun[4] yazin')

while True:
   if secimler=='1':
      sual1=input('istifadeci adiniz')
      sual2=input('parolunuz')
   elif secimler=="2":
      print('sisteme daxil oldunuz')
   elif secimler=="3":
      secimler
   elif secimler=="4":
      break



      


# secimler=input('qeydiiyatdan kecmek ucun [1] yazin\n sisteme daxil olmaq ucun [2] yazin \n ana menyuya qayitmaq ucun [3] yazin\n sistemden cixmaq ucun[4] yazin')
