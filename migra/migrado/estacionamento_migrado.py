MAXIMO_DE_VAGAS = 100
vagas = []

def iniciando_estacionamento():
    global vagas
    for i in range(MAXIMO_DE_VAGAS):
        vagas.append({
            'id': i + 1,
            'placa': '',
            'ocupado': False
        })

def mostrar_vagas():
    print("Vagas disponíveis:")
    for vaga in vagas:
        if not vaga['ocupado']:
            print(f"Vaga {vaga['id']} está livre.")

def estacionar_veiculo():
    placa = input("Informe a placa do veículo: ")

    for vaga in vagas:
        if not vaga['ocupado']:
            vaga['ocupado'] = True
            vaga['placa'] = placa
            print(f"Veículo com placa {placa} estacionado na vaga {vaga['id']}.")
            return
    print("Estacionamento cheio!")

def remover_veiculo():
    placa = input("Informe a placa do veículo a ser removido: ")

    for vaga in vagas:
        if vaga['ocupado'] and vaga['placa'] == placa:
            vaga['ocupado'] = False
            vaga['placa'] = ''
            print(f"Veículo com placa {placa} removido da vaga {vaga['id']}.")
            return
    print("Veículo não encontrado.")

iniciando_estacionamento()

while True:
    print("\nSistema de Gerenciamento de Estacionamento")
    print("1. Exibir Vagas")
    print("2. Estacionar Veículo")
    print("3. Remover Veículo")
    print("4. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            mostrar_vagas()
        elif opcao == 2:
            estacionar_veiculo()
        elif opcao == 3:
            remover_veiculo()
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")