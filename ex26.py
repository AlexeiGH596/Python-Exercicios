frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.lower()
print(f'A letra A aparece {frase2.count("a")} vezes.')
print(f'Sua primeira aparição é na casa de número {frase2.find("a")+1}.')
print(f'E sua última aparição é na casa de número {frase2.rfind("a")+1}.')
