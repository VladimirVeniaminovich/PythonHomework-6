from random import randint

list1 = []
size = int(input("Введите размер поля:\n"))
for i in range(size):
    list2 =[]
    for j in range(size):
        list2.append(0)
    list1.append(list2)
def printing_field():
    for i in list1:
        print(i)
printing_field()
placement_x = randint(0, len(list2)-1)
placement_y = randint(0, len(list1)-1)
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == placement_y and j == placement_x:
            list1 [i] [j] += 1
printing_field()
shoot_x = int(input("Введите координату Х выстрела\n")) - 1
shoot_y = int(input("Введите координату Y выстрела\n")) - 1
while shoot_x != placement_x or shoot_y != placement_y: #Не могу понять почему, но когда здесь ставлю логическую
    shoot_x = int(input("Мимо\nВведите координату Х выстрела еще раз\n")) - 1 # "and", то код не работает,
    shoot_y = int(input("Введите координату Y выстрела\n")) - 1      # когда же ставлю "or", то работает как задуманно.
print("Корабль уничтожен, вы победили!")