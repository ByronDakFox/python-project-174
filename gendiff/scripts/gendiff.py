import argparse
import json


def parse_file(filepath):
    """Lee un archivo JSON."""
    with open(filepath) as f:
        return json.load(f)
    
def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        metavar="FORMAT"
    )
    args = parser.parse_args()

    # Leer los archivos
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    # Solo para comprobar que funciona
    print("Archivo 1 cargado:", data1)
    print("Archivo 2 cargado:", data2)


if __name__ == "__main__":
    main()