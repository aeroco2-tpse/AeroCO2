
import pandas as pd
import openap

def simulate_flight(airplane: str, mass_takeoff_assumed: float, flight_data: pd.DataFrame):
    """
    Simulate a flight using the reference model.

    Args:
        airplane (str): The type of airplane (e.g., "A319").
        mass_takeoff_assumed (float): The assumed takeoff mass in kg.
    """
    
    fuelflow = openap.FuelFlow(airplane)
    emission = openap.Emission(ac=airplane)


    mass_current = mass_takeoff_assumed
    fuel_every_step = []
    fuel_flow_every_step = []

    for i, row in flight_data.iterrows():
        ff = fuelflow.enroute(
            mass=mass_current,
            tas=row.groundspeed,
            alt=row.altitude,
            vs=row.vertical_rate,
        )
        fuel = ff * row.d_ts

        fuel_flow_every_step.append(ff)
        fuel_every_step.append(fuel)
        mass_current -= fuel
        
       
    result_df = flight_data.copy()

    result_df["fuel_flow"] = fuel_flow_every_step
    result_df["fuel"] = fuel_every_step

    result_df["co2_flow"] = emission.co2(
        result_df["fuel_flow"]
    )

    result_df["co2"] = (
        result_df["co2_flow"] * result_df["d_ts"] / 1000
    )

    total_fuel = result_df["fuel"].sum()
    total_co2 = result_df["co2"].sum()

    return {
        "fuel_consumed": total_fuel,
        "co2_emissions": total_co2,
        "flight_data": result_df,
        "initial_mass": mass_takeoff_assumed,
        "final_mass": mass_current
    }

    
   