plantas = {}

def get_plantas(): return plantas

def inserir_planta(planta):
    nome_planta = planta.nome
    if nome_planta not in plantas.keys():
        plantas[nome_planta] = planta
        return True
    else:
        print('Planta' + nome_planta + 'já tem cadastro na Região')
        return False
    
def set_plantas(plantas1):
    global plantas
    plantas = plantas1

class Planta:

    def __init__(self,nome,toxicidade, origem):
        self.nome = nome
        self.toxicidade  = toxicidade if toxicidade in ('não tóxica','baixa', 'moderada', 'alta') else 'indefinida'
        self.origem = origem

    def __str__(self):
        formato = '{} {:<25} {} {:<11} {} {:<17} {}'
        planta_formatado = formato.format('|',self.nome,'|' ,self.toxicidade, '|', self.origem, '|')
        return planta_formatado

class PlantaMedicinal(Planta):
    def __init__(self,nome,toxicidade, origem, parte_utilizada, propriedade_terapeutica):
        super().__init__(nome, toxicidade, origem)
        self.parte_utilizada =  parte_utilizada if parte_utilizada in ('folhas', 'raízes', 'flores') else 'indefinida'
        self.propriedade_terapeutica = propriedade_terapeutica if propriedade_terapeutica in ('anti-inflamatória', 'analgésica', 'digestiva') else 'indefinida'

    def __str__(self):
        formato = '{} {:<25} {} {:<11} {} {:<17} {} {:<12} {} {:<18} {}'
        planta_medicinal_formatado = formato.format('|',  self.nome,'|', self.toxicidade, '|', self.origem, '|', self.parte_utilizada, '|', self.propriedade_terapeutica, '|')
        return planta_medicinal_formatado

class PlantaTóxica(Planta):
    def __init__(self,nome, toxicidade, origem, composto_tóxico, efeito_colateral):
        super().__init__(nome, toxicidade, origem)
        self.composto_tóxico = composto_tóxico if composto_tóxico in ('alcalóides', 'glicosídeos', 'saponinas') else 'indefinida'
        self.efeito_colateral = efeito_colateral if efeito_colateral in ( 'náusea', 'paralisia', 'alucinação') else 'indefinida'

    def __str__(self):
        formato = '{} {:<25} {} {:<11} {} {:<17} {} {:<12} {} {:<18} {}'
        planta_toxica_formatado = formato.format('|', self.nome,'|' , self.toxicidade,'|', self.origem,'|', self.composto_tóxico, '|', self.efeito_colateral, '|')
        return planta_toxica_formatado