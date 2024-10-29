import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
try:
    imagem = cv2.imread("mesa.jpg")
    bbox, label, conf = cv.detect_common_objects(imagem, confidence=0.25, model='yolov3-tiny')
    print(bbox, label, conf)

    out = draw_bbox(imagem, bbox, label, conf, write_conf=True)

    cv2.imshow("Objeto detectado", out)
    cv2.waitKey()

except Exception as erro:
    print('Erro: ', erro)

