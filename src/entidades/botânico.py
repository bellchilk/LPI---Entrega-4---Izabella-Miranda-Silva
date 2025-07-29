
botânicos = {}

def get_botânicos(): return botânicos

def inserir_botânico(botânico):
    nome_botânico = botânico.nome
    if nome_botânico not in botânicos.keys():
        botânicos[nome_botânico] = botânico
        return True
    else:
        print('Botânico' + nome_botânico + 'já tem cadastro')
        return False

def set_botânicos(botânicos1):
    global botânicos
    botânicos = botânicos1

class Botânico:

    def __init__(self,nome,especialidade,titulação, anos_experiência):
        self.nome = nome
        self.especialidade = especialidade if especialidade in ('taxonomia vegetal', 'fisiologia vegetal', 'botânica econômica') else 'indefinida'
        self.titulação = titulação if titulação in ('graduação', 'especialização', 'mestrado', 'doutorado') else 'indefinida'
        self.anos_experiência = anos_experiência

    def __str__(self):
        formato = '{} {:<21} {} {:<19} {} {:<10} {} {:<8} {}'
        botânico_formatado = formato.format('|',self.nome, '|',self.especialidade,'|',self.titulação, '|', str(self.anos_experiência) + ' anos', '|')
        return botânico_formatado