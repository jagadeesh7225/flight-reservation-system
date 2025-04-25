from collections import deque

class SeatTree:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = set(range(total_seats))  # Set to track available seats

    def assign_seat(self):
        if self.available_seats:
            seat = self.available_seats.pop()
            return seat
        return None

    def cancel_seat(self, seat):
        if seat < self.total_seats:
            self.available_seats.add(seat)

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, price, total_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.price = price
        self.seat_tree = SeatTree(total_seats)
        self.waitlist = deque()

    def book_seat(self):
        seat = self.seat_tree.assign_seat()
        if seat is not None:
            return seat
        return None

    def add_to_waitlist(self, passenger):
        self.waitlist.append(passenger)

    def cancel_seat(self, seat):
        self.seat_tree.cancel_seat(seat)
        if self.waitlist:
            next_passenger = self.waitlist.popleft()
            return next_passenger
        return None

    def __str__(self):
        return (f"Flight {self.flight_number} from {self.origin} to {self.destination}, "
                f"Departure: {self.departure_time}, Price: ${self.price}, "
                f"Available Seats: {self.seat_tree.total_seats - len(self.seat_tree.available_seats)}")

class ReservationSystem:
    def __init__(self):
        self.flights = {}  # Hash table to store flights by flight number
        self.passengers = {}  # Hash table to store passenger information by ID
        self.booking_counter = 0  # Counter for booking IDs

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def search_flight(self, flight_number):
        return self.flights.get(flight_number)

    def book_flight(self, flight_number, passenger_name):
        flight = self.search_flight(flight_number)
        if flight:
            seat = flight.book_seat()
            if seat is not None:
                booking_id = self.booking_counter + 1
                self.booking_counter = booking_id
                self.passengers[booking_id] = {
                    'flight': flight,
                    'seat': seat,
                    'passenger_name': passenger_name
                }
                return booking_id
            else:
                flight.add_to_waitlist(passenger_name)
                return "Flight is fully booked. Added to waitlist."
        return "Flight not found."

    def cancel_booking(self, booking_id):
        booking = self.passengers.pop(booking_id, None)
        if booking:
            flight = booking['flight']
            seat = booking['seat']
            next_passenger = flight.cancel_seat(seat)
            if next_passenger:
                return f"Booking canceled. Seat {seat} is now available. Next passenger {next_passenger} has been allocated this seat."
            return f"Booking canceled and seat {seat} is available."
        return "Booking ID not found."

    def display_flights(self):
        for flight in self.flights.values():
            print(flight)

# Example usage:
def main():
    system = ReservationSystem()

    # Adding flights
    flight1 = Flight('FL123', 'New York', 'Los Angeles', '2024-09-10 10:00', 300, 100)
    flight2 = Flight('FL456', 'San Francisco', 'Chicago', '2024-09-11 15:00', 250, 50)

    system.add_flight(flight1)
    system.add_flight(flight2)

    # Display all flights
    print("Available flights:")
    system.display_flights()

    # Booking a flight
    booking_id = system.book_flight('FL123', 'John Doe')
    print(f"\nBooking response: {booking_id}")

    # Attempting to book another seat on the same flight
    booking_id = system.book_flight('FL123', 'Jane Smith')
    print(f"\nBooking response: {booking_id}")

    # Canceling a booking
    print("\n" + system.cancel_booking(1))

    # Display all flights after booking and cancellation
    print("\nAvailable flights after booking and cancellation:")
    system.display_flights()

if __name__ == "__main__":
    main()
