from pysat.formula import CNF
from pysat.solvers import Solver, Minisat22

def var_number(attribute, value, position):
    """Retourne le numéro de variable pour X_{a,v,p}"""
    return 1 + attribute * 25 + value * 5 + position

def decode_var(var_num):
    """Décode un numéro de variable en (attribut, valeur, position)"""
    var_num -= 1  
    attribute = var_num // 25
    remainder = var_num % 25
    value = remainder // 5
    position = remainder % 5
    return attribute, value, position

NATIONALITY = 0
COLOR = 1
PROFESSION = 2
ANIMAL = 3
DRINK = 4

nationalities = ['Anglais', 'Espagnol', 'Japonais', 'Italien', 'Norvégien']
colors = ['Rouge', 'Vert', 'Blanc', 'Jaune', 'Bleu']
professions = ['Peintre', 'Sculpteur', 'Diplomate', 'Violoniste', 'Docteur']
animals = ['Chien', 'Escargots', 'Renard', 'Cheval', 'Zèbre']
drinks = ['Thé', 'Café', 'Lait', 'Jus d\'orange', 'Eau']

attribute_names = ['Nationalité', 'Couleur', 'Profession', 'Animal', 'Boisson']
all_values = [nationalities, colors, professions, animals, drinks]

def main():
    cnf = CNF(from_file='zebra.cnf')
    s= Solver(name='m22')
    for clause in cnf.clauses:
        s.add_clause(clause)
    s.solve()
    solution = s.get_model()
    houses = [{'position': i+1} for i in range(5)]
    for var in solution:
        if var > 0:  
            attr, val, pos = decode_var(var)
            attr_name = attribute_names[attr]
            value_name = all_values[attr][val]
            houses[pos][attr_name] = value_name
    for house in houses:
        print(f"🏠 MAISON {house['position']}")
        print(f"   Nationalité : {house.get('Nationalité', '?')}")
        print(f"   Couleur     : {house.get('Couleur', '?')}")
        print(f"   Profession  : {house.get('Profession', '?')}")
        print(f"   Animal      : {house.get('Animal', '?')}")
        print(f"   Boisson     : {house.get('Boisson', '?')}")
        print()
    for house in houses:
        if house.get('Animal') == 'Zèbre':
            print(f"zèbre  → {house.get('Nationalité', '?')}")
        if house.get('Boisson') == 'Eau':
            print(f"eau  → {house.get('Nationalité', '?')}")



if __name__ == "__main__":
    main()
