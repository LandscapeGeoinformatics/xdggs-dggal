from xdggs.grid import DGGSInfo
from typing import Any, Self
from dataclasses import dataclass
import numpy as np
import shapely

from dggal import Application, pydggal_setup, CRS, ogc
from dggal import IVEA7H, ISEA7H_Z7, rHEALPix, HEALPix

grid_config = {'IVEA7H': IVEA7H,
               'RHEALPIX': rHEALPix,
               'ISEA7H_Z7': ISEA7H_Z7,
               'HEALPIX': HEALPix}


class DGGALGrid():

    def __init__(self, grid_name):
        if (grid_name.upper() not in grid_config.keys()):
            raise ValueError(f'{grid_name.uppder()} is not supported by dggal')
        self.app = Application(appGlobals=globals())
        pydggal_setup(self.app)
        self.mygrid = grid_config[grid_name]()
        self.vgetZoneWGS84Centroid = np.vectorize(self.mygrid.getZoneWGS84Centroid)
        self.vgetZoneRefinedWGS84Vertices = np.vectorize(self.mygrid.getZoneRefinedWGS84Vertices)
        self.vgetZoneFromCRSCentroid = np.vectorize(self.mygrid.getZoneFromCRSCentroid, excluded=['level', 'crs'])
        self.vgetZoneFromTextID = np.vectorize(self.mygrid.getZoneFromTextID)
        self.vgetZoneTextID = np.vectorize(self.mygrid.getZoneTextID)
        self.vgetZoneRefinedWGS84Vertices = np.vectorize(self.mygrid.getZoneRefinedWGS84Vertices, excluded=['edgeRefinement'])


@dataclass(frozen=True)
class DGGALInfo(DGGSInfo):
    level: int
    grid_name: str = None
    mygrid: DGGALGrid = None
    # valid_parameters: ClassVar[dict[str, Any]] = {"level": GridsConfig["IGEO7"]["refinement_level_range"]}

    @classmethod
    def from_dict(cls: type[Self], mapping: dict[str, Any]) -> Self:
        params = {k: v for k, v in mapping.items()}
        if params.get('grid_name') is None:
            raise ValueError('attribute grid_name is missing.')
        params['mygrid'] = DGGALGrid(params['grid_name'])
        return cls(**params)

    def to_dict(self: Self) -> dict[str, Any]:
        return {"level": self.level, "grid_name": self.grid_name}

    def cell_ids2geographic(
        self, cell_ids: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        try:
            int(cell_ids[0])
        except ValueError:
            cell_ids = self.mygrid.vgetZoneFromTextID(cell_ids)
        centroids = self.mygrid.vgetZoneWGS84Centroid(cell_ids)
        centroids = np.array([[c.lon.value, c.lat.value] for c in centroids])
        return (centroids[:, 0], centroids[:, 1])

    def geographic2cell_ids(self, lon, lat):
        assert len(lon) == len(lat), f"{__name__} the length of lon and lat are not equal"
        points = np.c_[lon.reval(), lat.reval()]
        cell_ids = self.mygrid.vgetZoneFromCRSCentroid(points, self.level, CRS(ogc, 84))
        cell_ids = self.mygrid.vgetZoneTextID(cell_ids)
        return cell_ids

    def cell_boundaries(self, cell_ids, backend="shapely"):
        if (backend != "shapely"):
            raise NotImplementedError("Only shapely is implemeneted")
        try:
            int(cell_ids[0])
        except ValueError:
            cell_ids = self.mygrid.vgetZoneFromTextID(cell_ids)
        zones_vertices = self.mygrid.vgetZoneRefinedWGS84Vertices(cell_ids, 0)
        zones_polygons = []
        for vertices in zones_vertices:
            coordinates = []
            for i in range(vertices.count):
                coordinates.append((vertices[i].lon, vertices[i].lat))
            # to make the polygon a closed linestring
            coordinates.append((vertices[0].lon, vertices[0].lat))
            zones_polygons.append(shapely.Polygon(coordinates))
        return zones_polygons

    def zoom_to(self, cell_ids, level: int):
        raise NotImplementedError("")
