class GardenError(Exception):
    """A basic error for garden problems"""

    def __init__(self, message: str = "Unspecified plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


class PlantError(GardenError):
    """GardenError for problems with plants"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught PlantError:{self.message}"


def water_plant(plant_name: str) -> None:
    if not (plant_name == plant_name.capitalize()):
        raise PlantError
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: tuple) -> None:
    print("Opening watering system")
    for plant in plants:
        try:
            plant + "abc"
        except ValueError:
            print(
                "Caught ValueError: invalid literal",
                f"for int() with base 10: '{plant}'"
                )
            return
    for plant in plants:
        try:
            water_plant(plant)
        except PlantError(f"Invalid plant name to water: '{plant}'") as msg:
            print(f"{msg}")
            print("Ending tests and returning to main")
            return
        finally:
            print("Closing watering system")