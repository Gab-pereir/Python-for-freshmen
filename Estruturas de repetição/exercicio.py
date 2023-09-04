# Construa um programa que receba o sexo e a idade de alunos de uma turma. Considere que o usuário não sabe a quantidade de alunos na turma. Ao fim, o programa deve exibir a quantidade de repazes acima de 18 anos e a média de idade das moças. Para encerrar o programa, informar uma idade negativa.

rapazes_maiores = 0
soma_feminina = 0
mocas = 0

while True:
    sexo = input("Sexo? [F/M]")
    idade = int(input("Idade:"))
    if idade < 0:
        break

    if sexo.upper() == "M":
        if idade > 18:
            rapazes_maiores += 1                
    elif sexo.upper() == "F":
        soma_feminina += idade
        mocas += 1
    else:
        print("Opção inválida")

media = 0
if mocas > 0:
    media = soma_feminina / mocas

print("Rapazes maiores de 18 anos:{}".format(rapazes_maiores))
print("Média de idade das moças:{}".format(media))