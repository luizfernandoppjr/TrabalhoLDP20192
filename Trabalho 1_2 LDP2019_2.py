import numpy as np
import random as rnd

class Pessoa(object):
    def __init__(self,regiao,dificuldade):#(rendimento_mensal_domiciliar, rede_ensino, modalidade,sexo, cor):
        self.regiao = regiao
        self.dificuldade = dificuldade
        #self.sexo = sexo
        #self.cor = cor
        #self.rendimento_mensal_domiciliar = rendimento_mensal_domiciliar
        #self.rede_ensino = rede_ensino
        #self.modalidade = modalidade

class Populacao(object):
    def __init__(self, tamanho):
        self.tamanho = tamanho

        #regiao//

        #Mostra a região e distribuição dessa categoria pelos dados da PNAD
        self.regiao_valores = [4350.00,4050.00,5783.00,5580.00,5642.00]
        self.regiao_texto = ["Norte","Nordeste","Sudeste","Sul","Centro-Oeste"]
        self.regiao_media = sum(self.regiao_valores) / len(self.regiao_valores)
        self.regiao_distrib = [x / sum(self.regiao_valores) for x in self.regiao_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.regiao_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        regiao_individuo = [1] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                regiao_individuo[k] = self.regiao_texto[j]
                k += 1
                
        #//regiao


        #dificuldade//

        #Explicita a dificuldade e a distribuição dessa categoria pelos dados da PNAD
        self.dificuldade_valores = [27.00,25.00,24.00,15.00,6.00]
        self.dificuldade_texto = ["Dificuldade financeira","Dificuldade de acesso ao local do curso","Dificuldade de cumprir o horário do curso","Outra","Falta de tempo para estudar"]
        self.dificuldade_media = sum(self.dificuldade_valores) / len(self.dificuldade_valores)
        self.dificuldade_distrib = [x / sum(self.dificuldade_valores) for x in self.dificuldade_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.dificuldade_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        dificuldade_individuo = [1] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                dificuldade_individuo[k] = self.dificuldade_texto[j]
                k += 1
        
        #//dificuldade
        
        
        #Gera a população
        self.individuos = [Pessoa(regiao_individuo[x],dificuldade_individuo[x]) for x in range(self.tamanho)]


    def amostra(self, n):
        return rnd.sample(self.individuos, n)

pop=Populacao(100)
print(pop.individuos[0].regiao)
