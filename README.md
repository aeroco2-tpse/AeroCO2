# AeroCO2

Software tool for evaluating the CO₂ reduction potential of lighter and more energy-efficient aircraft cabin components.

# About

AeroCO2 calculates how much fuel and CO₂ can be saved on a reference long-haul flight when cabin components become lighter or use less power. The Boeing 787 is the preferred reference aircraft.

# Current status
*Milestone "Lauffähiger Code", November 2026* 

First runnable prototype: `src/aeroco2/main.py` calculates fuel burn and CO₂ for an example A319 flight using OpenAP and plots the fuel flow. It is adapted from the OpenAP examples (see [Acknowledgements](#acknowledgements)). See [Setup](#setup) and [Usage](#usage) for how to run it.

# Requirements
- Python 3.11 or newer
- pip
- Git
- Runs on Windows, macOS and Linux

# Setup
Clone the repository:
``` bash
git clone https://github.com/aeroco2-tpse/AeroCO2.git
cd AeroCO2
```

Create and activate a virtual environment:

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

From the project root, with the virtual environment active:

```bash
python src/aeroco2/main.py
```

A window opens with a plot of the fuel flow over time. After closing it, the total fuel and CO₂ are printed in the terminal.

## Project structure

```
.
├── data/
│   └── flight_a319_opensky.csv   # example flight data (OpenAP)
├── src/
│   └── aeroco2/
│       └── main.py               # fuel and CO2 calculation
├── requirements.txt              # Python dependencies
└── README.md
```

## Data and assumptions

- **Flight data:** `data/flight_a319_opensky.csv` is an Airbus A319 flight from Paris-Le Bourget to Stockholm-Bromma on 2 January 2018, recorded by the [OpenSky Network](https://opensky-network.org). It contains no fuel or mass data, and the take-off and landing phases below about 8,000 ft are missing.
- **Take-off mass:** assumed to be 66,000 kg.
- **True airspeed:** the ground speed from the flight data is used as an approximation of true airspeed. This ignores wind.
- **CO₂ factor:** 3.16 kg CO₂ per kg of fuel (ICAO), as applied by the OpenAP emission model.

## Acknowledgements

The calculation in `main.py` is adapted from the OpenAP examples and documentation ([github.com/junzis/openap](https://github.com/junzis/openap), [openap.dev](https://openap.dev)). The example flight data in `data/` also comes from the OpenAP repository.

> Sun, J., Hoekstra, J. M., & Ellerbroek, J. (2020). OpenAP: An open-source aircraft performance model for air transportation studies and simulations. *Aerospace*, 7(8), 104.

## License

This project builds on OpenAP and is released under the GNU Lesser General Public License v3.0 (LGPL-3.0).

## Team

Florian Müller, Hubert Tanuwidjaja, Olga Makarova, Reyvaldo Siahaan, Timon Hellenthal

- **Client:** Mariia Halchynska, M.Sc. (FSR, TU Darmstadt)
- **Team supervisor:** Merha Imran
- **Contact:** olga.makarova@stud.tu-darmstadt.de


TPSE WiSe 2026/27, TU Darmstadt


A first runnable prototype in our target stack (Python, pip, OpenAP, pandas). The script src/aeroco2/main.py loads an example flight (Airbus A319, OpenSky data from data/), calculates the fuel burn minute by minute with the OpenAP fuel model, converts it to CO₂ and plots the fuel flow over time. The code is adapted from the OpenAP examples. 

How to build and start it: Described in README.md in our repository (https://github.com/aeroco2-tpse/AeroCO2), sections "Setup" and "Usage". In short: with Python 3.11 or newer, create a virtual environment (python -m venv .venv), activate it (macOS/Linux: source .venv/bin/activate, Windows: .venv\Scripts\activate), run pip install -r requirements.txt, then start with python src/aeroco2/main.py.