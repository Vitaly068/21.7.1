from Cat import Cat

cat_1 = Cat("Барон", "мальчик", 2, "сибирская кошка", "с29022020", "Без_дома")

print("Имя -", cat_1.name)
print("Пол -", cat_1.gender)
print("Возраст -", cat_1.age)
print("Порода -", cat_1.breed)
print("Регистрационный документ -", cat_1.registration_document)
print("Статус -", cat_1.status)

print("*******************")


cat_2 = Cat("Сэм", "мальчик", 2, "сибирская кошка", "с07032020", "Не приютили")

print("Имя -", cat_2.name)
print("Пол -", cat_2.gender)
print("Возраст -", cat_2.age)
print("Порода -", cat_2.breed)
print("Регистрационный документ -", cat_1.registration_document)
print("Статус -", cat_2.status)
