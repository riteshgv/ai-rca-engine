from datetime import datetime, timedelta


def build_windows(logs, window_minutes=5):
    windows = []
    current = []
    start_time = None

    for log in logs:
        ts = " ".join(log.split(" ")[:2])
        log_time = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

        if start_time is None:
            start_time = log_time

        if log_time - start_time <= timedelta(minutes=window_minutes):
            current.append(log)
        else:
            windows.append(current)
            current = [log]
            start_time = log_time

    if current:
        windows.append(current)

    return windows
