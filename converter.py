def tempConverter():
    tempChoice = int(input("Choose one option. \n[1] F to C converter\n[2] C to F converter"))
    if tempChoice==1:
        f = int(input("Enter temprature(in Fahrenheit)\t"))
        print('Converting to Celsius')
        c = (f - 32) * (5/9)
        print(f"Result :- {c} degree celsius")
    elif tempChoice==2:
        c = int(input("Enter temprature(in Celsius)\t"))
        print('Converting to Fahrenheit')
        f = c * (9/5) + 32
        print(f"Result :- {f} degree fahrenheit")
    else:
        print('Invalid Choice')

def lenConverter():
    lenChoice = int(input("Choose one option. \n[1] m to cm converter\n[2] cm to m converter"))
    if lenChoice==1:
        m = int(input("Enter Length(in mtr.)\t"))
        print('Converting to Centimeters')
        cm = m * 100
        print(f"Result :- {cm} cms.")
    elif lenChoice==2:
        cm = int(input("Enter Length(in cm)\t"))
        print('Converting to Meters')
        m = cm / 100
        print(f"Result :- {m} mtrs.")
    else:
        print('Invalid Choice')

def wightConverter():
    lenChoice = int(input("Choose one option. \n[1] kg to g converter\n[2] g to kg converter"))
    if lenChoice==1:
        kg = int(input("Enter Weight(in kg.)\t"))
        print('Converting to gms.')
        g = kg * 1000
        print(f"Result :- {g} grams")
    elif lenChoice==2:
        g = int(input("Enter Weight(in grams)\t"))
        print('Converting to Kgs.')
        kg = g / 1000
        print(f"Result :- {kg} mtrs.")
    else:
        print('Invalid Choice')

print("********** Welcome to Converter **********")
print("Choose one option. Press :\n[1] For Length converter\n[2] For Weight converter\n[3] For Temprature converter")
user_choice = int(input("Enter your choice:\t"))
# print(user_choice)
if user_choice == 1:
    lenConverter()

elif user_choice == 2:
    wightConverter()

elif user_choice == 3:
    tempConverter()

else:
    print("Invalid Choice")