import os
from PIL import Image, ImageOps, ImageDraw, ImageFont


def resize_images(folder_path, width, height):
    # Create the "modified" subfolder
    modified_folder_path = os.path.join(folder_path, 'modified')
    os.makedirs(modified_folder_path, exist_ok=True)

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            
            # Resize the image
            resized_image = image.resize((width, height))
            
            # Save the modified image
            modified_image_path = os.path.join(modified_folder_path, filename)
            resized_image.save(modified_image_path)
            
            # Close the image
            image.close()



def resize_images_keep_aspect_ratio(folder_path, width, height):
    # Create the "modified" subfolder
    modified_folder_path = os.path.join(folder_path, 'modified')
    os.makedirs(modified_folder_path, exist_ok=True)

    # Calculate the desired aspect ratio
    desired_ratio = width / height

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            
            # Calculate the current aspect ratio
            current_ratio = image.width / image.height

            # Resize the image while keeping its original aspect ratio
            if current_ratio > desired_ratio:
                # The image is too wide
                new_width = width
                new_height = round(new_width / current_ratio)
            else:
                # The image is too tall
                new_height = height
                new_width = round(new_height * current_ratio)
            
            resized_image = image.resize((new_width, new_height))

            # Add black borders to the image until it matches the desired aspect ratio
            delta_w = width - new_width
            delta_h = height - new_height
            padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
            final_image = ImageOps.expand(resized_image, padding)

            # Save the modified image
            modified_image_path = os.path.join(modified_folder_path, filename)
            final_image.save(modified_image_path)
            
            # Close the images
            image.close()
            final_image.close()

#    font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 100)



from PIL import Image, ImageDraw, ImageFont

def add_sold_text(folder_path):
    # Create the "sold" subfolder
    sold_folder_path = os.path.join(folder_path, 'sold')
    os.makedirs(sold_folder_path, exist_ok=True)

    # Choose a font for the text (this assumes that the Arial.ttf font file is in the same directory as this script)
    font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 100)

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Create a separate image for the text
            text_image = Image.new('RGBA', image.size, (255, 255, 255, 0))

            # Create a draw object
            draw = ImageDraw.Draw(text_image)

            # Add the text to the bottom right corner of the image
            text = 'SOLD'
            textwidth, textheight = draw.textsize(text, font)
            position = (image.width - textwidth - 10, image.height - textheight - 10)
            draw.text(position, text, font=font, fill=(255, 0, 0, 127))  # added transparency to the text color

            # Composite the original image with the text image
            composite = Image.alpha_composite(image.convert('RGBA'), text_image)

            # Convert the image back to RGB mode before saving
            composite = composite.convert('RGB')

            # Save the modified image
            sold_image_path = os.path.join(sold_folder_path, filename)
            composite.save(sold_image_path)

            # Close the images
            image.close()
            composite.close()
            text_image.close()
