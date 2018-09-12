# Currency Converter

dollars = float(input("Dollar Amount: "))
currencies = {"Yen": 111.47, "Cnuts": 7, "Groats": 104, "Scheckles": 0.3}
x = [print(i, "Amount:", currencies[i] * dollars)for i in currencies]
