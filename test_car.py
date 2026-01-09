from car import display_summary, get_service_category

def test_get_service_category():
    assert get_service_category(25000) == "Premium Service"
    assert get_service_category(17000) == "Gold Service"
    assert get_service_category(12000) == "Silver Service"
    assert get_service_category(8000) == "Basic Service"
    assert get_service_category(3000) == "Economy Service"


def test_display_summary():
    expected_output = (
        "\n--- Service Summary ---\n"
        "Car Owner Name      : john\n"
        "Car Model           : E173\n"
        "Car Type            : Sedan\n"
        "Total Service Cost  : ₹9505.00\n"
        "Service Category    : Premium Service\n"
        "Year of Production  : 2009"
    )

    result = display_summary(
        "john",
        "E173",
        "Sedan",
        9505,
        "Premium Service"
    )

    assert result == expected_output
