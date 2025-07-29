import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entidades.planta import get_plantas, set_plantas
from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from entidades.botânico import get_botânicos, set_botânicos
from entidades.região import get_regiões, set_regiões
from entidades.avaliação_toxicidade import get_avaliações_toxicidade, set_avaliações_toxicidade
from interfaces.interface_textual import loop_opções_execução
nome_arquivo = os.path.join(os.path.dirname(__file__), '..', '..', 'dados', 'avaliação_toxicidade_plantas.bin')

def salvar_aplicação():
    avaliação_toxicidade_plantas= []
    avaliação_toxicidade_plantas.append(get_botânicos())
    avaliação_toxicidade_plantas.append(get_plantas())
    avaliação_toxicidade_plantas.append(get_regiões())
    avaliação_toxicidade_plantas.append(get_avaliações_toxicidade())
    salvar_arquivo(nome_arquivo, objetos= avaliação_toxicidade_plantas)

def recuperar_aplicação():
    print(f"Tentando carregar arquivo de: {nome_arquivo}")
    dados = carregar_arquivo(nome_arquivo)
    
    if dados is None or len(dados) != 4:
        print("Arquivo inválido ou vazio - iniciando com estruturas vazias")
        set_botânicos({})
        set_plantas({})
        set_regiões({})
        set_avaliações_toxicidade([])
        return
    
    if dados[0]: set_botânicos(dados[0])
    if dados[1]: set_plantas(dados[1])
    if dados[2]: set_regiões(dados[2])
    if dados[3]: set_avaliações_toxicidade(dados[3])
    

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()