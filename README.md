# robotics-torque-tool
A simple MATLAB program for computing static torque (T = m·g·R) across defined mass and lever-arm ranges. Designed for actuator sizing and robot arm mechanics, featuring plots and CSV export.

This tool was originally created to estimate the required torque for a RoboCup@Home robot arm, where the maximum payload is 10 kg.  
It includes:

- Static torque computation across mass and lever arm ranges  
- Automatic table generation and CSV export  
- Engineering plot of Torque vs. Lever Length

### **Static Torque Computation**
Calculates torque values for all combinations of:
- Mass (kg)
- Lever arm length (m)
- Gravity (9.81 m/s²)

### **Results Table**
Outputs a clean table showing:
- Mass  
- Lever Length  
- Static Torque  
- Saves results to `static_torque_results.csv`.

### **Engineering Plots**
The script generates two visualizations:
- **Torque vs. Lever Length** for different masses  
- **Torque vs. Mass** for different lever lengths  

#### Example Plot
<p align="center">
  <img src="Images/static_torque_plot.png" width="500">
</p>
Useful for actuator selection, arm design, and mechanical analysis.
