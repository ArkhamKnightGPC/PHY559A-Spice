import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data from the table
capacitance = np.array([0, 0.1, 0.2, 0.5, 1])  # in pF
tp_up_to_down = np.array([0.11, 0.52, 0.81, 1.69, 3.11])  # in ns
tp_down_to_up = np.array([0.12, 0.62, 1.02, 1.82, 1.08])  # in ns

# Perform linear regression on the blue points
slope_blue, intercept_blue, r_value_blue, _, _ = linregress(capacitance, tp_up_to_down)

# Perform linear regression on the red points
slope_red, intercept_red, r_value_red, _, _ = linregress(capacitance, tp_down_to_up)

# Generate the regression lines
regression_line_blue = slope_blue * capacitance + intercept_blue
regression_line_red = slope_red * capacitance + intercept_red

# Plot scatter points and regression lines
plt.scatter(capacitance, tp_up_to_down, color='blue', label=r'$T_p(\text{up} \to \text{down})$')
plt.plot(capacitance, regression_line_blue, color='blue', linestyle='--', label='Linear Regression (blue)')

plt.scatter(capacitance, tp_down_to_up, color='red', label=r'$T_p(\text{down} \to \text{up})$')
plt.plot(capacitance, regression_line_red, color='red', linestyle='--', label='Linear Regression (red)')

# Add labels, legend, and title
plt.xlabel('Capacitance (pF)')
plt.ylabel('Propagation Time (ns)')
plt.title('Propagation Times with Linear Regression')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
