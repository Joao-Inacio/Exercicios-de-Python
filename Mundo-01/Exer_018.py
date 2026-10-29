import math

angulo = float(input("Digite o ângulo que você deseja: "))

angulo_ran = math.radians(angulo)

seno = math.sin(angulo_ran)
cosseno = math.cos(angulo_ran)
tangente = math.tan(angulo_ran)

print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")
