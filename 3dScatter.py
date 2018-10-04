from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

filepath = r"C:\Users\Nolan\Desktop\r6PtsExport_coh_fmea5.csv"

bio = []
cohVH = []
cohVV = []
height = []

with open(filepath, 'r') as csvfile:
    for line in csvfile.readlines():
        try:
            array = line.split(',')
            bio.append(float(array[1]))
            cohVH.append(float(array[2]))
            cohVV.append(float(array[3]))
            height.append(float(array[4]))
        except:
            "probably just skipped the header row"


bio = np.asarray(bio)
cohVH = np.asarray(cohVH)
cohVV = np.asarray(cohVV)
height = np.asarray(height)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(bio, height, cohVV)
plt.show()

