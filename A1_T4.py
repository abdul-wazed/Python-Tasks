Num1= 47
Num2= 102

print(f"{Num1} + {Num2} = {sum([Num1, Num2])}")
print(f"{Num2} - {Num1} = {Num2-Num1}")
print(f"{sum([Num1, Num2])} x {Num2-Num1}")
      
def substract_and_print (Num1, Num2,):
    Result1 = Num2 - Num1
    Result2 = Num1 + Num2 
    print(f"{Result1} * {Result2} = {Result1 * Result2}")
    print(f"({Num1} + {Num2}) * {Num2} - {Num1} = {Result1 * Result2}")
substract_and_print(47, 102)



