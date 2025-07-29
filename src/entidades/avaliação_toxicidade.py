from entidades.botânico import get_botânicos
from entidades.planta import PlantaMedicinal, PlantaTóxica
from entidades.região import  get_regiões


avaliações_toxicidade = []

def get_avaliações_toxicidade(): return avaliações_toxicidade

def inserir_avaliação_toxicidade(avaliação_toxicidade):
    if avaliação_toxicidade not in avaliações_toxicidade: avaliações_toxicidade.append(avaliação_toxicidade)
    else:
        print('Avaliação de Toxicidade já tem cadastro ---' + str(avaliação_toxicidade))

def criar_avaliação_toxicidade(ecossistema_região, nome_botânico,  n_plantas_alta_toxicidade, n_plantas_baixa_toxicidade):
    região = get_regiões()[ecossistema_região]
    if região is None:
        print('Região' + ecossistema_região + 'não cadastrada')
        return
    botânico = get_botânicos()[nome_botânico]
    if botânico is None:
        print('Botânico' + nome_botânico + 'não cadastrado')
        return
    avaliação_toxicidade = AvaliaçãoToxicidade(região, botânico, n_plantas_alta_toxicidade, n_plantas_baixa_toxicidade)
    return avaliação_toxicidade

def filtrar_avaliações_toxicidade(n_mínimo_alta_toxicidade = None,frequencia_máxima_acidentes_por_ano_região = None,especialidade_botânico = None,
                                     origem_planta = None, parte_utilizada_planta_medicinal = None, composto_tóxico_planta_tóxica= None ):
    avaliações_toxicidade_selecionadas = []
    for avaliação_toxicidade in avaliações_toxicidade:
        if n_mínimo_alta_toxicidade is not None and avaliação_toxicidade.n_plantas_alta_toxicidade < n_mínimo_alta_toxicidade: continue
        if frequencia_máxima_acidentes_por_ano_região is not None and avaliação_toxicidade.região.frequencia_acidentes_por_ano > frequencia_máxima_acidentes_por_ano_região: continue
        if especialidade_botânico is not None and avaliação_toxicidade.botânico.especialidade != especialidade_botânico: continue
        excluir_avaliação_toxicidade = False
        for planta in avaliação_toxicidade.região.plantas.values():
            if origem_planta is not None and planta.origem != origem_planta:
                excluir_avaliação_toxicidade = True
                break

            if isinstance(planta, PlantaMedicinal):
                if parte_utilizada_planta_medicinal is not None and planta.parte_utilizada != parte_utilizada_planta_medicinal:
                    excluir_avaliação_toxicidade = True
                    break
            elif isinstance(planta, PlantaTóxica):
                if composto_tóxico_planta_tóxica is not None and planta.composto_tóxico != composto_tóxico_planta_tóxica:
                    excluir_avaliação_toxicidade = True
                    break
        if excluir_avaliação_toxicidade: continue
        avaliações_toxicidade_selecionadas.append(avaliação_toxicidade)
    return avaliações_toxicidade_selecionadas

def set_avaliações_toxicidade(avaliações_toxicidade1):
    global avaliações_toxicidade
    avaliações_toxicidade = avaliações_toxicidade1

class AvaliaçãoToxicidade:

    def __init__(self, região, botânico, n_plantas_alta_toxicidade, n_plantas_baixa_toxicidade):
        self.região = região
        self.botânico = botânico
        self.n_plantas_alta_toxicidade = n_plantas_alta_toxicidade
        self.n_plantas_baixa_toxicidade = n_plantas_baixa_toxicidade

    def __str__(self):
        formato = '{} {:<19} {} {:<21} {} {:<4} {} {:<4} {}'
        avaliação_toxicidade_formato = formato.format('|', self.região.ecossistema, '|', self.botânico.nome, '|', str(self.n_plantas_alta_toxicidade), '|', str(self.n_plantas_baixa_toxicidade), '|')
        return avaliação_toxicidade_formato

    def str_atributos_plantas(self):
        atributos_plantas_str = ''
        for índice, planta in enumerate(self.região.plantas.values()):
            if(índice > 0): atributos_plantas_str += ' -- '
            atributos_plantas_str += planta.origem + ' - '
            if isinstance(planta, PlantaMedicinal): atributos_plantas_str += planta.parte_utilizada
            elif isinstance(planta, PlantaTóxica): atributos_plantas_str += planta.composto_tóxico
        return atributos_plantas_str

    def str_filtro(self):
        formato = '{:>3} {} {:<19} {} {:<122} {}'
        filtro_formatado = formato.format( self.região.frequencia_acidentes_por_ano, '|',self.botânico.especialidade, '|',str(self.str_atributos_plantas()), '|')
        return self.__str__() + filtro_formatado