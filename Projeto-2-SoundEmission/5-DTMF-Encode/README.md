---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
author: Hugo Mendes e Leonardo Pereira 
date: Setembro - 2017
---

# Docs

## Descrição da geração de tons

Foi usado a tabela DTMF (Dual-Tone Multi-Frequency) abaixo:

Hz|1209 |1336|1477|1633|
|---|---|---|---|---|
697|1   |2   |3   | A  |   |
770| 4|   5|   6| B  |
852| 7  | 8  | 9  | C  |
941| *  | 0 | #  | D  |

Na tabela acima são mostradas as frequências “altas” na linha superior e as baixas na coluna mais à esquerda.
A frequência é obtida do batimento da frequência alta e baixa de uma certa tecla, por exemplo, para a tecla 5 o tom enviado é a soma de uma senóide na frequência de 1336Hz com uma outra senóide de 770Hz.
A escolha destas frequências se deve principalmente pela baixa probabilidade de se produzir estas combinações de frequências com a voz humana.

## Descrição da frequência que compõe cada tom

    não entendi o que por aqui

## Comparação de gráficos recebidos e gerados
<h1> Tom 0 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder0.png" width="350"/>
  <img src="./src/plots/sound0.jpg" width="350"/>
</p>

<h1> Tom 1 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder1.png" width="350"/>
  <img src="./src/plots/sound1.jpg" width="350"/>
</p>

<h1> Tom 2 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder2.png" width="350"/>
  <img src="./src/plots/sound2.jpg" width="350"/>
</p>

<h1> Tom 3 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder3.png" width="350"/>
  <img src="./src/plots/sound3.jpg" width="350"/>
</p>

<h1> Tom 4 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder4.png" width="350"/>
  <img src="./src/plots/sound4.jpg" width="350"/>
</p>

<h1> Tom 5 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder5.png" width="350"/>
  <img src="./src/plots/sound5.jpg" width="350"/>
</p>

<h1> Tom 6 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder6.png" width="350"/>
  <img src="./src/plots/sound6.jpg" width="350"/>
</p>

<h1> Tom 7 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder7.png" width="350"/>
  <img src="./src/plots/sound7.jpg" width="350"/>
</p>

<h1> Tom 8 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder8.png" width="350"/>
  <img src="./src/plots/sound8.jpg" width="350"/>
</p>

<h1> Tom 9 </h1>
<div align="center"> Onda Gerada X Onda Recebida </div>
<p align="center">
  <img src="./src/plots/graphEncoder9.png" width="350"/>
  <img src="./src/plots/sound9.jpg" width="350"/>
</p>

<h1> Considerações em relação aos gráficos </h1>

Consideremos satisfatório as comparações finais obtidas nos gráficos. Obviamente não estavam 100% iguais, devido ao fato
que as ondas geradas pelo Encoder foram feitas a partir de funções senoidas específicas e "limpas", o que é praticamente 
impossível de detectar no decoder por causa de ruídos externos; é possível diminuir os erros através de filtros.