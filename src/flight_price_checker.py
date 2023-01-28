import argparse

# Initialize the parser
parser = argparse.ArgumentParser()

# Define the command line arguments
parser.add_argument("-s", "--start-date", help="Start date (YYYY-MM-DD)")
parser.add_argument("-r", "--return-date", help="Return date (YYYY-MM-DD)")
parser.add_argument("-f", "--from-location", help="Start location")
parser.add_argument("-t", "--to-location", help="Arrival location")
parser.add_argument("-o", "--sort", help="Sort results by price or departure time (price/time)", default="price")

# Parse the command line arguments
args = parser.parse_args()

# Print the results
print("Start date: ", args.start_date)
print("Return date: ", args.return_date)
print("Start location: ", args.from_location)
print("Arrival location: ", args.to_location)
print("Sort results by: ", args.sort)