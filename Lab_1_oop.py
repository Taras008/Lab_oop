class EcoFriendly:
    def eco_rating(self):
        return "Eco-friendly rating."


class Car:
    def __init__(self, brand, unique_number, price):
        self.__brand = brand
        self.__unique_number = unique_number
        self.price = price

    @property
    def brand(self):
        return self.__brand

    def get_description(self):
        return f"Vehicle: {self.__brand}, Unique number: {self.__unique_number}, Price: ${self.price}"

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        print(f"New price after {percentage}% discount: ${self.price}")

    @staticmethod
    def calculate_vat(price):
        return price * 0.2


class PassengerCar(Car, EcoFriendly):
    def __init__(self, brand, unique_number, price, number_of_seats):
        super().__init__(brand, unique_number, price)
        self.number_of_seats = number_of_seats

    def get_description(self):
        description = super().get_description()
        return f"{description}, Seats: {self.number_of_seats}, {self.eco_rating()}"

class Truck(Car, EcoFriendly):
    def __init__(self, brand, unique_number, price, max_load_capacity):
        super().__init__(brand, unique_number, price)
        self.max_load_capacity = max_load_capacity

    def get_description(self):
        description = super().get_description()
        return f"{description}, Max load capacity: {self.max_load_capacity} tons, {self.eco_rating()}"


class Buyer:
    def __init__(self, first_name, last_name, phone, email, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_contact_info(self):
        return f"Buyer: {self.get_full_name()}, Phone: {self.phone}, Email: {self.email}"


class PaymentSystem:
    @staticmethod
    def generate_invoice(vehicle, buyer_name):
        vat = Car.calculate_vat(vehicle.price)
        total_price = vehicle.price + vat
        print(f"Invoice for {buyer_name}: Vehicle Price: ${vehicle.price}, VAT: ${vat}, Total: ${total_price}")


class VehicleSale(PaymentSystem):
    def __init__(self, vehicle, buyer):
        self.vehicle = vehicle
        self.buyer = buyer

    def get_description(self):
        description = self.vehicle.get_description()
        buyer_info = self.buyer.get_contact_info()
        return f"Sale Date: {description}\nSold to: {buyer_info}"

    def generate_sale(self):
        self.generate_invoice(self.vehicle, self.buyer.get_full_name())


class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.sold_cars = []
        self.service_registry = []
        self.sales_registry = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Car added to salon: {car.get_description()}")

    def sell_car(self, car, buyer):
        if car in self.cars:
            self.cars.remove(car)
            sale = VehicleSale(car, buyer)
            sale.generate_sale()
            self.sales_registry.append(sale)
            print(f"Car sold to {buyer.get_full_name()}: {car.get_description()}")
            self.sold_cars.append(sale)
        else:
            print("Car not found in the salon!")

    def service_car(self, car, service_description, cost):
        if car in self.cars:
            self.service_registry.append((car, service_description, cost))
            print(f"Car {car.get_description()} is scheduled for service: {service_description}, cost: ${cost}")
        else:
            print("Car not found in the salon!")

    def show_available_cars(self):
        if not self.cars:
            print("No cars available in the salon.")
        else:
            for car in self.cars:
                print(car.get_description())

    def interactive_console(self):
        while True:
            print("\n--- Auto Salon Management ---")
            print("1. Add Passenger Car to Salon")
            print("2. Add Truck to Salon")
            print("3. Sell Car")
            print("4. Service Car")
            print("5. Show Available Cars")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                brand = input("Enter car brand: ")
                unique_number = input("Enter unique car number: ")
                price = float(input("Enter car price: "))
                number_of_seats = int(input("Enter number of seats: "))
                new_passenger_car = PassengerCar(brand, unique_number, price, number_of_seats)
                self.add_car(new_passenger_car)

            elif choice == '2':
                brand = input("Enter truck brand: ")
                unique_number = input("Enter unique truck number: ")
                price = float(input("Enter truck price: "))
                max_load_capacity = float(input("Enter max load capacity (tons): "))
                new_truck = Truck(brand, unique_number, price, max_load_capacity)
                self.add_car(new_truck)

            elif choice == '3':
                unique_number = input("Enter unique car/truck number: ")
                first_name = input("Enter buyer's first name: ")
                last_name = input("Enter buyer's last name: ")
                phone = input("Enter buyer's phone: ")
                email = input("Enter buyer's email: ")
                buyer = Buyer(first_name, last_name, phone, email)
                car = next((car for car in self.cars if car._Car__unique_number == unique_number), None)
                if car:
                    self.sell_car(car, buyer)
                else:
                    print("Car not found!")

            elif choice == '4':
                unique_number = input("Enter unique car/truck number for service: ")
                service_description = input("Enter service description: ")
                cost = float(input("Enter service cost: "))
                car = next((car for car in self.cars if car._Car__unique_number == unique_number), None)
                if car:
                    self.service_car(car, service_description, cost)
                else:
                    print("Car not found!")

            elif choice == '5':
                self.show_available_cars()

            elif choice == '6':
                print("Exiting salon management.")
                break

            else:
                print("Invalid option. Please try again.")

salon = AutoSalon("Luxury Vehicles")
salon.interactive_console()
