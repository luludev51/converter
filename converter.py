import os
import importlib
import sys
import time
from tqdm import tqdm


def clear():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

print("Loading modules...")
current_dir = "./plugins/"

i = 0
loaded_modules = {}

for filename in tqdm(os.listdir(current_dir)):
    if (
        filename.endswith(".py")
        and filename != "converter.py"
        and not filename.startswith("__")
    ):

        module_name = filename[:-3]
        file_path = os.path.join(current_dir, filename)

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        loaded_modules[module_name] = module
        spec.loader.exec_module(module)
        i += 1

input(f"{i} Modules loaded. Press Enter to continue...")
clear()


stop = False
while stop == False:
# Liste des tuples : (module, config)
    all_modules = []
    for mod in loaded_modules.values():
        if hasattr(mod, "config") and callable(mod.config):
            cfg = mod.config()
            category = cfg.get("category", "Uncategorized")
            cfg["category"] = category
            all_modules.append((mod, cfg))

    # Trie par catégorie
    all_modules.sort(key=lambda x: x[1]["category"])

    # Affiche avec numérotation
    current_category = None
    for i, (mod, cfg) in enumerate(all_modules, start=1):
        if cfg["category"] != current_category:
            current_category = cfg["category"]
            print(f"\n=== {current_category} ===")
        print(f"{i}. {cfg['name']} (v{cfg['version']})")

    # Sélection
    selection = int(input("\nSelect a module to use: "))
    module, config = all_modules[selection - 1]

    clear()
    print(f"- {config['name']} selected -\nDescription: {config['description']}\nVersion: {config['version']}")

    # Input / Output
    inputfile = input("Enter the input file path: ").replace('"', '')
    outputfile = input("Enter the output file path: ").replace('"', '')

    # Appel de la conversion
    module.convert(inputfile, outputfile)

    # Boucle pour continuer
    stop_input = input("Do you want to convert another file? (y/n): ").lower()
    if stop_input != 'y':
        stop = True
    else:
        clear()
