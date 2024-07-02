from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 210 S max special serias mega drive", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S25", "+79234567890"))
catalog.append(Smartphone("Google", "Pixel-Mixel", "+79345678901"))
catalog.append(Smartphone("Realme", "100 Pro GT Turbo", "+79456789012"))
catalog.append(Smartphone("Xiaomi", "MiyMiy 100 rentgen radiation", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
