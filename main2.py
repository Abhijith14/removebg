import os
from removebg import RemoveBg
from dotenv import load_dotenv

def remove_background(image_path, output_folder):

    # Load the API key from the .env file
    load_dotenv()
    api_key = os.getenv("REMOVE_BG_API_KEY")

    # Initialize the RemoveBg object with your API key
    # You can obtain your API key from https://www.remove.bg/
    # Make sure to sign up and get your free API key
    # rmbg = RemoveBg("", "error.log")  # Replace "YOUR_API_KEY" with your actual API key
    rmbg = RemoveBg(api_key, "error.log")

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extract the filename from the original image path
    filename = os.path.basename(image_path)

    # Set the output path for the image with the removed background
    output_path = os.path.join(output_folder, filename)

    # Remove the background from the image
    rmbg.remove(image_path=image_path, output_path=output_path, size="auto", confirm_resize=False)

    print(f"Background removed and saved: {output_path}")


# Example usage
image_folder = "input"
output_folder = "output"

# Iterate over the images in the input folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        remove_background(image_path, output_folder)
