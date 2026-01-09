
# Main Program
print("=== Car Service Cost Evaluation System ===\n")

# Input details
owner_name = input("Enter Car Owner Name: ")
car_model = input("Enter Car Model: ")
car_type = input("Enter Car Type (Hatchback / Sedan / SUV): ")

print("\nEnter Service Charges:")
engine_service = float(input("Engine Service Cost (₹): "))
brake_service = float(input("Brake Service Cost (₹): "))
general_maintenance = float(input("General Maintenance Cost (₹): "))

# Calculate total cost
total_cost = engine_service + brake_service + general_maintenance

# Determine service category
service_category = get_service_category(total_cost)

# Function to determine service category
def get_service_category(total_cost):
    if total_cost > 20000:
        return "Premium Service"
    elif 15000 <= total_cost <= 19999:
        return "Gold Service"
    elif 10000 <= total_cost <= 14999:
        return "Silver Service"
    elif 5000 <= total_cost <= 9999:
        return "Basic Service"
    else:
        return "Economy Service"
    

# Function to display service summary
def display_summary(owner_name, car_model, car_type, total_cost, service_category):
    print("\n--- Service Summary ---")
    print(f"Car Owner Name      : {owner_name}")
    print(f"Car Model           : {car_model}")
    print(f"Car Type            : {car_type}")
    print(f"Total Service Cost  : ₹{total_cost:.2f}")
    print(f"Service Category    : {service_category}")

if __name__ == "__main__":
    owner_name = "john"
    car_model = "E173"
    car_type = "Sedan"
    total_cost = 9505
    service_category = get_service_category(total_cost)
    display_summary(owner_name, car_model, car_type, total_cost, service_category) 
