import numpy as np
import skfuzzy as fuzz

# Input domain from 0 to 10 in 0.1 steps
x_universe = np.arange(0, 10.1, 0.1)

# Fuzzy membership functions for all food features
membership_funcs = {
    'taste': {
        'sweet': fuzz.trimf(x_universe, [0, 0, 2.5]),
        'salty': fuzz.trimf(x_universe, [2, 3.5, 5]),
        'spicy': fuzz.trimf(x_universe, [4, 5.5, 7]),
        'sour': fuzz.trimf(x_universe, [6, 7.5, 8.5]),
        'bitter': fuzz.trimf(x_universe, [8, 10, 10])
    },
    'price': {
        'cheap': fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'expensive': fuzz.trimf(x_universe, [6, 10, 10])
    },
    'temperature': {
        'cold': fuzz.trimf(x_universe, [0, 0, 4]),
        'warm': fuzz.trimf(x_universe, [3, 5, 7]),
        'hot': fuzz.trimf(x_universe, [6, 10, 10])
    },
    'prep_time': {
        'fast': fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'long': fuzz.trimf(x_universe, [6, 10, 10])
    },
    'calories': {
        'low': fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'high': fuzz.trimf(x_universe, [6, 10, 10])
    },
    'availability': {
        'common': fuzz.trimf(x_universe, [0, 0, 4]),
        'seasonal': fuzz.trimf(x_universe, [3, 5, 7]),
        'rare': fuzz.trimf(x_universe, [6, 10, 10])
    },
    'satiety': {
        'light': fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'filling': fuzz.trimf(x_universe, [6, 10, 10])
    }
}

# Map of feature names from Polish to internal keys
feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas przygotowania': 'prep_time',
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'poziom sytości': 'satiety'
}

# Labels for sliders shown in CLI
feature_sliders = {
    'smak': "| słodkie --- słone --- pikantne --- kwaśne --- gorzkie |",
    'cena': "| tanie --- średnie --- drogie |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas przygotowania': "| szybkie --- średnie --- długie |",
    'kaloryczność': "| niskokaloryczne --- średniokaloryczne --- wysokokaloryczne |",
    'dostępność': "| powszechna --- sezonowa --- rzadka |",
    'poziom sytości': "| lekka --- średnia --- sycąca |"
}

# Dataset of dishes and their features
# Each feature value is in range 0–10
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

# Computes fuzzy membership for a given value against all category functions
def ask_user_preferences():
    """
    Pyta użytkownika o wartość 0–10 dla każdej cechy.
    Jeśli wpisze '#', ta cecha jest pomijana (wartość = None).
    Zwraca: dict feature -> float | None
    """
    print("Wprowadź swoje wartości preferencji dla każdej cechy (0–10). Wpisz '#' aby pominąć.")
    preferences = {}
    for pl_name, key in feature_key.items():
        print(f"Preferencja dla '{pl_name.capitalize()}':")
        print(feature_sliders[pl_name])
        val = input("Twoja wartość (0–10 lub '#'): ").strip()
        if val == "#":
            preferences[key] = None
            continue
        try:
            num = float(val)
        except ValueError:
            num = 0.0
        preferences[key] = min(max(num, 0.0), 10.0)
    return preferences

# Computes fuzzy membership dict for all user preferences
def compute_user_memberships(user_values):
    return {
        feature: {
            cat: fuzz.interp_membership(x_universe, mf, user_values[feature])
            for cat, mf in membership_funcs[feature].items()
        } for feature in user_values
    }

# Asks the user to rank the importance of each feature and converts to normalized weights
def ask_user_feature_weights(excluded_features=None):
    """
    Pyta użytkownika o ranking ważności tylko dla nie-pominiętych cech.
    Input:
      excluded_features: set internal_key cech, które mają być pominięte
    Return: dict feature -> normalizowana waga (suma=1)
    """
    if excluded_features is None:
        excluded_features = set()

    # Budujemy mapę tylko dla cech nie-pominiętych
    num_to_feature = {
        1:'taste',2:'price',3:'temperature',4:'prep_time',
        5:'calories',6:'availability',7:'satiety'
    }
    available = {n: f for n, f in num_to_feature.items() if f not in excluded_features}

    print("\nTeraz uporządkuj ważność poniższych cech:")
    for num, feat in available.items():
        pl = next(pl for pl,k in feature_key.items() if k == feat)
        print(f"  {num}. {pl}")
    order_input = input(f"Kolejność (podaj {len(available)} unikalnych numerów): ").split()

    try:
        order_nums = list(map(int, order_input))
        if set(order_nums) != set(available.keys()):
            raise ValueError
    except ValueError:
        print("Błąd: podaj dokładnie odfiltrowane numery raz każdy.")
        exit(1)

    order_features = [available[n] for n in order_nums]
    # Nadawanie wag malejąco od len(...) do 1 i normalizacja sumy
    weights = {}
    total = sum(range(1, len(order_features)+1))
    for rank, feature in enumerate(order_features, start=1):
        w = len(order_features) - (rank - 1)
        weights[feature] = w / total

    return weights


# Computes the recommendation score for all dishes
def compute_scores(user_membership, weights):
    results = []
    for dish_name, features in dishes.items():
        score = 0.0
        for feature, dish_val in features.items():
            dish_mems = {
                cat: fuzz.interp_membership(x_universe, mf, dish_val)
                for cat, mf in membership_funcs[feature].items()
            }
            user_mems = user_membership[feature]
            feature_score = sum(user_mems[cat] * dish_mems[cat] for cat in dish_mems)
            score += weights[feature] * feature_score
        results.append((dish_name, score))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Prints the final ranking
def show_results(results):
    print("Zalecane dania:")
    for i, (dish, score) in enumerate(results, start=1):
        print(f"{i}. {dish} – wynik: {score:.2f}")


# Przykładowe użycie w main:
if __name__ == "__main__":
    user_values = ask_user_preferences()
    excluded = {feat for feat, val in user_values.items() if val is None}
    # fuzzyfikacja pomija None
    user_membership = compute_user_memberships({k:v for k,v in user_values.items() if v is not None})
    # ranking wag pomija cechy z excluded
    weights = ask_user_feature_weights(excluded_features=excluded)
    results = compute_scores(user_membership, weights)
    show_results(results)