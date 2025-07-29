# 🌿 Avaliação de Regiões com Plantas Tóxicas

Projeto acadêmico da disciplina **Linguagem e Programação I**  
Desenvolvido por **Izabella Miranda Silva**.

## 📌 Descrição

Sistema de gerenciamento para avaliação de regiões com plantas tóxicas e medicinais, permitindo:

- Cadastro de botânicos, plantas e regiões
- Associação de plantas às regiões
- Avaliações de toxicidade com diversos critérios
- Filtros avançados para análise dos dados
- Persistência dos dados entre execuções

## 🚀 Como executar

1. Certifique-se de ter o **Python 3.x** instalado
2. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/avaliacao-regioes-plantas-toxicas.git
```
3. Execute o programa principal:
```bash
python src/controle/avaliação_região_plantas_tóxicas.py
```

## 🧩 Estrutura do Projeto

### Principais Entidades
- **Planta**
  - Atributos: `nome`, `toxicidade`, `origem`
  - Subtipos:
    - `PlantaMedicinal`: `parte_utilizada`, `propriedade_terapeutica`
    - `PlantaTóxica`: `composto_tóxico`, `efeito_colateral`

- **Botânico**: `nome`, `especialidade`, `titulação`, `anos_experiência`
- **Região**: `ecossistema`, `uf`, `frequencia_acidentes_por_ano`, `época_risco`
- **AvaliaçãoToxicidade**: Associação entre região e botânico com contagem de plantas tóxicas

## 🛠️ Tecnologias utilizadas

![Python badge](https://img.shields.io/badge/-PYTHON-blue?style=for-the-badge&logo=python&logoColor=yellow)

- Python 3.x
- Biblioteca pickle para persistência
- Programação Orientada a Objetos


## ✨ Autoria

Desenvolvido por **Izabella Miranda Silva**  
📅 Entrega 4 — Linguagem e Programação I  
📍 Dourados – 17/06/2025
