def compute_confidence(distances: list[float]) -> float:
    if not distances:
        return 0.0

    avg_distance = sum(distances) / len(distances)

    # Convert distance → confidence (0–1)
    confidence = max(0.0, min(1.0, 1 - avg_distance))

    return round(confidence, 2)
