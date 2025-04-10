Geolocation = {}

for i in range(3):
    latitude = int(input("enter latitude: "))
    longitude = int(input("enter longitude"))
    Geolocation.update({latitude:longitude})
print(Geolocation)

for key, value in Geolocation.items():
    print(f"({key}),({value})")
