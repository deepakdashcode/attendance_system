import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

ALL_STUDENTS = dict()
try:
    f = open('.studentInfo.txt', 'r')
    ALL_STUDENTS = eval(str(f.read()))
    f.close()
except:
    pass


def getCurrentAttendances():
    attendance = []
    f = open('.attendance.txt', 'r')
    text = f.read()
    f.close()
    w = ''
    for i in text:
        if i != '\n':
            w = w + i
        else:
            currentTuple = eval(w)
            attendance.append(currentTuple)
            w = ''
    return attendance


def takeUniqueID():
    while True:
        from datetime import date
        from datetime import datetime

        currentDate = date.today()  # YYYY-MM-DT

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        # OPEN CV

        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode('utf-8')
            # MAKING BOUNDARY
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            pts2 = barcode.rect
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            print('Scanned')

        cv2.imshow('Result', img)
        cv2.waitKey(1)

        ##
        # ID = input('Enter your Form Number\n')

        try:
            ID = myData
            NAME = ALL_STUDENTS[int(ID)][0]
            BATCH_NAME = ALL_STUDENTS[int(ID)][1]
            currentDate = str(currentDate)
            current_time = str(current_time)
            currentTuple = (NAME, ID, BATCH_NAME, currentDate, current_time)
            print(currentTuple)
            currentAttendances = getCurrentAttendances()
            toAdd = True  # To check whether to add the currentTuple or not
            for i in currentAttendances:
                if i[1] == currentTuple[1] and i[3] == currentTuple[3]:
                    toAdd = False
            if toAdd:
                f = open('.attendance.txt', 'a')
                f.write(str(currentTuple) + "\n")
                f.close()
            cv2.putText(img, NAME, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        except:
            continue

        finally:
            continue


takeUniqueID()
