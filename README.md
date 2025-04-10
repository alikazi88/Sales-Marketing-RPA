# Sales-Marketing-RPA
This project simulates an end-to-end sales and marketing workflow automation, ideal for showcasing process enhancement, analytics integration, and smart reporting in a real-world business context.

## 🔁 Workflow Overview

The workflow includes:

1. **Campaign Data Simulation** – Emulates leads, conversions, and costs from multiple channels.
2. **Performance Metrics Calculation** – Automatically computes conversion rates, cost per lead, and cost per conversion.
3. **Markdown Report Generation** – Creates a human-readable `.md` report summarizing key campaign metrics.
4. **Notification Simulation** – Triggers a mock email to notify the marketing team (console simulation).

## 📈 Technologies Used

- **Python 3.x**
- **Pandas** for data processing
- **Markdown** generation for readable reports
- **MIMEText** for simulating email notifications
- **Datetime** and **time** for tracking process flow

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Sales-Marketing-RPA.git
cd Sales-Marketing-RPA
pip install pandas tabulate
python sales_marketing_rpa.py
```

# 📈 Sales & Marketing Performance Report
Generated on: 2025-04-10 14:30:00

| Campaign         |   Leads |   Conversions |   Cost |   Conversion Rate (%) |   Cost per Lead ($) |   Cost per Conversion ($) |
|:-----------------|--------:|--------------:|-------:|-----------------------:|---------------------:|---------------------------:|
| Email Blast      |     120 |            30 |    500 |                 25.00 |                 4.17 |                      16.67 |
| Social Media     |     200 |            50 |    800 |                 25.00 |                 4.00 |                      16.00 |
| Webinar          |      75 |            20 |    400 |                 26.67 |                 5.33 |                      20.00 |
| Referral Program |      50 |            15 |    200 |                 30.00 |                 4.00 |                      13.33 |


