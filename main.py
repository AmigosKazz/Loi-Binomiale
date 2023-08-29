import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binomial_probability(n, k, p):
    q = 1 - p
    return binomial_coefficient(n, k) * (p**k) * (q**(n - k))

def binomial_distribution(n, p):
    distribution = []
    for k in range(n + 1):
        probability = binomial_probability(n, k, p)
        distribution.append(probability)
    return distribution


n = int(input("Nombre d'essais : "))
p = float(input("Probabilité de succès : "))
distribution = binomial_distribution(n, p)

# Affichage des résultats
for k, probability in enumerate(distribution):
    print(f"P(X = {k}) = {probability}")