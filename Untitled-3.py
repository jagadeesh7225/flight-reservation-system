class Flight:
    def __init__(self, flight_number, origin, destination, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passenger_list = []  # List to hold passengers

    def book_seat(self, passenger):
        if self.available_seats > 0:
            self.passenger_list.append(passenger)
            self.available_seats -= 1
            return True
        return False

    def cancel_seat(self, passport_number):
        for passenger in self.passenger_list:
            if passenger.passport_number == passport_number:
                self.passenger_list.remove(passenger)
                self.available_seats += 1
                return True
        return False

    def __str__(self):
        return (f"Flight {self.flight_number}: {self.origin} -> {self.destination} | "
                f"Seats: {self.available_seats}/{self.total_seats}")


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


class FlightReservationSystem:
    def __init__(self):
        self.flights = {}  # Dictionary to store flights with flight number as key

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def find_flight(self, flight_number):
        return self.flights.get(flight_number)

    def book_flight(self, flight_number, passenger):
        flight = self.find_flight(flight_number)
        if flight:
            return flight.book_seat(passenger)
        return False

    def cancel_booking(self, flight_number, passport_number):
        flight = self.find_flight(flight_number)
        if flight:
            return flight.cancel_seat(passport_number)
        return False

    def view_flight(self, flight_number):
        flight = self.find_flight(flight_number)
        if flight:
            return str(flight)
        return "Flight not found."


def main():
    system = FlightReservationSystem()

    while True:
        print("\n--- Flight Reservation System ---")
        print("1. Add Flight")
        print("2. Book Flight")
        print("3. Cancel Booking")
        print("4. View Flight")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            total_seats = int(input("Enter number of seats: "))
            flight = Flight(flight_number, origin, destination, total_seats)
            system.add_flight(flight)
            print(f"Flight {flight_number} added successfully.")

        elif choice == '2':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            passport_number = input("Enter passport number: ")
            passenger = Passenger(name, passport_number)
            if system.book_flight(flight_number, passenger):
                print(f"Booking successful for {name} on flight {flight_number}.")
            else:
                print("Booking failed. Flight may not exist or no seats available.")

        elif choice == '3':
            flight_number = input("Enter flight number: ")
            passport_number = input("Enter passport number: ")
            if system.cancel_booking(flight_number, passport_number):
                print(f"Booking cancellation successful for passport number {passport_number}.")
            else:
                print("Cancellation failed. Flight or booking not found.")

        elif choice == '4':
            flight_number = input("Enter flight number: ")
            print(system.view_flight(flight_number))

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
