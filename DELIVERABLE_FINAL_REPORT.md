**Portada**:
- **Nombre:** [Tu Nombre Aquí]
- **Matrícula:** [Tu Matrícula Aquí]
- **Título del proyecto:** Tienda Web - Gestión de Productos y Carrito (Incremento 1)
- **Fecha:** [Fecha de entrega]

**Índice**
1. Inicio
2. Planificación (Estrategia de Trabajo)
  2.1 Nombre del proyecto
  2.2 Tecnologías
  2.3 Objetivo
  2.4 Alcance
  2.5 Cronograma
  2.6 Definición del primer Release (Requerimientos Funcionales y No Funcionales)
3. Metodología Scrum
  3.1 Tareas (Backlog inicial dividido en tareas)
  3.2 Equipo de trabajo (roles y responsabilidades)
  3.3 Herramientas a usar
  3.4 Épicas
  3.5 Ceremonias de Scrum (fechas sugeridas)
  3.6 Historias de usuario (10 historias con criterios de aceptación y puntos)
4. Plan de Pruebas
  4.1 Lista de requerimientos (funcionales y no funcionales)
  4.2 Criterios de aceptación/rechazo de pruebas
  4.3 Herramientas de pruebas y justificación
  4.4 Cronograma de ejecución de pruebas
  4.5 Plantillas para casos de pruebas
  4.6 Equipos de pruebas y responsabilidades
  4.7 Plan de automatización de pruebas
  4.8 Ejecución y evidencia
5. Demostración y Entregables
6. Conclusiones
7. Bibliografía

**1. Inicio**
Este documento describe la planificación, la metodología Scrum aplicada, el plan de pruebas y la evidencia requerida para la entrega final basada en el proyecto existente en este repositorio: aplicación web con páginas `Index`, `Crear`, `Editar`, `Lista`, y `Carrito`, y tests automatizados con `pytest`.

**2. Planificación (Estrategia de Trabajo)**
2.1 Nombre del proyecto
- Tienda Web - Gestión de Productos y Carrito

2.2 Tecnologías
- Frontend: HTML5, CSS, JavaScript (archivos en `docs/HTML`, `docs/CSS`, `docs/JS` del repo)
- Pruebas: Python, `pytest`, Selenium (si aplica) y utilidades en `tests/`.
- Control de versiones: `git` y repositorio GitHub (este repositorio).
- Gestión de proyecto: Jira o Azure DevOps (se recomienda Jira para seguimiento de historias y sprints).

2.3 Objetivo del proyecto
- Desarrollar una aplicación web simple para gestionar productos (crear, listar, editar, eliminar) y un carrito de compras, validando flujos básicos de usuario y calidad mediante pruebas manuales y automatizadas.

2.4 Alcance del proyecto
- Incluye UI estática/cliente con páginas para listar productos, crear/editar productos, carrito y login.
- Incluye pruebas de integración/automatizadas que validan flujos claves (crear producto, editar, eliminar, añadir al carrito, ver carrito, login básico).
- No incluye: pasarelas de pago, autenticación segura por backend, ni persistencia en servidor (si el proyecto actual no la tiene).


2.5 Cronograma del proyecto (actividades, plazos y responsables)

Nota: Se propone un sprint de 2 semanas comenzando el jueves siguiente al día de creación de este plan. Las fechas son ejemplos y pueden ajustarse según el calendario real del equipo.

| Actividad | Fecha inicio | Fecha fin | Duración | Responsable |
|---|---:|---:|---:|---|
| Preparación y análisis / Kickoff | 2025-12-10 | 2025-12-11 | 2 días | Product Owner / Scrum Master |
| Sprint 1 — Implementación Release 1 (Sprint principal) | 2025-12-10 | 2025-12-23 | 2 semanas | Developers (Dev1, Dev2) |
| Desarrollo de HU principales (HU-01 a HU-06) | 2025-12-10 | 2025-12-19 | 8 días | Developers |
| Automatización de pruebas iniciales | 2025-12-15 | 2025-12-21 | 7 días | QA + Devs |
| Pruebas manuales y ejecución final de tests | 2025-12-20 | 2025-12-22 | 3 días | QA |
| Correcciones y ajuste (bugfixing) | 2025-12-22 | 2025-12-23 | 2 días | Dev & QA |
| Demo / Sprint Review y Entrega del incremento | 2025-12-23 | 2025-12-23 | 1 día | Todo el equipo |

Responsables sugeridos (reemplazar por nombres reales):
- Product Owner: [Tu Nombre]
- Scrum Master: [Nombre del Scrum Master]
- Developer 1 (Frontend): Dev1 — implementa `Lista`, `Crear` (JS/CSS)
- Developer 2 (Frontend): Dev2 — implementa `Editar`, `Carrito` (JS/CSS)
- QA / Tester: QA — diseña y ejecuta casos, implementa pruebas `pytest` y E2E

2.6 Definición del primer Release
- Objetivo: Entregar un incremento funcional mínimo que permita gestionar productos y usar un carrito.
- Funcionalidades clave (Release 1):
  - Visualizar la lista de productos (`Lista.html`).
  - Crear un producto (`Crear.html`) y validar campos.
  - Editar un producto (`Editar.html`).
  - Eliminar un producto desde la lista.
  - Añadir/visualizar productos en `Carrito.html`.
  - Navegación básica y opciones de UI en `Index.html`.

- Requerimientos funcionales (RF):
  - RF1: El sistema debe mostrar la lista de productos.
  - RF2: El usuario debe crear un producto con nombre, descripción y precio.
  - RF3: El usuario debe editar un producto existente.
  - RF4: El usuario debe eliminar un producto.
  - RF5: El usuario puede añadir productos al carrito y ver el contenido.

- Requerimientos no funcionales (RNF):
  - RNF1: La aplicación debe cargar la página principal en < 3s (medición aproximada).
  - RNF2: Las validaciones de campos deben ejecutarse en cliente.
  - RNF3: Pruebas automatizadas deben ejecutarse en CI (si aplica) y pasar en el 90% de los escenarios críticos.

**3. Metodología Scrum**
3.1 Definir tareas a ejecutar (ejemplos desglosados por historias)
- T1: Crear componente/lista de productos y markup
- T2: Implementar formulario de creación con validaciones
- T3: Implementar edición de producto
- T4: Implementar eliminación con confirmación
- T5: Implementar carrito (add/remove)
- T6: Integrar flujos con tests automatizados (pytest + Selenium/requests)
- T7: Escritura de documentación y entrega

3.2 Equipo de trabajo
- Product Owner: [Nombre del estudiante] — define prioridades, acepta historias.
- Scrum Master: [Nombre] — facilita ceremonias, elimina impedimentos.
- Developers (2): Frontend/JS, integraciones sencillas.
- QA / Tester (1): Diseña y ejecuta pruebas manuales y automatizadas.

Habilidades requeridas: HTML/CSS/JS, testing con `pytest`, manejo básico de Git, comprensión de Scrum.

3.3 Herramientas que usarían
- Repositorio: GitHub (este repositorio). Razón: control de versiones y fácil integración con CI.
- Gestión de trabajo: Jira o Azure DevOps. Razón: seguimiento de historias, épicas y sprints.
- Pruebas: `pytest`, Selenium (o Playwright). Razón: pruebas reproducibles y automatizables.

3.4 Épicas (agrupar historias relacionadas)
- Épica 1: Gestión de Productos (crear, listar, editar, eliminar)
- Épica 2: Carrito de Compras (añadir, ver, eliminar del carrito)
- Épica 3: Calidad y Pruebas (automatización y documentación)


3.5 Ceremonias de Scrum (fechas y horarios concretos para Sprint 1 — 2025-12-10 a 2025-12-23)

- Sprint Planning: 2025-12-10, 10:00–12:00 — Objetivo: seleccionar historias a completar en el sprint, estimaciones y definición de done.
- Daily Standup: 2025-12-11 a 2025-12-19 (excluyendo fines de semana), 09:30–09:45 — 15 minutos, cada miembro responde: ¿qué hice ayer?, ¿qué haré hoy?, ¿impedimentos?.
- Backlog Grooming / Refinement (opcional): 2025-12-17, 14:00–15:00 — revisar próximas historias y dividir en tareas si es necesario.
- Sprint Review / Demo: 2025-12-23, 16:00–17:00 — demo del incremento (crear/editar/eliminar/añadir al carrito + ejecución de pruebas automatizadas).
- Sprint Retrospective: 2025-12-23, 17:00–17:30 — 30 minutos para identificar mejoras en el proceso.

Notas operativas:
- Reuniones en línea o presenciales según disponibilidad; grabar la demo para incluir en la evidencia del entregable.
- Los horarios son recomendados; ajustarlo al huso horario del equipo.


3.6 Historias de usuario (10 historias con criterios de aceptación, rechazo y puntos de historia)

Nota: Los puntos de historia son estimaciones relativas (1, 2, 3, 5). Todos los criterios detallados se encuentran en:
- `jira_user_stories_detailed.json` (formato JSON para integración con Jira)
- `jira_user_stories_detailed.csv` (formato CSV para importación directa a Jira)

**HU-01 — Ver lista de productos (2 pts)** — Épica: Gestión de Productos
- Como usuario, deseo poder visualizar la lista de productos para elegir uno que deseo comprar.
- Criterios de Aceptación: Página Lista.html muestra nombre/precio, lista no vacía cuando hay productos, mínimo 3 campos (nombre/desc/precio), productos sin autenticación, interfaz clara.
- Criterios de Rechazo: Lista vacía con productos disponibles, info incompleta, carga > 3s, errores de JS.
- Tests: `test_lista.py` (4 tests: happy path, lista vacía, búsqueda, caracteres especiales)

**HU-02 — Crear producto (3 pts)** — Épica: Gestión de Productos
- Como usuario, deseo poder crear un producto nuevo para agregarlo al sistema de inventario.
- Criterios de Aceptación: Formulario con campos (nombre/desc/precio), validación cliente, se guarda en localStorage, aparece en Lista.html, mensaje confirmación, precio con decimales.
- Criterios de Rechazo: Crear sin nombre/precio, no guardar localStorage, no aparecer en lista, precio negativo, sin validación.
- Tests: `test_crear.py` (4 tests: datos válidos, campos faltantes, caracteres especiales, precio negativo)

**HU-03 — Editar producto (3 pts)** — Épica: Gestión de Productos
- Como usuario, deseo poder editar un producto existente para corregir o actualizar su información.
- Criterios de Aceptación: Carga datos en Editar.html, campos editables, guarda en localStorage, cambios en Lista.html, confirmación, validación, opción cancelar.
- Criterios de Rechazo: Editar inexistente, no guardar localStorage, cambios no reflejados, campos vacíos permitidos, precio inválido, sin cancelar.
- Tests: `test_editar.py` (4 tests: datos válidos, inválidos, campos vacíos, descripción larga)

**HU-04 — Eliminar producto (2 pts)** — Épica: Gestión de Productos
- Como usuario, deseo poder eliminar un producto para mantener el inventario actualizado.
- Criterios de Aceptación: Botón eliminar en Lista.html, confirmación previa, elimina de localStorage, desaparece lista, confirmación visual, opción cancelar, otros productos intactos.
- Criterios de Rechazo: Eliminar sin confirmación, no eliminar localStorage, visible después, afectar otros, sin cancelar, eliminar inexistente.
- Tests: `test_eliminar.py` (3 tests: eliminación exitosa, cancelar, eliminar múltiples)

**HU-05 — Añadir al carrito (2 pts)** — Épica: Carrito de Compras
- Como usuario, deseo poder añadir productos al carrito para comprarlos después.
- Criterios de Aceptación: Botón 'Añadir carrito' en Lista.html, cantidad inicial 1, guarda sessionStorage, confirmación, permite múltiples unidades, incrementa cantidad si existe, badge/icono muestra cantidad.
- Criterios de Rechazo: Sin botón, no guarda sessionStorage, no aparece en Carrito.html, sin confirmación, no permite múltiples, carrito se borra al refrescar.
- Tests: `test_carrito.py` (4 tests: añadir producto, carrito vacío, múltiples productos, eliminar)

**HU-06 — Ver carrito y totales (2 pts)** — Épica: Carrito de Compras
- Como usuario, deseo ver el contenido del carrito con detalles y totales para verificar mi compra.
- Criterios de Aceptación: Muestra lista productos, cada uno con nombre/cantidad/precio unitario/subtotal, total general correcto, aumentar/disminuir cantidad, eliminar, carrito vacío visible, totales en tiempo real, validación cantidad (1-999).
- Criterios de Rechazo: Totales incorrectos, sin detalles, no cambiar cantidad, sin eliminar, totales no actualizan, cantidad 0 permitida, carrito no sincroniza.
- Tests: Cubierto en `test_carrito.py`

**HU-07 — Login básico (2 pts)** — Épica: Calidad y Pruebas
- Como usuario, deseo poder iniciar sesión para acceder a mis funcionalidades.
- Criterios de Aceptación: Login exitoso (admin/123), redirección a productos, sesión en sessionStorage, error claro (inválidas), validación campos no vacíos, indicador usuario, cerrar sesión, login no accesible si autenticado.
- Criterios de Rechazo: Login sin usuario/contraseña, no redirigir, no guardar sesión válida, guardar inválida, sin error, acceso sin validar, permitir si hay sesión, sin cerrar.
- Tests: `test_login.py` (4 tests: login exitoso, credenciales inválidas, campos vacíos, contraseña larga)

**HU-08 — Pruebas automatizadas (3 pts)** — Épica: Calidad y Pruebas
- Como desarrollador, deseo tener pruebas automatizadas que validen los flujos críticos para asegurar calidad.
- Criterios de Aceptación: Suite pytest con tests (crear/editar/eliminar/carrito/login), todos pasan, cobertura Happy Path/Negative/Boundary, ejecutables CLI `pytest tests/ -v`, reporte HTML, POM implementado.
- Criterios de Rechazo: Tests fallidos, cobertura < 70%, no ejecutables CLI, sin reportes, código duplicado, sin fixtures, sin documentar, tests flaky.
- Tests: 23 tests estructurados (ver PYTEST_EXECUTION_REPORT.md)

**HU-09 — Reportes y capturas en fallos (1 pt)** — Épica: Calidad y Pruebas
- Como QA, deseo recibir reportes y capturas de pantalla cuando los tests fallan para diagnosticar problemas.
- Criterios de Aceptación: Screenshots en `tests/reports/screenshots`, nombre con test name + timestamp, reporte HTML con path, logs navegador, duración tests, Pass/Fail/Skip, resolución 1024x768, reportes accesibles.
- Criterios de Rechazo: Sin screenshots, sin path en reporte, logs vacíos, reporte ilegible, baja resolución, sin timestamps, no accesibles, sin estructura.
- Tests: Infraestructura configurada en conftest.py

**HU-10 — Responsive básico (2 pts)** — Épica: Calidad y Pruebas
- Como usuario, deseo que las páginas se adapten a diferentes tamaños de pantalla para usar desde móviles.
- Criterios de Aceptación: Viewport 375px sin overflow horizontal, elementos accesibles/clickeables, fuentes legibles (≥12px), imágenes proporcionales, formularios adaptados, botones 44x44px, navegación clara, media queries implementadas.
- Criterios de Rechazo: Overflow horizontal, elementos no accesibles, texto ilegible, imágenes distorsionadas, formularios truncados, botones pequeños, nav confusa, sin responsive.
- Tests: Validación manual en navegador con DevTools

---

**Resumen de Cobertura: 22 puntos de historia totales, 3 épicas, 6 historias mapeadas a tests automatizados (HU-01 a HU-07), 23 casos de prueba implementados**

**4. Plan de Pruebas**
4.1 Lista de requerimientos funcionales y no funcionales (relacionados con las HU)
- Ver sección 2.6 (RF1..RF5) como fuente de requerimientos funcionales.
- No funcionales reseñados en RNF1..RNF3.

4.2 Criterios de aceptación y rechazo de pruebas
- Aceptación: El paso de prueba cumple los criterios definidos para la HU; no quedan defectos críticos abiertos.
- Rechazo: Fallas en validaciones o errores que impidan el flujo primario; se genera un ticket en Jira con pasos para reproducir y logs.

4.3 Herramientas de pruebas y justificación
- `pytest`: framework de pruebas ya presente en el repositorio.
- Selenium (o Playwright): para pruebas E2E en UI; justificar por automatización de acciones en navegador.
- GitHub Actions (o Azure Pipelines): para ejecutar suites en CI.

4.4 Cronograma de ejecución de pruebas
- Fase manual: durante el sprint (día 8-10) — QA ejecuta casos manuales.
- Fase automatizada: integración continua — ejecutar suite en cada PR y en nightly.

4.5 Plantillas para casos de pruebas
- Véase `docs/Test_Case_Template.md` (archivo añadido en el repo).

4.6 Equipos de pruebas y responsabilidades
- QA: diseño y ejecución de casos, reporte de defectos.
- Devs: arreglar defectos reportados, proveer soporte para automatización.

4.7 Plan de automatización de pruebas
- Priorizar HU críticas (HU-01 a HU-06) y automatizarlas primero.
- Uso de `pytest` + Selenium para pasos E2E. Automatizar: creación, edición, eliminación, añadir a carrito, login.
- Integrar ejecución en GitHub Actions para cada PR.

4.8 Ejecución y evidencia
- En el repositorio existen artefactos de pruebas en `tests/reports/screenshots/` (por ejemplo `405_localstorage.json` y `.txt`), y tests en `tests/automation` y `tests/test_cases`.
- Para la entrega, se deben adjuntar las capturas de pantalla o un video (ver sección 5).

**5. Demostración y Entregables**
5.1 Video
- Crear un video (3-6 minutos) mostrando: flujo de creación de producto, edición, eliminación, añadir al carrito y ejecución de la suite `pytest` mostrando tests automatizados que pasan. Incluir la URL del repositorio en pantalla.

5.2 Links funcionales (colocar las URLs reales aquí):
- Repositorio de código: `https://github.com/<usuario>/<repo>` (este repo — reemplazar por la URL real)
- Herramienta de gestión (Jira/Azure DevOps): https://... (poner enlace del tablero con las historias y sprints)
- Código de pruebas automatizadas: ruta en este repo `tests/automation` y `tests/test_cases`.

**6. Conclusiones**
- Este documento adapta la metodología Scrum al incremento 1 del proyecto existente. Para completar la entrega final se necesita subir el video de demostración y el tablero de gestión (Jira/Azure) con las historias creadas.

**7. Bibliografía**
- Scrum Guide — https://scrumguides.org/
- Documentación `pytest` — https://docs.pytest.org

---
Referencias a archivos en el repo:
- Código front-end: `docs/HTML/`, `docs/CSS/`, `docs/JS/` (en la estructura proporcionada).
- Tests: `tests/automation/`, `tests/test_cases/`.
- Capturas de prueba: `tests/reports/screenshots/`.

Fin del documento.
