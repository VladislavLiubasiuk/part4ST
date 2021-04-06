# part4ST
part 1
created the whole testing project, moved to git-specific folder and linked it to github depository

part2
???

part3
???

part 4
added locators.py and created a class with two new variables for login_page.py to use; testing login url, 2 forms


base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.

(Thank you, Nikolay Zhivats)
