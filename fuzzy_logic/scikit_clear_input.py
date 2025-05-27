import numpy as np
import skfuzzy as fuzz

# ——— MODEL DEFINITIONS ———

# Input domain from 0 to 10 in 0.1 steps
x_universe = np.arange(0, 10.1, 0.1)

# Fuzzy membership functions for all food features
membership_funcs = {
    'taste': {
        'sweet':   fuzz.trimf(x_universe, [0, 0, 2.5]),
        'salty':   fuzz.trimf(x_universe, [2, 3.5, 5]),
        'spicy':   fuzz.trimf(x_universe, [4, 5.5, 7]),
        'sour':    fuzz.trimf(x_universe, [6, 7.5, 8.5]),
        'bitter':  fuzz.trimf(x_universe, [8, 10, 10]),
    },
    'price': {
        'cheap':     fuzz.trimf(x_universe, [0, 0,   4]),
        'medium':    fuzz.trimf(x_universe, [3, 5,   7]),
        'expensive': fuzz.trimf(x_universe, [6, 10, 10]),
    },
    'temperature': {
        'cold': fuzz.trimf(x_universe, [0, 0, 4]),
        'warm': fuzz.trimf(x_universe, [3, 5, 7]),
        'hot':  fuzz.trimf(x_universe, [6, 10,10]),
    },
    'prep_time': {
        'fast':   fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'long':   fuzz.trimf(x_universe, [6,10,10]),
    },
    'calories': {
        'low':    fuzz.trimf(x_universe, [0, 0, 4]),
        'medium': fuzz.trimf(x_universe, [3, 5, 7]),
        'high':   fuzz.trimf(x_universe, [6,10,10]),
    },
    'availability': {
        'common':   fuzz.trimf(x_universe, [0, 0, 4]),
        'seasonal': fuzz.trimf(x_universe, [3, 5, 7]),
        'rare':     fuzz.trimf(x_universe, [6,10,10]),
    },
    'satiety': {
        'light':   fuzz.trimf(x_universe, [0, 0, 4]),
        'medium':  fuzz.trimf(x_universe, [3, 5, 7]),
        'filling': fuzz.trimf(x_universe, [6,10,10]),
    },
}

# Map Polish labels to internal feature keys
feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas przygotowania': 'prep_time',
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'poziom sytości': 'satiety',
}

# Slider labels for console prompts
feature_sliders = {
    'smak': "| słodkie --- słone --- pikantne --- kwaśne --- gorzkie |",
    'cena': "| tanie --- średnie --- drogie |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas przygotowania': "| szybkie --- średnie --- długie |",
    'kaloryczność': "| niskokaloryczne --- średniokaloryczne --- wysokokaloryczne |",
    'dostępność': "| powszechna --- sezonowa --- rzadka |",
    'poziom sytości': "| lekka --- średnia --- sycąca |",
}

# Dataset of dishes with feature values (0–10)
dishes = {
    "Burger":          {'taste':4, 'price':5, 'temperature':9, 'prep_time':1, 'calories':9, 'availability':1, 'satiety':9},
    "Lody":            {'taste':0, 'price':1, 'temperature':1, 'prep_time':1, 'calories':5, 'availability':1, 'satiety':1},
    "Skrzydełka (KFC)":{'taste':6, 'price':5, 'temperature':9, 'prep_time':1, 'calories':9, 'availability':1, 'satiety':5},
    "Sushi":           {'taste':4, 'price':9, 'temperature':1, 'prep_time':5, 'calories':1, 'availability':5, 'satiety':1},
    "Naleśniki":       {'taste':1, 'price':1, 'temperature':5, 'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Makaron":         {'taste':4, 'price':5, 'temperature':9, 'prep_time':5, 'calories':5, 'availability':1, 'satiety':9},
    "Pizza":           {'taste':4, 'price':5, 'temperature':9, 'prep_time':5, 'calories':9, 'availability':1, 'satiety':9},
    "Pierogi":         {'taste':4, 'price':1, 'temperature':5, 'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Schabowy":        {'taste':4, 'price':5, 'temperature':9, 'prep_time':5, 'calories':9, 'availability':1, 'satiety':9},
    "Frytki":          {'taste':4, 'price':1, 'temperature':9, 'prep_time':1, 'calories':9, 'availability':1, 'satiety':1},
    "Zapiekanka":      {'taste':4, 'price':1, 'temperature':9, 'prep_time':1, 'calories':5, 'availability':1, 'satiety':5},
    "Bigos":           {'taste':4, 'price':5, 'temperature':9, 'prep_time':9, 'calories':9, 'availability':5, 'satiety':9},
    "Żurek":           {'taste':8, 'price':1, 'temperature':9, 'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Kebab":           {'taste':6, 'price':5, 'temperature':9, 'prep_time':1, 'calories':9, 'availability':1, 'satiety':9},
    "Sałatka Cezar":   {'taste':4, 'price':5, 'temperature':1, 'prep_time':1, 'calories':1, 'availability':1, 'satiety':1},
    "Tacos":           {'taste':6, 'price':5, 'temperature':5, 'prep_time':1, 'calories':5, 'availability':5, 'satiety':5},
    "Pączki":          {'taste':1, 'price':1, 'temperature':5, 'prep_time':5, 'calories':9, 'availability':1, 'satiety':1},
    "Hot-dog":         {'taste':4, 'price':1, 'temperature':9, 'prep_time':1, 'calories':9, 'availability':1, 'satiety':5},
    "Kopytka":         {'taste':4, 'price':1, 'temperature':9, 'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Sernik":          {'taste':1, 'price':5, 'temperature':1, 'prep_time':9, 'calories':9, 'availability':1, 'satiety':5},
}

# ——— DATA COLLECTION ———

def collect_preferences():
    """
    Pyta o wartość 0–10 dla każdej cechy.
    Wpis '#' → wartość None (pominięcie).
    Zwraca: dict feature_key -> float|None
    """
    raw = {}
    print("Wprowadź swoje wartości (0–10). Wpisz '#' aby pominąć.")
    for pl, key in feature_key.items():
        print(f"\nPreferencja dla '{pl}':")
        print(feature_sliders[pl])
        v = input("Twoja wartość (0–10 lub '#'): ").strip()
        if v == '#':
            raw[key] = None
        else:
            try:
                n = float(v)
            except ValueError:
                n = 0.0
            raw[key] = min(max(n, 0.0), 10.0)
    return raw

# ——— DATA PROCESSING ———

def fuzzify(prefs):
    """
    prefs: dict feature -> float or None
    Pomija None, fuzzyfikuje pozostałe.
    Zwraca: dict feature -> dict category -> membership
    """
    mem = {}
    for feat, val in prefs.items():
        if val is None:
            continue
        mem[feat] = {
            cat: fuzz.interp_membership(x_universe, mf, val)
            for cat, mf in membership_funcs[feat].items()
        }
    return mem

def collect_weights(prefs):
    """
    prefs: dict feature -> float|None
    Pyta o ranking tylko nie-pominiętych cech.
    Zwraca: dict feature -> normalized weight (sum=1)
    """
    excluded = {f for f, v in prefs.items() if v is None}
    mapping = {
        1:'taste',2:'price',3:'temperature',4:'prep_time',
        5:'calories',6:'availability',7:'satiety'
    }
    avail = {n:f for n,f in mapping.items() if f not in excluded}

    print("\nUstal ważność cech:")
    for n, feat in avail.items():
        pl = next(pl for pl,k in feature_key.items() if k == feat)
        print(f"  {n}. {pl}")
    nums = list(map(int, input(f"Podaj {len(avail)} unikalnych numerów (np. 3 4 2 6 1 5 7): ").split()))
    order = [avail[n] for n in nums]

    total = sum(range(1, len(order)+1))
    weights = {
        feat: (len(order) - i) / total
        for i, feat in enumerate(order)
    }
    return weights

def score_dishes(user_mem, weights):
    """
    user_mem: dict feat->cat->membership
    weights: dict feat->weight
    Zwraca: lista (dish, score) posortowana malejąco
    """
    results = []
    for name, feats in dishes.items():
        s = 0.0
        for feat, val in feats.items():
            if feat not in user_mem or feat not in weights:
                continue
            dish_mem = {
                cat: fuzz.interp_membership(x_universe, mf, val)
                for cat, mf in membership_funcs[feat].items()
            }
            um = user_mem[feat]
            s += weights[feat] * sum(um[c] * dish_mem[c] for c in dish_mem)
        results.append((name, s))
    return sorted(results, key=lambda x: x[1], reverse=True)

# ——— DISPLAY ———

def display(results):
    print("\nZalecane dania:")
    for i, (dish, score) in enumerate(results, start=1):
        print(f"{i}. {dish} – wynik: {score:.2f}")

# ——— MAIN FLOW ———

if __name__ == "__main__":
    raw_prefs   = collect_preferences()
    user_mem    = fuzzify(raw_prefs)
    weights     = collect_weights(raw_prefs)
    ranking     = score_dishes(user_mem, weights)
    display(ranking)
