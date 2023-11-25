# 
import re

# suite de lettres en miniscule et un '+' (= métacaractère qui permet de dire que au moins nous devrons avoir un caractère)
expression = "[a-z]+"
# on compile notre expression régulière à travers la fonction 'compile()' qui se trouve qui se trouve sur notre module 
#  que l'on récupère dans une variable :
expression_compile = re.compile(expression)

# prend un schémas de recherche en premier argument et une chaine dans laquelle effectuer la recherche en deusième argument et
# l'objet de correspondance trouvé. Si la chaine ne correspond pas au motif, ça renvoi 'None' :
print(re.match(expression_compile, " "))
print(re.match(expression_compile, "1bonjour"))
print(re.match(expression_compile, "Hello"))
print(re.match(expression_compile, "hello"))

# permet d'analyse une chaine passée en deuxième argument à la recherche du premier emplacement ou l'expression régulièrepassée en premier
# argument trouve une correspondance et renvoi l'objet de correspondance trouvé ou 'None' si aucune position dans la chaine ne valide le motif :
print(re.search(expression_compile, " "))
print(re.search(expression_compile, "1bonjour"))
print(re.search(expression_compile, "Hello"))
print(re.search(expression_compile, "hello"))

# renvoi toutes les correspondances de l'expression régulière passée en premier argument 
# dans la chaine passée en deuxième argument sous forme de liste de chaines. Analyse de Gauche --> Droite
# et les correspondances sont renvoyées dans l'ordre où elles sont trouvées :
print(re.findall(expression_compile, " "))
print(re.findall(expression_compile, "123 bonjour Tout le monde"))
print(re.findall(expression_compile, "Hello"))
print(re.findall(expression_compile, "hello"))

# #email@exemple.com

regex = r"[A-Za-z0-9.+-_%]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"

# DÉTAILS :
# [A-Za-z0-9.+-_%]+ => permet d'indiquer les caractères et les symboles autorisés de 'email', le '+' indique qu'on s'attend à avoir plus d'un caractère
# puis le '@'
# [A-Za-z0-9.-]+ => 'exemple' pareil que pour 'email'
# le point '.', pour lui donner un sens on le précède d'un '\'
# [A-Z|a-z]{2,} => caractères et les symboles autorisés de 'com', 
                 # le '|' indique soit en MAJ. soit en min. et '{2,}' indique qu'on aura 2 caractères minimum.

# on va donc créer une fonction afin de vérifier chaque email, s'ils respectent ce format ou pas ?
def check(email):
    if(re.fullmatch(expression_compile, email)):
        print(f"le format de '{email}' est respecté")
    else:
        print(f"le format de '{email}' n'est pas respecté")

email = "exemple@gmail.com"
check(email)

# -----------------------------------------------------------------------------