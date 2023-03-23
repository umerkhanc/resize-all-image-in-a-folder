import os
from PIL import Image

# Set the target size for the images
target_size = (500, 500)

# Set the input and output folders
input_folder = 'folder names that contains images'
output_folder = 'here , folder which store resized images'

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Open the image file
        image = Image.open(os.path.join(input_folder, filename))
        
        # Resize the image to the target size using LANCZOS method
        image.thumbnail(target_size, Image.LANCZOS)
        
        # Save the resized image to the output folder with the same filename
        image.save(os.path.join(output_folder, filename))