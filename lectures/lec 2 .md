
Numerical Deriv cont

using $f'(x) = \frac{[f(x+dx) - f(x-dx)]}{2dx}$,
we get error on order $dx^2f'''$, 3rd order, pick cube root of digits for precision 
round off error is serious business

Interpolation!
- Extrapolate is when you infer data outside the function
- interpolation is between given points

Interpolation:
- Laziest is just round to nearest number
- better is weighted average from two closest (aka linear interp)
- assuming smooth (well defined by taylors)
  - try quadratic
  - do not pick closest three cause u'll definitely get jumps :3
  - what about cubic?
    - well now you need 4 points, nearest four points will not cause jumps assuming you limit it to go through points.

- try a polynomial thats 0 at all points but 1
  - can look in notes how to do, basically tkae x-x_n at all points need to be zero
 
- back to cubics:
  - they were cts. What about the derivs?
  - def splines: first n derivates are forced to be continuous
  - cubic splines are so common, usually just call them splines
  - typically require second deriv is cts so first deriv is guarunteed to be smooth.
  - commonly set $f'' = 0$ on the edges
