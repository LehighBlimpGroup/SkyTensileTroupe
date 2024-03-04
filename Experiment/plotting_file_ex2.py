import os
import csv
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)

# input_folder_path = "Experiment/folder2023_09_08_19_39_51"
input_folder_path = "Experiment/folder2023_09_08_21_57_27"

csv_leader = "leader.csv"  # Replace with the actual CSV filename
csv_follower1 = "follower1.csv"  # Replace with the actual CSV filename
csv_follower2 = "follower2.csv"  # Replace with the actual CSV filename

csv_file_path_leader = os.path.join(input_folder_path, csv_leader)
csv_file_path_follower1 = os.path.join(input_folder_path, csv_follower1)
csv_file_path_follower2 = os.path.join(input_folder_path, csv_follower2)

def get_column_values(row, column_indices):
    return [float(value) for value in row]


target_column_indices = [0, 1, 2, 3]  # Adjust these indices based on your header

with open(csv_file_path_leader, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)[0].split()  # Split the header into individual column names
    print("CSV Header:", header)  # Print header for debugging

    time_values, x_values, y_values, z_values, yaw_values = [], [], [], [], []
    x_setpoint, y_setpoint, z_setpoint, yaw_setpoint = [], [], [], []

    for row in csv_reader:
        values = row[0].split()  # Split the row into individual values
        data = get_column_values(values, target_column_indices)
        #         print(data)
        time_values.append(data[0])

        x_values.append(data[1])
        y_values.append(data[2])
        z_values.append(data[3])

        yaw_values.append(data[6])

        x_setpoint.append(data[7])
        y_setpoint.append(data[8])
        z_setpoint.append(data[9])
#         yaw_setpoint.append(data[10])


############################################################


# Create subplots using GridSpec
fig = plt.figure(figsize=(12,8))
gs = GridSpec(4, 1, figure=fig, height_ratios=[3, 3, 3, 0.5], hspace=0.4)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
ax3 = fig.add_subplot(gs[2, 0], sharex=ax1)
# ax_legend = fig.add_subplot(gs[3, 0])

# Plot x and y data with reference
ax1.plot(time_values, x_values, label='x')
ax1.plot(time_values, x_setpoint, label='Reference x', linestyle='dashed', color='red')
ax1.set_ylabel('$x$')

ax2.plot(time_values, y_values, label='y', color='orange')
ax2.plot(time_values, y_setpoint, label='Reference y', linestyle='dashed', color='red')
ax2.set_ylabel('y')

# Plot z data and reference
ax3.plot(time_values, z_values, label='z', color='green')
ax3.plot(time_values, z_setpoint, label='Reference z', linestyle='dashed', color='red')
ax3.set_ylabel('z')


# plt.show()



with open(csv_file_path_follower1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)[0].split()  # Split the header into individual column names
    print("CSV Header:", header)  # Print header for debugging

    time_values, x_values, y_values, z_values, yaw_values = [], [], [], [], []
    x_setpoint, y_setpoint, z_setpoint, yaw_setpoint = [], [], [], []

    for row in csv_reader:
        values = row[0].split()  # Split the row into individual values
        data = get_column_values(values, target_column_indices)
        #         print(data)
        time_values.append(data[0])

        x_values.append(data[1])
        y_values.append(data[2])
        z_values.append(data[3])

        # yaw_values.append(data[6])
        #
        # x_setpoint.append(data[7])
        # y_setpoint.append(data[8])
        # z_setpoint.append(data[9])
#         yaw_setpoint.append(data[10])


############################################################

# Plot x and y data with reference
ax1.plot(time_values, x_values, label='x')
# ax1.plot(time_values, x_setpoint, label='Reference x', linestyle='dashed', color='red')
ax1.set_ylabel('$x$')

ax2.plot(time_values, y_values, label='y', color='orange')
# ax2.plot(time_values, y_setpoint, label='Reference y', linestyle='dashed', color='red')
ax2.set_ylabel('y')

# Plot z data and reference
ax3.plot(time_values, z_values, label='z', color='green')
# ax3.plot(time_values, z_setpoint, label='Reference z', linestyle='dashed', color='red')
ax3.set_ylabel('z')



with open(csv_file_path_follower2, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)[0].split()  # Split the header into individual column names
    print("CSV Header:", header)  # Print header for debugging

    time_values, x_values, y_values, z_values, yaw_values = [], [], [], [], []
    x_setpoint, y_setpoint, z_setpoint, yaw_setpoint = [], [], [], []

    for row in csv_reader:
        values = row[0].split()  # Split the row into individual values
        data = get_column_values(values, target_column_indices)
        #         print(data)
        time_values.append(data[0])

        x_values.append(data[1])
        y_values.append(data[2])
        z_values.append(data[3])

        # yaw_values.append(data[6])
        #
        # x_setpoint.append(data[7])
        # y_setpoint.append(data[8])
        # z_setpoint.append(data[9])
#         yaw_setpoint.append(data[10])


############################################################

# Plot x and y data with reference
ax1.plot(time_values, x_values, label='x')
# ax1.plot(time_values, x_setpoint, label='Reference x', linestyle='dashed', color='red')
ax1.set_ylabel('$x$')

ax2.plot(time_values, y_values, label='y', color='orange')
# ax2.plot(time_values, y_setpoint, label='Reference y', linestyle='dashed', color='red')
ax2.set_ylabel('y')

# Plot z data and reference
ax3.plot(time_values, z_values, label='z', color='green')
# ax3.plot(time_values, z_setpoint, label='Reference z', linestyle='dashed', color='red')
ax3.set_ylabel('z')


plt.show()


