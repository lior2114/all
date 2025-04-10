geolocations = []
for i in range(3):
    latitude = float(input(f"Enter latitude{i+1}: "))
    longitude = float(input(f"Enter longitude{i+1}: "))
    geolocations.append({"latitude":latitude,"longtitude":longitude})
print(geolocations)

for loctaion in geolocations: #  קורא ממה שרשום בכתום לתוכנית   קורא ממה שרשום בכתום לתוכנית
    print(f"Latitude: {loctaion["latitude"]} Longitude: {loctaion["longtitude"]}")