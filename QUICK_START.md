# 🚀 Guía Rápida — Ejecutar Tests Automatizados

Este documento explica cómo ejecutar las pruebas E2E del proyecto.

## ⚠️ Nota Importante

Este contenedor (GitHub Codespaces) **no puede ejecutar los tests localmente** porque:
- No tiene acceso root para instalar librerías gráficas
- Chrome necesita librerías como libatk-1.0, libcups, libxkbcommon, etc.
- No hay servidor X11/display disponible

**Soluciones:**
- ✅ **Usar GitHub Actions** (RECOMENDADO): ublic.yml) automáticamente al hacer push
- ✅ **Ejecutar en máquina física con Chrome instalado**
- ✅ **Usar contenedor con permisos root (sudo)**

---

## Opción 1: GitHub Actions (RECOMENDADO ✅)

El proyecto tiene un workflow que ejecuta los tests automáticamente en `ubuntu-latest` (que tiene Chrome preinstalado).

**Pasos:**
1. Haz un commit y push a `main`
2. Ve a GitHub → pestaña **Actions**
3. Selecciona **Run E2E Tests**
4. Abre el run más reciente
5. Descarga el artifact **test-report-html**

---

## Opción 2: Máquina Física con Chrome

### Linux:
```bash
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver
pip install -r requirements.txt

# Terminal 1
cd docs && python3 -m http.server 8000

# Terminal 2
chmod +x ./run_tests.sh && ./run_tests.sh
```

### macOS:
```bash
brew install chromium
pip install -r requirements.txt

# Terminal 1
cd docs && python3 -m http.server 8000

# Terminal 2
chmod +x ./run_tests.sh && ./run_tests.sh
```

### Windows:
1. Instalar Chrome o Chromium
2. `pip install -r requirements.txt`
3. Terminal 1: `cd docs && python -m http.server 8000`
4. Terminal 2: `python -m pytest tests/automation/test_cases -v --html=reports/test_report.html --self-contained-html`

---

## Opción 3: Contenedor con Permisos Root

```bash
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver \
  libatk-1.0-0 libcups2 libxkbcommon0 libatspi2.0-0 libxcomposite1 \
  libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2

pip install -r requirements.txt

# Terminal 1
cd docs && python3 -m http.server 8000

# Terminal 2
chmod +x ./run_tests.sh && ./run_tests.sh
```

---

## Estructura de Tests

23 tests totales en 6 archivos:
- `test_login.py`: 4 tests
- `test_lista.py`: 4 tests
- `test_crear.py`: 4 tests
- `test_editar.py`: 4 tests
- `test_eliminar.py`: 3 tests
- `test_carrito.py`: 4 tests

---

## Ejecución Manual

```bash
# Todos los tests
python3 -m pytest tests/automation/test_cases -v

# Un archivo específico
python3 -m pytest tests/automation/test_cases/test_login.py -v

# Un test específico
python3 -m pytest tests/automation/test_cases/test_login.py::TestLogin::test_001_successful_login_with_valid_credentials -v
```

---

## Reportes

Se generan en `reports/`:
- `test_report.html` - Reporte interactivo
- `screenshots/` - Capturas de pantalla

---

## FAQ

**P: ¿Por qué los tests se saltan en este contenedor?**
R: Falta de librerías gráficas del sistema. Es normal. Usa GitHub Actions.

**P: ¿Cómo veo los resultados?**
R: Ve a GitHub Actions después de hacer push, descarga el artifact.

**P: ¿Puedo ejecutar un test específico?**
R: Sí: `pytest tests/automation/test_cases/test_login.py::TestLogin::test_001_successful_login_with_valid_credentials -v`

---

**Recomendación:** Usa GitHub Actions. Es la forma más simple y confiable.


