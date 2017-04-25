import face_recognition
import cv2


#capture from camera at location 0
cap = cv2.VideoCapture(0)
#set the width and height, and UNSUCCESSFULLY set the exposure time
cap.set(3,1280)
cap.set(4,1024)
cap.set(15, 0.1)

while True:
    ret, img = cap.read()
    cv2.imshow("input", img)
    #cv2.imshow("thresholded", imgray*thresh2)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows()
cv2.VideoCapture(0).release()

picture_of_me = face_recognition.load_image_file("elma.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("IMG_5024.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
Y= len(unknown_face_encoding)

x=0
# Now we can see the two face encodings are of the same person with `compare_faces`!
while Y>x:
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding[x])

    if results[0] == True:
        print("It's a picture of me!",x)
    else:
        print("It's not a picture of me!",x)

    x=x+1