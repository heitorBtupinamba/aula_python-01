workshop1 = {"Ana","Bruna","Cleuza","Dafne","Elena","Ana","Caio"}
workshop2 = {"Alice","Brenda","Caio", "Douglas","Eithor"}

participantes_a = set(workshop1)
participantes_b = set(workshop2)

print(f"Participantes do evento 1: {participantes_a}")
print(f"Participantes do evento 2: {participantes_b}")

todos_participantes = participantes_a.union(participantes_b)
print(f"Participantes: {todos_participantes}")
print(f"Total de participantes: {len(todos_participantes)}")

ambos_workshops = participantes_a.intersection(participantes_b)
print(ambos_workshops)