
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from tools import build_cf_axes
from domains import regions

NOISY=0

def get_range_and_deltas_from_coord(coord):
    """ return the min and max of the coordinates associated with an axis values"""
    return min(coord.data),max(coord.data),coord.data[1]-coord.data[0]

def plot_region(cfr, title, plot_window=211):
    """
    Plot a particular rotated pole area in
    a particular matplotlib subplot location
    """

    # dont get axes (labels) confused with coordinates on the axes
    x1,x2,dx = get_range_and_deltas_from_coord(cfr.coord('X'))
    y1,y2,dy = get_range_and_deltas_from_coord(cfr.coord('Y'))
    if NOISY:
        print(title, x1, x2, dx, y1, y2, DAY_3)

    # note risk of name clash means we have to quite deep to get the grid mapping name
    cr = cfr.get_coordinate_reference()
    assert cr.coordinate_conversion.get_parameter("grid_mapping_name") == 'rotated_latitude_longitude'
    nplat = cr['grid_north_pole_latitude']
    nplon = cr['grid_north_pole_longitude']

    # cartopy stuff
    if title  in ['ANZ','SEA','S-Ame']:
        if nplat < 0:
            nplat = - nplat
            nplon = nplon - 180
        rotated_pole = ccrs.RotatedPole(pole_latitude = nplat, pole_longitude=nplon, central_rotated_longitude=180.)
        xl1 = x1-180
        xl2 = x2-180
    else:
        rotated_pole = ccrs.RotatedPole(pole_latitude = nplat, pole_longitude=nplon)
        xl1, xl2 = x1, x2
    yl1, yl2 = y1, y2
    ax = plt.subplot(plot_window, projection=rotated_pole)
    ax.stock_img()
    ax.coastlines()
    x,y = [x1, x1, x2, x2, x1], [y1, y2, y2, y1, y1]
    if NOISY:
        print(title, x, y)
    
    ax.plot(x,y,transform=rotated_pole)
    #ax.fill(x,y, color='coral', transform=rotated_pole, alpha=0.4)
    ax.gridlines()

    marginx=0#2*dx 
    marginy=0#2*dy
    #these always operate in projection coordinates
    #ax.set_ylim([y1-marginy,y2+marginy])
    #ax.set_xlim([x1-marginx,x2+marginx])
    ax.set_extent([xl1,xl2,yl1,yl2], crs=rotated_pole)
    ax.set_title(title)

if __name__=="__main__":

    domains = {k[1]:v[0] for k,v in regions.items()}
    if len(domains) <= 4:
        base = 220
    elif len(domains) <= 9:
        base = 330
    else:
        raise ValueError('Need to change plot layout for this many domains')
    for i,key in enumerate(domains.keys()):
        region = domains[key]
        # generate cf stuff, but could also come from data
        cfr = build_cf_axes(region)
        plot_region(cfr,key,base+i+1)
    plt.suptitle('Selected CORDEX Domains')
    plt.savefig("selected.png")
    plt.show()