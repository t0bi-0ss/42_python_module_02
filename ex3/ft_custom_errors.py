class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str = "Unspecified plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class PlantError(GardenError):
    """GardenError for problems with plants"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class WaterError(GardenError):
    """GardenError for problems with watering"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    
def plant_error_tester(error_number: int, error_message: str) -> None:
    """Raises a different exception depending on error number"""

    match error_number:
        case 0:
            raise GardenError(error_message)
        case 1:
            raise PlantError(error_message)
        case 2:
            raise WaterError(error_message)
        case __:
            return


def exception_handler(error_number: int, error_message: str) -> None:
    """Handles all excepetions raised by plant_error_tester()"""

    try:
        plant_error_tester(error_number, error_message)
    except GardenError as msg:
        print(msg)
    except PlantError as msg:
        print(msg)
    except WaterError as msg:
        print(msg)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    exception_handler(1, "Caught PlantError: The tomato plant is wilting")
