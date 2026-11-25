from pathlib import Path
import pandas as pd
import openap
from aeroco2.flight_data import load_flight_data
from aeroco2.simulation import simulate_flight

# ---- Paths -----
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent
DATA_DIR = PROJECT_ROOT/"data/reference_flights"

flight_data = load_flight_data(DATA_DIR/"flight_a319_opensky.csv")

baseline_flight = simulate_flight(
    airplane="A319",
    mass_takeoff_assumed=66000,
    flight_data=flight_data
)

reduced_flight = simulate_flight(
    airplane="A319",
    mass_takeoff_assumed=65000,
    flight_data=flight_data
)

print(baseline_flight["fuel_consumed"])
print(baseline_flight["co2_emissions"])


print(reduced_flight["fuel_consumed"])
print(reduced_flight["co2_emissions"])