# Task 1
# Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
# На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер
# квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.

num = int(input("Вкажіть номер квартири: "))
if num > 144:
    print ("Такої квартири у цьому будинку немає")
elif num > 0:
    print ("Номер під'їзду:", (((num)//4)//9)+1)
if num > 0:
    print ("Номер поверху:", (num+1)%4%9)
if num > 0:
    print("Номер квартири на поверсі:", num%4)


