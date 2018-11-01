from random import randint


suits = {
    0: "paus",
    1: "ouros",
    2: "copas",
    3: "espadas",
    4: "paus do baralho 1",
    5: "ouros do baralho 1",
    6: "copas do baralho 1",
    7: "espadas do baralho 1",
    8: "paus do baralho 2",
    9: "ouros do baralho 2",
    10: "copas do baralho 2",
    11: "espadas do baralho 2",
    12: "paus do  baralho 3",
    13: "ouros do baralho 3",
    14: "copas do baralho 3",
    15: "espadas do baralho 3"









}
cards = {
    0: "As",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "10",
    10: "valete",
    11: "rainha",
    12: "rei",


}
def draw_cards(num_cartas, list_default=[]):
    for z in range(num_cartas):
        x = randint(0, 15)
        y = randint(0, 12)
        minhas_cartas = "{0} de {1}".format(cards[y], suits[x])
        if minhas_cartas not in list_default:
            list_default.append(minhas_cartas)
        else:
            num_cartas = num_cartas-z
            return draw_cards(num_cartas, list_default)
    return list_default
meu_desenho = draw_cards(20)


i = 0
for x in meu_desenho:
    i += 1
    if i == len(meu_desenho):
        print("... E a sua ultima carta e de : {0}".format(str(x)))
    else:
        print("você tem o  {0}  ".format(str(x)))
