# 1. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

# list=[5,1,1,9]
# cem=0
# for i in list:
#    cem=cem+i
# print(cem)   


# 2. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.
# list=[12,26,75,89,45]
# list.sort()
# print(list[-1])

# list = [110, 773, 322, 63, 1, 34, 5, 10]
# maximum =list [0]
# for i in list:
#    if i > maximum:
#     maximum = i

# print(f"The maximum value is: {maximum}")



# 3. Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.
# list=[12,26,75,89,45]
# list.sort()
# print(list[0])

# list = [110, 773, 322, 63, 1, 34, 5, 10]
# minimum =list [0]
# for i in list:
#    if i < minimum:
#     minimum = i

# print(f"The minimum value is: {minimum}")


# 4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
# list=['abc', 'xyz', 'aba', '1221']
# say=0
# for i in list:
#    if len(i)>=2 and i[0]==i[-1]:
#       print('result:'+i)


# 5. Write a Python program to check a list is empty or not.
# list=[ ]
# if len(list)==0:
#     print('bos')


#6. my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.
# my_text = 'Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.'
# text=my_text.split(" ")
# text.sort()
# print(str(text))

# 7.Write a Python program to select the odd items of a list.
# list=[56,89,24,55,74]
# for i in list:
#    if i%2==1:
#     print(i)