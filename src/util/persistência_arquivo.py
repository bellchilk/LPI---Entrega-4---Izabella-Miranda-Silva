import pickle


def salvar_arquivo(nome_arquivo, objetos):
    with open(nome_arquivo, 'wb') as arquivo:
        pickle.dump(objetos, arquivo)

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            return pickle.load(arquivo)
    except (IOError, pickle.PickleError):
        return None