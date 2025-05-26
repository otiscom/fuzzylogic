# -*- coding: utf-8 -*-
# System rekomendacji potraw oparty na logice rozmytej

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

# Funkcje przynależności (0-10)
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

# Mapowanie polskich nazw cech
feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas przygotowania': 'prep_time',
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'poziom sytości': 'satiety'
}

# Suwaki
feature_sliders = {
    'smak': "| słodkie --- słone --- pikantne --- kwaśne --- gorzkie |",
    'cena': "| tanie --- średnie --- drogie |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas przygotowania': "| szybkie --- średnie --- długie |",
    'kaloryczność': "| niskokaloryczne --- średniokaloryczne --- wysokokaloryczne |",
    'dostępność': "| powszechna --- sezonowa --- rzadka |",
    'poziom sytości': "| lekka --- średnia --- sycąca |"
}

# Dane potraw (0–10)
dishes = {
    "Burger": {'taste': 4, 'price': 5, 'temperature': 9, 'prep_time': 1, 'calories': 9, 'availability': 1, 'satiety': 9},
    "Lody": {'taste': 1, 'price': 1, 'temperature': 1, 'prep_time': 1, 'calories': 5, 'availability': 1, 'satiety': 1},
    "Skrzydełka (KFC)": {'taste': 6, 'price': 5, 'temperature': 9, 'prep_time': 1, 'calories': 9, 'availability': 1, 'satiety': 5},
    "Sushi": {'taste': 4, 'price': 9, 'temperature': 1, 'prep_time': 5, 'calories': 1, 'availability': 5, 'satiety': 1},
    "Naleśniki": {'taste': 1, 'price': 1, 'temperature': 5, 'prep_time': 5, 'calories': 5, 'availability': 1, 'satiety': 5},
    "Makaron": {'taste': 4, 'price': 5, 'temperature': 9, 'prep_time': 5, 'calories': 5, 'availability': 1, 'satiety': 9},
    "Pizza": {'taste': 4, 'price': 5, 'temperature': 9, 'prep_time': 5, 'calories': 9, 'availability': 1, 'satiety': 9},
    "Pierogi": {'taste': 4, 'price': 1, 'temperature': 5, 'prep_time': 5, 'calories': 5, 'availability': 1, 'satiety': 5},
    "Schabowy": {'taste': 4, 'price': 5, 'temperature': 9, 'prep_time': 5, 'calories': 9, 'availability': 1, 'satiety': 9},
    "Frytki": {'taste': 4, 'price': 1, 'temperature': 9, 'prep_time': 1, 'calories': 9, 'availability': 1, 'satiety': 1},
    "Zapiekanka": {'taste': 4, 'price': 1, 'temperature': 9, 'prep_time': 1, 'calories': 5, 'availability': 1, 'satiety': 5},
    "Bigos": {'taste': 4, 'price': 5, 'temperature': 9, 'prep_time': 9, 'calories': 9, 'availability': 5, 'satiety': 9},
    "Żurek": {'taste': 8, 'price': 1, 'temperature': 9, 'prep_time': 5, 'calories': 5, 'availability': 1, 'satiety': 5},
    "Kebab": {'taste': 6, 'price': 5, 'temperature': 9, 'prep_time': 1, 'calories': 9, 'availability': 1, 'satiety': 9},
    "Sałatka Cezar": {'taste': 4, 'price': 5, 'temperature': 1, 'prep_time': 1, 'calories': 1, 'availability': 1, 'satiety': 1},
    "Tacos": {'taste': 6, 'price': 5, 'temperature': 5, 'prep_time': 1, 'calories': 5, 'availability': 5, 'satiety': 5},
    "Pączki": {'taste': 1, 'price': 1, 'temperature': 5, 'prep_time': 5, 'calories': 9, 'availability': 1, 'satiety': 1},
    "Hot-dog": {'taste': 4, 'price': 1, 'temperature': 9, 'prep_time': 1, 'calories': 9, 'availability': 1, 'satiety': 5},
    "Kopytka": {'taste': 4, 'price': 1, 'temperature': 9, 'prep_time': 5, 'calories': 5, 'availability': 1, 'satiety': 5},
    "Sernik": {'taste': 1, 'price': 5, 'temperature': 1, 'prep_time': 9, 'calories': 9, 'availability': 1, 'satiety': 5}
}

# 1. Preferencje użytkownika
print("Wprowadź swoje preferencje dla cech (0–10):")
user_pref_values = {}
for pol_feature in feature_key:
    internal_key = feature_key[pol_feature]
    print(f"\nPreferencja dla cechy '{pol_feature.capitalize()}':")
    print(feature_sliders[pol_feature])
    val = input("Wybierz poziom (0–10): ")
    try:
        val = float(val)
    except ValueError:
        val = 0.0
    val = min(max(val, 0.0), 10.0)
    user_pref_values[internal_key] = val

# 2. Fuzzyfikacja preferencji
user_pref_membership = {}
for feature, val in user_pref_values.items():
    categories = membership_funcs[feature]
    user_pref_membership[feature] = {}
    for cat, (a, b, c) in categories.items():
        user_pref_membership[feature][cat] = triangular_membership(val, a, b, c)

# 3. Kolejność ważności cech wg numerów
print("\nUstal teraz kolejność ważności cech od najważniejszej do najmniej ważnej.")
print("Wpisz 7 unikalnych numerów odpowiadających cechom, oddzielonych spacjami.")
num_to_feature = {
    1: 'taste',
    2: 'price',
    3: 'temperature',
    4: 'prep_time',
    5: 'calories',
    6: 'availability',
    7: 'satiety'
}
for num, feat in num_to_feature.items():
    pl_name = list(feature_key.keys())[list(feature_key.values()).index(feat)]
    print(f"  {num}. {pl_name}")

order_input = input("\nKolejność cech (np. '4 1 2 7 5 3 6'): ")
try:
    order_nums = list(map(int, order_input.strip().split()))
    if sorted(order_nums) != list(range(1, 8)):
        raise ValueError
except ValueError:
    print("Błąd: Wprowadź dokładnie 7 unikalnych numerów od 1 do 7.")
    exit(1)

order_features = [num_to_feature[n] for n in order_nums]
weights = {}
total = 0
for rank, feature in enumerate(order_features, start=1):
    w = len(order_features) - (rank - 1)
    weights[feature] = w
    total += w
for feature in weights:
    weights[feature] /= total

# 4. Ranking potraw
results = []
for dish_name, feat_values in dishes.items():
    score = 0.0
    for feature, cats in membership_funcs.items():
        dish_val = feat_values[feature]
        feature_match = 0.0
        for cat, (a, b, c) in cats.items():
            dish_mem = triangular_membership(dish_val, a, b, c)
            user_mem = user_pref_membership[feature][cat]
            feature_match += user_mem * dish_mem
        score += weights[feature] * feature_match
    results.append((dish_name, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\n📋 Ranking rekomendowanych potraw:")
for i, (dish, score) in enumerate(results, start=1):
    print(f"{i}. {dish} – dopasowanie: {score:.2f}")
