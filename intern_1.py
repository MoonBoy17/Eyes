import cv2
import os

# setting the path to the folder having eyes pics
folder_path = 'C:\\Users\\harsh\\Downloads\\Eyes'

# looping over all the images in the folder
for file_name in os.listdir(folder_path):
    # for all the jpg images (the folder has only jpg images still to filter any other format)
    if file_name.endswith('.jpg'):
        # loading and displaying the image
        img = cv2.imread(os.path.join(folder_path, file_name))
        cv2.imshow('Image', img)
        cv2.waitKey(0)

# destroy all windows after displaying the images
cv2.destroyAllWindows()