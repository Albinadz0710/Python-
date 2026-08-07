from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15 Pro Max", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S24 Ultra", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Mi 14 Pro", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 8 Pro", "+79456789012"))
catalog.append(Smartphone("OnePlus", "12", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    

