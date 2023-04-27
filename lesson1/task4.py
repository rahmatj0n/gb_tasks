revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))

if revenue > costs:
    profit = revenue - costs
    print(f"Финансовый результат - прибыль, Ее величина: {profit}")
    print(f"Рентабельность выручки = {profit / revenue}")

    employees_count = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {profit / employees_count: .1f}")
else:
    print("Финансовый результат - убыток")
