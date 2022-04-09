# 1
print("\nYEARS AND MONTHS (INT)")
y = int(input("Years: "))
m = float(input("Months: "))
t = float(input("More months: "))
m = m*0.10
print(16/12)

if t <= 11:
    t = t*0.10
    print("t = 11 months")
    print(y+m, "+", "{: .1f}".format(t), "=", "{: .1f}".format(y+m+t), "year(s)")
elif t > 11:
    t = float(t/11)
    print("t > 11 months")
    print(y+m, "+", "{: .1f}".format(t), "=", "{: .1f}".format(y+m+t), "year(s)")

# 2
print("\nENERGY CONSUMPTION")
spent = int(input("Energy spent(kWh): "))
pay = 14
if spent <= 50:
    print("finalvalue: ", pay)
elif spent > 50:
    pay = pay + (spent-50)*0.25
    print("finalvalue: ", pay)
elif spent >= 100 and spent <= 200:
    pay = (pay + (spent-50)*0.25)*0.13
    print("finalvalue: ", pay)
elif spent > 200:
    pay = (pay + (spent-50)*0.25)*0.33
    print("finalvalue: ", pay)

# 3
print("\nWATER CHARGE")
wc = float(input("Water consumption: "))
lastconsumptionmonth = int(input("consumptionmonth: "))
finalvalue = float(0)


if wc >= 21 and wc <= 35:
    finalvalue = finalvalue + 2
    print("finalvalue: ", finalvalue, "RS")

elif wc >= 36 and wc <= 50:
    finalvalue = finalvalue + 3.50
    print("finalvalue: ", finalvalue, "RS")

elif wc >= 36 and wc <= 50:
    finalvalue = finalvalue + 5.50
    print("finalvalue: ", finalvalue, "RS")

elif wc >= 51:
    finalvalue = finalvalue + 7.00
    print("finalvalue: ", finalvalue, "RS")

elif wc < lastconsumptionmonth:
    finalvalue-finalvalue*0.3
    finalvalue*0.2
    print("finalvalue: ", finalvalue, "RS")

elif wc+wc*0.10 < lastconsumptionmonth:
    finalvalue+finalvalue*0.3
    print("finalvalue: ", finalvalue, "RS")
