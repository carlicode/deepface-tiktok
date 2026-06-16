# 🧠 Análisis Facial con DeepFace

Detecta **edad, género y emoción** desde una foto o en tiempo real con tu cámara — todo en Python, todo local, sin enviar datos a ningún servidor.

Demo del proyecto en [@carlicode](#) en TikTok e Instagram.

---

## ¿Qué hace?

| Script | Descripción |
|---|---|
| `analizar_foto.py` | Analiza una imagen y muestra edad, género y emoción en la terminal |
| `camara_tiempo_real.py` | Abre tu cámara y detecta edad y emoción en cada frame en vivo |

---

## ¿Cómo funciona por dentro?

DeepFace ejecuta tres pasos cada vez que le pasas una imagen:

1. **Detección** — localiza el rostro y lo recorta del fondo
2. **Normalización** — alinea ojos, nariz y boca a coordenadas fijas para que el modelo siempre compare caras en la misma posición
3. **Predicción** — pasa la cara normalizada por una red neuronal convolucional (CNN) entrenada con más de 500,000 imágenes etiquetadas por humanos

El modelo de edad no devuelve un número exacto sino el **promedio estadístico más probable** — por eso el margen típico es de ±5 años.

---

## Requisitos

- Python 3.9 o superior
- Cámara web (solo para el script en tiempo real)

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/deepface-tiktok.git
cd deepface-tiktok

# 2. Crea un entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate        # Mac / Linux
# .venv\Scripts\activate         # Windows

# 3. Instala las dependencias
pip install -r requirements.txt
```

> La primera vez que corras el script, DeepFace descargará los modelos automáticamente (~500 MB). Solo ocurre una vez.

---

## Uso

### Analizar una foto

```bash
python analizar_foto.py foto.jpg
```

Salida esperada:

```
🔍 Analizando: foto.jpg

🎂 Edad estimada  : 27 años
👤 Género         : Man
😄 Emoción        : happy
```

### Cámara en tiempo real

```bash
python camara_tiempo_real.py
```

Se abre una ventana con tu cámara. La edad y emoción aparecen sobre tu cara en cada frame. Presiona `Q` para cerrar.

---

## Emociones que detecta

`happy` · `sad` · `angry` · `surprise` · `fear` · `disgust` · `neutral`

---

## Solución de problemas

**No detecta mi cara en la foto**
Asegúrate de que el rostro esté bien iluminado y visible. Puedes desactivar la detección estricta cambiando `enforce_detection=True` a `False` en `analizar_foto.py`.

**Error al abrir la cámara**
Verifica que ninguna otra aplicación esté usando la cámara. En Mac, revisa los permisos en Preferencias del Sistema → Privacidad → Cámara.

**La instalación falla con errores de TensorFlow**
Prueba instalando primero: `pip install tf-keras` y luego `pip install deepface`.

---

## Créditos

- [DeepFace](https://github.com/serengil/deepface) — creada por **Sefik Ilkin Serengil**, inspirada en el paper de investigación facial de Meta (2014)
- [OpenCV](https://opencv.org/) — para captura de video en tiempo real

---

## Nota sobre uso responsable

Este proyecto es educativo. El reconocimiento facial tiene implicaciones éticas importantes — úsalo para aprender cómo funciona la IA por dentro, no para identificar personas sin su consentimiento.
