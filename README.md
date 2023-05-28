# color-identifier
Este é um programa em Python que utiliza a webcam para monitorar cores

## Funcionalidades

- Acesso à webcam para capturar imagens da tela.
- Processamento das imagens para identificar a cor predominante na tela.
- Verificação se a tela está vermelha ou verde.
- Exibição do resultado em tempo real.

## Requisitos do Sistema

- Python 3.x
- Biblioteca OpenCV

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode fazer o download no site oficial do Python: https://www.python.org/downloads/

2. Instale a biblioteca OpenCV executando o seguinte comando:

```shell
   pip install opencv-python
   ```

## Uso

1. Execute o programa monitoramento_maquininha.py.
2. A webcam será ativada e a tela da máquina de cartão será exibida em tempo real.
3. O programa calculará a quantidade de pixels vermelhos e verdes na imagem e exibirá se a tela está vermelha ou verde no console.
4. Pressione a tecla 'q' para encerrar o programa.

## Personalização

Você pode personalizar o programa de acordo com suas necessidades:

- Faixa de cores: Na função verificar_cor_maquininha, você pode ajustar os valores das variáveis lower_red, upper_red, lower_green e upper_green para corresponderem à cor exata que você gostaria de monitorar.

- Ações adicionais: Você pode adicionar outras ações com base no resultado da verificação de cor. Por exemplo, enviar um alerta, acionar um mecanismo de parada de produção, etc.

## Licença

Este projeto está licenciado sob a Licença MIT.