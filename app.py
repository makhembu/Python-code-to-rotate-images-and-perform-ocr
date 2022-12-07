from PIL import Image
import pytesseract

# Open the image file
image = Image.open('image.jpg')

# Rotate the image by 90 degrees
image = image.rotate(90)

# Save the rotated image
image.save('rotated_image.jpg')

# Perform OCR on the rotated image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
