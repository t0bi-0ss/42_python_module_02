def input_temperature(temp_str: str) -> int:
    """Takes string representation of temperature
    and return its int value"""
    print(f"Input data is '{temp_str}'")
    try:
        temperature = int(temp_str)
    except ValueError:
        raise
    else:
        return temperature


def test_temperature(temp_str: str) -> None:
    """Checks if input_temperature() was succesfull"""
    try:
        temperature = input_temperature(temp_str)
    except ValueError:
        print(
            "Caught input_temperature error: "
            ,"invalid literal for int() with base 10: '"
            ,temp_str
            ,"'"
        )
    else:
        print(f"Temperature is now {temperature}°C")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print("\nAll tests completed - program didn't crash!")