 
# 1.Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin ...........................................
# x=input('adinizi daxil edin:')
# print(x)


# 2.ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin................
# ad='alime'
# soyad='kerimova'
# tam_ad=ad.capitalize()+' '+soyad.capitalize()
# print('Salam'+ ' '+tam_ad)


# 4. Macarıstan” sözünü tərsinə çapa verin......................................................................
# ters = "macaristan"[::-1]
# print(ters)


# 6. Istenilen bir mətnin tam yarısını çap edin.................................................................
# text="What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type"
# metnin_yarisi=int(len(text)/2)
# print(metnin_yarisi)
# print(text[:125])


#5.Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. Languages: Python C JavaScript
# print('Languages: Python C JavaScript')


# 3.sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın.............................
# print('BAKI','SEKI', 'QUBA', 'AGDAS',sep='*')


#7. x = 10, y = 55 “and”-dən istifadə edərək x və y müqayisə edərək boolen dəyərləri çapa verin.


# 8.inputdan boshluqla ayrilmish iki eded daxil edin. Birinci ededi ikinci eded qeder quvvete yukseldin ve ashagidaki kimi ekrana yazdirin (f stringden istifade ederek).........................................................................................................
# eded_1=input('ededleri daxil edin:')
# eded_2=input('ededleri daxil edin:')
# son_netice=pow(int(eded_1), int(eded_2))
# netice='Netice: {} üstü {} {}-dir.'
# print(netice.format(eded_1, eded_2, son_netice))


# 9. word = “istədiyiniz sözü yaza bilərsiz” məsələn word = ‘culture’ “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın. Əgər söz varsa, ekranda belə bir nəticə çıxarın; “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin.................
# word='does'
# text='Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"'
# if word in text:
#    print('“does” sözü mətndə var')
# else:
#    print('not found')


# 10. 65 ədədinin 22 ədədinə olan qalığı ilə nisbətinin hasilini çapa verin.........................................................................
# birinci_eded=65
# ikinci_eded=22
# onlarin_qaligi= birinci_eded % ikinci_eded
# onlarin_nisbeti=birinci_eded/ikinci_eded
# print(onlarin_qaligi*onlarin_nisbeti)


# 11. x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. X 10-dan böyükdürsə və cüt ədədirsə, ekrana “OKAY” yazılsın, əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın


# 12.  iki ədəd götürüb dəyişkənlərə mənimsədin. Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, ekrana “Greater”, bərabərdirsə, “EQUAL” yox əgər kiçikdirsə, “SMALLER” yazılsın.

#13.  String data tipi yaradın və dəyərini 5.567-yə bərabər edin. Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.................
# import math
# x='5.567'
# x=float('5.567')
# print(math.trunc(x))

# 14. my_string = ‘f4.3989ts’. my_stringin ədədə bərabər olan hissəsin ilə özündən sonra gələn ən kiçik tam ədədə olan qüvvətini tapın

# 15. 1 və 8 arasında random bir ədəd götürsün proqram, sonra isə o ədədin kvadrat kökünü tapın (random kitabxansini research edin)..............
# import random
# x= random.randrange(1,8)
# import math
# print (math.sqrt(x))

# 16. 0 və 1 arasında olan təsadüfi bir ədədin 1 və 10 arasında olan təsadüfi bir ədələ hasilini tapın. (random kitabxansini research edin)......
# import random 
# x= random.random()
# y=random.randrange(1,10)
# hasil=float(x)*int(y)
# print(hasil)

# 17. x = “5.89” stringinin tam hissəsinin kubunu tapın..........................................................................................
# x='5.89'
# x=float('5.89')
# print(pow(int(x),3))


# 18. y = “4.92” stringini integere cast edin...................................................................................................
#  y='4.92'
# y=float('4.92')
# print(int(y))