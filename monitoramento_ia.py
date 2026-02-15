import cv2
import math
from ultralytics import YOLO

# --- CONFIGURAÇÃO DO PROJETO MRS LOGÍSTICA ---
# Objetivo: Detectar invasão de faixa ferroviária (Pessoas/Veículos)
# Tecnologia: YOLOv8 (State-of-the-art em Visão Computacional)

# 1. Carrega o Modelo (O "Cérebro")
# Na primeira vez, ele vai baixar o arquivo 'yolov8n.pt' automaticamente.
print("Carregando modelo de IA... Aguarde.")
model = YOLO('yolov8n.pt')

# 2. Fonte de Vídeo (0 = Webcam / Se tiver vídeo, coloque 'trem_movimento.mp4')
cap = cv2.VideoCapture('video_teste.mp4')

# Configurações de Visualização
largura, altura = 1280, 720
cap.set(3, largura)
cap.set(4, altura)

# As classes que o modelo conhece (COCO Dataset)
classNames = ["pessoa", "bicicleta", "carro", "moto", "aviao", "onibus", "trem", "caminhao", "barco", "semaforo"]

print("--- SISTEMA DE MONITORAMENTO MRS INICIADO ---")

while True:
    success, img = cap.read()
    if not success:
        break

    # A mágica acontece aqui: A IA analisa a imagem
    results = model(img, stream=True, verbose=False)

    # Status de Segurança (Padrão: Seguro)
    status_seguranca = "NORMAL"
    cor_status = (0, 255, 0) # Verde

    # Processar cada detecção
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Coordenadas do objeto
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Confiança (0 a 1)
            conf = math.ceil((box.conf[0] * 100)) / 100
            
            # Classe (O que é o objeto?)
            cls = int(box.cls[0])
            currentClass = classNames[cls] if cls < len(classNames) else "Objeto"

            # --- REGRA DE NEGÓCIO DE SEGURANÇA ---
            # Se for PESSOA, CARRO ou CAMINHÃO perto da via = PERIGO
            if currentClass in ["pessoa", "carro", "caminhao", "trem"] and conf > 0.5:
                
                # Define cor baseada no risco
                if currentClass == "pessoa":
                    color = (0, 0, 255) # Vermelho (Alto Risco de Atropelamento)
                    status_seguranca = "CRITICO - INVASAO DE VIA"
                    cor_status = (0, 0, 255)
                elif currentClass == "trem":
                    color = (255, 255, 0) # Azul (Monitoramento de Ativo)
                else:
                    color = (0, 165, 255) # Laranja (Veículo próximo)

                # Desenha o quadrado e o texto
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                cv2.putText(img, f'{currentClass.upper()} {int(conf*100)}%', (max(0, x1), max(35, y1 - 10)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # --- HUD (Display Profissional) ---
    # Cria uma barra preta no topo para parecer sistema de empresa
    cv2.rectangle(img, (0, 0), (largura, 50), (0, 0, 0), -1)
    
    # Texto do Status
    cv2.putText(img, f"MRS LOGISTICA | CAM-01 | STATUS: {status_seguranca}", (20, 35), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, cor_status, 2)

    # Mostra na tela
    cv2.imshow("Sistema de Prevencao de Acidentes - MRS", img)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()