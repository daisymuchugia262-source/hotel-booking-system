def services():
 total=0
 while True: 

   print("1. medication=200")
   print("2. scaning=300")
   print("3. screening=500")
   print("4. ICU=600")
   print("5. Ambulance=800")
   services=input(str("Which service do you want?"))
   if services=="1":
        price=200
   elif services=="2":
        price=300
   elif services=="3":
        price=500
   elif services=="4":
        price=600
   elif services=="5":
        price=800
   elif services=="0":
    break
   else:
    print("Invalid")
    continue

    total=total+price
    return total 