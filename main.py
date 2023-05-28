import cv2
import time

def verificar_cor_maquininha():
# inicializa o objeto de captura de video
    cap = cv2.VideoCapture(0)

    while True:
        # lê um frame do video
        ret, frame = cap.read()

        # verifica se o frame foi lido corretamente
        if not ret:
            print('--> Não foi possível ler o frame.')
            break

        # Exibe o frame capturado
        cv2.imshow('Webcam', frame) 

        # Converte o frame para o espaço de cores HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define a escala de cores para a cor vermelha e verde (você pode ajustar os valores conforme necessário)
        lower_red = (0, 70, 50)
        upper_red = (10, 255, 255)
        lower_green = (40, 70, 50)
        upper_green = (80, 255, 255)

        # Cria máscaras para identificar a cor vermelha e verde no frame
        red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
        green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

        #calcula a quantidade de pixels vermelhos é maior que a de pixels verdes
        red_pixels = cv2.countNonZero(red_mask)
        green_pixels = cv2.countNonZero(green_mask)

        # verifica se a quantidade de pixels vermelhos é maior que a de pixels verde
        if red_pixels > green_pixels:
            print('--> A Tela está vermelha.')
        elif green_pixels > red_pixels:
            print('--> A tela está verde.')   
        else:
            print('--> Não foi possível identificar a cor. Tentando novamente em 2 seg.')
            time.sleep(2)
            continue

        # exibe as máscaras
        cv2.imshow('Red Mask', red_mask)
        cv2.imshow('Green Mask', green_mask)

        # verifica se a tecla 'q' foi pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # libera os recursos utilizados
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    verificar_cor_maquininha()