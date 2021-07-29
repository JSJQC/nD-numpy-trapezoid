# nD-numpy-trapezoid
An n-dimensional trapezoid rule, implemented in NumPy. The functions could easily be put into a separate file for cleanness if desired

An 8GB RAM computer can handle around 250 million grid points (e.g. ~15,000 steps in two variables each). Using a lightweight IDE may allow more grid points to be used on a similar system.

This version runs a couple of orders of magnitude faster than the similar SymPy implementation also on this profile, and so is definitely preferable if a non-symbolic/non-exact solution is desired.
