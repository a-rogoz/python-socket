import json


print("What can I do for you?")
print("1 - produce a JSON string describing a vehicle")
print("2 - decode a JSON string into vehicle data")

try:
    choice = int(input("Your choice: "))
except ValueError as e:
    print("Incorrect choice. Try again.")


class Vehicle:
    def __init__(self, registration_no, year_of_prod, passenger, vehicle_mass):
        self.registration_no = registration_no
        self.year_of_prod = year_of_prod
        self.passenger = passenger
        self.vehicle_mass = vehicle_mass


class VehicleEncoder(json.JSONEncoder):
    def default(self, vehicle):
        if isinstance(vehicle, Vehicle):
            return vehicle.__dict__
        else:
            return super().default(self, vehicle)
        

class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)


if choice == 1:
    registration_no = input("Registration number: ")
    year_of_prod = input("Year of production: ")
    passenger = input("Passenger [y/n]: ")
    vehicle_mass = input("Vehicle mass: ")

    print("Resulting JSON string is:")
    vehicle = Vehicle(registration_no, year_of_prod, passenger, vehicle_mass)
    encoded_str = json.dumps(vehicle, cls=VehicleEncoder)
    print(encoded_str)
    print("Done")
elif choice == 2:
    json_str = input("Enter vehicle JSON string: ")
    decoded_str = json.loads(json_str, cls=VehicleDecoder)
    print(decoded_str.__dict__)
    print("Done")
else:
    raise ValueError("Incorrect choice.")