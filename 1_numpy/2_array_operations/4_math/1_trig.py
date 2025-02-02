import numpy as np

# array of angles in radians
angles = np.array([0, 1, 2])
print("Angles:", angles)

# compute the sine of the angles
sine_values = np.sin(angles)
print("Sine values:", sine_values)

# compute the inverse sine of the angles
inverse_sine = np.arcsin(angles)
print("Inverse Sine values:", inverse_sine)

# compute the cosine of the angles
cosine_values = np.cos(angles)
print("Cosine values:", cosine_values)

# compute the inverse cosine of the angles
inverse_cosine = np.arccos(angles)
print("Inverse Cosine values:", inverse_cosine)

# compute the tangent of the angles
tangent_values = np.tan(angles)
print("Tangent values:", tangent_values)

# compute the inverse tangent of the angles
inverse_tangent = np.arctan(angles)
print("Inverse Tangent values:", inverse_tangent)

# define an angle in radians
angle = 1.57079633
print("Initial angle in radian:", angle)

# convert the angle to degrees
angle_degree = np.degrees(angle)
print("Angle in degrees:", angle_degree)

# convert the angle back to radians
angle_radian = np.radians(angle_degree)
print("Angle in radians (after conversion):", angle_radian)
