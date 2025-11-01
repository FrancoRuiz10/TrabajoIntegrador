***PROYECTO CORREO ELECTRONICO***

el objetivo de este proyecto es realizar un sistema de mensajeria correo electronico interno 

para una empresa

Intregantes:
Franco Ruiz
Kevin Vargas

## Complejidad Algorítmica

Las operaciones principales del sistema de gestión de carpetas tienen las siguientes complejidades:

- `buscar_mensajes(criterio)`:  
  - Complejidad: **O(n)**  
  - Recorre todos los mensajes en la carpeta actual y sus subcarpetas de forma recursiva.  
  - `n` representa el total de mensajes en el árbol de carpetas.

- `mover_mensaje(mensaje, carpeta_destino)`:  
  - Complejidad: **O(1)** si se tiene acceso directo a ambas carpetas.  
  - Si se requiere buscar el mensaje primero, la operación puede ser **O(n)**.

- `mostrar_estructura()`:  
  - Complejidad: **O(c + m)**  
  - Donde `c` es el número total de carpetas y `m` el número total de mensajes.  
  - Utiliza recursividad para recorrer el árbol completo.

---

## Casos Límite y Manejo de Errores

El sistema contempla los siguientes escenarios especiales:

- **Mover mensaje a carpeta inexistente**:  
    Si el parámetro carpeta_destino no está definido o no es válido, es aconsejable realizar una verificación previa antes de intentar mover el mensaje. Actualmente, el método no genera una excepción específica en estos casos, pero se puede incorporar una validación utilizando funciones como isinstance() o hasattr() para asegurar que el destino sea una carpeta válida.

- **Mensaje no encontrado en la carpeta origen**:  
    En caso de que el mensaje no se encuentre dentro de la carpeta origen, la operación de movimiento no se ejecuta. Para mejorar la trazabilidad y el control de errores, se sugiere ampliar el método para emitir una advertencia o registrar el intento fallido mediante logs o excepciones personalizadas.

- **Búsqueda sin coincidencias**:  
    Cuando no se encuentran coincidencias durante la búsqueda, el método buscar_mensajes() devuelve una lista vacía. Esto facilita el manejo del resultado sin generar errores, permitiendo que el sistema responda de forma controlada con mensajes informativos como "No se encontraron resultados".

- **Carpetas vacías**:  
    Cuando una carpeta no contiene mensajes ni subcarpetas, el método mostrar_estructura() imprime únicamente su nombre. Esto asegura que la representación jerárquica del árbol se mantenga completa y coherente, incluso en casos donde algunas carpetas estén vacías.

---

## Recomendaciones
    Es recomendable incorporar validaciones explícitas dentro del método mover_mensaje() para prevenir fallos silenciosos y asegurar que las condiciones necesarias se cumplan antes de ejecutar la operación.

    Se sugiere documentar claramente los tipos esperados para los parámetros de cada método (por ejemplo, instancias de Mensaje o Carpeta) a fin de mejorar la legibilidad, facilitar el mantenimiento y permitir herramientas de análisis estático.

    Es importante incluir pruebas unitarias que contemplen estos escenarios, especialmente los casos límite, para garantizar la robustez del sistema ante entradas inesperadas o malformadas.