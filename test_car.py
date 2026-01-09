from car import display_summary

def test_display_summary():
    owner_name = "V001"
    car_model = "Toyota Camry"
    car_type = "Sedan"
    total_cost = 95000
    service_category = "Premium Service"
    expected_output = (
        "\n--- Service Summary ---\n"
        "Car Owner Name      : V001\n"
        "Car Model           : Toyota Camry\n"
        "Car Type            : Sedan\n"
        "Total Service Cost  : ₹95000.00\n"
        "Service Category    : Premium Service"
        "Year of Production: 2009"
    )
    assert display_summary(owner_name, car_model, car_type, total_cost, service_category) == expected_output