print("")
print("**************Python Calculator*****************")
print("")
print("Selecione o número da operação desejada:")
print("")

print("1 - Soma")
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

def soma(num1,num2):
		return num1 + num2
#essa opção com a função soma eu usei o retunr pq quero colocar
#os valores que serão digitados pelo usuário "3 + 2 = 5"

def subt(num1, num2):
		if num1 >= num2:
			print(num1-num2)
		else:
			print("Opção inválida")

def multi(num1,num2):
		print(num1*num2)
#nesse caso, não usei o return, usei o print direto; aqui
#o usuário so verá o resultado final e não a espressão "3 * 2 = 6"

def div(num1,num2):
	    print(num1/num2)

opcao = input('Digite sua opção(1/2/3/4): ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if opcao == "1":
	print(num1, " + ", num2, " = ", soma(num1,num2))
	
elif opcao == "2": 
	subt(num1,num2)
elif opcao == "3":
	multi(num1,num2)
else:
	div(num1,num2)