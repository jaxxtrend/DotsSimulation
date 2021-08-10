from dataclasses import dataclass as component


@component
class Citizen:
    """tag"""
    pass


@component
class Factory:
    """tag"""
    pass


@component
class Product:
    """tag"""
    pass


@component
class City:
    """tag"""
    pass


@component
class Household:
    """tag"""
    pass


@component
class Age:
    v: int = 0


@component
class Name:
    s: str = None


@component
class Income:
    v: float = 0.0


@component
class Subsidy:
    v: float = 0.0


@component
class Salary:
    v: float = 0.0


@component
class Money:
    v: float = 0.0


@component
class TaxRate:
    """Value in precents"""
    v: float = 20.0


@component
class WorkId:
    v: int = None


@component
class Cost:
    v: float = 0.0


@component
class Price:
    v: float = 0.0


@component
class Childrens:
    v: tuple = ()


@component
class Parents:
    v: tuple = ()


@component
class Population:
    v: int = 5


if __name__ == "__main__":
    # simple tests
    childrens = Childrens()
    childrens.v += ("sd", "asds", "sadsd")
    print(childrens)
