# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

### Explicación

- **Qué hace:** dado `x, y, a, b` calcula el **máximo** de rectángulos `a×b` (alineados a ejes) que caben en un `x×y`, permitiendo rotar 90°.
- **Lógica:**  
  - Sin rotación: $N_1=\lfloor x/a\rfloor\cdot\lfloor y/b\rfloor$
  - Todo rotado: $N_2=\lfloor x/b\rfloor\cdot\lfloor y/a\rfloor$
  - Mezcla por **columnas**: $N_x(k)=k\lfloor y/b\rfloor+\lfloor(x-ka)/b\rfloor\lfloor y/a\rfloor$, para $k=0.. \lfloor x/a\rfloor$
  - Mezcla por **filas**: $N_y(k)=k\lfloor x/a\rfloor+\lfloor(y-kb)/a\rfloor\lfloor x/b\rfloor$, para $k=0.. \lfloor y/b\rfloor$
  - **Resultado:** $\max (N_x^*, N_y^*)$ (los casos uniformes ya quedan cubiertos con $k=0$ o $k$ máximo).

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
*[Indica cuál bonus implementaste: Opción 1 (techo triangular) o Opción 2 (rectángulos superpuestos)]*




### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*




---

## 🤔 Supuestos y Decisiones

*[Si tuviste que tomar algún supuesto o decisión de diseño, explícalo aquí]*

