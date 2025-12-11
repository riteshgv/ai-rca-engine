def chunk_logs(logs, max_chunk_size=5):
    """
    Group log lines into chunks.
    Each chunk has max 5 logs (or configurable).
    """
    chunks = []
    buffer = []

    for log in logs:
        buffer.append(log)
        if len(buffer) >= max_chunk_size:
            chunks.append(buffer)
            buffer = []

    if buffer:
        chunks.append(buffer)

    return chunks

