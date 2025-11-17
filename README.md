
# Detecção de Círculos com OpenCV

Este projeto utiliza Python e OpenCV para detectar círculos em imagens e identificar a cor de cada círculo (Vermelho, Amarelo, Verde ou Azul).

A saída inclui:
* A imagem com círculos detectados e marcados.

* A contagem de círculos por cor.

* A contagem total de círculos.

Este projeto foi desenvolvido na disciplina DIM0141 - Visão Computacional.

## Bibliotecas e pacotes
```
opencv-python
numpy
```
## Execução

Para processar todas as imagens de 1.jpg a 8.jpg:

```bash
python contarCirculos.py
```

Para processar uma imagem específica, por exemplo 3.jpg:

```bash
python contarCirculos.py 3
```


## Observações

* Parâmetros do HoughCircles podem ser ajustados para melhorar a detecção.

* Os intervalos HSV foram definidos manualmente e podem ser calibrados conforme o ambiente.

* A análise de cor usa a mediana dos pixels, reduzindo ruído e falhas.
