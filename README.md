# 📊 Dashboard de Análise de Vídeos Virais (Projeto BI - UFC)



<p align="center">
  <a href="https://dashboard-bi-demo.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/Acessar%20Dashboard-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Link para o Dashboard">
  </a>
</p>

<p align="center">
  <a href="#-descrição-do-projeto">Descrição</a> •
  <a href="#-objetivos-acadêmicos">Objetivos</a> •
  <a href="#-principais-funcionalidades">Funcionalidades</a> •
  <a href="#️-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-executar-o-projeto">Como Executar</a> •
  <a href="#-autor">Autor</a>
</p>

---

## 📖 Descrição do Projeto

Este projeto faz parte da disciplina **Business Intelligence (UFC)** e está sendo desenvolvido **de forma incremental ao longo do semestre letivo de 2025**.  

O objetivo é aplicar **conceitos de BI, ETL e visualização de dados** utilizando **Python e Streamlit**, criando um **dashboard interativo** que analisa tendências de vídeos virais em plataformas como **TikTok** e **YouTube Shorts**.

A aplicação demonstra o uso de **ferramentas de análise exploratória, manipulação de dados e visualização interativa** em um contexto de *Business Intelligence moderno*.

---

## 🎯 Objetivos Acadêmicos

- Explorar o uso de **Python** em pipelines de **ETL/ELT**.  
- Desenvolver **dashboards interativos** com métricas e insights.  
- Aplicar práticas de **análise exploratória de dados (EDA)**.  
- Trabalhar com **visualização e storytelling de dados**.  

---

## ✨ Principais Funcionalidades

- **Visão Geral:** Exibe métricas consolidadas, tendências de visualizações e engajamento.  
- **Análise de Fatores:** Relaciona variáveis como hora, categoria e duração com desempenho.  
- **Análise Geográfica:** Apresenta comparativos de performance por país e região.  
- **Filtros Interativos:** Segmentação dinâmica por país, plataforma e tipo de dispositivo.   

> 🔎 *As seções de Machine Learning e NLP estão desativadas no momento.*

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido com um ecossistema moderno de **bibliotecas Python** voltadas para **ciência de dados e BI**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
</p>

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone este repositório
```bash
git clone https://github.com/seu-usuario/dashboard-bi-demo.git
cd dashboard-bi-demo
```

### 2️⃣ Crie e ative um ambiente virtual

No Linux / macOS (Para quem é nerd ou rico):
```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows [PowerShell] (Como um mero mortal comum):

```powershell
python -m venv venv
.\venv\Scripts\activate
```
### 4️⃣ Adicione o arquivo de dados

Certifique-se de que o arquivo youtube_shorts_tiktok_trends_2025.csv esteja na raiz do projeto, junto ao arquivo app.py.

### 5️⃣ Execute o aplicativo

```bash
streamlit run app.py
```
