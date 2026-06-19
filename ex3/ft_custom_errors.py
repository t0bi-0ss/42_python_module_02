class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str = "Unspecified plant error") -> None:
        self.message = message
        super().__init__(self.message)

class PlantError(GardenError):
    """GardenError for problems with plants"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

class WaterError(GardenError):
    """GardenError for problems with watering"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

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
