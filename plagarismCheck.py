import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from matplotlib.collections import PatchCollection

meas_upd_iter = [0,1,3,5,7,9]
right_state_trans_iter = [1,2,7,8,9]
up_state_trans_iter = [3,4,5,6]

z_true_det_marker = 0.7
z_false_det_marker = 0.25

markerPos = np.array(([4,4],[4,6],[4,8],[6,8],[8,8]))

u = 1
n = 10
px = np.ones((n,n)) / (n * n)

iter=10

# Make the first measurement
beliefs = [px]
px = measurement_update(px)

# Run Bayes Filter for 10 iterations
for i in range(1, iter):
    # State Transition
    if i in right_state_trans_iter:
        px = motion_update_u_r(px, u)
    elif i in up_state_trans_iter:
        px = motion_update_u_u(px, u)
    
    # Measurement Update
    if i in meas_upd_iter:
        px = measurement_update(px)
    
    beliefs.append(px)

%matplotlib widget

# Simulation -  You don't have to modify this section, 
# you can choose to use code from here to debug your outputs if you like
from ipywidgets import interact, IntSlider

fig, ax = plt.subplots()

curr_belief = beliefs[0]
im = plt.imshow(curr_belief, cmap='gray_r', vmin=0, vmax=1, extent=[0,10,0,10], origin='lower')
ax.set_xticks(np.arange(0,n))
ax.set_yticks(np.arange(0,n))
cbar = fig.colorbar(im, ticks=[0,1])
cbar.ax.set_yticklabels(['p(x)=0', 'p(x)=1'])
plt.grid()
ax.set_box_aspect(1)

# Add Markers
patches_marker = []
points= [[4,4.7], [5,4.7], [4,4], [4.5, 5], [5, 4], [4,4.7]]
patches_marker.append(Polygon(points))
points= [[4,6.7], [5,6.7], [4,6], [4.5, 7], [5, 6], [4,6.7]]
patches_marker.append(Polygon(points))
points= [[4,8.7], [5,8.7], [4,8], [4.5, 9], [5, 8], [4,8.7]]
patches_marker.append(Polygon(points))
points= [[6,8.7], [7,8.7], [6,8], [6.5, 9], [7, 8], [6,8.7]]
patches_marker.append(Polygon(points))
points= [[8,8.7], [9,8.7], [8,8], [8.5, 9], [9, 8], [8,8.7]]
patches_marker.append(Polygon(points))

p_m = PatchCollection(patches_marker, facecolor='r', edgecolor='k')
ax.add_collection(p_m)
    
robot_gt_poses = [[3.5,4.5], [4.5, 4.5], [4.5, 5.5], [4.5, 6.5], [4.5, 7.5], [4.5, 8.5], [5.5, 8.5], [6.5, 8.5], [7.5, 8.5], [8.5, 8.5]]
patches_robot = []

# Show the belief updates
def show_beliefs(step):
    plt.cla()
    ax.add_collection(p_m)
    
    ax.set_xticks(np.arange(0,n))
    ax.set_yticks(np.arange(0,n))
    plt.grid()
    ax.set_box_aspect(1)
    
    curr_belief = beliefs[step]
    im = plt.imshow(curr_belief, cmap='gray_r', vmin=np.min(px), vmax=np.max(px), extent=[0,10,0,10], origin='lower')
    
    # Add Gt Robot Pose For Reference
    patches_robot.clear()
    curr_gt_pose = robot_gt_poses[step]
    patches_robot.append(Circle((curr_gt_pose[0], curr_gt_pose[1]), 0.4))
    p_r = PatchCollection(patches_robot, facecolor='b', edgecolor='k')
    ax.add_collection(p_r)
    plt.show()
    plt.title(f'Time Step {step}')
    
interact(show_beliefs, step=IntSlider(value=0, max=len(beliefs)-1));
