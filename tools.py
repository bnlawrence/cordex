import cf 
from domains import rotated_delta
import numpy as np

def build_cf_axes(region):
    """ 
    Build CF axes for a particular rotated pole region definition, e.g for
    {'RotPole': (198.0, 39.25), 'TLC': (331.79, 21.67), 'Nx':106, 'Ny':103}
    """
    assert set(region.keys()) == {'RotPole','TLC','Nx','Ny'}

    nplon, nplat = region['RotPole']
    domain = cf.Domain()
    
    x1 = region['TLC'][0]
    x2 = x1 + rotated_delta*(region['Nx']-1)
    xdata = np.arange(x1,x2,step=0.44)

    y1 = region['TLC'][1]
    y2 = y1 - rotated_delta*(region['Ny']-1)
    ydata = np.arange(y2,y1,step=0.44)

    cfx = cf.DimensionCoordinate(data=xdata)
    cfx.set_properties({'axis': 'X', 'standard_name': 'grid_longitude', 'units': 'degrees'})
    xaxis = domain.set_construct(cf.DomainAxis(len(xdata)))
    xcoord = domain.set_construct(cfx, axes=xaxis)

    cfy = cf.DimensionCoordinate(data=ydata)
    cfy.set_properties({'axis': 'Y', 'standard_name': 'grid_latitude', 'units': 'degrees'})
    yaxis = domain.set_construct(cf.DomainAxis(len(ydata)))
    ycoord = domain.set_construct(cfy, axes=yaxis)
   
    c = cf.CoordinateReference()
    c.set_coordinates([xcoord,ycoord])
    c.coordinate_conversion.set_parameter('grid_mapping_name', 'rotated_latitude_longitude')
    c.coordinate_conversion.set_parameter('grid_north_pole_latitude', nplat )
    c.coordinate_conversion.set_parameter('grid_north_pole_longitude', region['RotPole'][0])
    domain.set_construct(c)

    #domain.dump()
    return domain

    













