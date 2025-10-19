# App de Controle de Gastos (CLI)

Um aplicativo de linha de comando simples para cadastrar despesas, listá-las e gerar um relatório final comparando o total com um **orçamento máximo** configurável.

> Feito para estudos iniciais de Python, com foco em estruturas básicas (listas, dicionários, funções) e controle de fluxo (`if/else`, `match/case`).

---

## ✨ Funcionalidades

- **Cadastrar despesa**: informa nome e valor; o app guarda como um dicionário dentro de uma lista.
- **Listar despesas**: exibe cada despesa já cadastrada.
- **Relatório final**: soma todas as despesas e informa se o total **ultrapassa** ou **não** o orçamento máximo.
- **Sair**: encerra a aplicação.

---

## 🧱 Requisitos

- **Python 3.10+** (o código usa `match/case`).
- Sistema operacional: Windows, macOS ou Linux.

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado (3.10 ou superior).
2. Baixe/clonar este repositório e salve o arquivo `app.py` na pasta do projeto.
3. No terminal, rode:

```bash
# Windows (PowerShell ou CMD)
python app.py

# macOS / Linux
python3 app.py
```

---

## 🧩 Estrutura e principais conceitos

- **Lista de despesas**: `despesas = []`
  - Cada item é um **dicionário** com as chaves:
    - `nome` (str): nome da despesa (ex.: "Internet")
    - `valor` (float): valor da despesa (ex.: 99.90)

- **Orçamento máximo**:
  - Constante no topo do arquivo: `orcamento_maximo = 3000.00`
  - Usado no relatório para comparar com o **total gasto**.

- **Menu principal**
  - Mostra 4 opções (cadastrar, listar, relatório, sair).
  - A navegação acontece por funções dedicadas para cada ação.

---

## 🖥️ Fluxo da aplicação

1. **`main()`** limpa a tela, mostra o menu e chama **`escolher_opcao()`**.
2. **`escolher_opcao()`** lê a escolha do usuário e usa `match/case` para direcionar:
   - `1` → **`cadastrar_despesas()`**
   - `2` → **`listar_despesas()`**
   - `3` → **`relatorio_final()`**
   - `4` → **`finalizar_app()`**
3. Após executar cada ação, a aplicação retorna ao menu (ou finaliza, no caso da opção 4).

---

## 🧪 Exemplo de uso

```
1. Cadastrar despesa
2. Listar despesas
3. Relatório final
4. Sair
Escolha uma opção: 1
Nome da despesa: Internet
Valor da despesa: 99.90
Internet foi cadastrada com sucesso!

Digite uma tecla para voltar ao menu principal: 

1. Cadastrar despesa
2. Listar despesas
3. Relatório final
4. Sair
Escolha uma opção: 2
- Internet             | 99.9

Digite uma tecla para voltar ao menu principal:

1. Cadastrar despesa
2. Listar despesas
3. Relatório final
4. Sair
Escolha uma opção: 3
Parabéns! Seus gastos foram R$ 99.9 e ficaram dentro do orçamento máximo de R$ 3000.0
Encerrando o programa...
```

> Dica: você pode melhorar a apresentação de valores monetários usando `f'R$ {valor:,.2f}'` (com atenção à formatação regional).

---

## 🛡️ Tratamento de erros (básico)

- Entradas não numéricas para **valor** geram `ValueError` ao converter para `float`.
- Entradas não numéricas para **opção do menu** são tratadas no `try/except` de `escolher_opcao()`.
- Lista vazia em **listar** mostra uma mensagem amigável ao usuário.

---

## 🧭 Organização das funções

- `exibir_menu()`: mostra as opções.
- `cadastrar_despesas()`: lê e adiciona uma despesa à lista.
- `listar_despesas()`: percorre a lista e imprime despesas.
- `relatorio_final()`: soma e compara com `orcamento_maximo`.
- `voltar_ao_menu_principal()`: pausa e volta ao menu.
- `limpar_tela()`: limpa o terminal de forma compatível (Windows/Linux/macOS).
- `opcao_invalida()`: mensagem e retorno ao menu.
- `finalizar_app()`: encerra com `sys.exit()`.
- `main()`: fluxo inicial (limpar tela → menu → escolher opção).

---

## 📄 Licença

Este projeto está licenciado sob a GNU General Public License v3.0 - veja o arquivo LICENSE para detalhes.

---

## 🙌 Agradecimentos

Feito com carinho para praticar Python. Se este material te ajudou, deixe uma ⭐ no repositório e compartilhe com alguém que está começando!
