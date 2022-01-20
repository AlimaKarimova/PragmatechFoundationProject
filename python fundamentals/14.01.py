

# 1. Write a Python program to select the odd items of a list.
# my_list=[5,25,86,12,13]
# def my_func():
#    for x in my_list:
#       if x%2!=0:
#          print(f'{x} is odd number')
# my_func()



# 2. Write a Python function to sum all the numbers in a list.
# my_list=[5,25,86,12,13]
# def sum_func(a):
#    sum=0
#    for i in a:
#       sum+=i
#    print(sum)
# sum_func(my_list)


#3. Write a Python function to multiply all the numbers in a list.
# my_list=[5,25,86,12,13]
# def sum_func(a):
#    sum=1
#    for i in a:
#       sum*=i
#    print(sum)
# sum_func(my_list)


# 4.Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.
from re import X


week_day=['0','monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
number_day=[1,2,3,4,5,6,7]
a=input('eded daxil edin:' )
a=int(a)
def returnDay(a):
   for i in number_day:
      if a>1 and a<7 and a==i:
         number_day.index(i)==range(len(week_day))
         print(f'{a}-nci gun {week_day[i]}')

returnDay(a)       

# Make a list of five or more usernames, including the name    'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user: • If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report? • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
# def greeting(*user_Name):
#    user_Name=input('please,write your nick name')

# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"} Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. Bunun ucun userden input alin. Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user ne sorushmaq isteyir. Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” sualina cavab axtarir. Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” “. Bu suali sorushduqda yes ve no secimleri verin. Eger yes yazsa dictionarydeki datadan istifade ederek Platonun doguldugu ili usere gosterin.Meselen country daxil etse proqram texmin etsin ki user platonun doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin. Eger mentiqsiz soz daxil edilse not found verin ekrana.

# len() funksiyasini ozunuz yazmaga calishin

# my_list= 'hello world'
# count=0
# for i in my_list:
#    count+=1
# print(count)


# funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin. Mes: [1,2,3,1] bu halda True qaytaracag
# number = input('ededleri daxil  edin: ')
# my_list= number.split()
# def yoxla(my_list):
#     for i in my_list:
#         if my_list[0] == my_list[-1]:
#            return True
#     return False
# print( yoxla(number))
# Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.
