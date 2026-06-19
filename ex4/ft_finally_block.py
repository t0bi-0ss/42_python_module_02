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
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: tuple[str, ...]) -> None:
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
    try:
        for plant in plants:
            try:
                water_plant(plant)
            except PlantError as msg:
                print(msg)
                print("Ending tests and returning to main")
                return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    tuple_1 = ("Tomato", "Lettuce", "Carrots")
    print("=== Garden Watering System ===\n")
    print("Tesing valid plants...")
    test_watering_system(tuple_1)
