import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entidades.planta import get_plantas, set_plantas
from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from entidades.botânico import get_botânicos, set_botânicos
from entidades.região import get_regiões, set_regiões
from entidades.avaliação_toxicidade import get_avaliações_toxicidade, set_avaliações_toxicidade
from interfaces.interface_textual import loop_opções_execução
nome_arquivo = 'avaliação_toxicidade_plantas'

def salvar_aplicação():
    avaliação_toxicidade_plantas= []
    avaliação_toxicidade_plantas.append(get_botânicos())
    avaliação_toxicidade_plantas.append(get_plantas())
    avaliação_toxicidade_plantas.append(get_regiões())
    avaliação_toxicidade_plantas.append(get_avaliações_toxicidade())
    salvar_arquivo(nome_arquivo, objetos= avaliação_toxicidade_plantas)

def recuperar_aplicação():
    avaliação_toxicidade_plantas = carregar_arquivo(nome_arquivo)
    if avaliação_toxicidade_plantas is not None:
        set_botânicos(avaliação_toxicidade_plantas[0])
        set_plantas(avaliação_toxicidade_plantas[1])
        set_regiões(avaliação_toxicidade_plantas[2])
        set_avaliações_toxicidade(avaliação_toxicidade_plantas[3])

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()