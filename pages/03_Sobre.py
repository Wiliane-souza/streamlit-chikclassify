from components.header import header
import streamlit as st
import pandas as pd

header(st)

tab1, tab2, tab3 = st.tabs(["Sobre", "Pré processamento", "O melhor modelo"])

with tab1:
    st.write("<h3>Sobre o projeto</h3>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> Em 2022, até a 52ª semana epidemiológica, o Brasil registrou 174.517 casos prováveis de Chikungunya, \
        uma arbovirose que, apesar de pouco mortal, pode causar sintomas de longa duração. \
        Esse número corresponde a um aumento de 78,9% de casos em relação ao ano anterior \
        tendo uma incidência de 81,8 casos a cada 100 mil habitantes. </p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> O processo de diagnóstico da Chikungunya pode ser realizado por profissionais de saúde de forma manual \
        ou utilizando artifícios tecnológicos. Modelos de aprendizado de máquina são capazes de aprender padrões \
        a partir de um conjunto de dados, tendo potencial para auxiliar no processo de diagnóstico de doenças e \
        tomada de decisão. Dessa forma, é possível reduzir a possibilidade de erros de diagnósticos, reduzir \
        custos de exames laboratoriais e até mesmo realizar atendimento em maior escala, especialmente em \
        locais com poucos recursos disponíveis para saúde. </p>", unsafe_allow_html=True)

with tab2:
    st.write("<h3>Pré processamento dos dados</h3>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> Nesse projeto é utilizada uma base com dados \
    reais de 140.516 pacientes brasileiros, coletados do Sistema de Informação de \
    Agravos de Notificação (SINAN) e do Portal de Dados Abertos do Recife (PDA). Originalmente, a base contava \
    com 120 colunas, também chamados de atributos. \
    Desses, foram removidos atributos capazes de enviezar os aprendizado do modelo \
    tais quais resultados de exames. Também foram removidos aqueles irrelevantes para a identificação \
    da Chikungunya, como região, datas, raça, idade e outros. Dessa forma, o número de atributos foi reduzido, e, com aplicação \
    de feature selection, foram mantidos 10 atributos. </p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify;'> Foram removidos os atributos irrelevantes que não possuiam informações relevantes para a \
    classificação Chikungunya, de acordo com os critérios: </p>", unsafe_allow_html=True)

    st.markdown("- Representa códigos identificadores (ID)")
    st.markdown("- Representa data")
    st.markdown("- Representa dados sociodemográficos")
    st.markdown("- Representa resultados de exames")
    st.markdown("- Representa informações relacionadas ao diagnóstico")

    st.write("<p style='text-align: justify;'> A partir dos 24 atributos restantes, foi realizada a remoção de atributos vazios, \
    ou seja, atributos que possuíam ao menos 50% de valores nulos ou que apresentavam informações sem significado. \
    Seguindo esse processo, 22 atributos permaneceram. Foi também realizada a transformação dos dados, que consiste \
    em converter valores não numéricos para valores numéricos. Sendo assim, o valor 'OUTRAS_DOENCAS' foi transformado \
    em 0, e o valor 'CHIKUNGUNYA', em 1, ambos pertencentes ao atributo 'CLASSI_FIN'. Os valores dos demais atributos \
    já estavam em formato numérico. Após a transformação dos dados, foram removidas os dados duplicados, restando um conjunto \
    de 8080 dados. Por fim, foi feito o balanceamento do dataset, visto que haviam 6510 dados classificados como 'OUTRAS_DOENCAS' \
    e somente 1570 como 'CHIKUNGUNYA'. Para tanto, foi realizado um undersampling randômico, evitando-se a criação de dados irreais \
    de pacientes nas amostras de treino e de teste, e totalizando finalmente um dataset com 3140 casos. </p>", unsafe_allow_html=True)

    st.image("./assets/img/balance_before.png", caption="Antes do under sampling", width=500)

    st.image("./assets/img/balance_after.png", caption="Depois do under sampling", width=500)

with tab3:
    st.write("<h3>O melhor modelo</h3>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'> O modelo que utiliza o método AdaBoost e a técnica de Grid Search, foi selecionado \
    como melhor modelo, tendo accuracy de 67,3%, precision de 67,2%, recall de 67,3% e f1-score de 67,2%, sendo\
    considerado , para os três últimos, as médias macro dos resultados. De maneira geral, todos os modelos tiveram métricas semelhantes, \
    que podem ser conferidas na página de predições, \
    porém, esse modelo se destaca por ter as métricas mais altas e utilizar os atributos sugeridos  por um especialista da área de saúde. \
    acessível. A seguir, são apresentados os resultados das otmizações do modelos, utilizados em seu treinamento. </p>", unsafe_allow_html=True)

    st.write("<h5>Grid Search</h5>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'>Primeiramente, foi aplicada a estratégia de grid search, que é utilizada para \
    identificar os melhores hiperparâmetros para treinamento do modelo. Para isso, foi utlizado o método GridSearchCV, em Python, \
    com k=10. Os parâmetros selecionados foram utilizados no treinamento final, sendo eles:</p>", unsafe_allow_html=True)


    df = pd.DataFrame({
        'Métrica': ['algorithm', 'estimator', 'learning_rate', 'n_estimators', 'random_state'],
        'Valor': ['SAMME.R', 'None', '1.0', '30', 'None']
    })

    st.table(data=df)

    st.write("<h5>Feature Selection</h5>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify;'>Os atributos utilizados para o treinamento do modelo foram selecionados por um médico voluntário, \
    que trabalhou durante dois anos e meio como clínico geral. Os seguintes atributos foram incluídos: febre, mialgia, cefaleia, exantema, vômito, náusea, \
    dor nas costas, conjuntivite, artrite, artralgia, petequias e dor retroorbital. </p>", unsafe_allow_html=True)

    st.write("<h5>Matriz de Confusão</h5>", unsafe_allow_html=True)

    st.image("./assets/img/mc_ada_boost_avaluated.png", caption="Matriz de confusão dos resultados do melhor modelo.", width=500)



