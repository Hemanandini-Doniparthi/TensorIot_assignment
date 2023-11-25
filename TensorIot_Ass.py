import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.spot_size = spot_size
        self.available_spots = square_footage // (spot_size[0] * spot_size[1])
        self.parking_lot = [None] * self.available_spots
        self.parking_map = {}

    def park_car(self, car, spot):
        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            self.parking_map[car.license_plate] = spot
            return f"Car with license plate {car} parked successfully in spot {spot}"
        else:
            return f"Spot {spot} is occupied. Car with license plate {car} could not be parked."

    def map_vehicles_to_spots(self):
        return json.dumps(self.parking_map, indent=2)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot):
        if parking_lot.available_spots > 0:
            spot = random.randint(0, len(parking_lot.parking_lot) - 1)
            return parking_lot.park_car(self, spot)
        else:
            return "Parking lot is full. Cannot park the car."

def main():
    parking_lot = ParkingLot(square_footage=2000)

    cars = [Car(str(random.randint(1000000, 9999999))) for _ in range(20)]

    for car in cars:
        result = car.park(parking_lot)
        print(result)
        if "successfully" not in result:
            break

    parking_map_json = parking_lot.map_vehicles_to_spots()
    with open("parking_map.json", "w") as json_file:
        json_file.write(parking_map_json)

if __name__ == "__main__":
    main()
