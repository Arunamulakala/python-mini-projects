#Eletricity Bill Generator

#100 below units-- 5 per unit
#101-200  units -- 7 per unit
#201-300  units -- 10 per unint
#301 above units-- 15 per unit


# 78units - 78*5
# 105 units- 100*5 , 5*7...

def billgenerator(units):
      if units<=100:
          Bill=units*5
      elif units<=200:
          Bill=(100*5)+((units-100)*7)
      elif units<=300:
          Bill=(100*5)+(100*7)+((units-200)*10)
      else:
          Bill=(100*5)+(100*7)+(100*10)+((units-300)*15)

      return Bill

units=int(input('Enter your units: '))
Total_bill=billgenerator(units)
print(f'Your Total Bill {units} -{Total_bill}/-')
