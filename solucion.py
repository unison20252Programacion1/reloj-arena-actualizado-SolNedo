# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"
    # la segunda línea no puede estar vacía: el primer carácter se usa para dibujar
    if s is None or len(s) == 0:
        return "Error: El caracter no puede ser una cadena vacia"
    ch = s[0]
    lines = []
    # Parte superior: m líneas, desde 2*m-1 hasta 1
    for k in range(0, m):
        espacios = k
        cuenta = 2 * (m - k) - 1
        lines.append(" " * espacios + ch * cuenta)
    # Parte inferior: m-1 líneas, desde 3 hasta 2*m-1
    for l in range(1, m):
        espacios = m - l - 1
        cuenta = 2 * l + 1
        lines.append(" " * espacios + ch * cuenta)
    return "\n".join(lines)
    
    # implementar la lógica para generar el reloj de arena en ASCII
