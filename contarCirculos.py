import numpy as np
import cv2
import sys


def encontrando_circulos(img_original):
    #limites superiores e inferiores das cores (HSV)
    vermelho_upper = np.array([10, 255, 255])
    vermelho_lower = np.array([0, 50, 50])
    
    azul_upper = np.array([110, 255, 255])
    azul_lower = np.array([90, 50, 50])

    verde_upper = np.array([85, 255, 255])
    verde_lower = np.array([60, 50, 50])

    amarelo_upper = np.array([40, 255, 255])
    amarelo_lower = np.array([25, 50, 50])
    
    #para aplicar a máscara
    hsv_img = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    #para aplicar o blur
    img_cinza = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    #imagem de entrada de HoughCircles
    img_gauss = cv2.GaussianBlur(img_cinza, (7, 7), 1.5)
    
    #função principal, parâmetros ajustados manualmente
    circulos = cv2.HoughCircles(img_gauss, cv2.HOUGH_GRADIENT, dp=1.1, minDist=30, param1=90, param2=30, minRadius=15, maxRadius=100)
    
    img_saida = img_original.copy()
    
    contagem = {'Vermelho': 0, 'Amarelo':0, 'Verde':0, 'Azul':0}
    
    #conversão dos parâmetros (x, y, r) para inteiro
    circulos = np.uint16(np.around(circulos))
    
    for i in circulos[0, :]:
        centro = (i[0], i[1]) # (x, y)
        raio = i[2]
        
        mask_temp = np.zeros(hsv_img.shape[:2], dtype=np.uint8)
        
        #desenho do círculo externo menos círculo interno
        cv2.circle(mask_temp, centro, raio, 255, -1)
        cv2.circle(mask_temp, centro, int(raio * 0.85), 0, -1)
        
        pixels_hsv = hsv_img[mask_temp == 255]
        
        h_median = np.median(pixels_hsv[:, 0])
        s_median = np.median(pixels_hsv[:, 1])
        v_median = np.median(pixels_hsv[:, 2])
        
        cor_detectada = None
        cor_bgr = (0, 0, 0)
        
        #comparando os valores medianos de H, S e V com os limites inferiores e superiores
        if (vermelho_lower[0] <= h_median <= vermelho_upper[0]) and \
            (vermelho_lower[1] <= s_median <= vermelho_upper[1]) and \
            (vermelho_lower[2] <= v_median <= vermelho_upper[2]):
                cor_detectada = 'Vermelho'
                cor_bgr = (0, 0, 255)
                contagem['Vermelho'] += 1
        
        elif (amarelo_lower[0] <= h_median <= amarelo_upper[0]) and \
                (amarelo_lower[1] <= s_median <= amarelo_upper[1]) and \
                (amarelo_lower[2] <= v_median <= amarelo_upper[2]):
                cor_detectada = 'Amarelo'
                cor_bgr = (0, 255, 255)
                contagem['Amarelo'] += 1
                
        elif (verde_lower[0] <= h_median <= verde_upper[0]) and \
                (verde_lower[1] <= s_median <= verde_upper[1]) and \
                (verde_lower[2] <= v_median <= verde_upper[2]):
                cor_detectada = 'Verde'
                cor_bgr = (0, 255, 0)
                contagem['Verde'] += 1
                
        elif (azul_lower[0] <= h_median <= azul_upper[0]) and \
                (azul_lower[1] <= s_median <= azul_upper[1]) and \
                (azul_lower[2] <= v_median <= azul_upper[2]):
                cor_detectada = 'Azul'
                cor_bgr = (255, 0, 0)
                contagem['Azul'] += 1
                
        if cor_detectada:
            cv2.circle(img_saida, centro, raio, cor_bgr, 3)
            cv2.circle(img_saida, centro, 2, (0, 0, 0), 3)
    
    #retornando
    #imagem com os círculos detectados
    #contagem individual de cores e
    #contagem total de círculos detectados
    return img_saida, contagem, len(circulos[0, :])
    

if len(sys.argv) == 1:
    lista = list(range(1, 9))
else:
    lista = [int(sys.argv[1])]

cores = ['Vermelho', 'Amarelo', 'Verde', 'Azul']

for i in lista:
    img = cv2.imread(str(i) + '.jpg')
    img_saida, contagem, total = encontrando_circulos(img)
    
    print('Imagem ' + str(i) + ": " + str(total))
    for c in cores:
        print('\t' + c + ": " + str(contagem[c]))

    cv2.imwrite('c' + str(i) + '.jpg', img_saida)