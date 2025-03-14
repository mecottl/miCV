import matplotlib.pyplot as plt

# Definir los colores en hexadecimal nuevamente
colores_morado = [
    "#D92FFF", "#BA00E9", "#A400D1", "#8E00B8",
    "#6A21C1", "#5310A3", "#40008C", "#39007D"
]

# Crear la figura con un tamaño adecuado
fig, ax = plt.subplots(figsize=(12, 3))

# Dibujar los rectángulos con los colores y agregar los códigos hexadecimales
for i, color in enumerate(colores_morado):
    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
    ax.text(i + 0.5, -0.1, color, ha='center', va='center', fontsize=10, 
            color='black', fontweight='bold')

# Ajustar los límites y ocultar ejes
ax.set_xlim(0, len(colores_morado))
ax.set_ylim(-0.5, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Guardar la imagen
plt.savefig("paleta_morado_hexa.png", dpi=300, bbox_inches='tight')

# Mostrar la imagen
plt.show()
