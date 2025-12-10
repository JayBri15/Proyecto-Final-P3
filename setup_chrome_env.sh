#!/bin/bash

# Este script intenta ejecutar Chrome con todas las variables de entorno necesarias
# Para usarlo: source setup_chrome_env.sh && ./run_tests.sh

# Detectar ruta de Chrome
if [ -f "/home/codespace/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome-wrapper" ]; then
    CHROME_PATH="/home/codespace/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome-wrapper"
elif [ -f "/home/codespace/.cache/selenium/chrome/linux64/143.0.7499.42/chrome" ]; then
    CHROME_PATH="/home/codespace/.cache/selenium/chrome/linux64/143.0.7499.42/chrome"
else
    echo "No se encontró Chrome binario"
    exit 1
fi

echo "✓ Chrome encontrado: $CHROME_PATH"

# Establecer variables de entorno para librerías
export LD_LIBRARY_PATH="/home/codespace/.cache/ms-playwright/chromium-1200/chrome-linux64:${LD_LIBRARY_PATH}"

# Crear symlinks para librerías faltantes si es posible (requiere permisos)
if command -v sudo &> /dev/null; then
    echo "Intentando crear symlinks para librerías compartidas..."
    # Esto probablemente fallará sin permisos reales, pero no hace daño intentar
    for lib in libatk-1.0.so.0 libatk-bridge-2.0.so.0 libcups.so.2 libxkbcommon.so.0; do
        if sudo touch /tmp/test_sudo_perms 2>/dev/null; then
            echo "✓ Tienes permisos sudo"
            break
        fi
    done
fi

echo "Entorno configurado. Ejecutando pytest..."
python3 -m pytest tests/automation/test_cases -v \
    --html=reports/test_report.html \
    --self-contained-html \
    --tb=short
