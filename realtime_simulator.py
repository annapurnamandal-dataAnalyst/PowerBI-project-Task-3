
import requests
import json
import random
import time
from datetime import datetime

# ========================================
# PASTE YOUR PUSH URL HERE (between the quotes)
# ========================================
PUSH_URL = "https://api.powerbi.com/beta/4b46cd26-ba39-4ada-a944-f8be685e61be/datasets/0c52617e-3711-41cb-84ef-d8f7793e8f50/rows?redirectedFromSignup=1&experience=power-bi&key=%2B6gnxt0GKe%2BmMJKQOsuOS%2B0tWXNelzjVL3yJc%2FsZ3c5rlIBn2dDHxbiSD56m5iBvMVMQvQRyrHS5q%2BiW4%2FFb1w%3D%3D"

# Sample data for realistic simulation
categories = ["Electronics", "Furniture", "Clothing", "Office Supplies", "Food & Beverage"]
regions = ["North", "South", "East", "West", "Central"]

# Statistics for console display
total_sent = 0
total_revenue = 0
failed_count = 0

print("=" * 60)
print("REAL-TIME SALES DATA SIMULATOR")
print("=" * 60)
print(f"Starting data stream at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Press Ctrl+C to stop")
print("=" * 60)
print()
try:
    while True:
        # Generate random realistic sales data
        sales_amount = round(random.uniform(25.00, 999.99), 2)
        quantity = random.randint(1, 10)
        category = random.choice(categories)
        region = random.choice(regions)
        
        # Create data packet
        data = [{
            "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
"sales_amount": sales_amount,
            "product_category": category,
            "region": region,
            "quantity": quantity
        }]
        
        # Send to Power BI
        try:
            response = requests.post(PUSH_URL, json=data, timeout=10)
            
            if response.status_code == 200:
                total_sent += 1
                total_revenue += sales_amount
                print(f"✓ #{total_sent:04d} | ${sales_amount:7.2f} | {category:20s} | {region:8s} | Qty: {quantity}")
            else:
                failed_count += 1
                print(f"✗ Error {response.status_code}: {response.text}")
        
        except requests.exceptions.RequestException as e:
            failed_count += 1
            print(f"✗ Connection Error: {str(e)[:50]}")
        
        # Display summary every 20 transactions
        if total_sent % 20 == 0 and total_sent > 0:
            avg_sale = total_revenue / total_sent
            print()
            print("-" * 60)
            print(f"SUMMARY: {total_sent} transactions | Total: ${total_revenue:,.2f} | Avg: ${avg_sale:.2f} | Failed: {failed_count}")
            print("-" * 60)
            print()
# Wait before sending next data point
        time.sleep(3)  # Send data every 3 seconds
        
except KeyboardInterrupt:
    print("\n")
    print("=" * 60)
    print("SIMULATION STOPPED")
    print("=" * 60)
    print(f"Total Transactions Sent: {total_sent}")
    print(f"Total Revenue Generated: ${total_revenue:,.2f}")
    print(f"Failed Attempts: {failed_count}")
    print(f"Session Duration: {(total_sent * 3) / 60:.1f} minutes")
    print("=" * 60)

