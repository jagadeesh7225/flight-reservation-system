import datetime

class Flight:
    def __init__(self, flight_id, airline, source, destination, departure_time, arrival_time, price, seats_available):
        self.flight_id = flight_id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats_available = seats_available

    def __str__(self):
        return f"Flight ID: {self.flight_id}\nAirline: {self.airline}\nSource: {self.source}\nDestination: {self.destination}\nDeparture Time: {self.departure_time}\nArrival Time: {self.arrival_time}\nPrice: {self.price}\nSeats Available: {self.seats_available}"

class Passenger:
    def __init__(self, passenger_id, name, age, contact, passport_number):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.contact = contact
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger ID: {self.passenger_id}\nName: {self.name}\nAge: {self.age}\nContact: {self.contact}\nPassport Number: {self.passport_number}"

class Reservation:
    def __init__(self, reservation_id, flight_id, passenger_id, seat_number):
        self.reservation_id = reservation_id
        self.flight_id = flight_id
        self.passenger_id = passenger_id
        self.seat_number = seat_number

    def __str__(self):
        return f"Reservation ID: {self.reservation_id}\nFlight ID: {self.flight_id}\nPassenger ID: {self.passenger_id}\nSeat Number: {self.seat_number}"

# Sample flight data
flights = [
    Flight(1, "Airline A", "City1", "City2", datetime.datetime(2024, 9, 1, 10, 0), datetime.datetime(2024, 9, 1, 12, 0), 500.0, 10),
    Flight(2, "Airline B", "City3", "City4", datetime.datetime(2024, 9, 2, 8, 0), datetime.datetime(2024, 9, 2, 11, 0), 600.0, 8),
    # ... add more flights
]

# Sample passenger data
passengers = [
    Passenger(1, "John Doe", 30, "1234567890", "ABC12345"),
    Passenger(2, "Jane Smith", 25, "9876543210", "DEF67890"),
    # ... add more passengers
]

# Sample reservation data
reservations = []

def display_flights():
    print("Available Flights:")
    for flight in flights:
        print(flight)

def search_flights(source, destination, departure_time, price):
    matching_flights = []
    for flight in flights:
        if (source is None or flight.source == source) and \
           (destination is None or flight.destination == destination) and \
           (departure_time is None or flight.departure_time == departure_time) and \
           (price is None or flight.price <= price):
            matching_flights.append(flight)
    return matching_flights

def reserve_flight(flight_id, passenger_id):
    for flight in flights:
        if flight.flight_id == flight_id:
            if flight.seats_available > 0:
                reservation_id = len(reservations) + 1
                seat_number = f"Seat {flight.seats_available}"
                reservation = Reservation(reservation_id, flight_id, passenger_id, seat_number)
                reservations.append(reservation)
                flight.seats_available -= 1
                print("Reservation successful!")
                return reservation
            else:
                print("Flight is fully booked.")
                return None
    print("Flight not found.")
    return None

def cancel_reservation(reservation_id):
    for reservation in reservations:
        if reservation.reservation_id == reservation_id:
            for flight in flights:
                if flight.flight_id == reservation.flight_id:
                    flight.seats_available += 1
            reservations.remove(reservation)
            print("Reservation canceled.")
            return True
    print("Reservation not found.")
    return False

def view_reservations(passenger_id):
    matching_reservations = []
    for reservation in reservations:
        if reservation.passenger_id == passenger_id:
            matching_reservations.append(reservation)
    return matching_reservations

def generate_ticket(reservation_id):
    for reservation in reservations:
        if reservation.reservation_id == reservation_id:
            # Generate ticket content (e.g., PDF, email)
            print("Ticket generated for Reservation ID:", reservation_id)
            return True
    print("Reservation not found.")
    return False

# Main loop
while True:
    print("\nFlight Reservation System")
    print("1. Display Flights")
    print("2. Search Flights")
    print("3. Reserve Flight")
    print("4. Cancel Reservation")
    print("5. View Reservations")
    print("6. Generate Ticket")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_flights()
    elif choice == 2:
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        departure_time = input("Enter departure time (YYYY-MM-DD HH:MM): ")
        price = input("Enter maximum price: ")
        if departure_time:
            departure_time = datetime.datetime.strptime(departure_time, "%Y-%m-%d %H:%M")
        if price:
            price = float(price)
        matching_flights = search_flights(source, destination, departure_time, price)
        if matching_flights:
            print("Matching Flights:")
            for flight in matching_flights:
                print(flight)
        else:
            print("No matching flights found.")
    elif choice == 3:
        flight_id = int(input("Enter flight ID: "))
        passenger_id = int(input("Enter passenger ID: "))
        reservation = reserve_flight(flight_id, passenger_id)
        if reservation:
            print("Reservation details:")
            print(reservation)
    elif choice == 4:
        reservation_id = int(input("Enter reservation ID: "))
        cancel_reservation(reservation_id)
    elif choice == 5:
        passenger_id = int(input("Enter passenger ID: "))
        reservations = view_reservations(passenger_id)
        if reservations:
            print("Your Reservations:")
            for reservation in reservations:
                print(reservation)
        else:
            print("No reservations found for this passenger.")
    elif choice == 6:
        reservation_id = int(input("Enter reservation ID: "))
        generate_ticket(reservation_id)
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")