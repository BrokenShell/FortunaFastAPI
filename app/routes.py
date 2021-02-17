from fastapi import APIRouter
import Fortuna

router = APIRouter()


# Float Functions #

@router.get("/canonical")
async def canonical():
    """ Flat uniform distribution
    @return: random Float in range [0.0, 1.0)
    """
    return Fortuna.canonical()


@router.get("/random-float/{low}/{high}")
async def random_float(low: float, high: float):
    """ Flat uniform distribution
    @param low: Float
    @param high: Float
    @return: random Float in range `[low, high)`
    """
    return Fortuna.random_float(low, high)


@router.get("/triangular/{low}/{high}/{mode}")
async def triangular(low: float, high: float, mode: float):
    """ Linear distribution about the mode
    @param low: Float
    @param high: Float
    @param mode: Float
    @return: random Float in range `[low, high]`
    """
    return Fortuna.triangular(low, high, mode)


# Integer Functions #

@router.get("/d/{sides}")
async def d(sides: int):
    """ Flat uniform distribution
    @param sides: Integer
    @return: random integer in the range [1, sides]
    """
    return Fortuna.d(sides)


@router.get("/dice/{rolls}/{sides}")
async def dice(rolls: int, sides: int):
    """ Geometric distribution based on the number and size of the dice rolled
    @param rolls: Integer, number of times to roll the die
    @param sides: Integer, die size or number of sides, most commonly six
    @return: random integer in range [X, Y] where X = rolls and Y = rolls * sides
    """
    return Fortuna.dice(rolls, sides)


@router.get("/random-below/{stop}")
def random_below(stop: int):
    """ Flat uniform distribution
    @param stop: Integer
    @return: random integer in the range [0, stop)
    """
    return Fortuna.random_below(stop)


@router.get("/random-range/{start}/{stop}")
def random_range(start: int, stop: int):
    """ Flat uniform distribution
    @param start: Integer
    @param stop: Integer
    @return: random integer in the range [start, stop)
    """
    return Fortuna.random_range(start, stop)


@router.get("/random-range-step/{start}/{stop}/{step}")
def random_range_step(start: int, stop: int, step: int):
    """ Flat uniform distribution
    @param start: Integer
    @param stop: Integer
    @param step: Integer
    @return: random integer in the range [start, stop) by increments of step
    """
    return Fortuna.random_range(start, stop, step)
