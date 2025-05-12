import os

_goggles_dir = os.path.dirname(__file__)

BASE_URL = "https://raw.githubusercontent.com/tavo-uemg/brave-api/main/src/brave/goggles/"
_goggles_dir = os.path.dirname(__file__)

__all__ = [
    os.path.splitext(f)[0]
    for f in os.listdir(_goggles_dir)
    if f.endswith(".goggle")
]

def __getattr__(name: str) -> str:
    if name in __all__:
        return f"{BASE_URL}{name}.goggle"
    raise AttributeError(f"module {__name__} has no attribute {name}")
