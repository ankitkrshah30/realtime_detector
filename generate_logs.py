import csv
import random
import time
from datetime import datetime

# Configuration for the data generation
USERS = ["user_A", "user_B", "user_C", "user_D", "user_E"]
NORMAL_LOCATIONS = {
    "user_A": "India",
    "user_B": "USA",
    "user_C": "India",
    "user_D": "Germany",
    "user_E": "USA",
}
ANOMALOUS_LOCATIONS = ["Russia", "China", "North Korea", "Brazil"]
LOG_FILE = "login_events.csv"
HEADER = ["timestamp", "user_id", "ip_address", "country", "status"]


def generate_log_entry():
    """Generates a single log entry, occasionally creating an anomaly."""
    user = random.choice(USERS)

    # Decide if this will be an anomalous login (10% chance)
    if random.random() < 0.1:
        # Create an ANOMALY
        country = random.choice(ANOMALOUS_LOCATIONS)
        status = random.choice(["success", "failure"])
    else:
        # Create a NORMAL login
        country = NORMAL_LOCATIONS[user]
        status = "success"

    timestamp = datetime.now().isoformat()
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    return [timestamp, user, ip_address, country, status]


def main():
    """Main function to continuously generate and write logs."""
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)

    print(f"Generating mock logs into '{LOG_FILE}'... Press CTRL+C to stop.")

    while True:
        try:
            log_entry = generate_log_entry()

            with open(LOG_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(log_entry)

            print(f"Appended log: {log_entry}")

            # *** THIS IS THE MODIFIED LINE FOR FASTER GENERATION ***
            time.sleep(random.uniform(0.1, 0.5))

        except KeyboardInterrupt:
            print("\nLog generation stopped.")
            break


if __name__ == "__main__":
    main()