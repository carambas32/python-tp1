import sys

# Partie 1
# 1.1 et 1.2
a = 3
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = 3.0
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = False
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = 0.0
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = 0
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = '0'
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = "0"
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = 2562378273826392638273628735283752867352736523765376254322874527653762538126170182010237528753276537623457624376243762347236423764747646746746723
print("a =", a, "->", type(a), ":", sys.getsizeof(a))
a = "abc"
print("a =", a, "->", type(a), ":", sys.getsizeof(a))

# a = 3 -> <class 'int'> : 28
# a = 3.0 -> <class 'float'> : 24
# a = False -> <class 'bool'> : 28
# a = 0.0 -> <class 'float'> : 24
# a = 0 -> <class 'int'> : 28
# a = 0 -> <class 'str'> : 42
# a = 0 -> <class 'str'> : 42
# a = 2562378273826392638273628735283752867352736523765376254322874527653762538126170182010237528753276537623457624376243762347236423764747646746746723 -> <class 'int'> : 88
# a = abc -> <class 'str'> : 44


# Exercice 1.3
a = 1
for i in range(10):
    print(i, a)
    print(sys.getsizeof(a))
    print()
    a *= 2

# Que vaut la variable a à la fin de la boucle ?
# => a vaut 2^1000 = 5357543035931336604742125245300009052807024058527668037218751941851755255624680612465991894078479290637973364587765734125935726428461570217992288787349287401967283887412115492710537302531185570938977091076523237491790970633699383779582771973038531457285598238843271083830214915826312193418602834034688

# Quelle différence observez-vous par rapport au même programme en C ?
# => En c un entier non signé de 64 bit ne peut pas valoir plus de 2^64 - 1

# Qu'en déduisez-vous sur la taille de la variable a au cours du programme ?
# => La taille de la variable augmente dynamiquement en fonction des besoins. C'est nolimit

# Mettez en évidence le phénomène avec la fonction sys.getsizeof() 
# => A la fin du programme, sys.getsizeof(a) retourne 160 alors que sur les premières itérations on part de 28. On voit la taille aumenter progressivement en fonction des besoins


# Exercice 1.4
s = "abcdefgh"
new_string = ""
for i in range(0, len(s)):
    if i % 2:
        new_string += s[i].upper()
    else:
        new_string += s[i]
print(new_string)
print(s.upper()[::-1])

# Exercice 1.5
for y in range(1, 11):
    for x in range(1, 11):
        # print('%4d' % (x * y) , end='') # Formattage de type c printf
        print('{:4}'.format(x * y) , end='') # Le formattage permet d'aligner les colonnes
    print()
    
    
# Exercice 1.6

def syracuse_terme_suivant(n):
    if n % 2 == 0:
        n = n // 2 # Permet de rester en int et pas en float
    else:
        n = n * 3 + 1
        
    return n
        
def syracuse (n):
    print('syracuse(%d)' % (n))
    nb_iterations = 0
    max = n
    print(n, end=' ')
    
    while n != 1:
        n = syracuse_terme_suivant(n)
        nb_iterations += 1
        if (n > max):
            max = n
        print(n, end=' ')
    
    print()
    print('Nombre d\'itérations : ', nb_iterations)
    print('Altitude max : ', max)
    
print('\n')
syracuse(17)
        
# Partie 2
print('\n--- Partie 2\n')

# Exercice 2.1
def even_numbers(n):
    return list(range(0, n + 1, 2))

L = even_numbers(20)
print('even numbers : ', L)
L.reverse()
print('reverse : ', L)
print()
    
# Exercice 2.2
def min_max_mean_list(l):
    
    if len(l) == 0:
        return {
            'min': None,
            'max': None,
            'mean': None,
        }
        
    nb_elements = 0
    max = l[0]
    min = l[0]
    sum = 0
    
    for v in l:
        sum += v
        nb_elements += 1
        
        if v > max:
            max = v
        
        if v < min:
            min = v
    
    mean = sum / nb_elements
    
    return {
        'min': min,
        'max': max,
        'mean': mean,
    }

# mylist = [4, 8, 100, 15, 99]
mylist = [5, 8, 2, 10, 4]
print(mylist, ' => ', min_max_mean_list(mylist), '\n')

# Exercice 2.3 : tri à bulles
def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
    
def bubble_sort(t):
    for i in range(len(t) - 1, 0, -1):
        for j in range(0, i):
            if t[j+1] < t[j]:
                swap(t, j, j+1)
                
                
# T = [6, 15, 2, -7, 8]
T = [5, 2, 8, 1, 4]
print('Tri à bulles : ', T, ' => ', end = '')
bubble_sort(T)
print(T, '\n')

# Exercice 2.4 : nombres premiers
def prime(n):
    if n < 2:
        return False
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
        
    return True

def prime_numbers(n):
    numbers = []
    for i in range(2, n+1):
        if prime(i):
            numbers.append(i)
            
    return numbers

print('Premiers nombres premiers (méthode 1) : ', prime_numbers(100))

# Crible d'Eratosthène
def prime_numbers2(n):
    l = list(range(2, n + 1))
    
    for v in l: # v = valeur dont on va supprimer les multiples
        for multiple in range(2 * v, n + 1, v): # multiples de v <= n
            if multiple in l:
                l.remove(multiple)
            
    return l

print('Premiers nombres premiers (méthode 2) : ', prime_numbers2(100), '\n')

# Exercice 2.5
notes = {
1256 : ('Martin', 18),
1318 : ('Dupuis', 13),
1579 : ('Dupont', 15),
1442 : ('Moulin', 13),
1731 : ('Robert', 10)
}

# 2.5.1
print('2.5 Dictionnaires')

def build_inv(d):
    d_inv = {}
    for (nom, note) in d.values():
        d_inv[nom] = note
        
    return d_inv

print(build_inv(notes))

# 2.5.2
def print_inv_dict(inv):
    noms = list(inv.keys())
    noms.sort()
    for i in noms:
        print('%s : %d' % (i, inv[i]))
        
print_inv_dict(build_inv(notes))

# 2.5.3
def build_grade_list(d):
    l = [ [] for i in range(21) ]
    # contient des listes vides pour i de 0 à 20
    
    for (name, grade) in d.values():
        l[grade].append(name)
    
    return l

print(build_grade_list(notes), '\n')

# Exercice 2.6 : logs
print('2.6 Logs')

logs = [
    { "ip": "192.168.1.1", "user": "alice", "status": "success" },
    { "ip": "192.168.1.2", "user": "bob", "status": "failure" },
    { "ip": "192.168.1.1", "user": "alice", "status": "failure" },
    { "ip": "192.168.1.3", "user": "charlie", "status": "success" }
]

def build_fail_registry(logs):
    failed_cnx = []
    for cnx in logs:
        if cnx['status'] == 'failure':
            failed_cnx.append({
                'ip': cnx['ip'],
                'user': cnx['user']
            })
            
    return failed_cnx

print(build_fail_registry(logs))

logs2 = [
    { "ip": "192.168.1.1", "user": "alice", "status": "success" },
    { "ip": "192.168.10.2", "user": "bob", "status": "failure" },
    { "ip": "192.168.10.1", "user": "alice", "status": "failure" },
    { "ip": "192.168.1.3", "user": "charlie", "status": "success" }
]

def logs2ip(logs):
    ip = []
    for cnx in logs:
        if cnx['ip'] not in ip:
            ip.append(cnx['ip'])
    
    return ip

def doublons_ip(logs, logs2):
    doublons =  []
    ip1 = logs2ip(logs)
    ip2 = logs2ip(logs2)
    for ip in ip1:
        if ip in ip2:
            doublons.append(ip)
            
    return doublons

print(doublons_ip(logs, logs2))