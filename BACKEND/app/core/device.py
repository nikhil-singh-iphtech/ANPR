from app.core.config import settings
import torch

def get_device()->str:
    if torch.cuda.is_available():
        return "cuda"

    if hasattr(torch.backends, "mps"):
        if torch.backends.mps.is_available():
            return "mps"


    return "cpu"
DEVICE=get_device()


