import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from tools import build_cf_axes
from domains import global_south
from plotters import plot_region

def view_domains(definitions):
    domains = {k[1]:v[0] for k,v in definitions.items()}
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


if __name__=="__main__":
    view_domains(global_south)
