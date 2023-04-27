width = int(input("Введите ширину шоколадки: "))
heigth = int(input("Введите длину шоколадки: "))

segments = int(input("Введите количество долек: "))

if width * heigth < segments:
    print("no")
elif width * heigth == segments:
    print("yes")
elif segments % width == 0 or segments % heigth == 0:
    print("yes")
else:
    print("no")
