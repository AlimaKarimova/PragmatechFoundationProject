# students=[]
# file=open('data.txt','a')
# class Student:
#    def __init__(self,_ad,_soyad,_email):
#       self.name=_ad
#       self.surname=_soyad
#       self.email=_email
#       file.write(f'{self.name} | {self.surname} | {self.email}/n')

#    def showStudentData(self):
#       print(f'{self.name} | {self.surname} | {self.email}')   



# while True:
#    emr=input('yeni telebe elave olunsunmu?(yes/no)') 
#    if emr=='yes':
#       ad=input('ad:')
#       soyad=input('soyad:')
#       email=input('email:')
#       student=Student(ad,soyad,email)
#    elif emr=='no':
#       for student in students:
#        student.showStudentData()
#    else:
#       break