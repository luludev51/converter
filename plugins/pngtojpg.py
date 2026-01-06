import PIL

def config():
    return {
        "name": "pngtojpg",
        "version": "1.0",
        "description": "Convert PNG images to JPG images.",
        "dependencies": ["PIL"],
        "input_extension": ["png"],
        "output_extension": ["jpg", "jpeg"],
        "category": "image"
    }

def convert(png_file_path, jpg_file_path):
    """
    Convert a PNG image to a JPG image.

    Parameters:
    png_file_path (str): The path to the input PNG file.
    jpg_file_path (str): The path to the output JPG file.
    """
    try:
        if not png_file_path.lower().endswith('.png'):
            png_file_path += '.png'
        if not jpg_file_path.lower().endswith('.jpg'):
            jpg_file_path += '.jpg'
        # Load the image file
        image = PIL.Image.open(png_file_path)
        if image.mode == "RGBA":
            background = PIL.Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])  # alpha channel comme masque
            image = background

        image.save(jpg_file_path, "jpeg")
        print(f"Conversion successful: '{png_file_path}' to '{jpg_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")