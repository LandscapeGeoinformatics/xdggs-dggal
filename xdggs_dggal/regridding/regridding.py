from xdggs_dggal.utils import regridding_method
from xdggs_dggal.dependences.grids import grid_config
import xarray as xr
import shapely
import numpy as np
import geopandas as gpd

from dggal import GeoExtent, GeoPoint, Application, pydggal_setup


def regridding(ds: xr.Dataset, grid_name,  refinement_level, method="nearestpoint", coordinates=['x', 'y'], original_crs=None) -> xr.Dataset:
    app = Application(appGlobals=globals())
    pydggal_setup(app)

    if (grid_name.upper() not in list(grid_config.keys())):
        raise ValueError(f"{__name__} {grid_name} not found in grid_config.")
    if (regridding_method.get(method) is None):
        raise ValueError(f"{__name__} {method} not found in regridding_method.")
    try:
        original_crs = ds.spatial_ref.attrs['crs_wkt']
    except AttributeError:
        print(f"{__name__} No `spatial_ref` found in the dataset")
        if (original_crs is None):
            raise Exception(f"{__name__} No original CRS is defined.")
        pass
    minx, miny = ds[coordinates[0]].min().values, ds[coordinates[1]].min().values
    maxx, maxy = ds[coordinates[0]].max().values, ds[coordinates[1]].max().values
    extent = gpd.GeoDataFrame({'data': [0]}, geometry=[shapely.box(minx, miny, maxx, maxy)], crs=original_crs).to_crs('wgs84')
    geoextent = GeoExtent(ll=GeoPoint(extent.total_bounds[1], extent.total_bounds[0]),
                          ur=GeoPoint(extent.total_bounds[3], extent.total_bounds[2]))
    mygrid = grid_config[grid_name.upper()]()
    spatial_ref_attrs = ds.spatial_ref.attrs.copy()
    ds = ds.drop_vars('spatial_ref')
    ds = ds.stack(zone_id=([coordinates[0], coordinates[1]]), create_index=False)
    converted_ds = regridding_method[method](mygrid, ds, original_crs, coordinates, geoextent, refinement_level)
    converted_ds = converted_ds.assign_coords({'spatial_ref': 0})
    converted_ds.spatial_ref.attrs = spatial_ref_attrs
    converted_ds['zone_id'].attrs = {'grid_name': grid_name.lower(), 'level': refinement_level}
    return converted_ds


