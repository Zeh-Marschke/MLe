# ==========================================
# general parameter and functions

LABEL_SIGNAL = 1
LABEL_BACKGROUND = -1

def get_label (label):
    if (label == LABEL_SIGNAL):
        return "signal    "
    if (label == LABEL_BACKGROUND):
        return "background"
    return "unknown   "

RANDOM_STATE = 42
