# -*- coding: utf-8 -*-
# Zaktualizowany system rekomendacji potraw oparty na logice rozmytej

def triangular_membership(x, a, b, c):
    x = float(x)
    a = float(a); b = float(b); c = float(c)
    if x <= a or x >= c:
        if a == b and x == a:
            return 1.0
        if b == c and x == c:
            return 1.0
        return 0.0
    if x == b:
        return 1.0
    if x < b:
        return (x - a) / (b - a) if (b - a) != 0 else 0.0
    else:
        return (c - x) / (c - b) if (c - b) != 0 else 0.0

membership_funcs = {
    'taste': {
        'sweet': (0, 0, 2.5),
        'salty': (2, 3.5, 5),
        'spicy': (4, 5.5, 7),
        'sour': (6, 7.5, 8.5),
        'bitter': (8, 10, 10)
    },
    'price': {
        'cheap': (0, 0, 4),
        'medium': (3, 5, 7),
        'expensive': (6, 10, 10)
    },
    'temperature': {
        'cold': (0, 0, 4),
        'warm': (3, 5, 7),
        'hot': (6, 10, 10)
    },
    'prep_time': {
        'fast': (0, 0, 4),
        'medium': (3, 5, 7),
        'long': (6, 10, 10)
    },
    'calories': {
        'low': (0, 0, 4),
        'medium': (3, 5, 7),
        'high': (6, 10, 10)
    },
    'availability': {
        'common': (0, 0, 4),
        'seasonal': (3, 5, 7),
        'rare': (6, 10, 10)
    },
    'satiety': {
        'light': (0, 0, 4),
        'medium': (3, 5, 7),
        'filling': (6, 10, 10)
    }
}

feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas przygotowania': 'prep_time',
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'poziom sytości': 'satiety'
}

feature_sliders = {
    'smak': "| słodkie --- słone --- pikantne --- kwaśne --- gorzkie |",
    'cena': "| tanie --- średnie --- drogie |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas przygotowania': "| szybkie --- średnie --- długie |",
    'kaloryczność': "| niskokaloryczne --- średniokaloryczne --- wysokokaloryczne |",
    'dostępność': "| powszechna --- sezonowa --- rzadka |",
    'poziom sytości': "| lekka --- średnia --- sycąca |"
}

feature_list = [
    ('smak', 'taste'),
    ('cena', 'price'),
    ('temperatura', 'temperature'),
    ('czas przygotowania', 'prep_time'),
    ('kaloryczność', 'calories'),
    ('dostępność', 'availability'),
    ('poziom sytości', 'satiety')
]

# Dane numeryczne potraw (wycięto dla skrócenia)
dishes = {...}  # dane jak wcześniej

print("Wprowadź swoje preferencje dla cech (0-10):")
user_pref_values = {}
for pol_feature, internal_key in feature_list:
    print(f"\nPreferencja dla cechy '{pol_feature.capitalize()}':")
    print(feature_sliders[pol_feature])
    val = input("Wybierz poziom (0-10): ")
    try:
        val = float(val)
    except ValueError:
        val = 0.0
    user_pref_values[internal_key] = max(0.0, min(10.0, val))

user_pref_membership = {}
for feature, val in user_pref_values.items():
    user_pref_membership[feature] = {
        cat: triangular_membership(val, *params)
        for cat, params in membership_funcs[feature].items()
    }

print("\nUstal teraz kolejność ważności cech od najważniejszej do najmniej ważnej.")
print("Wpisz 7 unikalnych numerów odpowiadających cechom, oddzielonych spacjami.")
print("Mapowanie cech na numery:")
for i, (pol, _) in enumerate(feature_list, start=1):
    print(f"  {i}. {pol}")
order_input = input("Kolejność cech (np. '4 1 2 7 5 3 6'): ")

try:
    indices = [int(i) - 1 for i in order_input.strip().split()]
    if sorted(indices) != list(range(7)):
        raise ValueError
    order_features = [feature_list[i][1] for i in indices]
except:
    print("\nBłąd: podano nieprawidłową kolejność cech. Upewnij się, że wpisano 7 różnych liczb od 1 do 7.")
    exit(1)

weights = {}
total = sum(range(1, 8))
for rank, feature in enumerate(order_features):
    weights[feature] = (7 - rank) / total

results = []
for dish_name, feat_values in dishes.items():
    score = 0.0
    for feature, cats in membership_funcs.items():
        dish_val = feat_values[feature]
        feature_match = sum(
            user_pref_membership[feature][cat] * triangular_membership(dish_val, *params)
            for cat, params in cats.items()
        )
        score += weights[feature] * feature_match
    results.append((dish_name, score))

results.sort(key=lambda x: x[1], reverse=True)
print("\nRanking rekomendowanych potraw:")
for i, (dish, score) in enumerate(results, start=1):
    print(f"{i}. {dish} – dopasowanie: {score:.2f}")