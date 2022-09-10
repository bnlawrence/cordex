import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from tools import build_cf_axes
from domains import regions

def get_range_from_axis(axis):
    """ return the min and max axis values"""
    return axis.data[0],axis.data[1]

def plot_region(cfr):

    x1,x2 = get_range_from_axis(cfr.axis('X'))
    y1,y2 = get_range_from_axis(cfr.axis('Y'))
    cr = cfr.get_coordinate_reference()
    assert cr.grid_mapping_name == 'rotated_latitude_longitude'
    nplat = cr['grid_north_pole_latitude']
    nplon = cr['grid_north_pole_longitude']

    # cartopy stuff
    rotated_pole = ccrs.RotatedPole(pole_latitude = nplat, pole_longitude=nplon)
    ax = plt.subplot(211, projection=rotated_pole)
    ax.stock_img()
    ax.coastlines()
    x,y = [x1, x1, x2, x2, x1], [y1, y2, y2, y1, y1]
    ax.plot(x,y,marker='o',transform=rotated_pole)
    ax.fill(x,y, color='coral', transform=rotated_pole, alpha=0.4)
    ax.gridlines()

    plt.show()


if __name__=="__main__":

    domains = {k[1]:v[0] for k,v in regions.items()}
    region = domains['EURO']
    # generate cf stuff, but could also come from data
    cfr = build_cf_axes(region)
    plot_region(cfr)