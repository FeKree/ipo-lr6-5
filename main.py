import random #Библиотека для генерации
sp = [random.randint(-50,50) for i in range(25)] #Список в котором будут храниться 25 чисел
nul = 0 #Переменная которая будет считать количество нулевых элементов для вывода процента от всех 25 чисел
pol = 0 #Переменная которая будет считать количество положительных элементов для вывода процента от всех 25 чисел
otr = 0 #Переменная которая будет считать количество отрицательных элементов для вывода процента от всех 25 чисел
nul1 = [] #Список для хранения нулевых элементов
pol1 = [] #Список для хранения положительных элементов
otr1 = [] #Список для хранения отрицательных элементов
min = min(sp) #Переменная в которой будет минимальное число из списка
max = max(sp) #Переменная в которой будет максимальное число из списка
nul_kol = 0 #Переменная для подсчета процента нулевых
pol_kol = 0 #Переменная для подсчета процента положительных
otr_kol = 0 #Переменная для подсчета процента отприцательных
for i in sp: #Цикл который будет перебирать 25 элементов и закидывать их в 3 списка в 6 7 8 строке
    if i > 0: #Условие для положительных элементов
        pol += 1 #Добавляем к счетчику положительных элементов 1
        pol1.append(i) #Добавляем к списку новое положительное число
    if i < 0: #Условие для отрицательных элементов
        otr += 1 #Добавляем к счетчику отрицательных элементов 1
        otr1.append(i) #Добавляем к списку новое отрицательное число
    if i == 0: #Условие для нулевых элементов
        nul += 1 #Добавляем к счетчику нулевых элементов 1
        nul1.append(i) #Добавляем к списку новое нулевое число
pol_kol = (pol / 25) * 100 #Находим процент положительных чисел со списка
otr_kol = (otr / 25) * 100 #Находим процент отрицательных чисел со списка
nul_kol = (nul / 25) * 100 #Находим процент нулевых чисел со списка
print("Список: ",sp) #Вывод списка
print("Количество положительных числел в списке: ", pol) #Вывод кол-ва пол. чисел
print("Количество отрицательных числел в списке: ", otr) #Вывод кол-ва отр. чисел
print("Количество нулей в списке: ", nul) #Вывод кол-ва нулей
print("Положительные числа из списка: ", pol1) #Вывод самих пол. чисел(если есть)
print("Отрицательные числа из списка: ", otr1) #Вывод самих отр. чисел(если есть)
print("Нули: ", nul1) #Вывод самих нулей(если есть)
print("Положительные числа списка: ", pol_kol, "%") #Вывод процента пол. чисел
print("Отрицательные числа списка: ", otr_kol, "%") #Вывод процента отр. чисел
print("Нули списка: ", nul_kol, "%") #Вывод процента нулей
print("Минимальное число списка: ", min) #Вывод мин. числа
print("Минимальное число списка: ", max) #Вывод макс. числа