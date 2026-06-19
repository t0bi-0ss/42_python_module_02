def garden_operations(operation_number: int) -> None:
    """Returns faulty code depending on operation number"""
    match operation_number:
        case 0:
            int("abc")
        case 1:
            1/0
        case 2:
            open("/non/existent/file")
        case 3:
            1 + "abc"
        case _:
            print("Operation completed successfully")
            return None


def test_error_type() -> None:
    """Shows each type of error happening"""
    operation_number = 0
    while (operation_number < 4):
        operation_number += 1
        print("Testing operation ", operation_number, "...")
        try:
            garden_operations(operation_number)
        except ValueError:
            print(
                "Caught ValueError: invalid literal",
                "for int() with base 10: 'abc'"
                )
        except ZeroDivisionError:
            print(
                "Caught ZeroDivisionError: division by zero"
            )
        except FileNotFoundError:
            print(
                "Caught FileNotFoundError: [Errno 2]",
                " No such file or directory: 'non/existent/file'"
            )
        except TypeError:
            print(
                "Caught TypeError: can only concatenate",
                " str (not \"int\") to str"
            )
    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_type()
