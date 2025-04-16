geolocations = []
for i in range(3):
    latitude = int(input(f"enter latitude{i+1}: "))
    longitude = int(input(f"enter longitude{i+1}: "))
    geolocations.append((latitude, longitude))
for latitude, longitude in geolocations:
    print(f"({latitude}, {longitude})")
