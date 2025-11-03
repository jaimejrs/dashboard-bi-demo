# app.py (Versão Demo )

# --- 1. Importação das Bibliotecas ---
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 2. Definição das Funções Auxiliares ---

@st.cache_data
def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
    """Carrega os dados de um arquivo CSV, tratando datas e criando colunas temporais."""
    try:
        df = pd.read_csv(
            caminho_arquivo,
            encoding='utf-8',
            delimiter=',',
            parse_dates=['publish_date_approx']
        )
    except FileNotFoundError:
        st.error(f"Erro: O arquivo de dados '{caminho_arquivo}' não foi encontrado.")
        st.info("Por favor, aguarde enquanto o repositório está a ser preparado. Se o erro persistir, verifique o nome do arquivo.")
        st.stop()

    df['year_month'] = df['publish_date_approx'].dt.to_period('M').astype(str)
    df['publish_dayofweek'] = df['publish_date_approx'].dt.day_name()
    return df

def plotar_grafico_linha(df, x_col, y_col, agg_func, titulo, **kwargs):
    """Função reutilizável para criar gráficos de linha agregados."""
    df_agg = df.groupby(x_col)[y_col].agg(agg_func).reset_index()
    fig = px.line(df_agg, x=x_col, y=y_col, markers=True, title=titulo, **kwargs)
    st.plotly_chart(fig, use_container_width=True)

def plotar_grafico_barra(df, x_col, y_col, titulo, **kwargs):
    """Função reutilizável para criar gráficos de barra."""
    fig = px.bar(df, x=x_col, y=y_col, title=titulo, **kwargs)
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Configurações Iniciais ---
st.set_page_config(layout="wide", page_title="Análise de Vídeos Virais (Demo BI)")

# --- 4. Carregamento Inicial e Filtros ---

# MODIFICAÇÃO IMPORTANTE: Removida a pasta 'data/' do caminho.
df_original = carregar_dados('youtube_shorts_tiktok_trends_2025.csv')

st.sidebar.header("Filtros")

# --- Lógica de Filtros ---
todos_paises_options = sorted(df_original['country'].unique())
selecionar_todos_paises = st.sidebar.checkbox("Selecionar Todos os Países", value=True)
if selecionar_todos_paises:
    paises_selecionados = st.sidebar.multiselect("Selecione os Países:", options=todos_paises_options, default=todos_paises_options)
else:
    paises_selecionados = st.sidebar.multiselect("Selecione os Países:", options=todos_paises_options)

todas_plataformas_options = sorted(df_original['platform'].unique())
selecionar_todas_plataformas = st.sidebar.checkbox("Selecionar Todas as Plataformas", value=True)
if selecionar_todas_plataformas:
    plataformas_selecionadas = st.sidebar.multiselect("Selecione as Plataformas:", options=todas_plataformas_options, default=todas_plataformas_options)
else:
    plataformas_selecionadas = st.sidebar.multiselect("Selecione as Plataformas:", options=todas_plataformas_options)

todos_dispositivos_options = sorted(df_original['device_type'].unique())
selecionar_todos_dispositivos = st.sidebar.checkbox("Selecionar Todos os Dispositivos", value=True)
if selecionar_todos_dispositivos:
    dispositivos_selecionados = st.sidebar.multiselect("Selecione o Device:", options=todos_dispositivos_options, default=todos_dispositivos_options)
else:
    dispositivos_selecionados = st.sidebar.multiselect("Selecione o Device:", options=todos_dispositivos_options)

# --- LÓGICA DE FILTRAGEM ---
df_filtrado = df_original.query(
    "country == @paises_selecionados and platform == @plataformas_selecionadas and device_type == @dispositivos_selecionados"
)

# --- 5. Construção do Dashboard ---
st.title("📊🎦 Análise de Performance de Vídeos Virais (Versão BI Demo)")

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados. Por favor, ajuste sua seleção.")
else:
    tab1, tab2, tab3, tab4 = st.tabs(["Visão Geral", "Análise dos Fatores", "Análise do Conteúdo", "Análise Geográfica"])

    with tab1:
        st.header("Visão Geral dos Dados")
        col1, col2 = st.columns(2)
        with col1:
            plotar_grafico_linha(df_filtrado, 'year_month', 'views', 'sum', 'Tendência Mensal de Visualizações', labels={'year_month': 'Mês', 'views': 'Total de Visualizações'})
            engagement_by_platform = df_filtrado.groupby('platform')['engagement_rate'].mean().reset_index()
            fig = px.pie(engagement_by_platform, values='engagement_rate', names='platform', title='Taxa de Engajamento Média', hole=.3)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            plotar_grafico_linha(df_filtrado, 'year_month', 'engagement_rate', 'mean', 'Tendência Mensal da Taxa de Engajamento', labels={'year_month': 'Mês', 'engagement_rate': 'Taxa de Engajamento Média'}, color_discrete_sequence=['green'])
            st.subheader("Análises Avançadas")
            st.info("A análise de Machine Learning foi removida nesta versão demonstrativa.")

    with tab2:
        st.header("Análise de Fatores de Performance")
        col1, col2 = st.columns(2)
        with col1:
            plotar_grafico_linha(df_filtrado, 'upload_hour', 'engagement_rate', 'mean', 'Engajamento por Hora de Upload', labels={'upload_hour': 'Hora do Dia (24h)', 'engagement_rate': 'Taxa de Engajamento Média'})
            engagement_by_category = df_filtrado.groupby('category')['engagement_total'].median().sort_values(ascending=False)
            plotar_grafico_barra(engagement_by_category, engagement_by_category.index, engagement_by_category.values, 'Engajamento Total Mediano por Categoria', color=engagement_by_category.index, labels={'x': 'Categoria', 'y': 'Engajamento Mediano'}, log_y=True)
        with col2:
            bins = [0, 15, 30, 60, 120, np.inf]
            labels = ['0-15s', '16-30s', '31-60s', '61-120s', '120s+']
            df_filtrado['duration_bin'] = pd.cut(df_filtrado['duration_sec'], bins=bins, labels=labels, right=False)
            engagement_by_duration = df_filtrado.groupby('duration_bin', observed=True)['engagement_rate'].mean().reset_index()
            plotar_grafico_barra(engagement_by_duration, 'duration_bin', 'engagement_rate', 'Engajamento por Duração do Vídeo', color='duration_bin', labels={'duration_bin': 'Faixa de Duração', 'engagement_rate': 'Taxa de Engajamento Média'})
            dias_ordem = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            engagement_by_weekday = df_filtrado.groupby('publish_dayofweek')['engagement_rate'].mean().reindex(dias_ordem).reset_index()
            plotar_grafico_barra(engagement_by_weekday, 'publish_dayofweek', 'engagement_rate', 'Engajamento por Dia da Semana', color='publish_dayofweek', labels={'publish_dayofweek': 'Dia da Semana', 'engagement_rate': 'Taxa de Engajamento Média'}, log_y=True)

    with tab3:
        st.header("Análise do Conteúdo dos Vídeos")
        st.info("As análises de conteúdo de texto (Top Palavras-chave, Sentimento) e Teste A/B foram removidas nesta versão demonstrativa.")
        st.warning("Esta aba está vazia nesta versão. Na versão completa, ela contém análises de Processamento de Linguagem Natural.")

    with tab4:
        st.header("Análise Geográfica")
        st.subheader("Performance por País (Visualizações vs. Engajamento)")
        analise_paises = df_filtrado.groupby('country').agg(avg_views=('views', 'mean'), avg_engagement_rate=('engagement_rate', 'mean'), video_count=('row_id', 'count')).reset_index()
        fig = px.scatter(analise_paises, x='avg_views', y='avg_engagement_rate', size='video_count', color='country', hover_name='country', log_x=True, size_max=60, text='country', labels={"avg_views": "Média de Visualizações (Log)", "avg_engagement_rate": "Taxa de Engajamento Média"})
        fig.update_traces(textposition='middle center', textfont=dict(color='white'))
        st.plotly_chart(fig, use_container_width=True)
        st.subheader("Taxa de Engajamento por Categoria e Região")
        pivot_engagement = df_filtrado.pivot_table(values='engagement_rate', index='region', columns='category', aggfunc='mean')
        if not pivot_engagement.empty:
            fig_heatmap = px.imshow(pivot_engagement, text_auto=".3f", aspect="auto", labels=dict(x="Categoria", y="Região", color="Engajamento Médio"), color_continuous_scale='YlGnBu')
            st.plotly_chart(fig_heatmap, use_container_width=True)
        else:
            st.info("Não há dados suficientes para criar o heatmap com os filtros atuais.")
