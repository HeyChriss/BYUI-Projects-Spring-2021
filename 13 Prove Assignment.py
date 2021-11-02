Wind = 0 
Temperature = float(input('What is the temperature?'))
Type_of_temperature = input ('Fahrenheit or Celsius (F/C)? ').capitalize()

if Type_of_temperature == 'C':
    C = ( Temperature * 9/5) + 32 
    for v in range(0, 65, 5):
        Wind_Chill = 35.74 + (0.6215 * C) - (35.75 * (v ** 0.16)) + (0.4275 * C) * (v ** 0.16)
        print (f'At temperature {C}F, and wind speed {v} mph, the windchill is: {Wind_Chill:.2f}')
elif Type_of_temperature == 'F':
    C = Temperature
    for v in range(0, 65, 5):
        Wind_Chill = 35.74 + (0.6215 * C) - (35.75 * (v ** 0.16)) + (0.4275 * C) * (v ** 0.16)
        print (f'At temperature {C}F, and wind speed {v} mph, the windchill is: {Wind_Chill:.2f}')
else:
    print ('This is the incorrect format')





