import json
from datetime import datetime

def convert_iso_to_millis(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

def unify_format(data):
    unified = {
        "deviceId": data.get("deviceId"),
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
    }

    ts = data.get("timestamp")
    unified["timestamp"] = convert_iso_to_millis(ts) if isinstance(ts, str) else ts
    return unified

# ---- Test Runner ----
if __name__ == "__main__":
    try:
        with open("data-1.json") as f1, open("data-2.json") as f2:
            d1 = json.load(f1)
            d2 = json.load(f2)

        print("Unified from data-1.json:")
        print(unify_format(d1))

        print("\nUnified from data-2.json:")
        print(unify_format(d2))
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
