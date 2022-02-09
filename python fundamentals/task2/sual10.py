
from os import name
from ssl import _PasswordType


istifadeciler=[]
 
 
class Istifadeci:
   def __init__(self,_adiniz,_parolunuz):
      self.name=_adiniz
      self.password=_parolunuz
      istifadeciler.append(self)



while True:
   emr=input('Qeydiyyatdan kecmek ucun [1] yazin\n Sisteme daxil olmaq ucun [2] yazin\n Ana Menyuya qayitmaq ucun [3] yazin\n Sistemden cixmaq ucun [4] yazin')
   if emr=='1':
      emr1=input('istifadeci adiniz')
      emr2=input('parolunuz')
      istifadeci=Istifadeci(name,_PasswordType)
   elif emr=='2':
      emr4=input('sisteme daxil olmaq ucun istifadeci adinizi yazin')
      
   else:
      break
