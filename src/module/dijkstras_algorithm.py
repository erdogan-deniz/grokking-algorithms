graph = {
    "S": {"A": 6},
    "S": {"B": 2},
    "B": {"A": 3},
    "B": {"F": 5},
    "A": {"F": 1}
}

pairs = {}


table = {
    "A": float("inf"),
    "B": float("inf"),
    "F": float("inf")
}


def update_weights():
    ...
