# numerical-integrators

Numerical Integrators in Python, made in partial fulfilment for the award of
certificate in CFI Summer School 2021.

Example workflow:

```python
from nint import Integrators

# initialising an integrator
integ1 = Integrators(scheme = "scheme-name")

# integrating some function "fname" - this should create a generator
# object stored in the "result" attribute of "integ1" object
integ1.integrate(
    func = fname,
    step = 0.001,
    init_val = initial_values,
    end = end_value
)

# return the integration result from previous command
res = list(integ1.result)
```

## Integration Schemes

1. Euler
2. Backward Euler
3. Heun
4. Midpoint
5. Runge-Kutta
6. Euler-Cromer
7. Verlet

## Resources

### For OOP

- [\[RealPytho\] OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [\[DataCamp\] Python OOP Tutorial](https://www.datacamp.com/community/tutorials/python-oop-tutorial)
- [\[Programiz\] Python OOP](https://www.programiz.com/python-programming/object-oriented-programming)

### For Numerical Integration

- [\[Wiki\] Numerical methods for ODE](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations)
- [\[Book\] Numerical Solution for ODE](http://homepage.divms.uiowa.edu/~atkinson/papers/NAODE_Book.pdf)
- [\[Slides\] Numerical integration of ODE for IVP](https://web.cecs.pdx.edu/~gerry/nmm/course/slides/ch12Slides.pdf)
- [\[Book\] IVP for ODE](https://fncbook.github.io/v1.0/ivp/overview.html)
