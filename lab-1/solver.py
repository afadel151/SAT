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

solution = [-1, -2, -3, 4, -5, -6, -7, 8, -9, -10, -11, 12, -13, -14, -15, -16, 
            -17, -18, -19, 20, 21, -22, -23, -24, -25, -26, -27, -28, 29, -30, 
            31, -32, -33, -34, -35, -36, -37, -38, -39, 40, -41, -42, 43, -44, 
            -45, -46, 47, -48, -49, -50, -51, 52, -53, -54, -55, 56, -57, -58, 
            -59, -60, -61, -62, 63, -64, -65, -66, -67, -68, 69, -70, -71, -72, 
            -73, -74, 75, -76, -77, 78, -79, -80, 81, -82, -83, -84, -85, -86, 
            -87, -88, 89, -90, -91, 92, -93, -94, -95, -96, -97, -98, -99, 100, 
            -101, -102, -103, -104, 105, 106, -107, -108, -109, -110, -111, -112, 
            113, -114, -115, -116, -117, -118, 119, -120, -121, 122, -123, -124, -125]

houses = [{'position': i+1} for i in range(5)]

for var in solution:
    if var > 0:  
        attr, val, pos = decode_var(var)
        attr_name = attribute_names[attr]
        value_name = all_values[attr][val]
        houses[pos][attr_name] = value_name

print("=" * 70)
print("SOLUTION DU PROBLÈME DU ZÈBRE")
print("=" * 70)
print()

for house in houses:
    print(f"🏠 MAISON {house['position']}")
    print(f"   Nationalité : {house.get('Nationalité', '?')}")
    print(f"   Couleur     : {house.get('Couleur', '?')}")
    print(f"   Profession  : {house.get('Profession', '?')}")
    print(f"   Animal      : {house.get('Animal', '?')}")
    print(f"   Boisson     : {house.get('Boisson', '?')}")
    print()

print("=" * 70)
print("VUE TABLEAU")
print("=" * 70)
print(f"{'Maison':<12} {'Nationalité':<12} {'Couleur':<12} {'Profession':<12} {'Animal':<12} {'Boisson':<12}")
print("-" * 70)
for house in houses:
    print(f"{house['position']:<12} "
          f"{house.get('Nationalité', '?'):<12} "
          f"{house.get('Couleur', '?'):<12} "
          f"{house.get('Profession', '?'):<12} "
          f"{house.get('Animal', '?'):<12} "
          f"{house.get('Boisson', '?'):<12}")

print()
print("=" * 70)
print("RÉPONSES AUX QUESTIONS CLASSIQUES")
print("=" * 70)
for house in houses:
    if house.get('Animal') == 'Zèbre':
        print(f"zèbre  → {house.get('Nationalité', '?')}")
    if house.get('Boisson') == 'Eau':
        print(f"💧 eau ? → {house.get('Nationalité', '?')}")
