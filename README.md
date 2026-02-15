# 👁️ Sistema de Visão Computacional para Segurança Ferroviária (POC)

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-purple?style=for-the-badge)

> **Projeto desenvolvido como Prova de Conceito (POC) para aumentar a segurança operacional em pátios e linhas férreas.**

![Demonstração do Sistema](demo_preview.png)

## 🎯 Objetivo do Projeto
Desenvolver uma solução de **monitoramento inteligente em tempo real** capaz de identificar intrusões em áreas de risco (trilhos e zonas de manobra) automaticamente, sem depender apenas da atenção humana.

O sistema simula uma câmera de segurança da **MRS Logística**, detectando pessoas próximas à via e emitindo alertas visuais imediatos para prevenir acidentes.

## 🛠️ Tecnologias Utilizadas
* **Python 3.10:** Linguagem base para processamento de dados.
* **YOLOv8 (Ultralytics):** Estado da arte em Inteligência Artificial para detecção de objetos com alta precisão e velocidade.
* **OpenCV:** Manipulação de vídeo e desenho de interfaces gráficas (HUD) sobre a imagem.
* **Lógica de Segurança:** Algoritmo que classifica o nível de risco (Normal vs Crítico) dependendo do objeto detectado na via.

## 🚀 Funcionalidades
* ✅ **Detecção de Humanos e Veículos:** Identifica pedestres, carros e caminhões.
* ✅ **Classificação de Risco:**
    * 🟢 **Verde:** Área segura / Monitoramento normal.
    * 🔴 **Vermelho:** ALERTA CRÍTICO (Invasão de Via).
* ✅ **HUD Profissional:** Interface visual que simula sistemas de CFTV corporativos.

## 💻 Como Executar
1. **Instalar Dependências:**
   ```bash
   pip install ultralytics opencv-python
