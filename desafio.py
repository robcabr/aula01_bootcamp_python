# Constante bonus

CONSTANTE_BONUS = 1000

# Nome do usuario 

nome_usuario = input("Por favor digite o seu nome: ")

# Salario

salario_usuario = int(input("Por favor digite o seu salario: "))

# Bonus

bonus_usuario = float(input("Por favor digite o seu bonus: "))

# Valor a receber

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario


# Imprima a mensagem personalizada incluindo o nome do usuario e o valor do bonus
print(f"Ola {nome_usuario}, o seu bonus será de {valor_do_bonus}")