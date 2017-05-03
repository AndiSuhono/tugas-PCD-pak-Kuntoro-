# nama : ANDI SUHONO
# NIM : 5301414085

import cv2
import sys

# mengambil video berukuran 640x480
video_capture = cv2.VideoCapture(0)
video_capture.set (3, 640)
video_capture.set (4, 480)

# selama program berjalan, mengulang proses pengambilan gambar, frame demi frame
while True:
    # menangkap frame-demi-frame
    ret, frame = video_capture.read()

    # mengubah gambar berwarna yang ditangkap oleh webcam menjadi skala keabuan
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # menampilkan frame
    cv2.imshow('Video', gray)

    # menutup window dengan tombol q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# berhenti berhubungan dengan webcam saat program ditutup
video_capture.release()
cv2.destroyAllWindows()