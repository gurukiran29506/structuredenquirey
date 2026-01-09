from car import display_summary

def test_display_summary():
    owner_name = "john"
    car_model = "E173"
    car_type = "Sedan"
    total_cost = 9505
    service_category = "Premium Service"
    expected_output = (
        "\n--- Service Summary ---\n"
        "Car Owner Name      : john\n"
        "Car Model           : E173\n"
        "Car Type            : Sedan\n"
        "Total Service Cost  : ₹9505.00\n"
        "Service Category    : Premium Service"
        "Year of Production: 2009"
    )
    assert display_summary(owner_name, car_model, car_type, total_cost, service_category) == expected_output
