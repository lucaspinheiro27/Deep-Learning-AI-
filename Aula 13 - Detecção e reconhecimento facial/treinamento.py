import cv2
import os
import numpy as np

eigen = cv2.face.EigenFaceRecognizer_create()
def getImagemPeloNome():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    print(caminhos)
    faces = []
    nomes = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.imread(caminhoImagem)
        imagemCinza = cv2.cvtColor(imagemFace, cv2.COLOR_BGR2GRAY)
        nome = os.path.split(caminhoImagem)[-1].split('_')[0]
        print(nome)
        if nome == 'Hellynson':
            nomes.append(1)
        elif nome == 'Fernanda':
            nomes.append(2)
        elif nome == 'alicia':
            nomes.append(3)
        else:
            nomes.append(0)

        faces.append(imagemCinza)
    return np.array(nomes), faces

nomes, faces = getImagemPeloNome()
print(nomes)
eigen.train(faces, nomes)
eigen.write('classificadoreigen.yml')