from typing import List
import random
import math

def get_new_alpha(alpha: float) -> float:
    return alpha * 0.5

def calculate_distance(weights: List[float], user_input: List[int]) -> float:
    return round(math.sqrt(sum((user_input[i] - weights[i])**2 for i in range(len(weights)))), 2)

def format_distance(weights: List[float], user_input: List[int], distance: float) -> str:
    terms = " + ".join([f"({weights[i]} - {user_input[i]})^2" for i in range(len(weights))])
    return f"√({terms}) = {distance}"

def update_weights(weights: List[float], alpha: float, user_input: List[int]) -> List[float]:
    return [round(w + alpha * (ui - w), 2) for w, ui in zip(weights, user_input)]

def format_update_process(weights: List[float], alpha: float, user_input: List[int]) -> str:
    return "\n".join(
        [f"{i + 1} = {weights[i]} + {alpha} * ({user_input[i]} - {weights[i]}) = {round(weights[i] + alpha * (user_input[i] - weights[i]), 2)}"
         for i in range(len(weights))]
    )

def main():
    alpha = 0.6
    w1 = [round(random.random(), 2) for _ in range(4)]
    w2 = [round(random.random(), 2) for _ in range(4)]
    inputs = [
        (1, 1, 0, 0),
        (0, 0, 0, 1),
        (1, 0, 0, 0),
        (0, 0, 0, 1)
    ]
    
    print("BOBOT AWAL")
    print(f"W1 = {w1}")
    print(f"W2 = {w2}")

    for _ in range(1):
        for i, inp in enumerate(inputs):
            print(f"\nITERASI-{i + 1}\n")
            print("Bobot Sebelum")
            print(f"W1 = {w1}")
            print(f"W2 = {w2}\n")
            
            d1 = calculate_distance(w1, inp)
            d2 = calculate_distance(w2, inp)

            print("D1:")
            print(format_distance(w1, inp, d1))
            print("\nD2:")
            print(format_distance(w2, inp, d2))
            
            new_alpha = get_new_alpha(alpha)
            print(f"\nα = 0.5 * α lama = 0.5 * {alpha} = {new_alpha}")
            alpha = new_alpha

            if d1 > d2:
                print("\nUpdate W2")
                print(format_update_process(w2, alpha, inp))
                w2 = update_weights(w2, alpha, inp)
            elif d1 < d2:
                print("\nUpdate W1")
                print(format_update_process(w1, alpha, inp))
                w1 = update_weights(w1, alpha, inp)

            print(f"\nW1 = {w1}")
            print(f"W2 = {w2}")

if __name__ == "__main__":
    main()
