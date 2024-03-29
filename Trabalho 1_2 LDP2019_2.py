import numpy as np
import random as rnd

class Pessoa:
    def __init__(self, rendimento_mensal_domiciliar, rede_ensino, modalidade,sexo,cor,regiao,idade):
        self.rendimento_mensal_domiciliar = rendimento_mensal_domiciliar
        self.rede_ensino = rede_ensino
        self.modalidade = modalidade
        self.sexo = sexo
        self.cor = cor
        self.regiao = regiao
        self.idade = idade

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


        #modalidade//

        #Estabelece os valores e distribuição dessa categoria pelos dados da PNAD
        self.modalidade_valores = [392.0, 85.0]
        self.modalidade_texto = ["Presencial",
                                                    "À Distância"]
        self.modalidade_media = sum(self.modalidade_valores) / len(self.modalidade_valores)
        self.modalidade_distrib = [x / sum(self.modalidade_valores) for x in self.modalidade_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.modalidade_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        modalidade_individuo = [0] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                modalidade_individuo[k] = self.modalidade_texto[j]
                k += 1
        
        #//modalidade
        
                
                #sexo//

        #Estabelece os valores e distribuição dessa categoria pelos dados da PNAD
        self.sexo_valores = [3118.0, 4170.0]
        self.sexo_texto = ['Mulheres','Homens']
        self.sexo_media = sum(self.sexo_valores) / len(self.sexo_valores)
        self.sexo_distrib = [x / sum(self.sexo_valores) for x in self.sexo_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.sexo_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        sexo_individuo = [0] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                sexo_individuo[k] = self.sexo_texto[j]
                k += 1
        
        #//sexo
                
        #cor//

      #Estabelece os valores e distribuição dessa categoria pelos dados da PNAD
        self.cor_valores = [4154.0,3071.0]
        self.cor_texto = ['Branca','Preta ou parda']
        self.cor_media = sum(self.cor_valores) / len(self.cor_valores)
        self.cor_distrib = [x / sum(self.cor_valores) for x in self.cor_valores]

        #Gera uma população numérica tomando a ditribuição dos valores da PNAD
        gerador = list(np.random.multinomial(self.tamanho, self.cor_distrib))
        
        #Categoriza essa população: de número para a categoria em texto
        cor_individuo = [0] * self.tamanho
        k = 0
        for j in range(len(gerador)):
            for i in range(gerador[j]):
                cor_individuo[k] = self.cor_texto[j]
                k += 1
        
        #//cor

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
        self.individuos = [Pessoa(renda_individuo[x], rede_ensino_individuo[x], modalidade_individuo[x], sexo_individuo[x], cor_individuo[x],regiao_individuo[x],dificuldade_individuo[x]) for x in range(self.tamanho)]


    def amostra(self, n):
        return rnd.sample(self.individuos, n)

pop=Populacao(100)
print(pop.individuos[0].regiao)
