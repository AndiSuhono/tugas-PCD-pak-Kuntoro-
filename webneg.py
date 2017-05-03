# nama : ANDI SUHONO
# NIM : 5301414085

import numpy as np
import cv2 # meng-import library yang dimiliki openCV 

# mengambil perintah webcam yang ada pada perangkat
# angka "1" webcam eksternal
# angka "2" untuk webcam internal perangkat
cap = cv2.VideoCapture(0)   

# selama program berjalan, mengulang proses pengambilan gambar, frame demi frame
while(True):
    # menangkap gambar frame demi frame
    ret, frame = cap.read() 

    # mengubah gambar berwarna yang ditangkap oleh webcam menjadi skala keabuan
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # menampilkan gambar yang ditangkap oleh webcam pada window,
    # kemudian di konversikan menjadi gambar negatif melalui angka "255-gray"  
    cv2.imshow('frame', 255-gray) # angka merupakan skala warna yang dimiliki setiap piksel 
    if cv2.waitKey(1) & 0xFF == ord('q'): # fungsi tombol "q" untuk keluar dari window
        break

# keluar dari aplikasi dan mematikan webcam
cap.release()
cv2.destroyAllWindows()