from pathlib import Path

from matplotlib import dates
import matplotlib
import pandas as pd
import openap
import matplotlib.pyplot as plt

# ---- Paths -----
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent
DATA_DIR = PROJECT_ROOT/"data"

mass_takeoff_assumed = 66000  # kg

fuelflow = openap.FuelFlow("A319")
emission = openap.Emission(ac="A319")
# Load the data
df = pd.read_csv(DATA_DIR/
    "flight_a319_opensky.csv",
    parse_dates=["timestamp"],
    dtype={"icao24": str},
)

# Calculate seconds between each  timestamp
df = df.assign(d_ts=lambda d: d.timestamp.diff().dt.total_seconds().bfill())

matplotlib.rc("font", size=11)
matplotlib.rc("font", family="DejaVu Sans")
matplotlib.rc("lines", linewidth=2, markersize=8)
matplotlib.rc("grid", color="darkgray", linestyle=":")


def format_ax(ax):
    ax.xaxis.set_major_formatter(dates.DateFormatter("%H:%M"))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.yaxis.set_label_coords(-0.1, 1.03)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha("left")
    ax.grid()


mass_current = mass_takeoff_assumed

fuelflow_every_step = []
fuel_every_step = []

for i, row in df.iterrows():
    ff = fuelflow.enroute(
        mass=mass_current,
        tas=row.groundspeed,
        alt=row.altitude,
        vs=row.vertical_rate,
    )
    fuel = ff * row.d_ts
    fuelflow_every_step.append(ff)
    fuel_every_step.append(fuel)
    mass_current -= fuel
    
#Expand the DataFrame with fuel flow, fuel and CO2 emission data
df = df.assign(fuel_flow=fuelflow_every_step, fuel=fuel_every_step)
df = df.assign(co2_flow=lambda d: emission.co2(d.fuel_flow))
df = df.eval("co2 = co2_flow * d_ts / 1000")
total_emission=df.co2.sum()
plt.figure(figsize=(7, 2))
plt.plot(df.timestamp, df.fuel_flow, color="tab:red")
plt.ylabel("fuel flow (kg/s)")
format_ax(plt.gca())
plt.show()
print(f"Total fuel consumed: {df.fuel.sum():.2f} kg")
print(f"Total emission CO2: {total_emission:.2f} kg")