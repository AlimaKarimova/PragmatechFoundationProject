# 1.  Bir dənə Restoran classı yaradın. Bu classa init() metdou bu classın adını (restaurant_name) və mətbəx növü (cuisine_type) adlı iki atribitunu saxlamalıdır. describe_restaurant() adlı bir metod yaradın hansı ki restoranın adını və mətbəxin növünü ekrana print etsin. Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa bit metdi yaradın. Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını, mətbəxinin növünü, restoran haqqında məlumatları və açıq olmasını çapa verin. Bu Restoran classından daha iki obyek yaradın və describe_restaurant metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.

# class Restoran:
#   def __init__(self,r_name,c_type):
#      self.restaurant_name=r_name
#      self.cuisine_type=c_type

#   def describe_restaurant (self):
#      print('restoranin adi:',self.restaurant_name,'metbexin tipi:',self.cuisine_type)

#   def open_restaurant (self):
#      print('restoran aciqdi')


# restoran_1=Restoran('Sushi','yapon')
# restoran_1.describe_restaurant()
# restoran_1.open_restaurant()

# restoran_2=Restoran('Acharuli','gurcu')
# restoran_2.describe_restaurant()

# restoran_3=Restoran('Vareniki','rus')
# restoran_3.describe_restaurant()


# 2.  User adlı yeni class yaradın. first_name, last_name və age atributları verin bu class-a. describe_user metdou yaradın user haqqında məlumatları çapa vermək üçün. greet_user adlı başqa bir metod yaradın hansı ki userin ad və soyadına salam verən bir mesaj ekrana yazdırsın. Bir neçə obyekt yaradın bu User class-ndan və hər birinin atribut və metodlarını istifadə edin. Ardinca login_attempts adlı bir atribut verin User classına. increment_ login_attempts adlı metod yaradın hansı ki hər dəfə işə düşəndə login_attempts 1 vahid artırır. reset_login_attempts adlı bir metod yaradın hansı ki login_attemptsləri sıfırlayır. Sonra bir user obyekti yaradın bu class-dan və increment_ login_attemptsi bir neçə dəfə istifadə etdikdən sonra userin neçə dəfə cəhd etdiyini çapa verin. Daha sonra cəhdlərin sayını sıfırlayın və yenidən cəhdlərin sayını çapa verin

# class User:
#     def __init__(self,f_name,l_name,age,login_attempts=0):
#       self.first_name=f_name
#       self.last_name=l_name
#       self.age=age
#       self.login_attempts=login_attempts

#     def describe(self):
#          print('user haqqinda melumatlar:',self.first_name,self.last_name,self.age)

#     def greet_user(self):
#          print('Hello',self.first_name,self.last_name)
   
#     def increment_login_attempts(self):
#        self.login_attempts+=1
#        print(self.login_attempts)

#     def reset_login_attempts(self):
#        self.login_attempts=0
#        print(self.login_attempts)     




# user_1=User('Alima','Karimova','29')
# user_1.describe()
# user_1.greet_user()
# user_1.increment_login_attempts()
# user_1.reset_login_attempts()

# user_2=User('Cavid','Karimov', '27')
# user_2.describe()
# user_2.greet_user()

# user_3=User('Murad','Karimov','23')
# user_3.describe()
# user_3.greet_user()


