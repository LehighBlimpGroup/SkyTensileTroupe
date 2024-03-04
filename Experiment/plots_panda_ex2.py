import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)


########## circle
# time_ini = 100
# time_final = 1100
# df_l = pd.read_csv('Experiment/folder2023_09_08_21_57_27/leader.csv', header=0, sep=" ")
# df_f1 = pd.read_csv('Experiment/folder2023_09_08_21_57_27/follower1.csv', header=0, sep=" ")
# df_f2 = pd.read_csv('Experiment/folder2023_09_08_21_57_27/follower2.csv', header=0, sep=" ")
# sm = 1
# file = 'experiment2.pdf'

# ########## Eight
time_ini = 1
time_final = 1
df_l = pd.read_csv('Experiment/folder2023_09_13_17_16_12/leader.csv', header=0, sep=" ")
df_f1 = pd.read_csv('Experiment/folder2023_09_13_17_16_12/follower1.csv', header=0, sep=" ")
df_f2 = pd.read_csv('Experiment/folder2023_09_13_17_16_12/follower2.csv', header=0, sep=" ")
sm = 1
file = 'experiment2_2.pdf'


t = df_l['time'].to_numpy()
x_leader = df_l['x'].to_numpy()
y_leader = df_l['y'].to_numpy()
z_leader = df_l['z'].to_numpy()



x1 = smooth(x_leader,sm)
y1 = smooth(y_leader,sm)
z1 = smooth(z_leader,sm)


xd_leader = df_l['waypoint_x'].to_numpy()
yd_leader = df_l['waypoint_y'].to_numpy()
zd_leader = df_l['waypoint_z'].to_numpy()


e_x = xd_leader - x1
e_y = yd_leader - y1
e_z = zd_leader - z1

norm1 = np.linalg.norm(np.array([e_x, e_y, e_z]).T, axis=1)


x_follower1 = df_f1['x'].to_numpy()
y_follower1 = df_f1['y'].to_numpy()
z_follower1 = df_f1['z'].to_numpy()

x_follower1 = np.resize(x_follower1, (len(x1)))
y_follower1 = np.resize(y_follower1, (len(y1)))
z_follower1 = np.resize(z_follower1, (len(z1)))

x2 = smooth(x_follower1,sm)
y2 = smooth(y_follower1,sm)
z2 = smooth(z_follower1,sm)

e_x2 = xd_leader + 1. - (x2)
e_y2 = yd_leader - (y2)
e_z2 = zd_leader - (z2)

norm2 = np.linalg.norm(np.array([e_x2, e_y2, e_z2]).T, axis=1)


x_follower2 = df_f2['x'].to_numpy()
y_follower2 = df_f2['y'].to_numpy()
z_follower2 = df_f2['z'].to_numpy()

x_follower2 = np.resize(x_follower2, (len(x1)))
y_follower2 = np.resize(y_follower2, (len(y1)))
z_follower2 = np.resize(z_follower2, (len(z1)))


x3 = smooth(x_follower2,sm)
y3 = smooth(y_follower2,sm)
z3 = smooth(z_follower2,sm)

e_x3 = xd_leader - 1 - (x3)
e_y3 = yd_leader - (y3)
e_z3 = zd_leader - (z3)

norm3 = np.linalg.norm(np.array([e_x3, e_y3, e_z3]).T, axis=1)

# fig, axs = plt.subplots(2, 1)
# plt.figure(figsize=(10,12))

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 1, figure=fig, height_ratios=[0.5, 1], hspace=0.2)


ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

ax1.plot(t[time_ini:-time_final]-t[time_ini], norm1[time_ini:-time_final], label='$e_L$')
ax1.plot(t[time_ini:-time_final]-t[time_ini], norm2[time_ini:-time_final], label='$e_1$')
ax1.plot(t[time_ini:-time_final]-t[time_ini], norm3[time_ini:-time_final], label='$e_2$')

# ax1.xlim([0, ])
ax1.axis(xmin=0.,xmax=t[-time_final]-t[time_ini])

ax1.set_ylabel('$e(m)$', fontsize=15)
ax1.set_xlabel('$Time(s)$',fontsize=15)
# plt.axis('equal')
ax1.legend(fontsize=15,loc = 'upper right')
ax1.grid()


####################################

ax2.plot(x1[time_ini:-time_final], y1[time_ini:-time_final], label='$x_L$')
# ax2.plot(xd_leader, yd_leader, 'r--', label='$x_d$')

ax2.plot(x2[time_ini:-time_final], y2[time_ini:-time_final], label='$x_1$')
ax2.plot(x3[time_ini:-time_final], y3[time_ini:-time_final], label='$x_2$')


ax2.set_ylabel('$y(m)$', fontsize=15)
ax2.set_xlabel('$x(m)$',fontsize=15)

# plt.ylabel("$y(m)$", fontsize=15)
# plt.xlabel("$x(m)$", fontsize=15)
ax2.axis('equal')
ax2.legend(fontsize=15,ncol=1,loc = 'upper right')
ax2.grid()

plt.savefig(file,bbox_inches="tight", dpi=250)


plt.show()
