def mashina_narxi(nomi, turi, rangi):
    if nomi.lower() == "malibu":
        if turi.lower() == "sedan":
            return f"Malibu {rangi.capitalize()} sedan narxi: 35,000$"
    elif nomi.lower() == "lacetti":
        if turi.lower() == "sedan":
            return f"Lacetti {rangi.capitalize()} sedan narxi: 15,000$"
    elif nomi.lower() == "cobalt":
        if turi.lower() == "sedan":
            return f"Cobalt {rangi.capitalize()} sedan narxi: 12,000$"
    elif nomi.lower() == "gentra":
        if turi.lower() == "sedan":
            return f"Gentra {rangi.capitalize()} sedan narxi: 13,000$"
    elif nomi.lower() == "captiva":
        if turi.lower() == "suv":
            return f"Captiva {rangi.capitalize()} SUV narxi: 40,000$"
    elif nomi.lower() == "trailblazer":
        if turi.lower() == "suv":
            return f"Trailblazer {rangi.capitalize()} SUV narxi: 45,000$"
    elif nomi.lower() == "traverse":
        if turi.lower() == "suv":
            return f"Traverse {rangi.capitalize()} SUV narxi: 50,000$"
    elif nomi.lower() == "equinox":
        if turi.lower() == "suv":
            return f"Equinox {rangi.capitalize()} SUV narxi: 30,000$"
    elif nomi.lower() == "spark":
        if turi.lower() == "hatchback":
            return f"Spark {rangi.capitalize()} hatchback narxi: 9,000$"
    elif nomi.lower() == "nexia":
        if turi.lower() == "sedan":
            return f"Nexia {rangi.capitalize()} sedan narxi: 10,000$"
    elif nomi.lower() == "toyota camry":
        if turi.lower() == "sedan":
            return f"Toyota Camry {rangi.capitalize()} sedan narxi: 30,000$"
    elif nomi.lower() == "lexus rx":
        if turi.lower() == "suv":
            return f"Lexus RX {rangi.capitalize()} SUV narxi: 50,000$"
    elif nomi.lower() == "bmw x5":
        if turi.lower() == "suv":
            return f"BMW X5 {rangi.capitalize()} SUV narxi: 60,000$"
    elif nomi.lower() == "mercedes e-class":
        if turi.lower() == "sedan":
            return f"Mercedes E-Class {rangi.capitalize()} sedan narxi: 70,000$"
    elif nomi.lower() == "audi q7":
        if turi.lower() == "suv":
            return f"Audi Q7 {rangi.capitalize()} SUV narxi: 65,000$"
    elif nomi.lower() == "tesla model 3":
        if turi.lower() == "sedan":
            return f"Tesla Model 3 {rangi.capitalize()} sedan narxi: 40,000$"
    elif nomi.lower() == "ford mustang":
        if turi.lower() == "sport":
            return f"Ford Mustang {rangi.capitalize()} sport narxi: 55,000$"
    elif nomi.lower() == "honda accord":
        if turi.lower() == "sedan":
            return f"Honda Accord {rangi.capitalize()} sedan narxi: 28,000$"
    elif nomi.lower() == "kia sportage":
        if turi.lower() == "suv":
            return f"Kia Sportage {rangi.capitalize()} SUV narxi: 25,000$"
    else:
        return "Bunday mashina mavjud emas yoki narxi aniqlanmagan. Iltimos, boshqa nom kiriting."
nomi = input("Mashina nomini kiriting (masalan, Malibu, Tesla Model 3, BMW X5): ")
turi = input("Mashina turini kiriting (masalan, sedan, suv, hatchback, sport): ")
rangi = input("Mashina rangini kiriting (masalan, qizil, oq, qora): ")
natija = mashina_narxi(nomi, turi, rangi)
print(natija)