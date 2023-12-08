Также отдельно про методы списков

1. append(): Добавляет элемент в конец списка.  
my_list = [1, 2, 3, 4, 5] 
my_list.append(6) 
print(my_list)  # Вывод: [1, 2, 3, 4, 5, 6] 
 
 
2. insert(): Вставляет элемент на указанную позицию в списке. 
python 
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 10) 
print(my_list)  # Вывод: [1, 2, 10, 3, 4, 5] 
 
 
3. remove(): Удаляет первое вхождение указанного элемента из списка. 
python 
my_list = [1, 2, 3, 4, 5] 
my_list.remove(3) 
print(my_list)  # Вывод: [1, 2, 4, 5] 
 
 
4. pop(): Удаляет и возвращает элемент на указанной позиции в списке. 
python 
my_list = [1, 2, 3, 4, 5] 
popped_element = my_list.pop(2) 
print(popped_element)  # Вывод: 3 
print(my_list)  # Вывод: [1, 2, 4, 5] 
 
 
5. index(): Возвращает индекс первого вхождения указанного элемента в списке. 
python 
my_list = [1, 2, 3, 4, 5] 
index = my_list.index(3) 
print(index)  # Вывод: 2 
 
 
6. count(): Возвращает количество вхождений указанного элемента в списке. 
python 
my_list = [1, 2, 3, 2, 4, 2, 5] 
count = my_list.count(2) 
print(count)  # Вывод: 3 
 
 
7. sort(): Сортирует список в порядке возрастания. 
python 
my_list = [5, 2, 4, 1, 3] 
my_list.sort() 
print(my_list)  # Вывод: [1, 2, 3, 4, 5] 
 
 
8. reverse(): Разворачивает список в обратном порядке. 
python 
my_list = [1, 2, 3, 4, 5] 
my_list.reverse() 
print(my_list)  # Вывод: [5, 4, 3, 2, 1]