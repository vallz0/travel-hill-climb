# Travel Hill Climb Optimizer ✈️

A Python application that uses the Hill Climbing algorithm to optimize flight schedules for multiple travelers. This project leverages the **mlrose** library to minimize the total travel cost while considering both outbound and return flights for each person in the group.

---

## Features 🌟
- **Cost Calculation**: Calculates the total cost of travel based on a predefined schedule.
- **Optimization**: Uses the Hill Climbing algorithm to find the most cost-effective flight schedule.
- **Multi-Traveler Support**: Handles multiple travelers departing from different origins to a common destination.
- **Clean Design**: Implements a modular, object-oriented design for easy maintenance and scalability.

---

## Technologies Used 🛠️
- **Python**: Core programming language.
- **mlrose**: Library for solving optimization problems using various algorithms, including Hill Climbing.
- **Type Hints**: For improved code readability and maintainability.

---

## Installation 📦

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/travel-hill-climb.git
   cd travel-hill-climb
   ```

2. Install dependencies:
   ```bash
   pip install mlrose
   ```

3. Add your flight data to a `flights.txt` file (sample format provided below).

4. Run the script:
   ```bash
   python hill_climb_travel.py
   ```

---

## Flight Data Format 🔄
Ensure the `flights.txt` file contains flight details in the following format:
```
Origin,Destination,Departure,Arrival,Price
LIS,FCO,08:00,10:00,250
MAD,FCO,09:30,12:00,200
...
```
Each line represents a flight with the following fields:
- **Origin**: The airport code for the departure location.
- **Destination**: The airport code for the arrival location.
- **Departure**: Departure time (e.g., `08:00`).
- **Arrival**: Arrival time (e.g., `10:00`).
- **Price**: Cost of the flight in integer format.

---

## Example Output 📊

When running the script, you will see an output similar to this:

- **Initial Cost**: 1500
- **Optimized Cost**: 1200
- **Best Schedule**: Detailed list of flights for each traveler.

Sample flight details:
```
Origin: LIS, Destination: FCO, Outbound: 08:00-10:00, Price: 250
Destination: FCO, Return: 18:00-20:00, Price: 300
...
```

---
