class Flight:
    def __init__(self, flight_number, origin, destination, seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.available_seats = seats
        self.passengers = []
        
    def book_seat(self, passenger):
        if self.available_seats > 0:
            self.passengers.append(passenger)
            self.available_seats -= 1
            return True
        return False
    
    def cancel_seat(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            self.available_seats += 1
            return True
        return False
    
    def __str__(self):
        return f"Flight {self.flight_number}: {self.origin} -> {self.destination} | Available Seats: {self.available_seats}/{self.seats}"

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
    
    def __str__(self):
        return f"Passenger: {self.name} (Passport: {self.passport_number})"

class Reservation:
    def __init__(self):
        self.flights = {}
    
    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight
    
    def book_flight(self, flight_number, passenger):
        if flight_number in self.flights:
            return self.flights[flight_number].book_seat(passenger)
        return False
    
    def cancel_flight(self, flight_number, passenger):
        if flight_number in self.flights:
            return self.flights[flight_number].cancel_seat(passenger)
        return False
    
    def view_flight(self, flight_number):
        if flight_number in self.flights:
            return str(self.flights[flight_number])
        return "Flight not found."

def main():
    # Create the reservation system
    reservation_system = Reservation()
    
    while True:
        print("\nFlight Reservation System")
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
            seats = int(input("Enter number of seats: "))
            flight = Flight(flight_number, origin, destination, seats)
            reservation_system.add_flight(flight)
            print(f"Flight {flight_number} added successfully.")
        
        elif choice == '2':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            passport_number = input("Enter passport number: ")
            passenger = Passenger(name, passport_number)
            if reservation_system.book_flight(flight_number, passenger):
                print(f"{name} successfully booked on flight {flight_number}.")
            else:
                print("Booking failed. Either the flight does not exist or there are no available seats.")
        
        elif choice == '3':
            flight_number = input("Enter flight number: ")
            name = input("Enter passenger name: ")
            passport_number = input("Enter passport number: ")
            passenger = Passenger(name, passport_number)
            if reservation_system.cancel_flight(flight_number, passenger):
                print(f"{name}'s booking on flight {flight_number} canceled successfully.")
            else:
                print("Cancellation failed. Either the flight does not exist or the passenger was not found.")
        
        elif choice == '4':
            flight_number = input("Enter flight number: ")
            flight_details = reservation_system.view_flight(flight_number)
            print(flight_details)
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
