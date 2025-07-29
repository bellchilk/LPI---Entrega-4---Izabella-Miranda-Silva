from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from entidades.região import Região, inserir_região, get_regiões

from entidades.botânico import Botânico, inserir_botânico, get_botânicos
from entidades.planta import PlantaMedicinal, PlantaTóxica, get_plantas, inserir_planta
from entidades.avaliação_toxicidade import get_avaliações_toxicidade, criar_avaliação_toxicidade, \
    inserir_avaliação_toxicidade, filtrar_avaliações_toxicidade


def loop_opções_execução():
    sair_loop = False
    cabeçalho_botânico = '\nBotânicos: nome - especialidade - titulação - anos de experiência'
    cabeçalho_planta = '\nPlantas: nome - toxicidade - origem\n- planta medicinal:[parte_utilizada - propriedade_terapeutica] | planta tóxica:[composto_tóxico - efeito_colateral]'
    cabeçalho_região_plantas = ('\nRegiões: ecossistema - uf - frequencia de acidentes por ano - época de risco'
    + '\n - Plantas:  nome - toxicidade - origem\n- planta medicinal:[parte_utilizada - propriedade_terapeutica] | planta tóxica:[composto_tóxico - efeito_colateral]')
    cabeçalho_avaliação_toxicidade = '\nAvaliações de Toxicidade:  região - botânico - número de plantas de alta toxicidade - número de plantas de baixa toxicidade'

    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]', retornar = True)
        if operação == None: break
        elif operação in ('C', 'I'):
            opção_conteúdo = ler_str('[B: Botânicos/ P: Plantas / R: Regiões / A: Avaliações de Toxicidade / <ENTER>: retornar]', retornar = True)
            if opção_conteúdo == None: pass
            elif opção_conteúdo == 'B':
                if operação == 'C': loop_leitura_botânicos()
                imprimir_objetos(cabeçalho_botânico, get_botânicos().values())
            elif opção_conteúdo == 'P':
                if operação == 'C': loop_leitura_plantas()
                imprimir_objetos(cabeçalho_planta, get_plantas().values())
            elif opção_conteúdo in 'R':
                if operação == 'C': loop_leitura_regiões()
                imprimir_regiões_plantas(cabeçalho_região_plantas)
            elif opção_conteúdo == 'A':
                if operação == 'C': loop_leitura_avaliações_toxicidade()
                imprimir_objetos(cabeçalho_avaliação_toxicidade, get_avaliações_toxicidade())
        elif operação == 'S': loop_seleção_avaliações_toxicidade()
        elif operação == 'T':
            imprimir_objetos(cabeçalho_botânico, get_botânicos().values())
            imprimir_objetos(cabeçalho_planta, get_plantas().values())
            imprimir_regiões_plantas(cabeçalho_região_plantas)
            imprimir_objetos(cabeçalho_avaliação_toxicidade, get_avaliações_toxicidade())

def imprimir_regiões_plantas(cabeçalho_região_plantas):
    print(cabeçalho_região_plantas)
    for índice, região in enumerate(get_regiões().values()):
        imprimir_objeto(índice= índice, objeto_str= str(região))
        imprimir_objetos_internos(região.plantas.values())

def loop_leitura_botânicos():
    sair_loop = False
    print('--- Leitura de Dados dos Botânicos ---')
    while not sair_loop:
        botânico = ler_botânico()
        if botânico is not None:
            inserir_botânico(botânico)
        else: print(' -ERRO: na leitura do botânico')
        sair_loop = ler_sair_loop('cadastro dos botânicos')

def loop_leitura_plantas():
    sair_loop = False
    print('--- Leitura de Dados dos Plantas ---')
    while not sair_loop:
        planta = ler_planta()
        if planta is not None:
            inserir_planta(planta)
        else: print(' -ERRO: na leitura do planta')
        sair_loop = ler_sair_loop('cadastro dos planta')

def loop_leitura_regiões():
    sair_loop = False
    print('--- Leitura de Dados das Regiões ---')
    while not sair_loop:
        região = ler_região()
        if região is not None:
            inserir_região(região)
            loop_leitura_plantas_região(região)
        else: print(' -ERRO: na leitura da região')
        sair_loop = ler_sair_loop('cadasto de regiões')

def loop_leitura_plantas_região(região):
    chave_plantas = ler_str('Nomes das plantas da região').split(',')
    if chave_plantas is not None:
        região.inserir_plantas(chave_plantas)
    else: print(' -ERRO: na leitura do planta da região')

def loop_leitura_avaliações_toxicidade():
    sair_loop = False
    print('--- Leitura de Dados de Avaliações de Toxicidade ---')
    while not sair_loop:
        avaliação_toxicidade = ler_avaliação_toxicidade()
        if avaliação_toxicidade is not None:
            inserir_avaliação_toxicidade(avaliação_toxicidade)
        else:
            print(' - ERRO : na leitura de avaliação da toxicidade')
        sair_loop = ler_sair_loop('cadastro de avaliação de toxicidade')

def ler_sair_loop(loop):
    try:
        sair = input('-- sair do loop de' + loop + '[S]:')
        if sair == 'S': return True
    except IOError: pass
    return False

def loop_seleção_avaliações_toxicidade():
    sair_loop = False
    print('--- Seleção de Avaliações de Toxicidade ---')
    while not sair_loop:
        filtros, avaliações_toxicidade_selecionadas  = selecionar_avaliações_toxicidade()
        if filtros is not None:
            cabeçalho = ('\nAvaliação de Toxicidade: região - botânico - número de plantas de alta toxicidade - número de plantas de baixa toxicidade'
                 + '\n -- Frequência máxima de acidentes por ano na região -  especialidade do botânico'
                 + '\n - plantas: [origem da planta - parte utilizada] | composto_tóxico]')
            imprimir_objetos_associação_filtros(cabeçalho, avaliações_toxicidade_selecionadas, filtros)
        sair_loop = ler_sair_loop('seleção de avaliações de toxicidade')

def ler_botânico():
    nome = ler_str('nome do botânico')
    if nome == None: return None
    especialidade = ler_especialidade_botânico()
    if especialidade == None: return None
    titulação = ler_titulação_botânico()
    if titulação == None: return None
    anos_experiência = ler_int_positivo('anos de experiência do botânico')
    if anos_experiência == None: return None
    return Botânico(nome, especialidade, titulação, anos_experiência)

def ler_região():
    ecossistema = ler_str('ecossistema da região')
    if ecossistema == None: return None
    uf = ler_uf_região()
    if uf == None: return None
    frequencia_acidentes_por_ano = ler_int_positivo('frequencia de acidentes por ano na região')
    if frequencia_acidentes_por_ano == None: return None
    época_risco = ler_época_risco_região()
    if época_risco == None: return None
    return Região(ecossistema, uf, frequencia_acidentes_por_ano, época_risco)

def ler_planta():
    nome = ler_str('nome do planta')
    if nome == None: return None
    toxicidade = ler_toxicidade_planta()
    if toxicidade == None: return None
    origem = ler_origem_planta()
    if origem == None: return None
    tipo_planta = ler_str('tipo planta [PM = Planta Medicibal/ PT = Planta Tóxica]')
    if tipo_planta == 'PM':
        parte_utilizada = ler_parte_utilizada()
        if parte_utilizada == None: return None
        propriedade_terapeutica = ler_propriedade_terapeutica()
        if propriedade_terapeutica == None: return None
        return PlantaMedicinal(nome, toxicidade, origem, parte_utilizada, propriedade_terapeutica)
    if tipo_planta == 'PT':
        composto_tóxico = ler_composto_tóxico()
        if composto_tóxico == None: return None
        efeito_colateral  = ler_efeito_colateral()
        if efeito_colateral == None: return None
        return PlantaTóxica(nome, toxicidade, origem, composto_tóxico, efeito_colateral)
    else: return None

def ler_avaliação_toxicidade():
    ecossistema_região = ler_str('ecossistema da região')
    if ecossistema_região == None: return None
    nome_botânico = ler_str('nome do botãnico')
    if nome_botânico == None: return None
    n_plantas_alta_toxicidade = ler_int_positivo('número de plantas com alta toxicidade da avaliação de toxicidade')
    if n_plantas_alta_toxicidade is None: return None
    n_plantas_baixa_toxicidade = ler_int_positivo('número de plantas com baixa toxicidade da avaliação de toxicidade')
    if n_plantas_baixa_toxicidade == None: return None
    return criar_avaliação_toxicidade(ecossistema_região, nome_botânico, n_plantas_alta_toxicidade, n_plantas_baixa_toxicidade)

def selecionar_avaliações_toxicidade():
    filtros = '\nFiltros --'
    n_mínimo_alta_toxicidade = ler_int_positivo('número mínimo de alta toxicidade', filtro = True)
    if n_mínimo_alta_toxicidade is not None: filtros += 'número mínimo de alta toxicidade: ' + str(n_mínimo_alta_toxicidade)
    frequencia_máxima_acidentes_por_ano_região = ler_int_positivo('frequência máxima de acidentes por ano na região', filtro = True)
    if frequencia_máxima_acidentes_por_ano_região is not None: filtros += '\n -frequência máxima de acidentes por ano na região: ' + str(frequencia_máxima_acidentes_por_ano_região)
    especialidade_botânico = ler_str('especialidade do botânico', filtro = True)
    if especialidade_botânico is not None: filtros += ' -especialidade do botânico: ' + str(especialidade_botânico)
    origem_planta = ler_str('origem da planta', filtro = True)
    if origem_planta is not None: filtros += '\n -origem da planta: ' + str(origem_planta)
    parte_utilizada_planta_medicinal = ler_str('parte utilizada da planta', filtro = True)
    if parte_utilizada_planta_medicinal is not None: filtros += ' -parte utilizada da planta medicinal: ' + str(parte_utilizada_planta_medicinal)
    composto_tóxico_planta_tóxica = ler_str('composto tóxico da planta tóxica', filtro = True)
    if composto_tóxico_planta_tóxica is not None: filtros += ' -composto tóxico da planta tóxica: ' + str(composto_tóxico_planta_tóxica)
    avaliações_toxicidade_selecionadas = filtrar_avaliações_toxicidade(n_mínimo_alta_toxicidade,frequencia_máxima_acidentes_por_ano_região,especialidade_botânico,
                                                                       origem_planta, parte_utilizada_planta_medicinal, composto_tóxico_planta_tóxica )
    return filtros, avaliações_toxicidade_selecionadas

def ler_str(dado, filtro= False, retornar= False):
    try:
        string = input('- ' + dado + ':')
        if len(string) == 0 and (filtro or retornar): return None
        if len(string) > 0: return string
    except IOError: pass
    print('Erro na leitura do dado:', + dado)
    return None

def ler_int_positivo(dado, filtro= False):
    try:
        string = input('- ' + dado + ':')
        if len(string) == 0 and filtro: return None
        int_positivo = int(string)
        if int_positivo > 0: return int_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do inteiro positivo:', + dado)
    return None

def ler_toxicidade_planta(filtro= False):
    try:
        string = input(' -toxicidade [N= não tóxica / B= baixa / M= moderada / A= alta]:')
        if len(string) == 0 and filtro: return None
        if string == 'N':return 'não tóxica'
        if string == 'B': return 'baixa'
        if string == 'M': return 'moderada'
        if string == 'A': return 'alta'
    except IOError: pass
    print('Erro na leitura da toxicidade da planta')
    return None

def ler_origem_planta(filtro= False):
    try:
        string = input(' -origem [E= Europa / A= África / S= Ásia / M= América do Sul / N= América do Norte]:')
        if len(string) == 0 and filtro: return None
        if string == 'E':return 'Europa'
        if string == 'A': return 'África'
        if string == 'S': return 'Ásia'
        if string == 'M': return 'América do Sul'
        if string == 'N': return 'América do Norte'
    except IOError: pass
    print('Erro na leitura da origem da planta')
    return None


def ler_parte_utilizada(filtro=False):
    try:
        string = input('-parte utilizada [F= folhas / R= raízes / L= flores]:')
        if len(string) == 0 and filtro: return None
        if string == 'F': return 'folhas'
        if string == 'R': return 'raízes'
        if string == 'L': return 'flores'
    except IOError: pass
    print('Erro na leitura da parte utilizada da planta medicinal')
    return None

def ler_propriedade_terapeutica(filtro=False):
    try:
        string = input('-propriedade terapeutica [A= anti-inflamatória / N= analgésica / D= digestiva]:')
        if len(string) == 0 and filtro: return None
        if string == 'A': return 'anti-inflamatória'
        if string == 'N': return 'analgésica'
        if string == 'D': return 'digestiva'
    except IOError: pass
    print('Erro na leitura da propiedade terapeutica da planta medicinal')
    return None

def ler_composto_tóxico(filtro=False):
    try:
        string = input('-composto tóxico [A= alcalóides / G= glicosídeos / S= saponinas]:')
        if len(string) == 0 and filtro: return None
        if string == 'A': return 'alcalóides'
        if string == 'G': return 'glicosídeos'
        if string == 'S': return 'saponinas'
    except IOError: pass
    print('Erro na leitura do composto tóxico da planta tóxica')
    return None

def ler_efeito_colateral(filtro=False):
    try:
        string = input('-efeito colateral [M = náusea / P= paralisia / U= alucinação]:')
        if len(string) == 0 and filtro: return None
        if string == 'M': return 'náusea'
        if string == 'P': return 'paralisia'
        if string == 'U': return 'alucinação'
    except IOError: pass
    print('Erro na leitura do efeito colateral da planta tóxica')
    return None

def ler_especialidade_botânico(filtro=False):
    try:
        string = input('-epecialidade [T = taxonomia vegetal / F= fisiologia vegetal / B= botânica econômica]:')
        if len(string) == 0 and filtro: return None
        if string == 'T': return 'taxonomia vegetal'
        if string == 'F': return 'fisiologia vegetal'
        if string == 'B': return 'botânica econômica'
    except IOError: pass
    print('Erro na leitura da especialidade do botânico')
    return None

def ler_titulação_botânico(filtro=False):
    try:
        string = input('-titulação [G = graduação / E= especialização / M= mestrado / D = doutorado]:')
        if len(string) == 0 and filtro: return None
        if string == 'G': return 'graduação'
        if string == 'E': return 'especialização'
        if string == 'M': return 'mestrado'
        if string == 'D': return 'doutorado'
    except IOError: pass
    print('Erro na leitura da titulação do botânico')
    return None

def ler_época_risco_região(filtro=False):
    try:
        string = input('-época de risco [V = verão / P= primavera / O= outono / I = inverno]:')
        if len(string) == 0 and filtro: return None
        if string == 'V': return 'verão'
        if string == 'P': return 'primavera'
        if string == 'O': return 'outono'
        if string == 'I': return 'inverno'
    except IOError: pass
    print('Erro na leitura da época de risco da região')
    return None

def ler_uf_região(filtro=False):
    try:
        string = input('-uf [M= MS  / S= SP / A= AM / G = GO / B= BA]:')
        if len(string) == 0 and filtro: return None
        if string == 'M': return 'MS'
        if string == 'S': return 'SP'
        if string == 'A': return 'AM'
        if string == 'G': return 'GO'
        if string == 'B': return 'BA'
    except IOError: pass
    print('Erro na leitura da uf da região')
    return None

