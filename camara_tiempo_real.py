import cv2
from deepface import DeepFace

def main():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("❌ No se pudo abrir la cámara.")
        return

    print("📷 Cámara activa. Presiona Q para salir.\n")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        try:
            resultados = DeepFace.analyze(
                frame,
                actions=["age", "emotion"],
                enforce_detection=False,
            )

            r = resultados[0]
            edad = r["age"]
            emocion = r["dominant_emotion"]

            region = r["region"]
            x, y, w, h = region["x"], region["y"], region["w"], region["h"]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(
                frame,
                f"{edad} anos | {emocion}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

        except Exception:
            pass

        cv2.imshow("DeepFace - Analisis en tiempo real", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
    print("\n✅ Cámara cerrada.")

if __name__ == "__main__":
    main()
