import numpy as np
import random as rnd

class Pessoa:
    def __init__(self, rendimento_mensal_domiciliar, rede_ensino):#, modalidade, sexo, cor, regiao, idade):
        self.rendimento_mensal_domiciliar = rendimento_mensal_domiciliar
        self.rede_ensino = rede_ensino
        #self.modalidade = modalidade
        #self.sexo = sexo
        #self.cor = cor
        #self.regiao = regiao
        #self.idade = idade

class Populacao:
    def __init__(self, tamanho):
        self.tamanho = tamanho

        #rendimento mensal domiciliar per capita//

        #Estabelece os valores e distribuição dessa categoria pelos dados da PNAD
        self.rendimento_mensal_domiciliar_valores = [472.0, 1442.0, 2551.0, 1176.0, 745.0, 496.0, 360.0]
        self.rendimento_mensal_domiciliar_texto = ["Sem rendimento a 1/2 salário mínimo",
                                                    "Mais de 1/2 a 1 salário mínimo",
                                                    "Mais de 1 a 2 salários mínimos",
                                                    "Mais de 2 a 3 salários mínimos",
                                                    "Mais de 3 a 5 salários mínimos",
                                                    "Mais de 5 salários mínimos",
                                                    "Sem declaração"]
        self.rendimento_mensal_domiciliar_media = sum(self.rendimento_mensal_domiciliar_valores) / len(self.rendimento_mensal_domiciliar_valores)
        self.rendimento_mensal_domiciliar_distrib = [x / sum(self.rendimento_mensal_domiciliar_valores) for x in self.rendimento_mensal_domiciliar_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.rendimento_mensal_domiciliar_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        renda_individuo = [0] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                renda_individuo[k] = self.rendimento_mensal_domiciliar_texto[j]
                k += 1
        
        #//rendimento mensal domiciliar per capita


        #rede_ensino//

        #Estabelece os valores e distribuição dessa categoria pelos dados da PNAD
        self.rede_ensino_valores = [105.0, 372.0]
        self.rede_ensino_texto = ["Pública",
                                                    "Particular"]
        self.rede_ensino_media = sum(self.rede_ensino_valores) / len(self.rede_ensino_valores)
        self.rede_ensino_distrib = [x / sum(self.rede_ensino_valores) for x in self.rede_ensino_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.rede_ensino_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        rede_ensino_individuo = [0] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                rede_ensino_individuo[k] = self.rede_ensino_texto[j]
                k += 1
        
        #//rede_ensino
        
        
        #Gera a população
        self.individuos = [Pessoa(renda_individuo[x], rede_ensino_individuo[x]) for x in range(self.tamanho)]


    def amostra(self, n):
        return rnd.sample(self.individuos, n)


pop = Populacao(10)
print(pop.individuos[1].rede_ensino)
