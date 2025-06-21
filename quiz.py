import json

with open('perguntas.json', 'r', encoding='utf-8') as arquivo:
    dados_perguntas = json.load(arquivo)
    perguntas = dados_perguntas['perguntas']


with open('ranking.json', 'r', encoding='utf-8') as arquivo:
    dados_ranking = json.load(arquivo)
    ranking = dados_ranking['jogadores']


while True:
    print("===== MENU =====")
    print("1. Iniciar Quiz")
    print("2. Mostrar Ranking")
    print("3. Desenvolvedoras")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':

        nome = input("Digite seu nome: ")

        pontuacao = 0

        for pergunta in perguntas:
            print("" + pergunta['pergunta'])
            for i, alt in enumerate(pergunta['alternativas']):
                print(f"{i + 1}. {alt}")

            resposta = input("Digite o número da resposta: ")

            try:
                indice = int(resposta) - 1
                if pergunta['alternativas'][indice] == pergunta['resposta']:
                    print("✅ correto!")
                    pontuacao += 1
                else:
                    print(f"❌ Errado! A resposta correta era: {pergunta['resposta']}")
            except:
                print("Resposta inválida.")

        print(f"{nome}, sua pontuação foi: {pontuacao} de {len(perguntas)}")

        ranking.append({"nome": nome, "pontuacao": pontuacao})

        with open('ranking.json', 'w', encoding='utf-8') as arquivo:
            json.dump({"jogadores": ranking}, arquivo, ensure_ascii=False, indent=4)

        print("Sua pontuação foi para o ranking😊!")

    elif opcao == '2':
        if not ranking:
            print("\n Ranking vazio!")
        else:
            print("\n===== 🏆 RANKING 🏆 =====")
            ranking_ordenado = sorted(ranking, key=lambda x: x['pontuacao'], reverse=True)

            for i, jogador in enumerate(ranking_ordenado, start=1):
                print(f"{i}. {jogador['nome']} - {jogador['pontuacao']} ponto(s)")

            print("==========================")

    elif opcao == '3':
        print("\n===== Desenvolvido por =====")
        print("💙 Maria Luiza Almeida")
        print("💚 Yasmin Rodrigues de Morais")

    elif opcao == '4':
        print("\nFinalizando!")
        break

    else:
        print("\n Opção inválida!")
