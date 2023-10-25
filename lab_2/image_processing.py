from PIL import Image

def get_image_size(file_path):
    if file_path.endswith((".png", ".jpg")):
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                return f"{width}x{height}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Not an image file"
