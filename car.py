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


def display_summary(owner_name, car_model, car_type, total_cost, service_category):
    return {
        "owner_name": owner_name,
        "car_model": car_model,
        "car_type": car_type,
        "total_cost": total_cost,
        "service_category": service_category
    }


def main():
    print("=== Car Service Cost Evaluation System ===\n")

    owner_name = input("Enter Car Owner Name: ")
    car_model = input("Enter Car Model: ")
    car_type = input("Enter Car Type (Hatchback / Sedan / SUV): ")

    engine_service = float(input("Engine Service Cost (₹): "))
    brake_service = float(input("Brake Service Cost (₹): "))
    general_maintenance = float(input("General Maintenance Cost (₹): "))

    total_cost = engine_service + brake_service + general_maintenance
    service_category = get_service_category(total_cost)

    result = display_summary(
        owner_name, car_model, car_type, total_cost, service_category
    )

    print("\n--- Service Summary ---")
    for k, v in result.items():
        print(f"{k.replace('_', ' ').title():20}: {v}")


if __name__ == "__main__":
    main()
