print("COVID-19")

suspeitos = 0
num_pac = int(input("Informe a quantidade de pacientes:"))

for x in range(num_pac):
    tosse = int(input("Está tossindo? \n1. Sim \n2. Não \nResp.:"))
    febre = int(input("Está com febre? \n1. Sim \n2. Não \nResp.:"))
    resp = int(input("Está com problemas para respirar? \n1. Sim \n2. Não \nResp.:"))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1 #suspeitos = suspeitos + 1

print("Suspeitos de COVID-19: {}".format(suspeitos))



