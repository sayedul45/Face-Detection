import sqlite3    # Database
import numpy
import cv2    # Open Camera

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   # to detect someone faces
cam = cv2.VideoCapture(0)   # zero means web camera

def insert_update(id, name, age):             # function is for sqlite database
    conn = sqlite3.connect("sqlite.db")     # connect with database
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(id)
    cursor = conn.execute(cmd)           # cursor to execute statement


    isRecordExist=0

    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):   # if there is exist any row in out table
        conn.execute("UPDATE STUDENTS SET name=? WHERE id=?",(name,id))
        conn.execute("UPDATE STUDENTS SET age=? WHERE id=?", (age, id))
    else:       # if there is no any row in the table
        conn.execute("INSERT INTO STUDENTS (id , name ,age) values(?,?,?)",(id ,name,age))

    conn.commit()
    conn.close()

# insert user defined values to the table
id = input("Enter User Id:")
name = input("Enter User Name:")
age = input("Enter User Age:")

insert_update(id,name,age)

# Detect face in Web Camera

sampleNum = 0       # Assume that there is no samples in dataset
while(True):
    ret,img = cam.read()    # open camera
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # convert the image BGR to GRAYSCALE
    faces = faceDetect.detectMultiScale(gray,1.5,5)


    for (x,y,w,h) in faces:
        sampleNum = sampleNum+1    # if face is detected increment the number
        cv2.imwrite("Dataset/user."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)   # delay time

    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>30):
        break
cam.release()
cv2.destroyAllWindows()











