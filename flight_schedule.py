import csv
class FlightSchedule:
    def __init__(self):
        self.flights = []
        self.plane_identifiers = []
        self.longestFlight = 0
        
    def read_data_from_file(self):
        with open("flight_data.csv", encoding='utf-8') as file:
            reader = csv.reader(file)
            mymax = 0
            planeset = set()
            for rows in reader:
                self.flights.append(rows[0])
                planeset.add(rows[1])
                if(mymax < int(rows[4])):
                    self.longestFlight = int(rows[0])
                    mymax = int(rows[4])
            
            self.plane_identifiers = list(planeset)

    def determine_longest_flight(self):
        return(self.longestFlight)
