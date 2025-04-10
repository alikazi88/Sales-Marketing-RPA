# Sales & Marketing Process Support Automation
# --------------------------------------------------
# Step-by-step project to simulate data-driven sales and marketing process automation

import time
from datetime import datetime
import pandas as pd
from email.mime.text import MIMEText

# Step 1: Simulate sales & marketing campaign data
def fetch_campaign_data():
    print("📊 Fetching campaign performance data...")
    time.sleep(1)
    return pd.DataFrame({
        "Campaign": ["Email Blast", "Social Media", "Webinar", "Referral Program"],
        "Leads": [120, 200, 75, 50],
        "Conversions": [30, 50, 20, 15],
        "Cost": [500, 800, 400, 200]
    })

# Step 2: Analyze performance metrics
def analyze_data(df):
    df["Conversion Rate (%)"] = round((df["Conversions"] / df["Leads"]) * 100, 2)
    df["Cost per Lead ($)"] = round(df["Cost"] / df["Leads"], 2)
    df["Cost per Conversion ($)"] = round(df["Cost"] / df["Conversions"], 2)
    return df

# Step 3: Generate a campaign performance report
def generate_report(df):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = [
        f"# 📈 Sales & Marketing Performance Report\n",
        f"Generated on: {timestamp}\n\n",
        df.to_markdown(index=False),
        "\n\n**Key Metrics Explained:**",
        "- Conversion Rate: % of leads that became customers",
        "- Cost per Lead: Efficiency of ad spend",
        "- Cost per Conversion: Profitability of the campaign"
    ]
    with open("campaign_report.md", "w", encoding="utf-8") as file:
        file.writelines(line + "\n" for line in report_lines)
    print("✅ Campaign performance report generated.")
    return timestamp

# Step 4: Notify marketing team (simulated email)
def send_notification(timestamp):
    sender = "analytics@company.com"
    recipient = "marketing@company.com"
    subject = "[Automated] Campaign Performance Report"
    body = f"The latest sales & marketing report was generated on {timestamp}. Please review the 'campaign_report.md' file."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    print("📤 Simulating email notification...")
    time.sleep(1)
    print(f"✅ Notification sent to {recipient} with subject '{subject}'")

# Run the end-to-end workflow
if __name__ == "__main__":
    print("🚀 Initiating Sales & Marketing Automation...")
    raw_data = fetch_campaign_data()
    analyzed_data = analyze_data(raw_data)
    generated_on = generate_report(analyzed_data)
    send_notification(generated_on)
    print("🎯 Process complete. Report ready for review.")
