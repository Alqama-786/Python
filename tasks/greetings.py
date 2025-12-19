# Morning: 11:00 AM - 12:00 PM
# Afternoon: 12:00 PM - 5:00 PM
# Evening: 5:00 PM - 9:00 PM
# Night: 9:00 PM - 12:00 AM

import time

hour = int(time.strftime("%H"))
min = time.strftime("%M")
sec = time.strftime("%S")
print(f"Current Time: {hour}:{min}:{sec}")

if hour > 7 and hour <= 11:
    print("Hey, Good Morning.")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 21:
    print("Good Evening")
elif hour >= 21 and hour < 24:
    print("Good Night")
else:
    print("Soja BKL.")