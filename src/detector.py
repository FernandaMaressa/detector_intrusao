import cv2
from ultralytics import YOLO
from datetime import datetime
import pygame
import time
import logging

# =======================
# CONFIGURAÇÕES
# =======================
HORARIO_INICIO_ALERTA = 23  
HORARIO_FIM_ALERTA = 6      
INTERVALO_DETECCAO = 4    
DURACAO_EXIBICAO = 3        
CAMINHO_ALARME = 'src/alarme.wav'

# =======================
# LOGGING
# =======================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# =======================
# FUNÇÕES AUXILIARES
# =======================
def inicializa_som(caminho_alarme):
    pygame.init()
    pygame.mixer.init()
    return pygame.mixer.Sound(caminho_alarme)

def detecta_intrusos(model, frame):
    pessoas_detectadas = []
    resultados = model.predict(frame, stream=True)
    frame_anotado = None

    for r in resultados:
        frame_anotado = r.plot()  
        for b in r.boxes:
            if int(b.cls) == 0:  
                x1, y1, x2, y2 = b.xyxy[0]
                largura = x2 - x1
                altura = y2 - y1
                area = largura * altura
                if largura > 100 and altura > 150 and area > 15000:
                    pessoas_detectadas.append(b)

    return pessoas_detectadas, frame_anotado

def esta_horario_alerta(hora_atual):
    return hora_atual >= HORARIO_INICIO_ALERTA or hora_atual < HORARIO_FIM_ALERTA

# =======================
# PROGRAMA PRINCIPAL
# =======================
def main():
    alarme = inicializa_som(CAMINHO_ALARME)
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    ultimo_tempo_deteccao = time.time()
    mostrar_deteccao_ate = 0
    frame_anotado = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        agora = datetime.now()
        hora_atual = agora.hour
        hora_formatada = agora.strftime("%H:%M:%S")
        tempo_atual = time.time()

        if tempo_atual - ultimo_tempo_deteccao >= INTERVALO_DETECCAO:
            ultimo_tempo_deteccao = tempo_atual

            pessoas_detectadas, frame_anotado = detecta_intrusos(model, frame)

            if pessoas_detectadas and esta_horario_alerta(hora_atual):
                logging.info("🚨 INTRUSO DETECTADO - ALARME DISPARADO 🚨")
                pygame.mixer.Sound.play(alarme)

            mostrar_deteccao_ate = tempo_atual + DURACAO_EXIBICAO

        if tempo_atual < mostrar_deteccao_ate and frame_anotado is not None:
            frame_exibido = frame_anotado.copy()
        else:
            frame_exibido = frame.copy()

        cv2.putText(frame_exibido, f"Hora: {hora_formatada}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame_exibido, "Detector de Intrusao", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Detecção de Intrusão", frame_exibido)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
