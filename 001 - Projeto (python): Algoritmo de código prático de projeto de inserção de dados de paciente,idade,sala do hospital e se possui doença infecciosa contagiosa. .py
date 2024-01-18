nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiante?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paicente será direcionada para a sala amarela - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa=="SIM":
    print("O paicente será direcionada para a sala amarela - SEM prioridade")
elif idade>=65 and doenca_infectocontagiosa=="NÃO":
    print("O paicente será direcionada para a sala branca - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa=="NÃO":
    print("O paicente será direcionada para a sala branca - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NÃO")

O MESMO CÓDIGO DE OUTRA FORMA:
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiante? (SIM/NÃO) ").upper()

if idade >= 65:
    prioridade = "COM" if doenca_infectocontagiosa == "SIM" else "SEM"
    sala_destino = "amarela" if doenca_infectocontagiosa == "SIM" else "branca"
    print(f"O paciente será direcionado para a sala {sala_destino} - {prioridade} prioridade")
elif idade < 65:
    prioridade = "COM" if doenca_infectocontagiosa == "SIM" else "SEM"
    sala_destino = "amarela" if doenca_infectocontagiosa == "SIM" else "branca"
    print(f"O paciente será direcionado para a sala {sala_destino} - {prioridade} prioridade")
else:
    print("Responda à suspeita de doença infectocontagiosa com SIM ou NÃO")

DICAS:
Nomes Significativos:

Use nomes significativos para variáveis. Isso torna o código mais legível.
Evite abreviações desnecessárias.
Indentação e Espaçamento:

Mantenha uma indentação consistente para melhor legibilidade.
Adicione espaços ao redor dos operadores para melhorar a clareza.
Entrada de Dados:

Forneça mensagens de prompt mais explicativas.
Condições Simplificadas:

Simplifique as condições para tornar o código mais claro.

Melhorias com a plicação de CLEAN CODE no código:
Principais melhorias realizadas:

Utilizei mensagens mais explicativas para a entrada de dados.
Simplifiquei as condições usando a lógica compartilhada para os casos de idade maior ou igual a 65 e menor que 65.
Introduzi variáveis para armazenar a prioridade e a sala de destino, evitando repetição de código.
Adotei f-strings para facilitar a formatação de strings.
