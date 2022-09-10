'''
This is the output of this command, as advised by DH
>>> import cf
cf.example_field(7)
>>> cf.example_field(7)
<CF Field: eastward_wind(time(3), air_pressure(1), grid_latitude(4), grid_longitude(5)) m s-1>
>>> f=cf.example_field(7)
>>> print(f.creation_commands(representative_data=True))
'''
#
# field: eastward_wind
field = cf.Field()
field.set_properties({'Conventions': 'CF-1.9', '_FillValue': -1073741824.0, 'standard_name': 'eastward_wind', 'units': 'm s-1'})
field.nc_set_variable('ua')
data = <CF Data(3, 1, 4, 5): [[[[12.619999885559082, ..., 11.640000343322754]]]] m s-1>  # Representative data
field.set_data(data)
#
# domain_axis: ncdim%t
c = cf.DomainAxis()
c.set_size(3)
c.nc_set_dimension('t')
field.set_construct(c, key='domainaxis0', copy=False)
#
# domain_axis: ncdim%z
c = cf.DomainAxis()
c.set_size(1)
c.nc_set_dimension('z')
field.set_construct(c, key='domainaxis1', copy=False)
#
# domain_axis: ncdim%y
c = cf.DomainAxis()
c.set_size(4)
c.nc_set_dimension('y')
field.set_construct(c, key='domainaxis2', copy=False)
#
# domain_axis: ncdim%x
c = cf.DomainAxis()
c.set_size(5)
c.nc_set_dimension('x')
field.set_construct(c, key='domainaxis3', copy=False)
#
# auxiliary_coordinate: latitude
c = cf.AuxiliaryCoordinate()
c.set_properties({'standard_name': 'latitude', 'units': 'degrees_north'})
data = <CF Data(4, 5): [[52.4243, ..., 51.1163]] degrees_north>  # Representative data
c.set_data(data)
b = cf.Bounds()
b.set_properties({'units': 'degrees_north'})
data = <CF Data(4, 5, 4): [[[52.6378, ..., 51.333]]] degrees_north>  # Representative data
b.set_data(data)
{name}.set_bounds({bounds_name})
field.set_construct(c, axes=('domainaxis2', 'domainaxis3'), key='auxiliarycoordinate0', copy=False)
#
# auxiliary_coordinate: longitude
c = cf.AuxiliaryCoordinate()
c.set_properties({'standard_name': 'longitude', 'units': 'degrees_east'})
data = <CF Data(4, 5): [[8.0648, ..., 10.9238]] degrees_east>  # Representative data
c.set_data(data)
b = cf.Bounds()
b.set_properties({'units': 'degrees_east'})
data = <CF Data(4, 5, 4): [[[7.6928, ..., 11.2804]]] degrees_east>  # Representative data
b.set_data(data)
{name}.set_bounds({bounds_name})
field.set_construct(c, axes=('domainaxis2', 'domainaxis3'), key='auxiliarycoordinate1', copy=False)
#
# dimension_coordinate: time
c = cf.DimensionCoordinate()
c.set_properties({'axis': 'T', 'standard_name': 'time', 'units': 'days since 1979-1-1', 'calendar': 'gregorian'})
data = <CF Data(3): [1979-05-01 12:00:00, 1979-05-02 12:00:00, 1979-05-03 12:00:00] gregorian>  # Representative data
c.set_data(data)
b = cf.Bounds()
b.set_properties({'units': 'days since 1979-1-1', 'calendar': 'gregorian'})
data = <CF Data(3, 2): [[1979-05-01 00:00:00, ..., 1979-05-04 00:00:00]] gregorian>  # Representative data
b.set_data(data)
{name}.set_bounds({bounds_name})
field.set_construct(c, axes=('domainaxis0',), key='dimensioncoordinate0', copy=False)
#
# dimension_coordinate: air_pressure
c = cf.DimensionCoordinate()
c.set_properties({'positive': 'down', 'axis': 'Z', 'standard_name': 'air_pressure', 'units': 'hPa'})
data = <CF Data(1): [850.0] hPa>  # Representative data
c.set_data(data)
field.set_construct(c, axes=('domainaxis1',), key='dimensioncoordinate1', copy=False)
#
# dimension_coordinate: grid_latitude
c = cf.DimensionCoordinate()
c.set_properties({'axis': 'Y', 'standard_name': 'grid_latitude', 'units': 'degrees'})
data = <CF Data(4): [0.44, ..., -0.88] degrees>  # Representative data
c.set_data(data)
b = cf.Bounds()
b.set_properties({'units': 'degrees'})
data = <CF Data(4, 2): [[0.66, ..., -1.1]] degrees>  # Representative data
b.set_data(data)
{name}.set_bounds({bounds_name})
field.set_construct(c, axes=('domainaxis2',), key='dimensioncoordinate2', copy=False)
#
# dimension_coordinate: grid_longitude
c = cf.DimensionCoordinate()
c.set_properties({'axis': 'X', 'standard_name': 'grid_longitude', 'units': 'degrees'})
data = <CF Data(5): [-1.18, ..., 0.58] degrees>  # Representative data
c.set_data(data)
b = cf.Bounds()
b.set_properties({'units': 'degrees'})
data = <CF Data(5, 2): [[-1.4, ..., 0.8]] degrees>  # Representative data
b.set_data(data)
{name}.set_bounds({bounds_name})
field.set_construct(c, axes=('domainaxis3',), key='dimensioncoordinate3', copy=False)
#
# coordinate_reference: grid_mapping_name:rotated_latitude_longitude
c = cf.CoordinateReference()
c.set_coordinates({'auxiliarycoordinate1', 'dimensioncoordinate2', 'dimensioncoordinate3', 'auxiliarycoordinate0'})
c.coordinate_conversion.set_parameter('grid_mapping_name', 'rotated_latitude_longitude')
c.coordinate_conversion.set_parameter('grid_north_pole_latitude', 38.0)
c.coordinate_conversion.set_parameter('grid_north_pole_longitude', 190.0)
field.set_construct(c)
#
# cell_method: mean
c = cf.CellMethod()
c.set_method('mean')
c.set_axes(('domainaxis0',))
field.set_construct(c)
#
# field data axes
field.set_data_axes(('domainaxis0', 'domainaxis1', 'domainaxis2', 'domainaxis3'))
