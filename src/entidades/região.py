from entidades.planta import get_plantas

regiões = {}

def get_regiões(): return regiões

def inserir_região(região):
    ecossistema_região = região.ecossistema
    if ecossistema_região not in regiões.keys():
        regiões[ecossistema_região] = região
        return True
    else:
        print('Região' + ecossistema_região + 'já tem cadastro')
        return False

def set_regiões(regiões1):
    global regiões
    regiões = regiões1

class Região:

    def __init__(self, ecossistema, uf, frequencia_acidentes_por_ano, época_risco):
        self.ecossistema = ecossistema
        self.uf = uf
        self.frequencia_acidentes_por_ano = frequencia_acidentes_por_ano
        self.época_risco = época_risco if época_risco in  ('verão', 'primavera', 'outono', 'inverno') else 'indefinida'
        self.plantas = {}

    def __str__(self):
        formato = '{} {:<19} {} {:<3} {} {:<3} {} {:<10} {}'
        região_formatada = formato.format('|', self.ecossistema, '|',self.uf,'|',str(self.frequencia_acidentes_por_ano),'|', self.época_risco, '|')
        return região_formatada

    def inserir_plantas(self,nomes_plantas):
        for nome_planta in nomes_plantas:
            if nome_planta in get_plantas().keys():
                self.plantas[nome_planta] = get_plantas()[nome_planta]
            else:
                print('Planta ' + nome_planta + ' não tem cadastro')