##
#   Author: Gil Soco
#   Description:
#    This module provides functions to calculate static torque for various mechanical systems.
#                           T = m * g * R
#   Includes:
#       - Automatic table ggeneration
#       - Engineering plots
#
#   Outputs:
#       py-static_torque_results.csv
#       py-static_torque_plot.png

import matplotlib.pyplot as plt

g = 9.81  # Acceleration due to Gravity (m/s^2)
masses = [3, 7, 10]  # Masses (m) in kg
lever_lengths = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # Lever lengths (R) in meters

def calculate_static_torque(mass, lever_length):
    """
    Calculate static torque.
    
    Parameters:
    mass (float): Mass in kg.
    lever_length (float): Lever length in meters.
    
    Returns:
    float: Static torque in Nm.
    """
    return mass * g * lever_length  

def generate_torque_table(masses, lever_lengths):
    """
    Generate a table of static torque values for given masses and lever lengths.
    
    Parameters:
    masses (list): List of masses in kg.
    lever_lengths (list): List of lever lengths in meters.
    
    Returns:
    list: List of tuples containing (mass, lever_length, torque).
    """
    torque_table = []
    for mass in masses:
        for lever_length in lever_lengths:
            torque = calculate_static_torque(mass, lever_length)
            torque_table.append((mass, lever_length, torque))
    return torque_table

def save_torque_table_to_csv(torque_table, filename='CSV/py-static_torque_results.csv'):
    """
    Save the torque table to a CSV file.
    
    Parameters:
    torque_table (list): List of tuples containing (mass, lever_length, torque).
    filename (str): Name of the output CSV file.
    """
    import csv
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mass (kg)', 'Lever Length (m)', 'Static Torque (Nm)'])
        for row in torque_table:
            writer.writerow(row)

def plot_torque_values(torque_table, filename='py-static_torque_plot.png'):
    """
    Plot static torque values and save the plot as an image.
    
    Parameters:
    torque_table (list): List of tuples containing (mass, lever_length, torque).
    filename (str): Name of the output image file.
    """
    
    masses = [row[0] for row in torque_table]
    lever_lengths = [row[1] for row in torque_table]
    torques = [row[2] for row in torque_table]
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(lever_lengths, torques, c=masses, cmap='viridis', s=100)
    plt.colorbar(scatter, label='Mass (kg)')
    plt.title('Static Torque vs Lever Length')
    plt.xlabel('Lever Length (m)')
    plt.ylabel('Static Torque (Nm)')
    plt.grid(True)
    plt.savefig("Images/"+filename)
    plt.close()

if __name__ == "__main__":
    torque_table = generate_torque_table(masses, lever_lengths)
    save_torque_table_to_csv(torque_table)
    plot_torque_values(torque_table)