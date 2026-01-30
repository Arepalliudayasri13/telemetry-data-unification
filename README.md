# Telemetry Data Unification

## Project Overview
This project unifies telemetry data from multiple JSON data sources into a single structured output. The solution processes input telemetry files and generates a consolidated result file.

## Files Included
- `main.py` – Main script that processes telemetry data.
- `data-1.json` – First telemetry data source.
- `data-2.json` – Second telemetry data source.
- `pyproject.toml` – Project configuration and dependencies.
- `uv.lock` – Dependency lock file for environment consistency.

## How It Works
The program:
1. Reads telemetry data from input JSON files.
2. Processes and combines the datasets.
3. Outputs unified results into a result file.

## How to Run
1. Ensure Python is installed.
2. Place input JSON files in the project folder.
3. Run:

```bash
python main.py
