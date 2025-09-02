|||||||||||||||||||||||| LECTURE 1 ||||||||||||||||||||||||

precision in singles is about 10^16
  be super careful when taking differences in small numbers

Double = 2x Single
8 exp vs 11 exp,
23 mantisa vs 52 mantissa

Numerical Derivative 
- want to find right dx to always maximize precision accross the actual answer and the round off error
- dx = sqrt(epsilon(f(x)/f''(x))) is better
- very easy for it to be much better to use 10e-2 instead of 10-16 for max accuracy


|||||||||||||||||||||||| LECTURE 2 ||||||||||||||||||||||||

Numerical Deriv cont

using $f'(x) = \frac{[f(x+dx) - f(x-dx)]}{2dx}$,
we get error on order $dx^2f'''$, 3rd order, pick cube root of digits for precision 
round off error is serious business

Interpolate
