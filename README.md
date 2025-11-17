# Instruções

- Siga fielmente a entrada e a saída solicitadas.

# Tarefa 6

Nesta tarefa você deverá contar o número de discos vermelhos, amarelos, verdes e azuis nas imagens numeradas de 1.jpg a 8.jpg. Note que cada disco tem um círculo interno e externo. O programa contarCirculos.py contém o código a partir do qual deve começar sua implementação.

- contarCirculos.py:
	
	- **entrada:** um inteiro **k** como argumentos da linha de comando **opcional** (use sys.argv). Caso o inteiro seja fornecido, o programa processará apenas a imagem k.jpg, caso contrário processará todas as imagens de 1.jpg a 8.jpg. A variável lista presente no programa contém todos os inteiros que serão processados.
	- **saída:** a string Imagem k: t, onde t é o total de discos na imagem, seguido de 4 strings, cada qual com uma cor e o subtotal de discos naquela cor específica. O programa, em sua versão final, não deve exibir imagens na tela, mas gravar a imagem do resultado da detecção no arquivo ck.jpg. Nessa imagem do resultado, deve colocar um círculo não preenchido, com um centro marcado, em cada disco na cor e com raio correspondentes. Esses círculos devem estar sobrepostos à imagem original. O círculo deve, **de preferência**, casar com o círculo externo do disco.
	- **observação 1:** as imagens de 1.jpg a 5.jpg são mais fáceis; as imagens de 6.jpg a 8.jpg são mais difíceis pois contém muitas sobreposições, mas tente o melhor possível!
	- **observação 2:** pode utilizar quaisquer funções prontas do opencv ou numpy, caso ajudem na tarefa.
	- **observação 3:** o código inicial fornecido já segue a entrada e saída, bastando fazer as devidas adaptações.
	- **observação 4:** para as imagens mais desafiantes, você pode implementar do zero caso queira aproveitar o fato que todos os discos contém um círculo interno e externo, com a razão entre os raios constante. Lembre-se também de que você pode separar em 4 detecções distintas, para que os os pontos pertencentes a um círculo de uma cor não interfira na detecção dos círculos de outras cores.
