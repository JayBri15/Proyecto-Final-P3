# Plantilla de Caso de Prueba

**ID del caso:** TC-001

**Título:** [Breve título del caso]

**Descripción:**
Descripción detallada del objetivo del caso de prueba.

**Precondiciones:**
- Listar estados previos (p. ej. usuario autenticado, existencia de productos)

**Pasos:**
1. Paso 1: navegar a `Lista.html`
2. Paso 2: Click en "Crear" (ir a `Crear.html`)
3. Paso 3: Llenar campos y enviar

**Datos de prueba:**
- Nombre: "Producto Prueba"
- Descripción: "Descripción"
- Precio: 10.00

**Resultado esperado:**
- El producto aparece en `Lista.html` con los datos correctos.

**Resultado real:**
- (Completar tras ejecución)

**Estado:**
- (Pass/Fail)

**Evidencia:**
- Ruta a captura de pantalla o log: `tests/reports/screenshots/<archivo>`

**Observaciones / Defectos:**
- Si falla, adjuntar link al ticket de Jira y pasos para reproducir.

---
Plantilla rápida para pruebas automatizadas (`pytest`):

1. Nombre del test: `test_crear_producto` — ubicar en `tests/test_cases/test_crear.py`
2. Preparación: limpiar el estado si aplica (fixture)
3. Ejecución: ejecutar los pasos del caso
4. Verificación: assert sobre DOM o datos persistidos
