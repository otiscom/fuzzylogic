# -*- coding: utf-8 -*-
# System rekomendacji potraw oparty na logice rozmytej

# Definicja trójkątnej funkcji przynależności
def triangular_membership(x, a, b, c):
    """Oblicza stopień przynależności (μ) dla wartości x
    względem trójkątnej funkcji przynależności zdefiniowanej
    przez punkty (a, b, c)."""
    if a == b and b == c:
        return 1.0  # degenerowany przypadek (nieużywany w praktyce)
    if a == b:
        # Left-shoulder triangle (maksimum od a w lewo)
        if x <= b:
            return 1.0
        elif x <= c:
            return (c - x) / float(c - b) if (c - b) != 0 else 0.0
        else:
            return 0.0
    elif b == c:
        # Right-shoulder triangle (maksimum od c w prawo)
        if x >= b:
            return 1.0
        elif x >= a:
            return (x - a) / float(b - a) if (b - a) != 0 else 0.0
        else:
            return 0.0
    else:
        # Wewnętrzna funkcja trójkątna
        if x <= a or x >= c:
            return 0.0
        elif x <= b:
            return (x - a) / float(b - a) if (b - a) != 0 else 0.0
        else:  # x > b and x < c
            return (c - x) / float(c - b) if (c - b) != 0 else 0.0

# Definicje wartości lingwistycznych i ich funkcji przynależności dla każdej cechy
membership_funcs = {
    "smak": {
        "słodkie": (0, 0, 5),
        "słone": (0, 5, 10),
        "pikantne": (5, 10, 10)
    },
    "cena": {
        "tanie": (0, 0, 5),
        "średnie": (0, 5, 10),
        "drogie": (5, 10, 10)
    },
    "temperatura": {
        "zimne": (0, 0, 5),
        "ciepłe": (0, 5, 10),
        "gorące": (5, 10, 10)
    },
    "czas przygotowania": {
        "szybkie": (0, 0, 5),
        "średnie": (0, 5, 10),
        "długie": (5, 10, 10)
    },
    "kaloryczność": {
        "niskokaloryczne": (0, 0, 5),
        "średniokaloryczne": (0, 5, 10),
        "wysokokaloryczne": (5, 10, 10)
    },
    "dostępność": {
        "rzadka": (0, 0, 5),
        "umiarkowana": (0, 5, 10),
        "powszechna": (5, 10, 10)
    },
    "sytość": {
        "lekka": (0, 0, 5),
        "umiarkowana": (0, 5, 10),
        "sycąca": (5, 10, 10)
    }
}

# Baza 20 potraw z przypisanymi wartościami lingwistycznymi cech
dishes = {
    "Burger":        {"smak": "słone", "cena": "średnie", "temperatura": "gorące", "czas przygotowania": "szybkie", "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"},
    "Pizza":         {"smak": "słone", "cena": "średnie", "temperatura": "gorące", "czas przygotowania": "średnie", "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"},
    "Salad":         {"smak": "słone", "cena": "tanie",   "temperatura": "zimne",  "czas przygotowania": "szybkie", "kaloryczność": "niskokaloryczne", "dostępność": "powszechna", "sytość": "lekka"},
    "Sushi":         {"smak": "słone", "cena": "drogie",  "temperatura": "zimne",  "czas przygotowania": "długie",  "kaloryczność": "średniokaloryczne", "dostępność": "umiarkowana", "sytość": "umiarkowana"},
    "Steak":         {"smak": "słone", "cena": "drogie",  "temperatura": "gorące", "czas przygotowania": "średnie", "kaloryczność": "wysokokaloryczne", "dostępność": "umiarkowana", "sytość": "sycąca"},
    "Soup":          {"smak": "słone", "cena": "tanie",   "temperatura": "gorące", "czas przygotowania": "długie",  "kaloryczność": "niskokaloryczne", "dostępność": "powszechna", "sytość": "lekka"},
    "Pasta":         {"smak": "słone", "cena": "średnie", "temperatura": "gorące", "czas przygotowania": "średnie", "kaloryczność": "średniokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"},
    "Curry":         {"smak": "pikantne","cena": "średnie", "temperatura": "gorące", "czas przygotowania": "długie", "kaloryczność": "wysokokaloryczne", "dostępność": "umiarkowana", "sytość": "sycąca"},
    "Ice Cream":     {"smak": "słodkie","cena": "tanie",   "temperatura": "zimne",  "czas przygotowania": "szybkie", "kaloryczność": "średniokaloryczne", "dostępność": "powszechna", "sytość": "lekka"},
    "Cake":          {"smak": "słodkie","cena": "średnie", "temperatura": "ciepłe", "czas przygotowania": "długie",  "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "umiarkowana"},
    "Sandwich":      {"smak": "słone", "cena": "tanie",   "temperatura": "zimne",  "czas przygotowania": "szybkie", "kaloryczność": "średniokaloryczne", "dostępność": "powszechna", "sytość": "umiarkowana"},
    "Fried Chicken": {"smak": "pikantne","cena": "tanie",  "temperatura": "gorące", "czas przygotowania": "średnie", "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"},
    "Tacos":         {"smak": "pikantne","cena": "tanie",  "temperatura": "ciepłe", "czas przygotowania": "szybkie", "kaloryczność": "średniokaloryczne", "dostępność": "rzadka", "sytość": "umiarkowana"},
    "Stew":          {"smak": "słone", "cena": "tanie",   "temperatura": "gorące", "czas przygotowania": "długie",  "kaloryczność": "średniokaloryczne", "dostępność": "umiarkowana", "sytość": "sycąca"},
    "Kebab":         {"smak": "słone", "cena": "tanie",   "temperatura": "gorące", "czas przygotowania": "szybkie", "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"},
    "Pancakes":      {"smak": "słodkie","cena": "tanie",   "temperatura": "ciepłe", "czas przygotowania": "średnie", "kaloryczność": "wysokokaloryczne", "dostępność": "powszechna", "sytość": "umiarkowana"},
    "Burrito":       {"smak": "pikantne","cena": "tanie",  "temperatura": "gorące", "czas przygotowania": "szybkie", "kaloryczność": "wysokokaloryczne", "dostępność": "umiarkowana", "sytość": "sycąca"},
    "Hotdog":        {"smak": "słone", "cena": "tanie",   "temperatura": "gorące", "czas przygotowania": "szybkie", "kaloryczność": "średniokaloryczne", "dostępność": "powszechna", "sytość": "lekka"},
    "Ribs":          {"smak": "słodkie","cena": "drogie",  "temperatura": "gorące", "czas przygotowania": "długie",  "kaloryczność": "wysokokaloryczne", "dostępność": "rzadka", "sytość": "sycąca"},
    "Pierogi":       {"smak": "słone", "cena": "tanie",   "temperatura": "ciepłe", "czas przygotowania": "długie",  "kaloryczność": "średniokaloryczne", "dostępność": "powszechna", "sytość": "sycąca"}
}

# Lista cech (zachowujemy kolejność do wyświetlania i wag)
features = ["smak", "cena", "temperatura", "czas przygotowania", "kaloryczność", "dostępność", "sytość"]

# Powitanie i instrukcje
print("Witaj w systemie rekomendacji potraw (logika rozmyta).")
print("Oceń każdą z poniższych cech w skali od 0 do 10, a następnie podaj kolejność ważności cech.")

# Pobieranie preferencji użytkownika dla każdej cechy
user_values = {}
for feature in features:
    while True:
        try:
            val = float(input(f"Podaj preferencję dla cechy '{feature}' (0–10): "))
        except ValueError:
            print("Błędna wartość. Wprowadź liczbę od 0 do 10.")
            continue
        if val < 0 or val > 10:
            print("Wartość poza zakresem. Podaj liczbę w przedziale 0–10.")
        else:
            user_values[feature] = val
            break

# Pobieranie kolejności ważności cech
print("\nUstal teraz kolejność ważności cech od najważniejszej do najmniej ważnej.")
print("Wpisz 7 unikalnych numerów odpowiadających cechom, oddzielonych spacjami.")
print("Mapowanie cech na numery: ")
for i, feature in enumerate(features, start=1):
    print(f"  {i}. {feature}")
rank_order = []
while True:
    order_input = input("Kolejność cech (np. '4 1 2 7 5 3 6'): ").strip().split()
    if len(order_input) != 7:
        print("Podaj dokładnie 7 liczb w odpowiedniej kolejności.")
        continue
    try:
        rank_order = [int(x) for x in order_input]
    except ValueError:
        print("Błędny format. Użyj numerów oddzielonych spacjami.")
        continue
    # Sprawdzamy poprawność zakresu i unikalność
    if any(n < 1 or n > 7 for n in rank_order) or len(set(rank_order)) != 7:
        print("Podaj 7 *różnych* liczb z zakresu 1–7.")
        continue
    break

# Przypisanie wag na podstawie rankingu (7 dla najważniejszej cechy, ... 1 dla ostatniej)
weights = {}
for position, feat_index in enumerate(rank_order, start=1):
    feat_name = features[feat_index - 1]  # konwersja numer cechy -> nazwa cechy
    weights[feat_name] = 8 - position  # 8-pos => daje 7,6,...,1

# Normalizacja wag (opcjonalnie, żeby sumowały się do 1)
total_weight = sum(weights.values())
for feat in weights:
    weights[feat] = weights[feat] / total_weight

# Fuzzyfikacja preferencji użytkownika - obliczenie μ dla każdej kategorii każdej cechy
user_fuzzy = {}
for feat, val in user_values.items():
    user_fuzzy[feat] = {}
    for category, (a, b, c) in membership_funcs[feat].items():
        mu = triangular_membership(val, a, b, c)
        user_fuzzy[feat][category] = mu

# Obliczenie dopasowania każdej potrawy do preferencji
results = []  # lista (wynik, nazwa potrawy)
for dish_name, attrs in dishes.items():
    total_score = 0.0
    for feat in features:
        dish_cat = attrs[feat]              # kategoria potrawy dla cechy feat
        mu_pref = user_fuzzy[feat][dish_cat]# stopień preferencji użytkownika dla tej kategorii
        total_score += mu_pref * weights[feat]
    results.append((total_score, dish_name))

# Sortowanie wyników malejąco po dopasowaniu
results.sort(reverse=True, key=lambda x: x[0])

# Wyświetlenie rankingu potraw
print("\n=== Rekomendacje potraw ===")
for score, dish_name in results:
    # formatowanie wyniku μ do 2 miejsc po przecinku
    print(f"{dish_name}: μ = {score:.2f}")
