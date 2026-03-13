from PIL import Image

def config():
    return {
        "name": "WebP to ICO Converter",
        "version": "1.0",
        "description": "Converts WebP images to ICO format.",
        "dependencies": [],
        "input_extension": [".webp"],
        "output_extension": [".ico"],
        "category": "image"
    }

def convert(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGBA")
            if not output_path.lower().endswith(".ico"):
                output_path += ".ico"
            img.save(output_path, format="ICO")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
