#!/bin/bash
# Script para instalar Firefox y ejecutar tests
# Este script instala las dependencias mínimas de Firefox

echo "🔧 Intentando instalar Firefox..."

# Intentar instalar Firefox (requiere permisos)
if command -v apt-get &> /dev/null; then
    echo "Usando apt-get (puede requerir sudo)..."
    apt-get update -y 2>/dev/null && apt-get install -y firefox-esr 2>/dev/null && echo "✓ Firefox instalado" || echo "⚠ No se pudo instalar Firefox con apt-get"
elif command -v yum &> /dev/null; then
    echo "Usando yum..."
    yum install -y firefox 2>/dev/null && echo "✓ Firefox instalado" || echo "⚠ No se pudo instalar Firefox con yum"
else
    echo "⚠ No se encontró un gestor de paquetes (apt-get, yum)"
fi

# Si Firefox no está disponible, intentar usar Chromium del sistema
if ! command -v firefox &> /dev/null && ! command -v chromium &> /dev/null && ! command -v chromium-browser &> /dev/null; then
    echo "⚠ Ni Firefox ni Chromium están disponibles"
    echo "Por favor, instala una de estas opciones:"
    echo "  - Firefox: apt-get install firefox-esr"
    echo "  - Chromium: apt-get install chromium chromium-chromedriver"
    exit 1
fi

echo "✓ Navegador disponible"
echo ""
echo "Ejecutando tests..."
cd /workspaces/Proyecto-Final-P3
python3 -m pytest tests/automation/test_cases -v --html=reports/test_report.html --self-contained-html
