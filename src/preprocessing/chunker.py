def chunk_logs(logs, window_size=5):
    chunks = []
    for i in range(0, len(logs), window_size):
        window = logs[i:i + window_size]
        chunks.append("\n".join(window))
    return chunks

