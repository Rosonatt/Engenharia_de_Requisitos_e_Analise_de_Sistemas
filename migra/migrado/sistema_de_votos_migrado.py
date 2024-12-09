candidatos = {
    1: "Opção 1",
    2: "Opção 2",
    3: "Opção 3"
}


votos = {1: 0, 2: 0, 3: 0}

def mostrar_menu():
    print(f"\n=*=*= Sistema de Votação =*=*=")
    print(f"Escolha uma opção:")
    for numero, nome in candidatos.items():
        print(f"{numero} - {nome}")
    print(f"0 - Finalizar votação")

def mostrar_resultados():
    print(f"\n=== Resultados ===")
    total = sum(votos.values())
    
    if total == 0:
        print(f"Nenhum voto registrado!")
        return
    
    for numero, nome in candidatos.items():
        print(f"{nome}: {votos[numero]} votos")
    
    vencedor = max(votos, key=votos.get)
    print(f"Vencedor: {candidatos[vencedor]} com {votos[vencedor]} votos")

try:
    while True:
        mostrar_menu()
        escolha = int(input("\nSua escolha: "))
        
        if escolha == 0:
            break
        elif escolha in candidatos:
            votos[escolha] += 1
            print(f"Seu voto registrado!")
        else:
            print(f"Esta opção inválida!")
            
except ValueError:
    print(f"Por favor, digite um número válido!")
finally:
    mostrar_resultados()