"""
TODO: A very useful temperature-conversion app.
"""
def is_it_cold_f(temp_f: float) -> bool:
    """
    Determines if the supplied temp is below a threshold

    Parameters
    ==========
    temp_f : float
        supplied temp in F

    Returns
    =======
    bool
        True if below threshold
    """
    if temp_f < 68:
        return True 
    else:
        return False

def greet_human() -> None:
    """
    Get a name from the keyboard and say hello!
    """
    name: str = input("what is your name?")

    print(f"hello {name}")

def main() -> None:
    pass

if __name__ == "__main__":
    main()
