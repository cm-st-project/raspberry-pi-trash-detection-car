# Imports
import cv2
import torch
from picamera2 import Picamera2
import time
import os

# load model
print('Loading Model...')
model_path = 'trash_model.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# Initialize the pi camera
pi_camera = Picamera2()
# Convert the color mode to RGB
config = pi_camera.create_preview_configuration(
	main={"format": "RGB888", "size":(320,240)},
	
	)

pi_camera.configure(config)
# Start the pi camera and give it a second to set up
pi_camera.start()
time.sleep(1)

def detect_objects(image):
	print('Detecting Trash...')
	temp_path = 'temp.png'

	cv2.imwrite(temp_path, image)
	imgs = [temp_path]

	# Inference
	results = model(imgs)
	df = results.pandas().xyxy[0]
	# print(df)
	detected_objects = []
	for index, row in df.iterrows():
		p1 = (int(row['xmin']), int(row['ymin']))
		p2 = (int(row['xmax']), int(row['ymax']))
		name = row['name']
		detected_objects.append((name, p1, p2, round(row['confidence'] * 100, 2)))
		print(row)

	os.remove(temp_path)

	return detected_objects


def draw_on_image(image, objectsDetected, color=(255, 0, 0), thickness=2,
                       fontScale=1, font=cv2.FONT_HERSHEY_SIMPLEX):
	print('Drawing on Image...')
	for name, start_point, end_point, confidence in objectsDetected:
		# Using cv2.rectangle() method
		# Draw a rectangle with blue line borders of thickness of 2 px
		image = cv2.rectangle(image, start_point, end_point, color, thickness)
		org = (start_point[0], start_point[1] - 10)
		# Using cv2.putText() method
		image = cv2.putText(image, f'{name} {confidence}%', org, font,
			fontScale, color, thickness, cv2.LINE_AA)
	return image


def getDetectedObjectsAndShowImage():
	# Get a image frame as a numpy array
	image = pi_camera.capture_array()
	# flip image
	image = cv2.flip(image,0)

	# display the image
	cv2.imshow("Detecting...", image)
	time.sleep(1)

	# Detect Objects
	objectsDetected = detect_objects(image)
#	print("objectsDetected")
#	print(objectsDetected)

	# Draw on the image
	image = draw_on_image(image, objectsDetected)

	# display the image
	cv2.imshow("Detected", image)
	time.sleep(1)
	return objectsDetected




def main():
	# Load the image


	while True:
		# Get a image frame as a numpy array
		image = pi_camera.capture_array()
		# flip image
		image = cv2.flip(image,0)

		# Detect Objects
		objectsDetected = detect_objects(image)

		# Draw on the image
		image = draw_on_image(image, objectsDetected)

		# display the image
		cv2.imshow("Video", image)


		# This waits for 1 ms and if the 'q' key is pressed it breaks the loop	 
		if cv2.waitKey(42) == ord('q'):
			break

	print('Done!!')


if __name__ == "__main__":
    main()
