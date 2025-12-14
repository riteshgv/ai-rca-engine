from src.rca.confidence import compute_confidence

def test_confidence():
    distances = [0.2, 0.3, 0.4]
    confidence = compute_confidence(distances)
    print("Confidence:", confidence)

if __name__ == "__main__":
    test_confidence()
