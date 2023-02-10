class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, n1: int, n2: int) -> int | None:  # Compares two numbers and returns the mayor
        if n1 > n2:
            mayor = n1
        elif n2 > n1:
            mayor = n2
        elif n1 == n2:
            mayor = None
        return mayor
