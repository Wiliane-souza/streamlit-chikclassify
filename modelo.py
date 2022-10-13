import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import pickle

path = './databases/'
arquivo = path + 'proc_database.csv'

dataset = pd.read_csv(arquivo, sep=';', header=0)

print(f'base carregada com sucesso')



# y -> colunas, exceto a alvo
X = np.array(dataset.drop(labels=['CLASSI_FIN'], axis=1))

# y -> coluna alvo
y = np.array(dataset['CLASSI_FIN'])

print(f'Amostra X: {X[0:5]}')
print(f'Amostra y: {y[0:5]}')


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(f'Dataset de treinamento: {len(X_train)} linhas')
print(f'Dataset de teste: {len(X_test)} linhas')


param_grid = [ # valores dos hiperparametros que o grid vai percorrer
    {
        'criterion': ['gini', 'entropy'], # 2
        'splitter': ['best', 'random'], # 2
        'max_depth': [None, 1, 3, 5], # 4
        'min_samples_leaf': [1, 3, 5, 7, 9, 11], # 6
        'min_samples_split': [2, 5, 8] # 3
    } 
] # 288 combinações x 10 do CV = 2880 combinações

decision_tree = DecisionTreeClassifier() # selecionando o modelo a ser aplicado o grid

model_grid = GridSearchCV(
    estimator=decision_tree, # modelo a ser aplicado o grid
    param_grid=param_grid, # os hiperparametros que o grid vai percorrer
    cv=10, # valor de k para o kfold, usado no cross-validation
    scoring='accuracy', # métrica de avaliação usada para avaliar a performance dos hiperparametros
    n_jobs=-1, # numero de processadores usados para rodar o código. -1 usa todos disponíveis
    verbose=100
)

# rodando o grid...
model_grid.fit(X_train, y_train) 

# Treinamento (usando bases de treino)
decision_tree.fit(X_train, y_train)

print('DecisionTreeClassifier treinado com sucesso! Realizando classificações...')


print('Best score:', model_grid.best_score_) # qual foi a melhor pontuação NO TREINO
print('Best params', model_grid.best_params_) # quais os melhores hiperparametros?


best_model = model_grid.best_estimator_ # aqui recebemos o modelo com os hiperparametros que tiveram o melhor resultado na base de treino
y_pred = best_model.predict(X_test) # predizendo na base de teste


print(y_pred.shape)
# print(y_tree_pred.shape)
# print(f'Acurácia: {accuracy_score(y_test, y_tree_pred)}')

print(f'Acurácia: {accuracy_score(y_test, y_pred)}')

print(f'Relatório de Classificação:\n {classification_report(y_test, y_pred)}')

plt.rcParams['figure.figsize'] = (5, 4)

print(f'Matriz de confusão: ')
plot_confusion_matrix(best_model, X_test, y_test, cmap='Blues')

filename_model = "model/model.sav"
pickle.dump(best_model, open(filename_model, 'wb'))

