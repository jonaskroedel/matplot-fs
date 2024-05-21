import numpy as np
import matplotlib.pyplot as plt

# Define constants
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads
V0 = 5  # Initial voltage in volts

# Time array for charging and discharging
t_charge = np.linspace(0, 5 * R * C, 1000)
t_discharge = np.linspace(0, 5 * R * C, 1000)

# Voltage across capacitor during charging
V_charge = V0 * (1 - np.exp(-t_charge / (R * C)))

# Voltage across capacitor during discharging
V_discharge = V0 * np.exp(-t_discharge / (R * C))

# Create the plot
plt.figure(figsize=(10, 6))

# Plot charging curve
plt.plot(t_charge, V_charge, label='Charging', color='blue')

# Plot discharging curve
plt.plot(t_discharge, V_discharge, label='Discharging', color='red')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Capacitor Charging and Discharging')
plt.legend()
plt.grid(True)

# Show the plot
pls.savefig("etl.png")
plt.show()
