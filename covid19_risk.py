print("Please answer the following questions only by 'yes' or 'no' ")
while True :
    age = input("Are you a cigarette addict older than 75 years old?").lower()
    if age == "yes" :
        break
    elif age == "no" :
        break
    else:
        continue
while True :        
    chronic = input("Do you have a severe chronic disease?").lower()
    if chronic == "yes" :
        break
    elif chronic == "no" :
        break
    else:
        continue
while True :        
    immune = input("Is your immune system too weak?").lower()
    if immune == "yes" :
        break
    elif immune == "no" :
        break
    else:
        continue
        
if age == "yes" :
    age = True
else:
    age = False
if chronic == "yes" :
    chronic = True
else:
    chronic = False
if immune == "yes" :
    immune = True
else:
    immune = False
if age or chronic or immune :
    print("Yor are in risky group")
else:
    print("You are not risky group")
