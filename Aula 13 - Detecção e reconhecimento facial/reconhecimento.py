import cv2

detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read('classificadoreigen.yml')

largura, altura = 220, 220

font = cv2.QT_FONT_NORMAL
camera = cv2.VideoCapture(0)
fim = False
while not fim:
    status, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30,30))
    try:
        for x, y, l, a in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y+a, x:x+l], (altura,largura))
            cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)
            nome, confianca = reconhecedor.predict(imagemFace)
            print(confianca)
            if nome == 1:
                nome = 'Hellynson'
            elif nome == 2:
                nome = 'Fe'
            elif nome == 3:
                nome = 'Alicia'

            cv2.putText(imagem, str(nome), (x,y+altura-20), font, 2, (0,0,255))
    except:
        print("Não consegui reconhecer...")
    cv2.imshow("Faces", imagem)
    if cv2.waitKey(1) == ord('q'):
        fim = True


