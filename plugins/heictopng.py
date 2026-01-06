from PIL import Image
import pillow_heif

def config():
    return {
        "name": "heictopng",
        "version": "1.2",
        "description": "Convert HEIC images to PNG images.",
        "dependencies": ["PIL"],
        "input_extension": ["heic", "heif"],
        "output_extension": ["png"],
        "category": "image"
    }

def convert(heic_file_path, png_file_path):
    """
    Convert a HEIC image to a PNG image.

    Parameters:
    heic_file_path (str): The path to the input HEIC file.
    png_file_path (str): The path to the output PNG file.
    """
    try:
        if not png_file_path.lower().endswith('.png'):
            png_file_path += '.png'
        if not heic_file_path.lower().endswith('.heic'):
            heic_file_path += '.heic'
        # Load the image file
        # heic_file_path = heic_file_path.replace('\\', '/')
        heif_file = pillow_heif.read_heif(heic_file_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
        )
        image.save(png_file_path, "PNG")


        print(f"Conversion successful: '{heic_file_path}' to '{png_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")