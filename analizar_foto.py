import sys
from deepface import DeepFace

def analizar(ruta: str):
    print(f"\n🔍 Analizando: {ruta}\n")

    resultados = DeepFace.analyze(
        ruta,
        actions=["age", "gender", "emotion"],
        enforce_detection=True,
    )

    r = resultados[0]
    print(f"🎂 Edad estimada  : {r['age']} años")
    print(f"👤 Género         : {r['dominant_gender']}")
    print(f"😄 Emoción        : {r['dominant_emotion']}")
    print()

if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "foto.jpg"
    analizar(ruta)
