import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Define the font and scale
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6

# Define the color and thickness of the text
text_color = (0, 0, 255) # blue color
text_thickness = 1

# Add text below each planet
# Sun
cv2.putText(img, "Sun", (50, 50), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Mercury
cv2.putText(img, "Mercury", (150, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Venus
cv2.putText(img, "Venus", (250, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Earth
cv2.putText(img, "Earth", (350, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Mars
cv2.putText(img, "Mars", (450, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Jupiter
cv2.putText(img, "Jupiter", (550, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Saturn
cv2.putText(img, "Saturn", (700, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Uranus
cv2.putText(img, "Uranus", (850, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Neptune
cv2.putText(img, "Neptune", (1000, 100), font, font_scale, text_color, text_thickness, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display Colored Image
cv2.imshow("Display Image",img)

# Convert Colored Image To Grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Display Grayscale Image
cv2.imshow("Grayscale", gray_img)


#print(gray_img)
