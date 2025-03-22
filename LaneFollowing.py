# implementation of canny edge detection for lane following
import cv2
import matplotlib.pyplot as plt
import numpy as np

def grey(image):
  #convert to grayscale
    image = np.asarray(image)
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

  #Apply Gaussian Blur --> Reduce noise and smoothen image
def gauss(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

  #outline the strongest gradients in the image --> this is where lines in the image are
def canny(image):
    edges = cv2.Canny(image,50,150)
    return edges

def region(image):
    height, width = image.shape
    #isolate the gradients that correspond to the lane lines
    triangle = np.array([
                       [[0, height], [2000,1000], [width, height]]
                       ])
    #create a black image with the same dimensions as original image
    mask = np.zeros_like(image)
    #create a mask (triangle that isolates the region of interest in our image)
    mask = cv2.fillPoly(mask, triangle, 255)
    mask = cv2.bitwise_and(image, mask)
    return mask

def display_lines(image, lines):
    lines_image = np.zeros_like(image)
    #make sure array isn't empty
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line
            #draw lines on a black image
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return lines_image

def average(image, lines):
    left = []
    right = []

    if lines is not None:
      for line in lines:
        print(line)
        x1, y1, x2, y2 = line.reshape(4)
        #fit line to points, return slope and y-int
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        print(parameters)
        slope = parameters[0]
        y_int = parameters[1]
        #lines on the right have positive slope, and lines on the left have neg slope
        if slope < 0:
            left.append((slope, y_int))
        else:
            right.append((slope, y_int))
            
    #takes average among all the columns (column0: slope, column1: y_int)
    right_avg = np.average(right, axis=0)
    left_avg = np.average(left, axis=0)
    #create lines based on averages calculates
    left_line = make_points(image, left_avg)
    right_line = make_points(image, right_avg)
    return np.array([left_line, right_line])

def make_points(image, average):
    print(average)
    slope, y_int = average
    y1 = image.shape[0]
    #how long we want our lines to be --> 3/5 the size of the image
    y2 = int(y1 * (3/5))
    #determine algebraically
    x1 = int((y1 - y_int) // slope)
    x2 = int((y2 - y_int) // slope)
    return np.array([x1, y1, x2, y2])

current_frame = cv2.imread("test.jpg")
#plt.imshow(current_frame)
current_frame_greyscale = grey(current_frame)

current_frame_hsv = cv2.cvtColor(current_frame, cv2.COLOR_RGB2HSV)
lower_yellow = np.array([10,100,100], dtype = "uint8")
upper_yellow = np.array([100,255,255], dtype = "uint8")
mask_yellow = cv2.inRange(current_frame_hsv, lower_yellow, upper_yellow)
mask_white = cv2.inRange(current_frame_greyscale, 200, 255)
mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
mask_yw_image = cv2.bitwise_and(current_frame_greyscale, mask_yw)

frame_copy = np.copy(mask_yw_image)
frame_edges = cv2.Canny(frame_copy, 50, 150)
isolated = region(frame_edges)
cv2.waitKey(0)

lines = cv2.HoughLinesP(isolated, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
averaged_lines = average(frame_copy, lines)
black_lines = display_lines(frame_copy, averaged_lines)
#taking wighted sum of original image and lane lines image
lanes = cv2.addWeighted(frame_copy, 0.8, black_lines, 1, 1)

plt.imshow(isolated)
cv2.waitKey(0)
plt.show()
plt.imshow(lanes)
plt.show()