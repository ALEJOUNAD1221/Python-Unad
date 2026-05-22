# ==========================================
# SISTEMA DE PROMOCIONES - MENÚ RESTAURANTE
# ==========================================

# Matriz del menú:
# [Nombre del Producto, Categoría, Precio Base]

menu = [
    ["Hamburguesa Especial", "Comida Rápida", 25000],
    ["Pizza Familiar", "Comida Rápida", 42000],
    ["Ensalada César", "Saludable", 18000],
    ["Jugo Natural", "Bebidas", 9000],
    ["Filete de Pollo", "Plato Fuerte", 32000],
    ["Postre de Chocolate", "Postres", 15000]
]

# Variables de la promoción
categoria_objetivo = "Comida Rápida"
umbral_precio = 20000
descuento = 0.15


# ==========================================
# FUNCIÓN PARA CALCULAR PRECIO FINAL
# ==========================================

def calcular_precio_final(categoria, precio_base):
    
    # Verificar condiciones de promoción
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base - (precio_base * descuento)
    else:
        precio_final = precio_base

    return precio_final


# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print("==========================================")
print(" MENÚ DEL RESTAURANTE CON PROMOCIONES ")
print("==========================================\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base:,.0f}")
    print(f"Precio Final: ${precio_final:,.0f}")
    print("------------------------------------------")