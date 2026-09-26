# Ultrasonic Radar using Python

import random
import time

def ultrasonic_radar():
print("\n===== ULTRASONIC RADAR =====")

```
for angle in range(0, 181, 15):

    # Simulate ultrasonic sensor distance
    distance = random.randint(10, 200)

    print(f"Angle: {angle:3d}° | Distance: {distance} cm")

    if distance < 30:
        print("  ⚠️ Object detected nearby!")

    time.sleep(0.3)
```

while True:
print("\n1. Start Radar Scan")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    ultrasonic_radar()

elif choice == "2":
    print("Ultrasonic Radar Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
