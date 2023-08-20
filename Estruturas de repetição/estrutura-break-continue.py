#A estrutura BREAK termina a estrutura de repetição que a contém
#A instrução CONTINUE é uado para pulat o código dentro de uma estrutura de repetição apenas na iteração atual

#Exemplo:

print("COVID-19")

suspeitos = 0

while True:
    tosse = int(input("Está tossindo? \n1. Sim \n2. Não \nResp.:"))
    febre = int(input("Está com febre? \n1. Sim \n2. Não \nResp.:"))
    resp = int(input("Está com problemas para respirar? \n1. Sim \n2. Não \nResp.:"))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1 #suspeitos = suspeitos + 1

    resp = input("Ainda existem pacientes a serem atendidos? [S|N]")
    if resp.upper() == "N":
        break

    
print("Suspeitos de COVID-19: {}".format(suspeitos))
