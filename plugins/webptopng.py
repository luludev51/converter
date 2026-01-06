import PIL

def config():
    return {
        "name": "webptopng",
        "version": "1.0",
        "description": "Convert WebP images to PNG images.",
        "dependencies": ["PIL"],
        "input_extension": ["webp"],
        "output_extension": ["png"],
        "category": "image"
    }

def convert(webp_file_path, png_file_path):
    """
    Convert a WebP image to a PNG image.

    Parameters:
    webp_file_path (str): The path to the input WebP file.
    png_file_path (str): The path to the output PNG file.
    """
    try:
        if not png_file_path.lower().endswith('.png'):
            png_file_path += '.png'
        if not webp_file_path.lower().endswith('.webp'):
            webp_file_path += '.webp'
        # Load the image file
        image = PIL.Image.open(webp_file_path)

        image.save(png_file_path, "png")
        print(f"Conversion successful: '{webp_file_path}' to '{png_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")