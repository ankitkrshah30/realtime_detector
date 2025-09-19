import pathway as pw
import logging
from pathway.xpacks.io.fs import FileProcessingMode

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
        mode=FileProcessingMode(mode='streaming', file_watcher='POLLING'),
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