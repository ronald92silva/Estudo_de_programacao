largura = float(input("Qual a largura:\n"))
altura = float(input("Altura:\n"))

rendeTinta = float(2)

area_a_pintar = largura * altura

qt_tinta = area_a_pintar // rendeTinta

if area_a_pintar % rendeTinta > 0:
    qt_tinta += 1

print('A área à pintar é de {:.2f}'.format(area_a_pintar))

print(f"Você precisará de {qt_tinta} litros de tinta.")
