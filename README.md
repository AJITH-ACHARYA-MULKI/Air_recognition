# Air_recognition

introduction:
	Handwritten recognition is the ability of a computer to receive and interpret intelligible handwritten input from sources such as paper documents, pattern drawn in front of webcam, photographs and other sources. such system are especially useful for building advanced user interface that do not require tradition mechanism of 
linguistic input such as pen-up-pen-down motion, hardware input devices or virtual keyboards.
In this project we build on operncv application that can track an object's movement, using which a user can draw pattern and system will recognise that pattern.

Project Description:
	Given the real time webcam data, python application uses OpenCV library to track an red/blue color
and allows the user to draw by moving the object, which makes user to write charecter and digits in front of webcam. 
Later the input data is captured and send it to the further process like Convolution Neural Network(CNN) to recognise pattern drawn by the user.

<img src="https://github.com/AJITH-ACHARYA-MULKI/Air_recognition/blob/master/images/image.png" width=300px height=150px>


Code Requirements
	This application is written in Python 3.8.5 and it uses the very famous OpenCV library.
OpenCV is a computer vision and machine learning software library that includes many common image analysis algorithms that will help us build custom, intelligent computer vision applications.

Code Explanation
Step 1: Initialize Some Stuff
Firstly, we import the necessary libraries.

Step 2: Start Reading The Video (Frame by Frame)
Now we use the OpenCV function cv2.VideoCapture() method to read a video,
 frame by frame (using a while loop), either from a video file or from a webcam in real-time.
 In this case, we pass 0 to the method to read from a webcam.

Step 2: Find The Contour-Of-Interest (objetc with blue/red color)
Once we start reading the webcam feed, we constantly look for a blue color object in the frames with the help of cv2.inRange() method and use the b_Upper and b_Lower variables initialized in Step 0.
 Once we find the contour, we do a series of image operations and make it smooth.
 They just makes our lives easier.
