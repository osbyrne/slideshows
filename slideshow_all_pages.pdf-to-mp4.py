import os
import cv2
from PyPDF2 import PdfReader
from pdf2image import convert_from_path


# usage notice:
# 1. Install python3, pip3, and the following packages:
#    - PyPDF2
#    - pdf2image
#    - opencv-python
# 2. Put this file in the same directory as the PDF files you want to convert.
# 3. Run this file with python3.
# you can choose the framerate of the video by changing the framerate variable below.

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        print(f"Found PDF file: {filename}")
        
        with open(filename, 'rb') as file:
            print(f"Processing {filename}...")
            pdf = PdfReader(file)
            
            for i in range(len(pdf.pages)):
                page = pdf.pages[i]
                images = convert_from_path(file.name, dpi=200, first_page=i+1, last_page=i+1)

                for j, image in enumerate(images):
                    print(f"Saving page {i}...")
                    image.save(f"{filename}_{i}.jpg", 'JPEG')

image_files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.jpg')]

# Read the first image to get the dimensions
first_image = cv2.imread(image_files[0])
height, width, _ = first_image.shape # video to take the shape of your PDF

# Define the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
framerate = 14
video = cv2.VideoWriter('video.mp4', fourcc, framerate, (width, height))

# Write each image to the video
for image_file in image_files:
    image = cv2.imread(image_file)
    video.write(image)

# Release the VideoWriter object
video.release()
print("Video created successfully.")

# Delete all .jpg files
for filename in os.listdir('.'):
    if filename in image_files:
        os.remove(filename)
        print(f"Deleted {filename}.")
