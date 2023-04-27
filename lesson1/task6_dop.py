ticket_number = list(map(int, list(input("Введите номер билета: "))))

if sum(ticket_number[:3]) == sum(ticket_number[3:]):
    print("yes")
else:
    print("no")
