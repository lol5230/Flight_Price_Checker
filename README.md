## Documentation

### Server
The server consists of the FlightChecker class. This creates an object that saves a token to the API. The front end can 
have the FlightChecker object search for data on flights by giving it departure location and date and arrival location 
and date. Dates should be given in the format YYYY-MM without a day. The locations should correspond to a three letter
airport codes easily found online. The server can also sort information based on price (lowest to highest) and departure
times (earliest to latest). 

### Client
The client is a fairly simple python script to be run from the command line. The user will put in 4 required arugments
with fifth argument being optional. Below is an example of a valid command.
```commandline
python flight_price_checker.py -s "2023-06" -r "2023-06" -f "PIT" -t "JFK" -o "departure"
```
Here's the output that command returned:
```commandline
Flights to JFK from PIT:
  Flight Option 1:
    Price: $329
    Departure: Wednesday, June 14, 2023 at 06:30 AM
    Return: Saturday, June 17, 2023 at 09:55 AM
  Flight Option 2:
    Price: $235
    Departure: Wednesday, June 14, 2023 at 01:03 PM
    Return: Wednesday, June 21, 2023 at 09:15 AM

```

For more information about the arguments the user can run:
```commandline
python flight_price_checker.py --help
```

### Installation
1. Install Python 3.11.1
2. Run `pip install -r requirements.txt` (don't forget to activate a virtual environment if you want to)