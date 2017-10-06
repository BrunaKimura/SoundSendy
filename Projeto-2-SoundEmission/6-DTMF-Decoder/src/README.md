---
title: Camada Física -  APS 5 - DTMF - Encoder e recepção
author: Hugo Mendes e Leonardo Pereira 
date: Setembro - 2017
---

# Docs

## Comparação de gráficos recebidos e gerados
<h1> Tom 0 </h1>
<div align="center"> Frequências geradas (1336,941) X Frequências recebidas (1336.03,941.02) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier0.png" width="350"/>
    <img src="./plots/DecodeF0.png" width="350"/>
</p>

<h1> Tom 1 </h1>
<div align="center"> Frequências geradas (1209, 697) X Frequências recebidas (1209.02,697.01)  </div>
<p align="center">
  <img src="./plots/graphEncoderFurier1.png" width="350"/>
    <img src="./plots/DecodeF1.png" width="350"/>
</p>

<h1> Tom 2 </h1>
<div align="center"> Frequências geradas (1336,697) X Frequências recebidas (1336.03, 697.01)  </div>
<p align="center">
  <img src="./plots/graphEncoderFurier2.png" width="350"/>
   <img src="./plots/DecodeF2.png" width="350"/>
</p>

<h1> Tom 3 </h1>
<div align="center"> Frequências geradas (1477,697) X Frequências recebidas (1477.02, 697.01) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier3.png" width="350"/>
   <img src="./plots/DecodeF3.png" width="350"/>
</p>

<h1> Tom 4 </h1>
<div align="center"> Frequências geradas (1209,770) X Frequências recebidas (1209.02, 770.01) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier4.png" width="350"/>
    <img src="./plots/DecodeF4.png" width="350"/>
</p>

<h1> Tom 5 </h1>
<div align="center"> Frequências geradas (1336,770) X Frequências recebidas (1336.03, 770.01) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier5.png" width="350"/>
    <img src="./plots/DecodeF5.png" width="350"/>
</p>

<h1> Tom 6 </h1>
<div align="center"> Frequências geradas (1477,770) X Frequências recebidas (1477.02, 770.01) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier6.png" width="350"/>
   <img src="./plots/DecodeF6.png" width="350"/>
</p>

<h1> Tom 7 </h1>
<div align="center"> Frequências geradas (1209,852) X Frequências recebidas (1209.02, 852.02) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier7.png" width="350"/>
   <img src="./plots/DecodeF7.png" width="350"/>
</p>

<h1> Tom 8 </h1>
<div align="center"> Frequências geradas (1336,852) X Frequências recebidas (1336.02, 852.02) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier8.png" width="350"/>
   <img src="./plots/DecodeF8.png" width="350"/>
</p>

<h1> Tom 9 </h1>
<div align="center"> Frequências geradas (1477,852) X Frequências recebidas (1477.02, 852.02) </div>
<p align="center">
  <img src="./plots/graphEncoderFurier9.png" width="350"/>
  <img src="./plots/DecodeF9.png" width="350"/>
</p>

## consideração sobre os gráficos
A diferença entre os gráficos da transformada de fourier do sinal emitido e do recebido se deve aos ruídos presente no ambiente na hora de capturar o som, entretanto, os maiores picos que simbolizam a frequência detectada são totalmente compatíveis.

<h1> Tempo utilizado </h1>

Os gráficos foram plotados com os sinais recebidos em intervalos de 1 segundo.
