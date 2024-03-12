import numpy as np

# calculating the WSI of each TRB
# basin
bas = np.loadtxt("./basin.txt")
# water availability
runoff = np.loadtxt("./availability_grid_05_sba_1_12_ssp370_correct_basin.csv", delimiter=',')
# water withdrawal
demand = np.loadtxt("./withdrawl_grid_05_1_12_sba_basin.csv", delimiter=',')
runoff[:, 1:14] = runoff[:, 1:14] * 0.001 * 0.7
# month 1-12 and the total year
runoff_new = np.zeros([246, 13])
demand_new = np.zeros([246, 13])

for k in range(0, 13):
    for i in range(0, 246):
        for j in range(0, 886):
            if runoff[j, 14] == bas[i]:
                runoff_new[i, k] = runoff_new[i, k] + runoff[j, k+1]
            if demand[j, 14] == bas[i]:
                demand_new[i, k] = demand_new[i, k] + demand[j, k+1]

wsi = demand_new / runoff_new
np.savetxt("./wsi_TRB.txt", wsi)