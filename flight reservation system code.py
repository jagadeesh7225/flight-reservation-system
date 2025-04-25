class Flight:
    def __init__(self, flight_number, origin, destination, total_seats=100):  # Default seats
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passenger_list = []  # List to hold passengers

    def book_seat(self, passenger, seat_count):
        if self.available_seats >= seat_count:
            for _ in range(seat_count):
                self.passenger_list.append(passenger)
            self.available_seats -= seat_count
            return True
        return False

    def cancel_seat(self, passport_number):
        passengers_to_remove = [
            passenger for passenger in self.passenger_list if passenger.passport_number == passport_number
        ]
        if passengers_to_remove:
            for passenger in passengers_to_remove:
                self.passenger_list.remove(passenger)
            self.available_seats += len(passengers_to_remove)
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

    def generate_flight_number(self, origin, destination):
        return f"{origin[:3].upper()}-{destination[:3].upper()}"

    def find_or_create_flight(self, origin, destination):
        flight_number = self.generate_flight_number(origin, destination)
        if flight_number not in self.flights:
            # Create the flight if not found
            flight = Flight(flight_number, origin, destination)
            self.flights[flight_number] = flight
        return self.flights[flight_number]

    def book_flight(self, origin, destination, passenger, seat_count):
        flight = self.find_or_create_flight(origin, destination)
        return flight.book_seat(passenger, seat_count)

    def cancel_booking(self, origin, destination, passport_number):
        flight_number = self.generate_flight_number(origin, destination)
        flight = self.flights.get(flight_number)
        if flight:
            return flight.cancel_seat(passport_number)
        return False

    def view_flight(self, origin, destination):
        flight_number = self.generate_flight_number(origin, destination)
        flight = self.flights.get(flight_number)
        if flight:
            return str(flight)
        return "Flight not found."


def main():
    system = FlightReservationSystem()

    while True:
        print("\n--- Flight Reservation System ---")
        print("1. Book Flight")
        print("2. Cancel Booking")
        print("3. View Flight")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            name = input("Enter passenger name: ")
            passport_number = input("Enter passport number: ")
            seat_count = int(input("Enter number of seats to book: "))
            passenger = Passenger(name, passport_number)
            if system.book_flight(origin, destination, passenger, seat_count):
                print(f"Booking successful for {name} from {origin} to {destination} for {seat_count} seat(s).")
            else:
                print("Booking failed. No enough seats available.")

        elif choice == '2':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            passport_number = input("Enter passport number: ")
            if system.cancel_booking(origin, destination, passport_number):
                print(f"Booking cancellation successful for passport number {passport_number}.")
            else:
                print("Cancellation failed. Flight or booking not found.")

        elif choice == '3':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            print(system.view_flight(origin, destination))

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
