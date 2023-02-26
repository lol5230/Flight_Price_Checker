import requests
from datetime import datetime


class FlightChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.flight_data = None

    def get_flight_price_data(self, origin, destination, depart_date, return_date):
        """
        Get the response for the flight data based on user input

        :param origin: String, 3 letters for airport code
        :param destination: String, 3 letters for airport code
        :param depart_date: YYYY-MM or YYYY-MM-DD
        :param return_date: YYYY-MM or YYYY-MM-DD
        :return:The json from the api response
        """
        # Set the API endpoint and required parameters

        # Build the API endpoint URL with the variables
        url = f"http://api.travelpayouts.com/v1/prices/cheap?origin={origin}&destination={destination}&depart_date={depart_date}&return_date={return_date}&currency=usd&token={self.api_key}"

        # Send the request and retrieve the response in JSON format
        self.flight_data = requests.get(url).json()

    def sort_flight_data_by_departure(self):
        """
        Return the list of flights in order of the earliest departure to latest
        """
        if self.flight_data['data']:
            city = list(self.flight_data["data"].keys())[0]

            # Get the flights dictionary from the data dictionary using the city key
            flights_dict = self.flight_data["data"][city]

            # Create a list of tuples containing the departure date and the flight data
            flights_list = [(datetime.strptime(flights_dict[i]["departure_at"], "%Y-%m-%dT%H:%M:%S%z"), flights_dict[i])
                            for i in flights_dict]

            # Sort the list by the departure date
            sorted_flights = sorted(flights_list, key=lambda x: x[0])

            # Create a new flights dictionary with the sorted data
            sorted_flights_dict = {str(i): sorted_flights[i][1] for i in range(len(sorted_flights))}

            # Create a new JSON object with the sorted data
            sorted_json = {"success": self.flight_data["success"], "data": {"NYC": sorted_flights_dict},
                           "currency": self.flight_data["currency"]}

            return sorted_json

        return None

    def sort_flight_data_by_price(self):
        """
        Returns the list of flights in order of lowest to highest price
        """
        # Find the city key in the data dictionary
        if self.flight_data['data']:
            city = list(self.flight_data["data"].keys())[0]

            # Get the flights dictionary from the data dictionary using the city key
            flights_dict = self.flight_data["data"][city]

            # Create a list of tuples containing the price and the flight data
            flights_list = [(flights_dict[i]["price"], flights_dict[i]) for i in flights_dict]

            # Sort the list by the price
            sorted_flights = sorted(flights_list, key=lambda x: x[0])

            # Create a new flights dictionary with the sorted data
            sorted_flights_dict = {str(i): sorted_flights[i][1] for i in range(len(sorted_flights))}

            # Create a new JSON object with the sorted data
            sorted_json = {"success": self.flight_data["success"], "data": {city: sorted_flights_dict},
                           "currency": self.flight_data["currency"]}

            return sorted_json

        return None


