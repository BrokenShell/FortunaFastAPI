# Fortuna FastAPI
## Random Value Toolkit

### Application Routes
- #### Swagger Docs
    - `/` Interactive Testing and Documentation

- #### Random Floats
    - `/canonical` Returns a random Float in range [0.0, 1.0) with flat uniform distribution.
    - `/random-float/{low}/{high}` Returns a random Float in range `[low, high)` with flat uniform distribution.
    - `/triangular/{low}/{high}/{mode}` Returns a random Float in range `[low, high]`. Linear distribution about the mode.

- #### Random Integers
    - `/d/{sides}` Returns a random integer in the range [1, sides] with flat uniform distribution.
    - `/dice/{rolls}/{sides}` Returns a random integer in range [X, Y] where X = rolls and Y = rolls * sides. Geometric distribution based on the number and size of the dice rolled.
    - `/random-below/{stop}` Returns a random integer in the range [0, stop) with flat uniform distribution.
    - `/random-range/{start}/{stop}` Returns a random integer in the range [start, stop) with flat uniform distribution.
    - `/random-range-step/{start}/{stop}/{step}` Returns a random integer in the range [start, stop) by increments of step. Flat uniform distribution. 
