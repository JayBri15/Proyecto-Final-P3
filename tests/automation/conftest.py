"""
Fixture para inicializar WebDriver de Selenium.
Soporta Chrome, Firefox y Edge. webdriver-manager descarga drivers automáticamente.

IMPORTANTE: Para ejecutar estos tests necesitas:
- Linux/Mac/Windows con navegador instalado (Chrome, Firefox o Edge), O
- Ejecutar en un contenedor/CI que ya tenga navegadores (GitHub Actions ubuntu-latest, etc.)

En contenedores sin navegadores del sistema, los tests se omitirán con un mensaje claro.
"""
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from .config.config import BROWSER, HEADLESS, SCREENSHOTS_DIR
from .config.config import LISTA_URL
import json


@pytest.fixture(scope="function")
def driver():
    """
    Inicializa y retorna un WebDriver Selenium.
    Intenta Chrome primero, luego Firefox, luego Edge.
    webdriver-manager descarga automaticamente los drivers.
    Se ejecuta antes de cada test y se cierra después.
    """
    driver = None
    exception_log = []
    
    # Definir rutas conocidas de Chrome y chromedriver en caché
    cached_chrome_paths = [
        "/home/codespace/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome-wrapper",
        "/home/codespace/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome",
        "/home/codespace/.cache/selenium/chrome/linux64/143.0.7499.42/chrome",
        "/home/codespace/.cache/selenium/chrome/linux64/143.0.7499.40/chrome",
    ]
    cached_chromedriver_paths = [
        "/home/codespace/.cache/selenium/chromedriver/linux64/143.0.7499.42/chromedriver",
        "/home/codespace/.cache/selenium/chromedriver/linux64/143.0.7499.40/chromedriver",
    ]
    
    # Intentar Chrome primero
    try:
        options = webdriver.ChromeOptions()
        
        # Argumentos de headless para contenedor sin display
        options.add_argument("--headless=new")  # Headless mode (requerido)
        options.add_argument("--no-sandbox")  # Desactivar sandboxing
        options.add_argument("--disable-dev-shm-usage")  # No usar /dev/shm
        options.add_argument("--disable-gpu")  # Deshabilitar GPU
        options.add_argument("--single-process")  # Procesos únicos
        options.add_argument("--disable-web-resources")  # Minimizar recursos
        options.add_argument("--disable-extensions")  # Sin extensiones
        options.add_argument("--disable-plugins")  # Sin plugins
        options.add_argument("--disable-sync")  # Sin sincronización
        options.add_argument("--disable-breakpad")  # Sin crash reporting
        options.add_argument("--disable-default-apps")  # Sin apps por defecto
        options.add_argument("--no-first-run")  # Sin wizard de primer run
        options.add_argument("--no-service-autorun")  # Sin auto-inicio de servicios
        options.add_argument("--disable-backgrounding-occluded-windows")  # Sin background
        options.add_argument("--disable-hang-monitor")  # Sin monitor de bloqueos
        options.add_argument("--disable-popup-blocking")  # Sin bloqueo de popups
        options.add_argument("--disable-prompt-on-repost")  # Sin prompt on repost
        options.add_argument("--disable-reading-from-canvas")  # Sin lectura canvas
        options.add_argument("--disable-renderer-backgrounding")  # Sin bg rendering
        options.add_argument("--disable-device-discovery-notifications")  # Sin notificaciones device
        options.add_argument("--disable-features=InterestFeedContentSuggestions")  # Sin feed
        options.add_argument("--metrics-recording-only")  # Solo métricas
        options.add_argument("--mute-audio")  # Sin audio
        options.add_argument("--no-default-browser-check")  # Sin check navegador por defecto
        options.add_argument("--disable-background-networking")  # Sin red en background
        options.add_argument("--disable-client-side-phishing-detection")  # Sin detección phishing
        options.add_argument("--disable-component-extensions-with-background-pages")  # Sin componentes
        options.add_argument("--disable-component-update")  # Sin actualización componentes
        options.add_argument("--disable-profile-avatar-menu")  # Sin avatar menu
        
        # Usar directorio temporal para perfil
        options.add_argument("--user-data-dir=/tmp/chrome_user_data")
        
        # Buscar Chrome binario en caché
        chrome_binary = None
        for path in cached_chrome_paths:
            if os.path.isfile(path) and os.access(path, os.X_OK):
                chrome_binary = path
                break
        
        if chrome_binary:
            options.binary_location = chrome_binary
            print(f"✓ Usando Chrome binario en: {chrome_binary}")
        
        # Buscar chromedriver en caché o usar webdriver-manager
        chromedriver_path = None
        for path in cached_chromedriver_paths:
            if os.path.isfile(path) and os.access(path, os.X_OK):
                chromedriver_path = path
                break
        
        if chromedriver_path:
            service = ChromeService(chromedriver_path)
            print(f"✓ Usando chromedriver en: {chromedriver_path}")
        else:
            service = ChromeService(ChromeDriverManager().install())
            print(f"✓ Usando chromedriver descargado por webdriver-manager")
        
        driver = webdriver.Chrome(service=service, options=options)
        print("✓ Chrome WebDriver inicializado")
        
    except Exception as e:
        exception_log.append(f"Chrome: {str(e)[:100]}")
        
        # Intentar Firefox como fallback
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless") if HEADLESS else None
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            print("✓ Firefox WebDriver inicializado")
            
        except Exception as e2:
            exception_log.append(f"Firefox: {str(e2)[:100]}")
            
            # Intentar Edge como último recurso
            try:
                options = webdriver.EdgeOptions()
                options.add_argument("--headless=new") if HEADLESS else None
                service = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service, options=options)
                print("✓ Edge WebDriver inicializado")
                
            except Exception as e3:
                exception_log.append(f"Edge: {str(e3)[:100]}")
                
                # Si nada funcionó, omitir test con mensaje claro
                msg = (
                    "⚠ No fue posible inicializar ningún navegador (Chrome, Firefox, Edge).\n"
                    "Esto es normal en contenedores sin navegadores instalados.\n"
                    "Para ejecutar tests E2E localmente, instala uno de estos:\n"
                    "  - Chrome: apt-get install chromium chromium-chromedriver\n"
                    "  - Firefox: apt-get install firefox-esr\n"
                    "Para ejecutar en CI, usa GitHub Actions con ubuntu-latest (incluye Chrome/Firefox).\n"
                    f"Detalles de error: {'; '.join(exception_log)}"
                )
                pytest.skip(msg)
    
    # Si se inicializó algún driver, continuar
    if driver is None:
        pytest.skip("No se pudo inicializar ningún WebDriver")
    
    # Asegurar que el directorio de screenshots exista
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    
    # Seed localStorage with sample products
    try:
        sample_products = [
            {"id": "p1", "name": "Pelota", "desc": "Pelota de fútbol", "price": 9.99, "image": ""},
            {"id": "p2", "name": "Aro", "desc": "Aro para jugar", "price": 5.5, "image": ""},
            {"id": "p3", "name": "Cometa", "desc": "Cometa colorida", "price": 12.0, "image": ""}
        ]
        driver.get(LISTA_URL)
        driver.execute_script("localStorage.setItem('pdj_products_v1', arguments[0]);", json.dumps(sample_products))
        driver.execute_script("sessionStorage.removeItem('pdj_cart');")
    except Exception:
        # No bloquear si seed falla
        pass
    
    yield driver
    
    # Cleanup
    try:
        driver.quit()
    except Exception:
        pass




@pytest.fixture(scope="function")
def take_screenshot(driver):
    """
    Fixture para capturar pantallas durante las pruebas
    """
    def _screenshot(name):
        filename = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
        driver.save_screenshot(filename)
        return filename
    
    return _screenshot

