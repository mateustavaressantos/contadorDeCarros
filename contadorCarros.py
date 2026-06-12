import cv2
import numpy as np

video = cv2.VideoCapture('rodovia.mp4')
contador = 0

# 2. CONFIGURAÇÃO DOS SENSORES
#    A rodovia tem 6 faixas divididas pelo canteiro central:
#      - Sentido ESQUERDO (E1, E2, E3): faixas do lado esquerdo da tela
#      - Sentido DIREITO  (D1, D2, D3): faixas do lado direito da tela

sensores = [
    # Sentido ESQUERDO
    {
        "nome": "E1", "lado": "Esquerdo",
        "x": 30,  "y": 560, "w": 130, "h": 35,
        "limiar": 1800, "liberado": True
    },
    {
        "nome": "E2", "lado": "Esquerdo",
        "x": 160, "y": 560, "w": 140, "h": 35,
        "limiar": 1500, "liberado": True
    },
    {
        "nome": "E3", "lado": "Esquerdo",
        "x": 300, "y": 560, "w": 145, "h": 35,
        "limiar": 1500, "liberado": True
    },
    # Sentido DIREITO─
    {
        "nome": "D1", "lado": "Direito",
        "x": 620, "y": 560, "w": 150, "h": 35,
        "limiar": 1900, "liberado": True
    },
    {
        "nome": "D2", "lado": "Direito",
        "x": 770, "y": 560, "w": 150, "h": 35,
        "limiar": 2000, "liberado": True
    },
    {
        "nome": "D3", "lado": "Direito",
        "x": 920, "y": 560, "w": 155, "h": 35,
        "limiar": 2000, "liberado": True
    },
]

# Processamento morfológico
kernel = np.ones((6, 6), np.uint8)

while True:
    ret, img = video.read()

    # Se o vídeo acabar, o loop fecha
    if not ret:
        break

    img = cv2.resize(img, (1100, 720))

    # Conversão para escala de cinza e binarização adaptativa
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh   = cv2.adaptiveThreshold(imgGray, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 12)
    imgDil  = cv2.dilate(imgTh, kernel, iterations=2)

    # Loop pelos 6 sensores 
    for s in sensores:
        x, y, w, h = s["x"], s["y"], s["w"], s["h"]

        # Recorte da área do sensor e contagem de pixels brancos
        recorte = imgDil[y:y+h, x:x+w]
        brancos = cv2.countNonZero(recorte)

        # Lógica de contagem: só conta quando o sensor está liberado
        if brancos > s["limiar"] and s["liberado"]:
            contador += 1
            s["liberado"] = False   # Bloqueia APENAS este sensor

        if brancos < s["limiar"]:
            s["liberado"] = True    # Libera APENAS este sensor

        # Cor do retângulo: Verde = livre | Roxo = veículo detectado
        cor_sensor = (0, 255, 0) if s["liberado"] else (255, 0, 255)
        cv2.rectangle(img, (x, y), (x + w, y + h), cor_sensor, 3)

        # Nome do sensor + pixels detectados
        cv2.putText(img, f"{s['nome']} | Px: {brancos}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

    # Placar no topo da tela
    cv2.rectangle(img, (30, 15), (420, 105), (0, 0, 0), -1)   # fundo preto
    cv2.putText(img, f"Total: {contador}",
                (40, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 255, 255), 3)

    cv2.imshow('Contador de Veiculos - Rodovia Completa', img)

    # Pressione 'q' para fechar
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Resumo final no terminal
print(f"\nTotal de veiculos contados: {contador}\n")

video.release()
cv2.destroyAllWindows()