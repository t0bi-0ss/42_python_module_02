class OutOfRangeError(Exception):
    """Exception raised for numbers outside a desired range"""


def input_temperature(temp_str: str) -> int:
    """Takes string representation of temperature
    and return its int value"""
    print(f"Input data is '{temp_str}'")
    try:
        temperature = int(temp_str)
        if temperature > 40 or temperature < 0:
            print("Caught input_temperature error: ", end="")
            raise OutOfRangeError
    except ValueError:
        print("Caught input_temperature error: ", end="")
        raise
    else:
        return temperature


def test_temperature(temp_str: str) -> None:
    """Checks if input_temperature() was succesfull"""
    try:
        temperature = input_temperature(temp_str)
    except ValueError:
        print(
            "invalid literal for int() with base 10: '",
            temp_str,
            "'",
        )
    except OutOfRangeError:
        temperature = int(temp_str)
        if temperature < 0:
            print(
            temperature,
            "°C is too cold for plants (min 0°C)"
        )
        elif temperature > 40:
            print(
                temperature,
                "°C is too hot for plants (max 40°C)"
            )
    else:
        print(f"Temperature is now {temperature}°C")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print("\nAll tests completed - program didn't crash!")
