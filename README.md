Detector de Intrusão com Visão Computacional 🚨

Este projeto implementa um sistema inteligente para detecção de intrusos em tempo real usando Visão Computacional e Inteligência Artificial.
O objetivo é monitorar ambientes como casas, escritórios ou indústrias e detectar automaticamente a presença de pessoas, disparando um alarme sonoro fora do horário configurado.

--- Tecnologias e bibliotecas utilizadas ---

🐍 Python — linguagem base do projeto
📷 OpenCV — para captura e processamento de vídeo
🤖 YOLOv8 (Ultralytics) — modelo pré-treinado para detecção de objetos em tempo real
🎮 Pygame — para exibir o vídeo em tempo real e tocar o som do alarme
🕒 Datetime & Time — para controlar o horário e frequência de detecção

--- Como executar o projeto ---

-> Clone o repositório

git clone https://github.com/SeuUsuario/detector_intrusao.git
cd detector_intrusao

-> Crie e ative um ambiente virtual

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

-> Instale as dependências

pip install -r requirements.txt

-> Execute o sistema

python src/detector.py

--- Como funciona ---

O script acessa a webcam do seu computador.
A cada 4 segundos, realiza uma varredura com o modelo YOLOv8 para identificar todos os objetos no ambiente.
Desenha caixas (bounding boxes) ao redor de todos os objetos detectados, não apenas pessoas.
Exibe o horário atual sobre o vídeo.
Fora do horário configurado (por padrão, das 23h às 6h), se detectar pessoas, dispara um alarme sonoro usando o Pygame.
Isso torna o sistema útil para: Segurança residencial, evitando movimentação fora de horários permitidos, monitoramento de escritórios após expediente, áreas industriais com acesso restrito em determinados turnos.

--- Como configurar o horário do alarme ---

No arquivo `src/detector.py` você encontrará:

    if pessoas and (hora_atual >= 23 or hora_atual < 6):

Basta alterar para o horário que você deseja.

🎯 Diferenciais do projeto
✅ Detecção com YOLOv8, um dos modelos mais rápidos e eficientes do mercado
✅ Exibe caixas ao redor de todos os objetos detectados, não apenas pessoas
✅ Alarme sonoro configurado para tocar fora do horário permitido
✅ Código comentado e organizado, fácil de adaptar para:
--CFTV com câmeras IP
--Monitoramento multi-câmeras
--Integração com banco de dados de logs

⭐ Deixe seu star!
Se este projeto te ajudou ou te inspirou, não esquece de deixar uma ⭐ no repositório! Isso motiva a continuar criando projetos open-source 😊
