Legendre Polynomials

and use for integration

sum of weights should be # of points -1
  - =num of intervals

Pnc_n = f
c_n = P_n^-1f

need weights to follow simpson's rule
- something about weights $\alpha   P^{-1}f$

when integrating using quadratics ie simpsons, need to set integration points to a valid count (2 * n + 1)
- 2 is the order of poly

even order polynomials

Error Estimation:
- pickk order, then vary step till acc is good
- dopare f(4dx) and f(2dx), do the error change as expected? if not maybe try smaller step

- for quadratic, factor 2 dx -> factor 16 in error
- error should usually be less than difference of f(dx) and f(2dx)


Romberg Integration:
- get better things in higher order
- int from -a to a, do a bunch of coarse integrals, use that to estimate high order of taylors, and cancel a bunch of terms.
- built into scipy
- scipy.integrate.romb
- scipy.integrate.romberg
- help(romberg)
