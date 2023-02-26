import argparse
import subprocess
from flight_api import FlightChecker
import datetime


def is_valid_airport_code(code):
    """
    Returns true if the given Airport code is a valid one
    :param code: String, 3-letter code
    :return: Boolean true or false
    """
    command = ['curl', '-u', '179fe01e4a38a76:4d1a2496fe',
               f'https://aviation-edge.com/v2/public/routes?key=4d1a2496fe&departureIata={code}']
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


def format_date(date_str):
    """
    Helps format dates from the JSON returns
    :param date_str: The date string from a returned date from the FlightData api
    :return: String of a formatted date
    """
    dt = datetime.datetime.fromisoformat(date_str[:-6])
    return dt.strftime("%A, %B %d, %Y at %I:%M %p")


if __name__ == '__main__':
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Define the command line arguments
    parser.add_argument("-s", "--start-date", help="Start date (YYYY-MM)")
    parser.add_argument("-r", "--return-date", help="Return date (YYYY-MM)")
    parser.add_argument("-f", "--from-location",
                        help="The three letter designation of the airport at the start location")
    parser.add_argument("-t", "--to-location",
                        help="The three letter designation of the airport at the arrival location")
    parser.add_argument("-o", "--sort", help="Sort results by price or departure time (price/time)", default="price",
                        choices=['price', 'departure'])

    # Parse the args
    args = parser.parse_args()

    # Check if the airport codes are valid
    if not is_valid_airport_code(args.from_location):
        print(f"{args.from_location} is not a valid airport code, retry with a valid airport code")
        exit()

    if not is_valid_airport_code(args.to_location):
        print(f"{args.to_location} is not a valid airport code, retry with a valid airport code")
        exit()

    flight_checker = FlightChecker("a8c1bd2866bbff395e449ff3cdb3b16a")
    flight_checker.get_flight_price_data(args.from_location, args.to_location, args.start_date, args.return_date)

    flights = None
    if args.sort == 'price':
        flights = flight_checker.sort_flight_data_by_price()
    elif args.sort == 'departure':
        flights = flight_checker.sort_flight_data_by_departure()

    if flights:
        for city, flights in flights['data'].items():
            print(f"Flights to {args.to_location} from {args.from_location}:")
            for i, flight in flights.items():
                print(f"  Flight Option {int(i) + 1}:")
                print(f"    Price: ${flight['price']}")
                print(f"    Departure: {format_date(flight['departure_at'])}")
                print(f"    Return: {format_date(flight['return_at'])}")

    else:
        print("There are no flights that fit those parameters")
