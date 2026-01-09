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
    return (
        "\n--- Service Summary ---\n"
        f"Car Owner Name      : {owner_name}\n"
        f"Car Model           : {car_model}\n"
        f"Car Type            : {car_type}\n"
        f"Total Service Cost  : ₹{total_cost:.2f}\n"
        f"Service Category    : {service_category}\n"
        f"Year of Production  : 2009"
    )


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

    print(
        display_summary(
            owner_name,
            car_model,
            car_type,
            total_cost,
            service_category
        )
    )


if __name__ == "__main__":
    main()
