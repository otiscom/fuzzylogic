#!/usr/bin/env python3
import json
import os
import random
import numpy as np
import skfuzzy as fuzz
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Union

BIAS_FILE = "biases.json"
x_universe = np.arange(0, 10.1, 0.1)

# ——— MODEL DEFINITIONS ———

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
        'cold':  fuzz.trimf(x_universe, [0, 0, 4]),
        'warm':  fuzz.trimf(x_universe, [3, 5, 7]),
        'hot':   fuzz.trimf(x_universe, [6, 10,10]),
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

feature_key = {
    'smak': 'taste',
    'cena': 'price',
    'temperatura': 'temperature',
    'czas przygotowania': 'prep_time',
    'kaloryczność': 'calories',
    'dostępność': 'availability',
    'poziom sytości': 'satiety',
}

feature_sliders = {
    'smak': "| słodkie --- słone --- pikantne --- kwaśne --- gorzkie |",
    'cena': "| tanie --- średnie --- drogie |",
    'temperatura': "| zimne --- ciepłe --- gorące |",
    'czas przygotowania': "| szybkie --- średnie --- długie |",
    'kaloryczność': "| niskokaloryczne --- średniokaloryczne --- wysokokaloryczne |",
    'dostępność': "| powszechna --- sezonowa --- rzadka |",
    'poziom sytości': "| lekka --- średnia --- sycąca |",
}

dishes = {
    "Burger":          {'taste':4, 'price':5, 'temperature':9,  'prep_time':1, 'calories':9, 'availability':1, 'satiety':9},
    "Lody":            {'taste':0, 'price':1, 'temperature':1,  'prep_time':1, 'calories':5, 'availability':1, 'satiety':1},
    "Skrzydełka (KFC)":{'taste':6, 'price':5, 'temperature':9,  'prep_time':1, 'calories':9, 'availability':1, 'satiety':5},
    "Sushi":           {'taste':4, 'price':9, 'temperature':1,  'prep_time':5, 'calories':1, 'availability':5, 'satiety':1},
    "Naleśniki":       {'taste':1, 'price':1, 'temperature':5,  'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Makaron":         {'taste':4, 'price':5, 'temperature':9,  'prep_time':5, 'calories':5, 'availability':1, 'satiety':9},
    "Pizza":           {'taste':4, 'price':5, 'temperature':9,  'prep_time':5, 'calories':9, 'availability':1, 'satiety':9},
    "Pierogi":         {'taste':4, 'price':1, 'temperature':5,  'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Schabowy":        {'taste':4, 'price':5, 'temperature':9,  'prep_time':5, 'calories':9, 'availability':1, 'satiety':9},
    "Frytki":          {'taste':4, 'price':1, 'temperature':9,  'prep_time':1, 'calories':9, 'availability':1, 'satiety':1},
    "Zapiekanka":      {'taste':4, 'price':1, 'temperature':9,  'prep_time':1, 'calories':5, 'availability':1, 'satiety':5},
    "Bigos":           {'taste':4, 'price':5, 'temperature':9,  'prep_time':9, 'calories':9, 'availability':5, 'satiety':9},
    "Żurek":           {'taste':8, 'price':1, 'temperature':9,  'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Kebab":           {'taste':6, 'price':5, 'temperature':9,  'prep_time':1, 'calories':9, 'availability':1, 'satiety':9},
    "Sałatka Cezar":   {'taste':4, 'price':5, 'temperature':1,  'prep_time':1, 'calories':1, 'availability':1, 'satiety':1},
    "Tacos":           {'taste':6, 'price':5, 'temperature':5,  'prep_time':1, 'calories':5, 'availability':5, 'satiety':5},
    "Pączki":          {'taste':1, 'price':1, 'temperature':5,  'prep_time':5, 'calories':9, 'availability':1, 'satiety':1},
    "Hot-dog":         {'taste':4, 'price':1, 'temperature':9,  'prep_time':1, 'calories':9, 'availability':1, 'satiety':5},
    "Kopytka":         {'taste':4, 'price':1, 'temperature':9,  'prep_time':5, 'calories':5, 'availability':1, 'satiety':5},
    "Sernik":          {'taste':1, 'price':5, 'temperature':1,  'prep_time':9, 'calories':9, 'availability':1, 'satiety':5},
}

# ——— TD(λ) MODEL ———

class TDLambda:
    def __init__(self, alpha=0.05, gamma=0.9, lambd=0.8):
        self.alpha, self.gamma, self.lambd = alpha, gamma, lambd
        self.V = defaultdict(float)
        self.E = defaultdict(float)

    def start(self, state: Tuple):
        self.prev_state = state
        self.E.clear()

    def update(self, state: Tuple, reward: float, next_state: Tuple):
        delta = reward + self.gamma * self.V[next_state] - self.V[state]
        self.E[state] += 1.0
        for s in list(self.V):
            self.V[s] += self.alpha * delta * self.E[s]
            self.E[s] *= self.gamma * self.lambd
        self.prev_state = next_state

    def load(self, filename=BIAS_FILE):
        if os.path.exists(filename):
            with open(filename) as f:
                data = json.load(f)
            self.V = defaultdict(float,
                {tuple(json.loads(k)): v for k, v in data.items()})

    def save(self, filename=BIAS_FILE):
        with open(filename, "w") as f:
            json.dump({json.dumps(k): v for k, v in self.V.items()}, f, indent=2)

# ——— INPUT VALIDATION ———

def input_number(prompt: str, allow_float=False) -> Optional[float]:
    valid = set("0123456789.") if allow_float else set("0123456789")
    while True:
        s = input(prompt).strip()
        if s == "#":
            return None
        if all(c in valid for c in s) and s.count('.')<=1:
            return float(s) if allow_float else float(int(s))
        print("Enter a number (0–10) or '#'.")

def input_feedback(prompt: str) -> Optional[int]:
    while True:
        s = input(prompt).strip()
        if s == "#":
            return None
        if s in ("0","1"):
            return int(s)
        print("Enter '0' or '1' or '#'.")

# ——— FUZZY & SCORING ———

def collect_preferences() -> Dict[str, Optional[float]]:
    prefs: Dict[str, Optional[float]] = {}
    print("Enter 0–10 or '#' to skip.")
    for pl, key in feature_key.items():
        print(f"\n{pl.capitalize()} {feature_sliders[pl]}")
        prefs[key] = input_number("Value: ", allow_float=True)
    return prefs

def fuzzify(prefs: Dict[str, float]) -> Dict[str, Dict[str, float]]:
    mem: Dict[str, Dict[str, float]] = {}
    for feat, val in prefs.items():
        if val is None: continue
        mem[feat] = {
            cat: fuzz.interp_membership(x_universe, mf, val)
            for cat, mf in membership_funcs[feat].items()
        }
    return mem

def collect_weights(prefs: Dict[str, float]) -> Dict[str, float]:
    active = [f for f,v in prefs.items() if v is not None]
    print("\nSet feature importance:")
    for i,feat in enumerate(active,1):
        print(f"  {i}. {feat}")
    while True:
        order = input("Order (e.g. '2 1 3'): ").split()
        if len(order)==len(active) and all(o.isdigit() for o in order):
            nums = list(map(int, order))
            if set(nums)==set(range(1,len(active)+1)):
                break
        print(f"Provide {len(active)} unique numbers 1–{len(active)}.")
    total = sum(range(1,len(active)+1))
    return { active[i-1]: (len(active)-i+1)/total for i in nums }

def compute_fuzzy_scores(prefs: Dict[str,float], weights: Dict[str,float]) -> Dict[str,float]:
    user_mem = fuzzify(prefs)
    scores: Dict[str,float] = {}
    for d, feats in dishes.items():
        s = 0.0
        for feat, dish_val in feats.items():
            if feat not in user_mem or feat not in weights: continue
            dish_mem = {
                cat: fuzz.interp_membership(x_universe, mf, dish_val)
                for cat, mf in membership_funcs[feat].items()
            }
            s += weights[feat] * sum(user_mem[feat][c]*dish_mem[c] for c in dish_mem)
        scores[d] = s
    return scores

def compute_final_scores(fuzzy_scores: Dict[str,float], bias: float, beta=0.1) -> Dict[str,float]:
    return { d: fuzzy_scores[d] + beta*bias for d in fuzzy_scores }

def rank_dishes(final_scores: Dict[str,float]) -> List[Tuple[str,float]]:
    return sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

# ——— DISPLAY & FEEDBACK ———

def show_ranked_list_with_annotation(
    ranking: List[Tuple[str,float]],
    fuzzy_scores: Dict[str,float],
    bias_value: float,
    beta: float = 0.1
):
    bias_contrib = beta * bias_value
    print("\n=== DISH RANKING ===")
    for i, (dish, final_score) in enumerate(ranking, 1):
        fz = fuzzy_scores[dish]
        td_delta = final_score - fz
        if td_delta > 0:
            tag = "TD promotion"
        elif td_delta < 0:
            tag = "TD demotion"
        else:
            tag = "pure fuzzy"
        print(f"{i}. {dish} ({final_score:.2f}) — fuzzy: {fz:.2f}; {tag}")

def feedback_loop(ranking: List[Tuple[str,float]], td: TDLambda, state: Tuple):
    for dish, _ in ranking:
        fb = input_feedback(f"\nIs '{dish}' correctly ranked? (0=no,1=yes,#=end): ")
        if fb is None:
            break
        td.update(state, fb, state)

# ——— MAIN ———

def main():
    td = TDLambda()
    td.load()

    prefs = collect_preferences()
    weights = collect_weights(prefs)
    fuzzy_scores = compute_fuzzy_scores(prefs, weights)

    state = tuple(prefs[k] for k in sorted(prefs))
    td.start(state)

    bias_val = td.V[state]
    final_scores = compute_final_scores(fuzzy_scores, bias_val)
    ranking = rank_dishes(final_scores)

    show_ranked_list_with_annotation(ranking, fuzzy_scores, bias_val)
    feedback_loop(ranking, td, state)

    td.save()
    print("\nThank you for your feedback!")

if __name__ == "__main__":
    main()
