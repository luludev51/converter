import PIL

def config():
    return {
        "name": "jpgtopng",
        "version": "1.2",
        "description": "Convert JPG images to PNG images.",
        "dependencies": ["PIL"],
        "input_extension": ["jpg", "jpeg"],
        "output_extension": ["png"],
        "category": "image"
    }

def convert(jpg_file_path, png_file_path):
    """
    Convert a JPG image to a PNG image.

    Parameters:
    jpg_file_path (str): The path to the input JPG file.
    png_file_path (str): The path to the output PNG file.
    """
    try:
        if not png_file_path.lower().endswith('.png'):
            png_file_path += '.png'
        if not jpg_file_path.lower().endswith('.jpg'):
            jpg_file_path += '.jpg'
        # Load the image file
        image = PIL.Image.open(jpg_file_path)

        image.save(png_file_path, "png")
        print(f"Conversion successful: '{jpg_file_path}' to '{png_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")