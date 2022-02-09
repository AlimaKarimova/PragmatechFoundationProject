
from countries import olkeler

# # 1. butun seherlerin sayini ekranda gostersin ...yazildi
# def CountAllCities():
#    print(range(len(olkeler.values()))+1)

# CountAllCities()   


# 2. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.
# list=[12,26,75,89,45]
# list.sort()
# print(list[-1])

# list = [110, 773, 322, 63, 1, 34, 5, 10]
# maximum =list [0]
# for i in list:
#    if i > maximum:
#     maximum = i

#2.en cox sehere sahib olan olkeni gostersin 
# def CityCountMax():
#    max=0
#    for x,y in olkeler.items():
#       if len(x)>max:
#          maxolke=max
#          max=len(x)
#          maxolke=x
#    print(maxolke)      

 
# CityCountMax()



# 3. olke adi daxil edildiyi zaman o olkeye aid olan seherlerin adlarini ekranda gostersin ...yazildi
# olke_adi=input('olke adi daxil edin')
# def FindCountry(olke_adi):
#    if olke_adi in olkeler:
#      print(olkeler[olke_adi])

# FindCountry(olke_adi)



#4.seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin ...yazildi

# cityname=input('seherin adini daxil edin ')
# def FindCity(cityname):
#    for x,y in olkeler.items():
#       if cityname in y:
#          print(x)

# FindCity(cityname)




