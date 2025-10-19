# Importa módulos da biblioteca padrão:
# - os: para comandos do sistema (ex.: limpar a tela)
# - sys: para encerrar o programa com sys.exit()
# - platform: para descobrir o sistema operacional (Windows, Linux, etc.)
import os, sys, platform

# Cria uma lista vazia que guardará vários dicionários,
# cada um representando uma despesa com 'nome' e 'valor'.
despesas = []

# Define o orçamento máximo permitido para o total das despesas.
orcamento_maximo = 3000.00

# Define uma função que apenas mostra as opções do menu na tela.
def exibir_menu():
    
    # Exibe as opções numeradas para o usuário escolher.
    print('1. Cadastrar despesa')
    print('2. Listar despesas')
    print('3. Relatório final')
    print('4. Sair')

# Define a função responsável por cadastrar (inserir) uma nova despesa.
def cadastrar_despesas():

    # Pede ao usuário o nome da despesa (ex.: "Internet").
    nome_da_despesa = input('Nome da despesa: ')

    # Pede o valor da despesa e converte para float (número com casas decimais).
    # Se o usuário digitar algo que não é número, isso gera ValueError.
    valor_da_despesa = float(input('Valor da despesa: '))

    # Monta um dicionário com as informações da despesa.
    dados_da_despesa = {'nome': nome_da_despesa, 'valor': valor_da_despesa}

    # Adiciona o dicionário na lista global de despesas.
    despesas.append(dados_da_despesa)

    # Dá um feedback amigável de que a despesa foi cadastrada.
    print(f'{nome_da_despesa} foi cadastrada com sucesso!')

    # Depois de cadastrar, volta para o menu principal.
    voltar_ao_menu_principal()

# Define a função que percorre e mostra todas as despesas já cadastradas.
def listar_despesas():

    # Se a lista estiver vazia, informa que não há despesas.
    if not despesas:
        print('Nenhuma despesa cadastrada ainda.')
    else:
        # Se houver despesas, percorre cada item da lista.
        for despesa in despesas:

            # Pega o nome da despesa do dicionário atual.
            nome_da_despesa = despesa['nome']

            # Pega o valor da despesa do dicionário atual.
            valor_da_despesa = despesa['valor']

            # Imprime a linha formatada: nome alinhado à esquerda e valor ao lado.
            print(f'- {nome_da_despesa.ljust(20)} | {valor_da_despesa}')

    # Ao fim da listagem (ou da mensagem de vazio), volta ao menu principal.
    voltar_ao_menu_principal()

# Define a função que calcula e mostra o total e diz se passou do orçamento.
def relatorio_final():

    # Soma, com segurança, o campo 'valor' de cada despesa (0 se a chave não existir).
    total = sum(item.get('valor', 0) for item in despesas)

    # Compara o total com o orçamento máximo e informa o resultado.
    if total > orcamento_maximo:
        print(f'Seus gastos totais foram de R$ {total}. Você ultrapassou o limite de orçamento de R$ {orcamento_maximo}')
    else:
        print(f'Parabéns! Seus gastos foram R$ {total} e ficaram dentro do orçamento máximo de R$ {orcamento_maximo}')
    
    # Depois do relatório, encerra o aplicativo.
    finalizar_app()

# Define a função que pausa e retorna ao menu principal.
def voltar_ao_menu_principal():

    # Aguarda o usuário pressionar alguma tecla (Enter) para continuar.
    input('\nDigite uma tecla para voltar ao menu principal: ')
    
    # Chama a função main() novamente para redesenhar o menu e perguntar a opção.
    main()

# Define a função para limpar o texto no terminal, de forma compatível com o SO.
def limpar_tela():

    # Se for Windows, usa 'cls'; caso contrário, usa 'clear' (Linux/Mac).
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# Define a função para tratar qualquer opção inválida escolhida pelo usuário.
def opcao_invalida():

    # Mensagem de erro simples.
    print('\nOpção inválida!\n')

    # Retorna ao menu principal após a mensagem.
    voltar_ao_menu_principal()

# Define a função para finalizar o aplicativo.
def finalizar_app():

    # Mensagem final de encerramento.
    print('Encerrando o programa...')

    # Sai do programa imediatamente.
    sys.exit()

# Define a função que lê a opção do usuário e direciona o fluxo do programa.
def escolher_opcao():

    try:
        # Lê a opção digitada e converte para inteiro.
        opcao_escolhida = int(input('Escolha uma opção: '))

        # Usa o 'match-case' (Python 3.10+) para decidir o que fazer com base na opção.
        match opcao_escolhida:
            case 1:
                cadastrar_despesas()
            case 2:
                listar_despesas()
            case 3:
                relatorio_final()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    
    # Se o usuário não digitar um número inteiro, cai aqui e tratamos como inválido.
    except ValueError:
        opcao_invalida()
                
# Função principal que organiza a sequência: limpar, mostrar menu e ler opção.
def main():

    # Limpa a tela do terminal antes de mostrar o menu.
    limpar_tela()

    # Mostra as opções disponíveis.
    exibir_menu()

    # Pergunta e trata a escolha do usuário.
    escolher_opcao()

# "Ponto de entrada" do script: só executa main() se este arquivo for rodado diretamente.
if __name__ == '__main__':
    main()