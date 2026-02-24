
# Case Study Title: Temperature Monitoring System

"""
Problem Statement:
Build a Python code to display messages according to the temperature received from an assumed IoT system.
Accept max and min limit temperature.
Generate random values for temperature at every 2 second interval.
Compare with the limits to display appropriate value.
"""
"""
Program Requirements:
Accept maximum and minimum temperature value.
Generate random temperature value under certain limit (e.g. 0 to 100) for every 2 seconds
Compare the generated value with min and max limits and display the following messages:
“Alert: Temperature is too high” if value exceeded from max limit 
“Alert: Temperature is too low” if value below the min limit 
“Temperature is within acceptable limit” if value is within limits
"""

import random


min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\nTemperature Monitoring System Started...\n")

#for printing
while 1==1:
    
    current_temp = random.uniform(0, 100)
    
    print("Current Temperature:",round(current_temp,2),"°C")
    

    if current_temp > max_temp:
        print("Alert: Temperature is too high")
        
    elif current_temp < min_temp:
        print("Alert: Temperature is too low")
        
    else:
        print("Temperature is within acceptable limit")
    
    print("\n")
    # for delay 
    for i in range(10000000):
        pass