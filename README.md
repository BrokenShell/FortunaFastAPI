# Fortuna FastAPI
## Random Value Toolkit

### Fortuna Documentation
- https://pypi.org/project/Fortuna/

### Fortuna Repo
- https://github.com/BrokenShell/Fortuna

### Fortuna Installation (macOS & Linux)
```shell
pip install Fortuna
```

### Application API Routes
- #### Swagger Docs
    - `/` Interactive Testing and Documentation

- #### Random Floats
    - `/canonical` Returns a random Float in range `[0.0, 1.0)` with flat uniform distribution.
    - `/random-float/{low}/{high}` Returns a random Float in range `[low, high)` with flat uniform distribution.
    - `/triangular/{low}/{high}/{mode}` Returns a random Float in range `[low, high]`. Linear distribution about the mode.

- #### Random Integers
    - `/d/{sides}` Returns a random integer in the range `[1, sides]` with flat uniform distribution.
    - `/dice/{rolls}/{sides}` Returns a random integer in range `[X, Y]` where X = rolls and Y = rolls * sides. Geometric distribution based on the number and size of the dice rolled.
    - `/random-below/{stop}` Returns a random integer in the range `[0, stop)` with flat uniform distribution.
    - `/random-range/{start}/{stop}` Returns a random integer in the range `[start, stop)` with flat uniform distribution.
    - `/random-range-step/{start}/{stop}/{step}` Returns a random integer in the range `[start, stop)` by increments of step. Flat uniform distribution. 

## The Challenge
```
1/1 point: Get the app to run
1/1 point: No warnings or errors
1/1 point: Write a new unit test - MonkeyScope, performance and distribution test suite
1/1 point: PEP8 linter, PyCharm
1/1 point: Passes all PEP8 tests
1/1 point: Clean Branches, my branches are always clean
1/1 point: Accurate Readme - the library is fully documented -> https://pypi.org/project/Fortuna/
3/3 points: Several new endpoints created -> https://fortuna-fastapi.herokuapp.com/
3/3 points: Find a todo. The only todo I have is to create a web API
3/3 points: Write a README
0/5 points: Connect to a DB - Connected MongoDB, tested but not used
5/5 points Update all dependent libraries - Cython
7/7 points: c-extension or deploy it to PyPi.org - Both
10/10 points: Docker, Fortuna runs great in Docker
10/10 points: Upgrade a major Dependency -> Updated Storm, the core C++ library
+5 bonus points for transcribing this competition from JS to Python!
```
