import bill
import contact

co = contact.Contact("Volvo")
x = bill.Bill(200, co)

print(co)
print(x.quantity)
print(x.contact.name)

if __name__ == "__main__":
    co = contact.Contact("Audi")
    x = bill.Bill(300, co)

    print(x.quantity)
    print(x.contact.name)