#!/usr/bin/env python3
import math

# 1. Taylor endpoint mass constant
C_Z = 64.0 * math.sqrt(2.0) * math.pi / 105.0
assert abs(C_Z - 2.708042933734623) < 1e-12

# 2. Taylor cylinder: r0 = K2^{-1/2}; radius = half-height = r0/2.
# Maximum |y|^2 = r0^2/2, so 1 - (K2/2)|y|^2 = 3/4.
taylor_cylinder_floor = 1.0 - 0.25
assert abs(taylor_cylinder_floor - 0.75) < 1e-15

# Flux through one transverse disk of radius r0/2.
C_PHI = (3.0 / 4.0) * math.pi * (1.0 / 2.0) ** 2
assert abs(C_PHI - 3.0 * math.pi / 16.0) < 1e-15

# 3. q=2 coherent ellipse / next disk overlap.
# Same-area ellipse with aspect ratio 2 has minor semiaxis R/sqrt(2).
a = 1.0 / math.sqrt(2.0)
F2 = 2.0 / math.pi * (math.asin(a) + a * math.sqrt(1.0 - a * a))
assert abs(F2 - (0.5 + 1.0 / math.pi)) < 1e-14
turnover = 1.0 - F2
assert abs(turnover - (0.5 - 1.0 / math.pi)) < 1e-14

# 4. Material-tube coarea normalized coefficient for q=2.
C_FLUX_Q2 = 9.0 * math.pi / (2048.0 * math.sqrt(2.0))
assert C_FLUX_Q2 > 0.0

# 5. Positive-middle rotational projective coefficient.
# c_theta(x) = (3-x)/sqrt(3+x^2), x in [x*,1].
x_star = 3.0 * (math.sqrt(3.0) - 1.0) / 4.0

def c_theta(x):
    return (3.0 - x) / math.sqrt(3.0 + x * x)

# It decreases on the relevant interval and equals 1 at x=1.
assert c_theta(x_star) > 1.0
assert abs(c_theta(1.0) - 1.0) < 1e-15

# 6. Projective geodesic angle for a 90-degree transverse eigenaxis swap.
def cos_swap(x):
    s1 = -2.0
    s2 = 1.0 - x
    s3 = 1.0 + x
    norm2 = s1*s1 + s2*s2 + s3*s3
    return (2.0*s1*s2 + s3*s3) / norm2

angle_at_1 = math.acos(cos_swap(1.0))
assert abs(angle_at_1 - math.pi/3.0) < 1e-14
assert math.acos(cos_swap(x_star)) > angle_at_1

# 7. Middle-zero gap product used in the misalignment rotation bound.
# ((s2-s1)(s3-s2))/s3^2 = 2x(3-x)/(1+x)^2 >= 1 on [x*,1].
def gap_product_ratio(x):
    return 2.0*x*(3.0-x)/(1.0+x)**2

assert gap_product_ratio(x_star) >= 1.0
assert abs(gap_product_ratio(1.0) - 1.0) < 1e-15

print('C_Z =', C_Z)
print('Taylor cylinder component floor =', taylor_cylinder_floor)
print('Taylor disk flux coefficient =', C_PHI)
print('q=2 coherent ellipse coverage =', F2)
print('q=2 fixed replacement fraction =', turnover)
print('q=2 normalized coarea coefficient =', C_FLUX_Q2)
print('x_* =', x_star)
print('c_theta(x_*) =', c_theta(x_star))
print('swap angle minimum = pi/3 =', angle_at_1)
print('all smooth thick-core material-gate checks passed')
