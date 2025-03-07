from datetime import datetime, timezone


def GetCurrentUTCTime() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
