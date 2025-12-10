# Guía de Entrega Final — Proyecto Tienda Web

Este documento contiene instrucciones paso a paso para completar la entrega final del proyecto Agile-Scrum, incluyendo importación de historias a Jira, grabación de video de demostración y compilación de enlaces funcionales.

---

## 1. Importar Historias de Usuario a Jira (en Español)

### Paso 1: Preparar el archivo CSV

El archivo `jira_user_stories.csv` en la raíz del repositorio contiene las 10 historias de usuario. Verifica que el archivo esté disponible en:
```
/workspaces/Proyecto-Final-P3/jira_user_stories.csv
```

**Contenido esperado:** 10 filas de historias (HU-01 a HU-10) con columnas:
- Resumen
- Descripción
- Aceptación Criterios
- Puntos de Historia
- Epic
- Tipo
- Prioridad
- Asignado

### Paso 2: Acceder a Jira

1. Abre tu instancia de Jira (Cloud o Server).
2. En la esquina superior derecha, haz clic en el icono de **Configuración** (⚙️ engranaje).
3. En el menú desplegable, selecciona **Sistema** (o **Administración del sistema** en algunas versiones).

### Paso 3: Navegar a Importación de CSV

1. En la página de Sistema, busca la sección **Importación y exportación**.
2. Selecciona **Importar desde CSV** (o `Importación de sistema externo > CSV`).
3. Haz clic en el botón **Importar** o similar.

### Paso 4: Seleccionar el archivo CSV

1. En el asistente de importación, selecciona el archivo `jira_user_stories.csv`.
2. Confirma la **codificación** (UTF-8) y el **delimitador** (coma `,`).
3. Haz clic en **Siguiente**.

### Paso 5: Seleccionar proyecto destino

1. Elige el **proyecto** en el que deseas importar las historias (p. ej., "PROYECTO_TIENDA" con clave "TW").
2. Confirm si deseas crear épicas nuevas o usarlas existentes.
3. Haz clic en **Siguiente**.

### Paso 6: Mapear columnas CSV a campos Jira (en español)

En esta pantalla crucial, mapea cada columna CSV con los campos de Jira:

| Columna CSV | Campo Jira (español) | Ejemplo de valor |
|---|---|---|
| Resumen | Resumen | HU-01 - Ver lista de productos |
| Descripción | Descripción | Mostrar la lista de productos en la página de 'Lista'... |
| Aceptación Criterios | (Opcional) Criterios de aceptación* | La página Lista.html muestra Nombre y Precio... |
| Puntos de Historia | Puntos de historia** | 2 |
| Epic | Nombre de épica | Gestión de Productos |
| Tipo | Tipo | Historia |
| Prioridad | Prioridad | Media |
| Asignado | Asignado | (usuario existente o dejar vacío) |

**Notas importantes:**
- *Si `Criterios de aceptación` no aparece en el listado, crea primero el campo personalizado en `Configuración > Campos > Campos personalizados` como un campo de texto de varias líneas.
- **Si `Puntos de historia` no aparece, busca `Story Points` o crea el campo personalizado (tipo: Número) antes de importar.
- Si algún campo no aparece, déjalo sin mapear (el asistente saltará esa columna).

### Paso 7: Revisar mapeo y ejecutar importación

1. Revisa la vista previa del mapeo; confirma que todos los campos están correctamente asignados.
2. Haz clic en **Importar** para ejecutar la importación.
3. Espera a que se complete. Jira mostrará un log con el número de issues creados y errores (si los hay).

### Paso 8: Verificar historias importadas

1. Abre tu proyecto en Jira.
2. Ve al **Backlog** o **Historias**.
3. Verifica que las 10 historias (HU-01 a HU-10) estén presentes con:
   - Resumen correcto
   - Descripción y criterios de aceptación
   - Puntos de historia asignados
   - Épicas asociadas (Gestión de Productos, Carrito de Compras, Calidad y Pruebas)
   - Prioridades (Media, Alta, Baja)

Si falta algún campo (p. ej., Puntos de historia vacíos), repite los pasos 2-7 con el campo personalizado creado en Jira.

**Próximo paso:** Crea un Sprint 1 con estas historias y planifica según el cronograma en `DELIVERABLE_FINAL_REPORT.md` (2025-12-10 a 2025-12-23).

---

## 2. Grabar y Compartir Video de Demostración

### Requisitos del video:
- Duración: 3-6 minutos.
- Resolución: mínimo 1080p (Full HD) o superior.
- Contenido:
  1. Mostrar la URL del repositorio (GitHub) en pantalla.
  2. Demostrar flujo de creación de producto (`Crear.html`): rellenar formulario, guardar, verificar que aparece en `Lista.html`.
  3. Demostrar edición de producto (`Editar.html`): cambiar datos, guardar, verificar cambios en lista.
  4. Demostrar eliminación de producto: seleccionar producto, eliminar, verificar confirmación y que desaparece de lista.
  5. Demostrar carrito: añadir uno o más productos a `Carrito.html`, mostrar cantidad y total.
  6. Ejecutar suite `pytest`: abrir terminal, navegar a raíz del repo, ejecutar `pytest tests/` o `pytest -v`, mostrar resultados (tests pasando).
  7. Cerrar con un resumen: "Incremento 1 completado con X historias, Y tests, Z puntos de historia."

### Herramientas recomendadas para grabar:
- **Windows**: OBS Studio (gratuito), Camtasia, ScreenFlow, o la herramienta nativa "Grabador de pantalla" (Grabar > Win + G).
- **macOS**: OBS Studio, ScreenFlow, Quicktime (Archivo > Nueva grabación de pantalla).
- **Linux**: OBS Studio, SimpleScreenRecorder, FFmpeg (desde terminal).

### Pasos para grabar con OBS Studio (multiplataforma, gratuito):

1. **Descargar e instalar OBS Studio** (https://obsproject.com/).
2. **Configurar fuente de grabación:**
   - Abre OBS.
   - En `Fuentes`, haz clic en `+` y selecciona `Captura de pantalla` (o `Ventana` si quieres capturar solo una ventana).
   - Selecciona el monitor/ventana a grabar.
3. **Configurar audio** (opcional):
   - En `Dispositivos de audio`, asigna un micrófono si quieres narración.
4. **Configurar salida de grabación:**
   - Ve a `Configuración > Salida`.
   - En la pestaña `Grabación`, elige formato (MP4 o MKV), carpeta destino y calidad (1080p/30fps sugerido).
5. **Iniciar grabación:**
   - Haz clic en `Comenzar grabación`.
   - Realiza la demostración (pasos del requisito anterior).
   - Haz clic en `Detener grabación` cuando termines.
6. **Localizar archivo:**
   - El video se guardará en la carpeta especificada en configuración (p. ej., `~/Videos` o `C:\Users\[Usuario]\Videos\`).

### Dónde subir el video:

Opción A: **YouTube (privado o no listado)**
- Crea un proyecto/playlist privado.
- Sube el video.
- Copia el enlace (p. ej., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
- Comparte el enlace en el documento final o en la entrega de la asignatura.

Opción B: **Google Drive o OneDrive**
- Crea una carpeta compartida.
- Sube el video.
- Comparte el enlace con permisos de visualización.

Opción C: **Repositorio GitHub (GitHub Releases)**
- En tu repositorio GitHub, ve a `Releases`.
- Crea un nuevo release (p. ej., `v1.0.0` o `Release-Entrega-Final`).
- Sube el archivo de video como asset.
- Copia el enlace de descarga del asset.

---

## 3. Compilar Enlaces Funcionales para la Entrega

### Enlace 1: Repositorio de código

**URL:** `https://github.com/JayBri15/Proyecto-Final-P3`

**Verificación:**
- ✅ Abierto al público (o comparte acceso).
- ✅ Contiene carpetas: `docs/HTML`, `docs/CSS`, `docs/JS`, `tests/`.
- ✅ README.md presente con descripción del proyecto.
- ✅ Archivos de configuración: `requirements.txt`, `pytest.ini`, etc.
- ✅ Commit history visible (mínimo 3-5 commits mostrando progreso).

**En el documento final, incluye:**
```
Repositorio: https://github.com/JayBri15/Proyecto-Final-P3
```

### Enlace 2: Tablero de Jira con Historias de Usuario

**Cómo obtener el enlace de Jira:**
1. Abre tu proyecto en Jira.
2. Ve al **Backlog** o **Panel** (Board).
3. Copia la URL del navegador (p. ej., `https://[tu-instancia].atlassian.net/jira/software/c/projects/PROYECTO/board/1`).
4. Comparte el tablero:
   - En Jira Cloud: `Proyecto > Configuración > Permisos de proyecto` → asegúrate de que tu profesor/evaluador tenga acceso.
   - Alternativamente, comparte la URL con permisos de lectura pública (si lo permite la configuración).

**En el documento final, incluye:**
```
Jira - Backlog/Sprint 1: https://[tu-instancia].atlassian.net/jira/software/c/projects/[TU_PROYECTO]/board/[ID]
```

### Enlace 3: Código de Pruebas Automatizadas

**Ubicación en el repositorio:**
```
tests/automation/
tests/test_cases/
  - test_lista.py
  - test_crear.py
  - test_editar.py
  - test_eliminar.py
  - test_carrito.py
  - test_login.py
```

**Cómo verificar que funcionan:**
```bash
cd /workspaces/Proyecto-Final-P3
pip install -r requirements.txt  # Instala dependencias (pytest, etc.)
pytest tests/ -v  # Ejecuta todos los tests
```

**En el documento final, incluye:**
```
Código de pruebas: https://github.com/JayBri15/Proyecto-Final-P3/tree/main/tests/test_cases
Reportes: https://github.com/JayBri15/Proyecto-Final-P3/tree/main/tests/reports
```

### Enlace 4: Video de Demostración

**Formato:**
```
Video de demostración del incremento 1: [URL del video en YouTube/Drive/GitHub Releases]
Duración: [X minutos]
Contenido: Flujos CRUD, carrito, tests automatizados
```

---

## 4. Documento Final — Checklist de Entrega

Antes de entregar, verifica que incluyas:

### Documentación (4 puntos):
- ✅ `DELIVERABLE_FINAL_REPORT.md`: Portada, índice, planificación, Scrum, plan de pruebas.
- ✅ Cronograma detallado con fechas (2025-12-10 a 2025-12-23).
- ✅ Definición del primer Release con RF y RNF.
- ✅ Ecuación de historias (HU-01 a HU-10) con criterios de aceptación y puntos.

### Metodología Scrum (5 puntos):
- ✅ Tareas definidas (T1-T7 o similar).
- ✅ Equipo de trabajo con roles y responsabilidades.
- ✅ Herramientas especificadas (GitHub, Jira, pytest).
- ✅ 3 Épicas definidas (Gestión de Productos, Carrito, Calidad y Pruebas).
- ✅ Ceremonias Scrum con fechas (Sprint Planning, Daily Standup, Review, Retrospective).
- ✅ 10 Historias de usuario importadas a Jira.

### Plan de Pruebas (7 puntos):
- ✅ Lista de RF y RNF mapeados a historias.
- ✅ Criterios de aceptación/rechazo de pruebas.
- ✅ Herramientas justificadas (pytest, Selenium, OBS, etc.).
- ✅ Cronograma de ejecución (manual y automatizada).
- ✅ Plantilla de caso de prueba (`docs/Test_Case_Template.md`).
- ✅ Equipos y responsabilidades (QA, Devs).
- ✅ Plan de automatización (historias prioritarias, cobertura de tests).

### Demostración y Entregables (4 puntos):
- ✅ Video (3-6 min): Demostración de funcionalidades y tests pasando.
- ✅ Repositorio funcional: GitHub con código, tests, reportes.
- ✅ Jira con historias: Tablero con 10 historias visibles y enlace compartido.
- ✅ Pruebas automatizadas: Tests en `tests/test_cases`, reportes en `tests/reports`.

---

## 5. Envío Final

Compila en un documento de Word o PDF (o en este mismo README, reemplazando placeholders):

1. **Portada** (rellena):
   - Nombre: [TU NOMBRE]
   - Matrícula: [TU MATRÍCULA]
   - Título: "Tienda Web - Gestión de Productos y Carrito (Agile-Scrum)"
   - Fecha: 2025-12-23 (o fecha real de entrega)

2. **Índice enumerado** (copia de `DELIVERABLE_FINAL_REPORT.md`).

3. **Secciones principales:**
   - Planificación (Estrategia de Trabajo)
   - Metodología Scrum
   - Plan de Pruebas
   - Demostración y Entregables (con enlaces + embedido video si es posible)

4. **Enlaces y evidencia:**
   ```
   Repositorio: https://github.com/JayBri15/Proyecto-Final-P3
   Jira Backlog: https://[tu-jira-url]
   Video: https://[tu-video-url]
   ```

5. **Conclusiones** y **Bibliografía**.

---

## Comandos útiles para ejecutar/verificar

```bash
# Clonar o navegar al repo
cd /workspaces/Proyecto-Final-P3

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest tests/ -v

# Ejecutar tests con reporte HTML
pytest tests/ --html=reports/test_report.html --self-contained-html

# Mostrar estructura del proyecto
tree -L 2
```

---

**¡Listo para entregar!** Sigue estos pasos y tu entrega cubrirá los 20 puntos solicitados. 🎯
