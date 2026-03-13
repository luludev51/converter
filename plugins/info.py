import os

def config():
    return {
        "name": "INFORMATIONS",
        "version": "1.0",
        "description": "Provides information about the converter. (no input or output required)",
        "dependencies": [],
        "input_extension": [],
        "output_extension": [],
        "category": ".Informations"
    }

def convert(input_file, output_file):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Converter")
    print("Version: 1.5")
    print("Author: luludev51")
    print("Use this converter to convert files from one format to anodether. Simply select the desired module and provi the input and output file paths.")
    print("For more information, visit https://github.com/luludev51/converter")