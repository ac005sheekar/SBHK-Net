import cv2
import time
import math

cap = cv2.VideoCapture(0)
count = 0

while True:
    start = time.time()
    ret, frame = cap.read()
    end = time.time()

    fps = math.ceil(1/ (end/start))
    count += 1

    if count ==1:
        average_fps = fps
    else:
        average_fps = math.ceil((average_fps * count + fps) / (count + 1))

    cv2.putText(frame, "FPS: " + str(fps), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "Average FPS: " + str(average_fps), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break