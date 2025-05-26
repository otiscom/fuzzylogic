# -*- coding: utf-8 -*-
# System rekomendacji potraw oparty na logice rozmytej

# Funkcja trójkątnej przynależności fuzzy
def triangular_membership(x, a, b, c):
    """Oblicza przynależność punktu x do trójkątnego zbioru rozmytego określonego punktami (a, b, c)."""
    x = float(x)
    a = float(a); b = float(b); c = float(c)
    if x <= a or x >= c:
        # x poza zakresem trójkąta
        if a == b and x == a:
            return 1.0  # przypadek gdy trójkąt degeneruje do punktu (a == b)
        if b == c and x == c:
            return 1.0  # przypadek gdy trójkąt degeneruje do punktu (b == c)
        return 0.0
    if x == b:
        # wierzchołek trójkąta
        return 1.0
    if x < b:
        # rosnąca krawędź trójkąta
        return (x - a) / (b - a) if (b - a) != 0 else 0.0
    else:
        # opadająca krawędź trójkąta
        return (c - x) / (c - b) if (c - b) != 0 else 0.0

# Definicje zbiorów rozmytych (funkcji przynależności) dla kategorii każdej cechy (na skali 0-10)
membership_funcs = {
    'taste': {
        'mild':    (0, 0, 5),   # słodkie smak
        'medium':  (0, 5, 10),  # średni (umiarkowany) smak
        'intense': (5, 10, 10)  # intensywny (wyrazisty) smak
    },
    'price': {
        'cheap':    (0, 0, 5),   # tania cena
        'medium':   (0, 5, 10),  # średnia (umiarkowana) cena
        'expensive':(5, 10, 10)  # wysoka (droga) cena
    },
    'temperature': {
        'cold':  (0, 0, 5),    # zimne danie
        'warm':  (0, 5, 10),   # ciepłe (umiarkowane)
        'hot':   (5, 10, 10)   # gorące danie
    },
    'time': {
        'fast':   (0, 0, 5),   # szybko (krótki czas)
        'medium': (0, 5, 10),  # średni czas
        'slow':   (5, 10, 10)  # długo (długi czas)
    },
    'calories': {
        'low':    (0, 0, 5),   # niska kaloryczność
        'medium': (0, 5, 10),  # średnia
        'high':   (5, 10, 10)  # wysoka kaloryczność
    },
    'availability': {
        'easy':   (0, 0, 5),   # łatwo dostępna
        'medium': (0, 5, 10),  # umiarkowana dostępność
        'hard':   (5, 10, 10)  # trudno dostępna
    },
    'satiety': {
        'low':    (0, 0, 5),   # niski poziom sytości
        'medium': (0, 5, 10),  # średni
        'high':   (5, 10, 10)  # wysoki poziom sytości
    }
}

# Przykładowe predefiniowane potrawy z przypisanymi wartościami cech (0-10)
dishes = {
    "Burger": {
        'taste': 8,
        'price': 3,
        'temperature': 8,
        'time': 4,
        'calories': 8,
        'availability': 9,
        'satiety': 7
    },
    "Pizza": {
        'taste': 8,
        'price': 5,
        'temperature': 8,
        'time': 5,
        'calories': 8,
        'availability': 8,
        'satiety': 8
    },
    "Sushi": {
        'taste': 7,
        'price': 8,
        'temperature': 2,
        'time': 8,
        'calories': 4,
        'availability': 5,
        'satiety': 5
    },
    "Sałatka": {  # Salad
        'taste': 6,
        'price': 4,
        'temperature': 5,
        'time': 3,
        'calories': 3,
        'availability': 7,
        'satiety': 4
    },
    "Stek": {
        'taste': 9,
        'price': 7,
        'temperature': 9,
        'time': 7,
        'calories': 7,
        'availability': 4,
        'satiety': 9
    }
}

# Mapowanie polskich nazw cech na klucze wewnętrzne
feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas': 'time',             # 'czas przygotowania' też będzie zmapowany do 'time'
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'sytość': 'satiety'
}

# 1. Pobieranie preferencji użytkownika dla każdej cechy
print("Wprowadź swoje preferencje dla podanych cech (0 = najniżej, 10 = najwyżej):")
user_pref_values = {}
# Ustalona kolejność pytań zgodnie z listą cech:
features_in_order = ['smak','cena','temperatura','czas','kaloryczność','dostępność','sytość']
feature_sliders = {
    'smak': "| łagodny --- średni --- intensywny |",
    'cena': "| tania --- średnia --- droga |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas': "| szybko --- średnio --- długo |",
    'kaloryczność': "| niska --- średnia --- wysoka |",
    'dostępność': "| łatwa --- średnia --- trudna |",
    'sytość': "| niski poziom --- średni --- wysoki |"
}
for pol_feature in features_in_order:
    internal_key = feature_key[pol_feature]
    # Wyświetl "suwak" tekstowy dla danej cechy
    print(f"\nPreferencja dla cechy '{pol_feature.capitalize()}':")
    print(feature_sliders[pol_feature])
    val = input("Wybierz poziom (0-10): ")
    try:
        val = float(val)
    except ValueError:
        val = 0.0  # w razie błędnego wpisu, domyślnie 0
    # ogranicz w przedziale 0-10
    if val < 0: val = 0.0
    if val > 10: val = 10.0
    user_pref_values[internal_key] = val

# 2. Fuzzyfikacja preferencji użytkownika (obliczenie przynależności do kategorii dla każdej cechy)
user_pref_membership = {}
for feature, val in user_pref_values.items():
    categories = membership_funcs[feature]
    user_pref_membership[feature] = {}
    for cat, (a, b, c) in categories.items():
        user_pref_membership[feature][cat] = triangular_membership(val, a, b, c)

# 3. Pobranie od użytkownika kolejności ważności cech
print("\nPodaj cechy w kolejności od najważniejszej do najmniej ważnej, oddzielone przecinkami.")
print("Dostępne cechy: smak, cena, temperatura, czas, kaloryczność, dostępność, sytość")
order_input = input("Kolejność cech: ")
# Podziel i zmapuj nazwy na klucze wewnętrzne
order_list_polish = [x.strip().lower() for x in order_input.split(',')]
# Obsługa ewentualnych synonimów (np. "czas przygotowania" -> "czas", "poziom sytości" -> "sytość")
for i in range(len(order_list_polish)):
    if order_list_polish[i] == "czas przygotowania":
        order_list_polish[i] = "czas"
    if order_list_polish[i] == "poziom sytości":
        order_list_polish[i] = "sytość"
# Mapowanie na klucze wewnętrzne
order_features = [feature_key.get(feat, None) for feat in order_list_polish]
# Sprawdzenie poprawności wejścia
if None in order_features or len(order_features) != len(feature_key):
    print("Błąd: Niepoprawna lista cech. Upewnij się, że podałeś wszystkie cechy oddzielone przecinkami.")
    exit(1)

# Przydzielenie wag (7 dla pierwszej cechy, 6 dla drugiej, ..., 1 dla ostatniej) i normalizacja
weights = {}
num_features = len(order_features)
total = 0
for rank, feature in enumerate(order_features, start=1):
    w = num_features - (rank - 1)  # np. 7,6,...,1
    weights[feature] = w
    total += w
for feature in weights:
    weights[feature] /= total  # normalizacja do sumy 1

# 4. Obliczenie dopasowania każdej potrawy do preferencji użytkownika
results = []
for dish_name, feat_values in dishes.items():
    score = 0.0
    # dla każdej cechy oblicz dopasowanie (iloczyn skalarny wektora przynależności użytkownika i potrawy)
    for feature, cats in membership_funcs.items():
        # oblicz przynależności potrawy do kategorii (fuzzyfikacja cechy potrawy)
        dish_val = feat_values[feature]
        # sumuj iloczyny przynależności (preferencja vs potrawa) dla wszystkich kategorii danej cechy
        feature_match = 0.0
        for cat, (a, b, c) in cats.items():
            dish_mem = triangular_membership(dish_val, a, b, c)
            user_mem = user_pref_membership[feature][cat]
            feature_match += user_mem * dish_mem
        # pomnóż przez wagę ważności tej cechy
        score += weights[feature] * feature_match
    results.append((dish_name, score))

# 5. Sortowanie potraw malejąco według dopasowania
results.sort(key=lambda x: x[1], reverse=True)

# Wyświetlenie rankingu potraw
print("\nRanking rekomendowanych potraw:")
for i, (dish, score) in enumerate(results, start=1):
    print(f"{i}. {dish} – dopasowanie: {score:.2f}")
