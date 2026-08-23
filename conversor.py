numero = float(input("Insira o seu número: "))

conversor = input("Qual conversão escolhe? jarda, pe ou metro? ")

convec_tupla = {'jarda', 'pe', 'metro'}

def jarda_to_pe(conversor):
    print("Escolheu Jarda")

jarda = numero / 3
if conversor == 'jarda':
    print(jarda)

def pe_to_metro(conversor):
    print("Escolheu pe")
    
pe = numero / 3.281
if conversor == 'pe':
    print(pe)
    
def metro_to_jarda(conversor):
    print("Escolheu metro")

metro = numero / 1.094
if conversor == 'metro':
    print(metro)    

    




