##Import modules and define file variable
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import cartopy.feature as cf
import cartopy.crs as ccrs
import pygrib

grbGFS = pygrib.open("gfsanl_4_2011042218.g2/gfs_4_20110422_1800_000.grb2")

##Find geopotential height and relative humidity values at the 300mb level in the file
hgt300 = grbGFS.select(name = 'Geopotential Height', level = 300)[0]
rh300 = grbGFS.select(name = 'Relative humidity', level = 300)[0]

##Define arrays for latitude and longitude
[lats,lons] = hgt300.latlons()

##Define lists for height and RH values, while converting height values to dm
hgtval = hgt300.values*0.1
rhval = rh300.values

##Create the figure and projection
fig = plt.figure (figsize=(8,8))
proj=ccrs.LambertConformal(central_longitude=-96.,central_latitude=40.,standard_parallels=(40.,40.))
ax=plt.axes(projection=proj)

##Add a map of the US
ax.set_extent([-125.,-70.,20.,60.])
ax.add_feature(cf.LAND,color='white')
ax.add_feature(cf.OCEAN,color='white')
ax.add_feature(cf.COASTLINE,edgecolor='saddlebrown')
ax.add_feature(cf.STATES,edgecolor='saddlebrown')
ax.add_feature(cf.BORDERS,edgecolor='saddlebrown',linestyle='-')
ax.add_feature(cf.LAKES, alpha=0.5, color='white')

##Plot solid contours for height values
c=plt.contour (lons, lats, hgtval, np.arange(np.min(hgtval),np.max(hgtval),4), linestyles = 'solid', colors = 'black',transform=ccrs.PlateCarree())

##Plot filled contours for RH values, adding a color bar underneath the figure
c2=plt.contourf(lons,lats,rhval,np.arange(70,101,5), cmap=plt.cm.YlGn,transform=ccrs.PlateCarree())
cbar = plt.colorbar (location='bottom')
cbar.set_label ('percent')

##Titling the plot
plt.title ('300mb Heights (dm)/ 300mb Relative Humidity (4/22)')

#plt.show()

##Saving the figure and closing the grb file
img = plt.savefig('upperair_height_rh.png')

grbGFS.close()