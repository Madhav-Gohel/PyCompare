import cv2
import threading


new_dimension = 360

def rotate_image(input_image_path, degrees = 90):
    try:
        # Read the image
        img = cv2.imread(input_image_path)

        # Get the image dimensions
        height, width = img.shape[:2]

        # Calculate the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degrees, 1)

        # Apply the rotation to the image
        rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

        return rotate_image
    except Exception as e:
        print(f"An error occurred: {e}")

def resize(image, height = new_dimension, width = new_dimension):
    try:
        # Read the image
        print("Reading image")
        img = cv2.imread(image)

        # Resize the image
        print("Resizing image")
        resized_img = cv2.resize(img, (width, height)) #Convert the image to a 360x360 image

        # Save the resized image
        return id(resized_img)
    
    except Exception as e:
        print(f"An error occurred: {e}")

def resize_with_multithreading(images):
    threads = []
    resized_images = []

    # Create a thread for each image
    for image in images:
        thread = threading.Thread(target=lambda: resized_images.append(resize("./photos/"+image)))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return resized_images

# Example usage
images = ['image1.jpg', 'image10.jpg', 'image100.jpg', 'image11.jpg', 'image12.jpg', 'image13.jpg', 'image14.jpg', 'image15.jpg', 'image16.jpg', 'image17.jpg', 'image18.jpg', 'image19.jpg', 'image2.jpg', 'image20.jpg', 'image21.jpg', 'image22.jpg', 'image23.jpg', 'image24.jpg', 'image25.jpg', 'image26.jpg', 'image27.jpg', 'image28.jpg', 'image29.jpg', 'image3.jpg', 'image30.jpg', 'image31.jpg', 'image32.jpg', 'image33.jpg', 'image34.jpg', 'image35.jpg', 'image36.jpg', 'image37.jpg', 'image38.jpg', 'image39.jpg', 'image4.jpg', 'image40.jpg', 'image41.jpg', 'image42.jpg', 'image43.jpg', 'image44.jpg', 'image45.jpg', 'image46.jpg', 'image47.jpg', 'image48.jpg', 'image49.jpg', 'image5.jpg', 'image50.jpg', 'image51.jpg', 'image52.jpg', 'image53.jpg', 'image54.jpg', 'image55.jpg', 'image56.jpg', 'image57.jpg', 'image58.jpg', 'image59.jpg', 'image6.jpg', 'image60.jpg', 'image61.jpg', 'image62.jpg', 'image63.jpg', 'image64.jpg', 'image65.jpg', 'image66.jpg', 'image67.jpg', 'image68.jpg', 'image69.jpg', 'image7.jpg', 'image70.jpg', 'image71.jpg', 'image72.jpg', 'image73.jpg', 'image74.jpg', 'image75.jpg', 'image76.jpg', 'image77.jpg', 'image78.jpg', 'image79.jpg', 'image8.jpg', 'image80.jpg', 'image81.jpg', 'image82.jpg', 'image83.jpg', 'image84.jpg', 'image85.jpg', 'image86.jpg', 'image87.jpg', 'image88.jpg', 'image89.jpg', 'image9.jpg', 'image90.jpg', 'image91.jpg', 'image92.jpg', 'image93.jpg', 'image94.jpg', 'image95.jpg', 'image96.jpg', 'image97.jpg', 'image98.jpg', 'image99.jpg']
resized_images = resize_with_multithreading(images)
print(resized_images)