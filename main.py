import bill
import contact

if __name__ == "__main__":
    co = contact.Contact("Audi")
    x = bill.Bill(300, "xsdz23", co)

    print(x.quantity)
    print(x.contact.name)