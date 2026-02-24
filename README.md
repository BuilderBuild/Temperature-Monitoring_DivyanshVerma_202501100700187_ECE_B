# Temperature-Monitoring_DivyanshVerma_202501100700187_ECE_B
Case Study 2: Temperature Monitoring System by Python

**Problem Statement:**
Build a Python code to display messages according to the temperature received from an assumed IoT system.
Accept max and min limit temperature.
Generate random values for temperature at every 2 second interval.
Compare with the limits to display appropriate value.

**Program Requirements:**
Accept maximum and minimum temperature value.
Generate random temperature value under certain limit (e.g. 0 to 100) for every 2 seconds
Compare the generated value with min and max limits and display the following messages:
“Alert: Temperature is too high” if value exceeded from max limit 
“Alert: Temperature is too low” if value below the min limit 
“Temperature is within acceptable limit” if value is within limits


**Sample Test CASE:**

**A) Max=80 and min=50**
 
Enter minimum temperature limit: 50
Enter maximum temperature limit: 80

Temperature Monitoring System Started...

Current Temperature: 19.4 °C
Alert: Temperature is too low


Current Temperature: 9.38 °C
Alert: Temperature is too low


Current Temperature: 87.61 °C
Alert: Temperature is too high
	

Current Temperature: 12.65 °C
Alert: Temperature is too low


Current Temperature: 75.18 °C
Temperature is within acceptable limit


Current Temperature: 8.95 °C
Alert: Temperature is too low
....and so on 



**B) Max=70 and min=50**

Enter minimum temperature limit: 50
Enter maximum temperature limit: 70

Temperature Monitoring System Started...

Current Temperature: 70.96 °C
Alert: Temperature is too high


Current Temperature: 54.09 °C
Temperature is within acceptable limit


Current Temperature: 5.24 °C
Alert: Temperature is too low


Current Temperature: 70.79 °C
Alert: Temperature is too high


Current Temperature: 84.39 °C
Alert: Temperature is too high


Current Temperature: 53.16 °C
Temperature is within acceptable limit
.... and so on
