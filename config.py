def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt  but it is a directory, couldn't read it.")
    except PermissionError:
        print("Found config.txt but you don't have permission.")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("Got a problem trying to read the file:", err)


if __name__ == "__main__":
    main()

loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split("\n"):
    try:
        key, value = line.split("=")
        parsed_config[key] = value
    except ValueError:
        print(f"Unable to parse {line}")

print(parsed_config)
