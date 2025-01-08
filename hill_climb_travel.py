from typing import List, Tuple, Dict
import mlrose

class Flight:
    def __init__(self, origin: str, destination: str, departure: str, arrival: str, price: int):
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.price = price


class TravelSchedule:
    def __init__(self, people: List[Tuple[str, str]], final_destination: str, flights: Dict[Tuple[str, str], List[Flight]]):
        self.people = people
        self.final_destination = final_destination
        self.flights = flights

    def calculate_total_cost(self, schedule: List[int]) -> int:
        flight_id = -1
        total_cost = 0

        for i in range(len(schedule) // 2):
            origin = self.people[i][1]
            flight_id += 1
            outbound = self.flights[(origin, self.final_destination)][schedule[flight_id]]
            total_cost += outbound.price
            flight_id += 1
            return_flight = self.flights[(self.final_destination, origin)][schedule[flight_id]]
            total_cost += return_flight.price

        return total_cost

    def print_schedule(self, schedule: List[int]) -> None:
        flight_id = -1
        for i in range(len(schedule) // 2):
            origin = self.people[i][1]
            flight_id += 1
            outbound = self.flights[(origin, self.final_destination)][schedule[flight_id]]
            flight_id += 1
            return_flight = self.flights[(self.final_destination, origin)][schedule[flight_id]]

            print(f"Origin: {origin}, Destination: {self.final_destination}, Outbound: {outbound.departure}-{outbound.arrival}, Price: {outbound.price}")
            print(f"Destination: {self.final_destination}, Return: {return_flight.departure}-{return_flight.arrival}, Price: {return_flight.price}")


def load_flights(file: str) -> Dict[Tuple[str, str], List[Flight]]:
    flights: Dict[Tuple[str, str], List[Flight]] = {}

    with open(file) as f:
        for line in f:
            origin, destination, departure, arrival, price = line.strip().split(",")
            flights.setdefault((origin, destination), []).append(Flight(origin, destination, departure, arrival, int(price)))

    return flights


if __name__ == "__main__":
    people: List[Tuple[str, str]] = [
        ("Lisbon", "LIS"),
        ("Madrid", "MAD"),
        ("Paris", "CDG"),
        ("Dublin", "DUB"),
        ("Brussels", "BRU"),
        ("London", "LHR"),
    ]
    destination: str = "FCO"

    flights = load_flights("flights.txt")

    travel_schedule = TravelSchedule(people, destination, flights)

    example_schedule: List[int] = [1, 2, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]

    initial_cost = travel_schedule.calculate_total_cost(example_schedule)
    print(f"Initial cost: {initial_cost}")

    def fitness_function(schedule: List[int]) -> int:
        return travel_schedule.calculate_total_cost(schedule)

    fitness = mlrose.CustomFitness(fitness_function)

    problem = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

    best_solution, best_cost = mlrose.hill_climb(problem, random_state=1)

    print("\nBest solution found:")
    travel_schedule.print_schedule(best_solution)
    print(f"Total cost of the best solution: {best_cost}")
