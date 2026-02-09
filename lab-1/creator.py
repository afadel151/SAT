
def var_number(attribute, value, position):
    """
    Retourne le numéro de variable pour X_{a,v,p}
    Numérotation: 1 à 125
    """
    return 1 + attribute * 25 + value * 5 + position

def write_clause(f, clause):
    """Écrit une clause dans le fichier CNF"""
    f.write(' '.join(map(str, clause)) + ' 0\n')

NATIONALITY = 0  
COLOR = 1        
PROFESSION = 2   
ANIMAL = 3       
DRINK = 4        

ANGLAIS, ESPAGNOL, JAPONAIS, ITALIEN, NORVEGIEN = 0, 1, 2, 3, 4
ROUGE, VERT, BLANC, JAUNE, BLEU = 0, 1, 2, 3, 4
PEINTRE, SCULPTEUR, DIPLOMATE, VIOLONISTE, DOCTEUR = 0, 1, 2, 3, 4
CHIEN, ESCARGOTS, RENARD, CHEVAL, ZEBRE = 0, 1, 2, 3, 4
THE, CAFE, LAIT, JUS_ORANGE, EAU = 0, 1, 2, 3, 4

clauses = []

for attr in range(5):
    for val in range(5):
        clause = [var_number(attr, val, pos) for pos in range(5)]
        clauses.append(clause)
        for p1 in range(5):
            for p2 in range(p1+1, 5):
                clauses.append([-var_number(attr, val, p1), -var_number(attr, val, p2)])

for attr in range(5):
    for pos in range(5):
        clause = [var_number(attr, val, pos) for val in range(5)]
        clauses.append(clause)
        for v1 in range(5):
            for v2 in range(v1+1, 5):
                clauses.append([-var_number(attr, v1, pos), -var_number(attr, v2, pos)])


for pos in range(5):
    clauses.append([-var_number(NATIONALITY, ANGLAIS, pos), var_number(COLOR, ROUGE, pos)])
    clauses.append([-var_number(COLOR, ROUGE, pos), var_number(NATIONALITY, ANGLAIS, pos)])

for pos in range(5):
    clauses.append([-var_number(NATIONALITY, ESPAGNOL, pos), var_number(ANIMAL, CHIEN, pos)])
    clauses.append([-var_number(ANIMAL, CHIEN, pos), var_number(NATIONALITY, ESPAGNOL, pos)])

for pos in range(5):
    clauses.append([-var_number(NATIONALITY, JAPONAIS, pos), var_number(PROFESSION, PEINTRE, pos)])
    clauses.append([-var_number(PROFESSION, PEINTRE, pos), var_number(NATIONALITY, JAPONAIS, pos)])

for pos in range(5):
    clauses.append([-var_number(NATIONALITY, ITALIEN, pos), var_number(DRINK, THE, pos)])
    clauses.append([-var_number(DRINK, THE, pos), var_number(NATIONALITY, ITALIEN, pos)])

clauses.append([var_number(NATIONALITY, NORVEGIEN, 0)])
for pos in range(5):
    clauses.append([-var_number(COLOR, VERT, pos), var_number(DRINK, CAFE, pos)])
    clauses.append([-var_number(DRINK, CAFE, pos), var_number(COLOR, VERT, pos)])

for pos in range(4):
    clauses.append([-var_number(COLOR, BLANC, pos), var_number(COLOR, VERT, pos+1)])
    clauses.append([-var_number(COLOR, VERT, pos+1), var_number(COLOR, BLANC, pos)])

for pos in range(5):
    clauses.append([-var_number(PROFESSION, SCULPTEUR, pos), var_number(ANIMAL, ESCARGOTS, pos)])
    clauses.append([-var_number(ANIMAL, ESCARGOTS, pos), var_number(PROFESSION, SCULPTEUR, pos)])

for pos in range(5):
    clauses.append([-var_number(PROFESSION, DIPLOMATE, pos), var_number(COLOR, JAUNE, pos)])
    clauses.append([-var_number(COLOR, JAUNE, pos), var_number(PROFESSION, DIPLOMATE, pos)])

clauses.append([var_number(DRINK, LAIT, 2)])
clauses.append([var_number(COLOR, BLEU, 1)])

for pos in range(5):
    clauses.append([-var_number(PROFESSION, VIOLONISTE, pos), var_number(DRINK, JUS_ORANGE, pos)])
    clauses.append([-var_number(DRINK, JUS_ORANGE, pos), var_number(PROFESSION, VIOLONISTE, pos)])

for pos in range(5):
    neighbors = []
    if pos > 0:
        neighbors.append(var_number(ANIMAL, RENARD, pos-1))
    if pos < 4:
        neighbors.append(var_number(ANIMAL, RENARD, pos+1))
    if neighbors:
        clauses.append([-var_number(PROFESSION, DOCTEUR, pos)] + neighbors)

for pos in range(5):
    neighbors = []
    if pos > 0:
        neighbors.append(var_number(ANIMAL, CHEVAL, pos-1))
    if pos < 4:
        neighbors.append(var_number(ANIMAL, CHEVAL, pos+1))
    if neighbors:
        clauses.append([-var_number(PROFESSION, DIPLOMATE, pos)] + neighbors)

for pos in range(5):
    clauses.append([-var_number(COLOR, BLANC, pos), var_number(ANIMAL, ZEBRE, pos)])
    clauses.append([-var_number(ANIMAL, ZEBRE, pos), var_number(COLOR, BLANC, pos)])

clause = [var_number(DRINK, EAU, pos) for pos in range(5)]
clauses.append(clause)

num_vars = 125
num_clauses = len(clauses)

with open('zebra.cnf', 'w') as f:
    f.write(f'p cnf {num_vars} {num_clauses}\n')
    for clause in clauses:
        write_clause(f, clause)

