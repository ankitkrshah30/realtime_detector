import pathway as pw
import logging

# THE FIX: Add these two lines to set the log level.
# This will hide the noisy INFO messages from the Pathway engine.
logging.basicConfig(level=logging.WARNING)

class LoginEvent(pw.Schema):
    timestamp: pw.DateTimeNaive
    user_id: str
    ip_address: str
    country: str
    status: str

def run():
    login_stream = pw.io.csv.read(
        "./login_events.csv",
        schema=LoginEvent,
        mode="streaming",
        autocommit_duration_ms=1000,
    )

    anomalies = login_stream.filter(
        (login_stream.country == "Russia") | (login_stream.country == "China")
    )

    print("\n--- Waiting for anomalies. The table will appear below and update in real-time. ---\n")
    pw.debug.compute_and_print(anomalies)

    pw.run()

if __name__ == "__main__":
    run()