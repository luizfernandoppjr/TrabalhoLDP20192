class Populacao:
    def __init__(self, tamanho):
        self.tamanho = tamanho

        self.rendimento_mensal_domiciliar_valores = [472, 1442, 2551, 1176, 745, 496, 360]
        self.rendimento_mensal_domiciliar_distrib = [x / sum(self.rendimento_mensal_domiciliar_valores) for x in self.rendimento_mensal_domiciliar_valores]

        self.individuos = [Pessoa(np.random.multinomial(self.tamanho, self.rendimento_mensal_domiciliar_distrib)) for i in range(tamanho)]


    def amostra(self, n):
        return rnd.sample(self.individuos, n)


pop = Populacao(100)
print(pop.amostra(10))