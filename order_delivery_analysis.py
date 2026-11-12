# Order Delivery Analysis

orders = [
    {"id": 101, "status": "Delivered", "days": 3},
    {"id": 102, "status": "Pending", "days": 0},
    {"id": 103, "status": "Delivered", "days": 5},
    {"id": 104, "status": "Cancelled", "days": 0},
    {"id": 105, "status": "Delivered", "days": 2},
    {"id": 106, "status": "Pending", "days": 0},
    {"id": 107, "status": "Delivered", "days": 4},
    {"id": 108, "status": "Cancelled", "days": 0},
]

# Total orders
total_orders = len(orders)

# Count order status
delivered = sum(1 for order in orders
                if order["status"] == "Delivered")

pending = sum(1 for order in orders
              if order["status"] == "Pending")

cancelled = sum(1 for order in orders
                if order["status"] == "Cancelled")

# Average delivery time
delivery_days = [
    order["days"] for order in orders
    if order["status"] == "Delivered"
]

average_days = sum(delivery_days) / len(delivery_days)

# Delivery success percentage
success_rate = (delivered / total_orders) * 100

# Display results
print("ORDER DELIVERY ANALYSIS")
print("-----------------------")

print("Total Orders:", total_orders)
print("Delivered Orders:", delivered)
print("Pending Orders:", pending)
print("Cancelled Orders:", cancelled)

print("Average Delivery Time:", average_days, "days")
print("Delivery Success Rate:", success_rate, "%")
