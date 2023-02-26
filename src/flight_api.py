import requests
from datetime import datetime


class FlightChecker:
    def __init__(self, api_key):
        """
        The FlightChecker class creates an object that interfaces with the FlightData API served by Travelpayouts.
        To instantiate an object, the token for the API must be passed.
        :param api_key: String
        """
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
        url = f"http://api.travelpayouts.com/v1/prices/cheap?origin={origin}&destination={destination}&depart_date={depart_date}&return_date={return_date}&currency=usd&token={self.api_key}"
        self.flight_data = requests.get(url).json()

    def sort_flight_data_by_departure(self):
        """
        Return the list of flights in order of the earliest departure to latest
        """
        if self.flight_data['data']:
            city = list(self.flight_data["data"].keys())[0]
            flights_dict = self.flight_data["data"][city]

            flights_list = [(datetime.strptime(flights_dict[i]["departure_at"], "%Y-%m-%dT%H:%M:%S%z"), flights_dict[i])
                            for i in flights_dict]

            sorted_flights = sorted(flights_list, key=lambda x: x[0])

            sorted_flights_dict = {str(i): sorted_flights[i][1] for i in range(len(sorted_flights))}

            sorted_json = {"success": self.flight_data["success"], "data": {"NYC": sorted_flights_dict},
                           "currency": self.flight_data["currency"]}

            return sorted_json

        return None

    def sort_flight_data_by_price(self):
        """
        Returns the list of flights in order of lowest to highest price
        """
        if self.flight_data['data']:
            city = list(self.flight_data["data"].keys())[0]

            flights_dict = self.flight_data["data"][city]

            flights_list = [(flights_dict[i]["price"], flights_dict[i]) for i in flights_dict]

            sorted_flights = sorted(flights_list, key=lambda x: x[0])

            sorted_flights_dict = {str(i): sorted_flights[i][1] for i in range(len(sorted_flights))}

            sorted_json = {"success": self.flight_data["success"], "data": {city: sorted_flights_dict},
                           "currency": self.flight_data["currency"]}

            return sorted_json

        return None
