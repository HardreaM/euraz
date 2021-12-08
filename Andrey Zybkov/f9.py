def f (mass, cost, y, k):
    cost_per_kg = cost / mass
    print(y*cost_per_kg)
    print(k/cost_per_kg)

f(1.5, 159, 3, 700)