import pandas as pd
import os

def generate_report(report_data):

    # Create outputs folder automatically
    os.makedirs("outputs", exist_ok=True)

    df = pd.DataFrame(report_data)

    report_path = os.path.join(
        "outputs",
        "email_report.csv"
    )

    df.to_csv(report_path, index=False)

    print("Report generated successfully.")