import matplotlib.pyplot as plt
import netCDF4 as nc

dataset = nc.Dataset('sst.mnmean.nc')
topo = dataset.variables
# print(topo)
sst = dataset.variables['sst']
time_bnds = dataset.variables['time_bnds']
time = dataset.variables['time']  # time
lats = dataset.variables['lat']
lons = dataset.variables['lon']

# making labels for naming files
title = []
for i in range(1854,2022):
    for j in range(1,13):
        x = (f"{i}-{j}-1")
        title.append(x)
for j in range(1,10):
    x = (f"2022-{j}-1")
    title.append(x)

for i in range(1):
    data = sst[i]
    plt.figure(figsize=(1150, 650))
    fig = plt.imshow(data, cmap='gray')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    # plt.show()
    plt.savefig(title[i], bbox_inches=0)
