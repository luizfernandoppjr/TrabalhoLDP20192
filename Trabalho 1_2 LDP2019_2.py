import numpy as np
import random as rnd

class Pessoa:
    def __init__(self, rendimento_mensal_domiciliar):#, rede_ensino, modalidade, sexo, cor, regiao, idade):
        self.rendimento_mensal_domiciliar = rendimento_mensal_domiciliar
        #self.rede_ensino = rede_ensino
        #self.modalidade = modalidade
        #self.sexo = sexo
        #self.cor = cor
        #self.regiao = regiao
        #self.idade = idade

class Populacao:
    def __init__(self, tamanho):
        self.tamanho = tamanho

        #rendimento mensal domiciliar per capita
        self.rendimento_mensal_domiciliar_valores = [472, 1442, 2551, 1176, 745, 496, 360]
        self.rendimento_mensal_domiciliar_texto = ["Sem rendimento a 1/2 salário mínimo",
                                                    "Mais de 1/2 a 1 salário mínimo",
                                                    "Mais de 1 a 2 salários mínimos",
                                                    "Mais de 2 a 3 salários mínimos",
                                                    "Mais de 3 a 5 salários mínimos",
                                                    "Mais de 5 salários mínimos",
                                                    "Sem declaração"]
        self.rendimento_mensal_domiciliar_media = sum(self.rendimento_mensal_domiciliar_valores) / len(self.rendimento_mensal_domiciliar_valores)
        self.rendimento_mensal_domiciliar_distrib = [x / sum(self.rendimento_mensal_domiciliar_valores) for x in self.rendimento_mensal_domiciliar_valores]


        gerador = np.random.multinomial(100, self.rendimento_mensal_domiciliar_distrib)
        
        renda_individuo = []
        for j in range(len(gerador)):
            for i in range(len(self.rendimento_mensal_domiciliar_distrib)):
                if gerador[j] <= sum(self.rendimento_mensal_domiciliar_distrib[0:i]):
                    renda_individuo[j] = i
                    break

        


        self.individuos = [Pessoa(np.random.multinomial(self.tamanho, self.rendimento_mensal_domiciliar_distrib) * self.rendimento_mensal_domiciliar_media)  for i in range(tamanho)]


    def amostra(self, n):
        return rnd.sample(self.individuos, n)


pop = Populacao(100)
print(pop.amostra(10))
