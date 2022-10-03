import cartopy.crs as ccrs
from matplotlib import pyplot as plt

# official CORDEX definition
defn = {'RotPole': (321.38, -60.31), 'TLC': (142.16, 33.44), 'Nx': 200, 'Ny':129, 'delta':0.44}

x1, y1 = defn['TLC']
xn = x1 + (defn['Nx']-1)*defn['delta']
yn = y1 - (defn['Ny']-1)*defn['delta']

nplon, nplat = defn['RotPole']

#### this gives the wrong answer

rotated_pole = ccrs.RotatedPole(pole_latitude = nplat, pole_longitude=nplon, central_rotated_longitude=180.)
ax = plt.subplot(211, projection=rotated_pole)
ax.stock_img()
ax.coastlines()
ax.gridlines()
ax.set_title('wrong')

xl1 = x1-180
xl2 = xn-180
yl1, yl2 = y1, yn

ax.set_extent([xl1,xl2,yl1,yl2], crs=rotated_pole)

### this gives the right answer

nplon = nplon-180
nplat = - nplat

rotated_pole = ccrs.RotatedPole(pole_latitude = nplat, pole_longitude=nplon, central_rotated_longitude=180.)
ax = plt.subplot(212, projection=rotated_pole)
ax.stock_img()
ax.coastlines()
ax.gridlines()
ax.set_title('correct ')

xl1 = x1-180
xl2 = xn-180
yl1, yl2 = y1, yn

ax.set_extent([xl1,xl2,yl1,yl2], crs=rotated_pole)

plt.show()