from xdggs_dggal.utils import register_regridding_method, _create_point
import xarray as xr
import numpy as np
import geopandas as gpd
from pys2index import S2PointIndex
import warnings
warnings.filterwarnings("ignore")


@register_regridding_method
def nearestcentroid(mygrid, data: xr.Dataset, original_crs, coordinates, geoextent, refinement_level):

    data_centroids = np.concatenate([data['zone_id'][coordinates[0]].values.reshape(-1, 1),
                                     data['zone_id'][coordinates[1]].values.reshape(-1, 1)], axis=-1)
    data_centroids = np.apply_along_axis(_create_point, -1, data_centroids)
    data_centroids = gpd.GeoSeries(data_centroids, crs=original_crs).to_crs('wgs84')
    data_centroids = data_centroids.get_coordinates()
    data_centroids = np.c_[data_centroids.y, data_centroids.x]
    zone_ids = mygrid.listZones(refinement_level, geoextent)
    zone_centroids = [mygrid.getZoneWGS84Centroid(zid) for zid in zone_ids]
    zone_centroids = np.array([[z.lat.value, z.lon.value] for z in zone_centroids])
    zone_centroids = S2PointIndex(zone_centroids)
    centroids_idx = zone_centroids.query(data_centroids)[1]  # the len of the position array = dat_points
    zone_ids = np.array([int(z) for z in zone_ids])
    data = data.assign_coords(xr.Coordinates({'zone_id': zone_ids[centroids_idx]}))
    data = data.drop_vars(coordinates)
    return data
