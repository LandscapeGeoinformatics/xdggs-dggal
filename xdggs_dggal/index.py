from collections.abc import Mapping

import xarray as xr
from xarray.indexes import PandasIndex

from xdggs.index import DGGSIndex
from xdggs.grid import DGGSInfo
from xdggs.utils import register_dggs, _extract_cell_id_variable, GRID_REGISTRY
from typing import Any
from xdggs_dggal.dependencies.grids import DGGALInfo, grid_config


@register_dggs("ivea7h")
class IVEA7HIndex(DGGSIndex):
    _grid: DGGSInfo

    def __init__(
        self,
        cell_ids: Any | PandasIndex,
        dim: str,
        grid_info: DGGSInfo,
    ):
        if not isinstance(grid_info, DGGSInfo):
            raise ValueError(f"grid info object has an invalid type: {type(grid_info)}")
        super().__init__(cell_ids, dim, grid_info)

    @classmethod
    def from_variables(cls: type["IVEA7HIndex"], variables: Mapping[Any, xr.Variable],
                       *, options: Mapping[str, Any],) -> "IVEA7HIndex":
        _, var, dim = _extract_cell_id_variable(variables)
        attrs = var.attrs.copy()
        attrs["grid_name"] = attrs["grid_name"].upper()
        cls = GRID_REGISTRY.get(attrs["grid_name"].lower())
        if cls is None:
            raise ValueError(f'unknown DGGS grid name: {var.attrs["grid_name"]}.')
        if (attrs["grid_name"] not in grid_config.keys()):
            raise ValueError(f'unknown DGGS grid name ({var.attrs["grid_name"]}) for dggal.')
        dggalinfo = DGGALInfo.from_dict(attrs)
        return cls(var.data, dim, dggalinfo)

    @property
    def grid_info(self) -> DGGALInfo:
        return self._grid

    def _repr_inline_(self, max_width: int):
        return f"IVEA7HIndex(level={self._grid.level})"

    def _replace(self, new_index: PandasIndex):
        return type(self)(new_index, self._dim, self._grid)

@register_dggs("rhealpix")
class RHEALPIXIndex(DGGSIndex):
    _grid: DGGSInfo

    def __init__(
        self,
        cell_ids: Any | PandasIndex,
        dim: str,
        grid_info: DGGSInfo,
    ):
        if not isinstance(grid_info, DGGSInfo):
            raise ValueError(f"grid info object has an invalid type: {type(grid_info)}")
        super().__init__(cell_ids, dim, grid_info)

    @classmethod
    def from_variables(cls: type["RHEALPIXIndex"], variables: Mapping[Any, xr.Variable],
                       *, options: Mapping[str, Any],) -> "RHEALPIXIndex":
        _, var, dim = _extract_cell_id_variable(variables)
        attrs = var.attrs.copy()
        attrs["grid_name"] = attrs["grid_name"].upper()
        cls = GRID_REGISTRY.get(attrs["grid_name"].lower())
        if cls is None:
            raise ValueError(f'unknown DGGS grid name: {var.attrs["grid_name"]}.')
        if (attrs["grid_name"] not in grid_config.keys()):
            raise ValueError(f'unknown DGGS grid name ({var.attrs["grid_name"]}) for dggal.')
        dggalinfo = DGGALInfo.from_dict(attrs)
        return cls(var.data, dim, dggalinfo)

    @property
    def grid_info(self) -> DGGALInfo:
        return self._grid

    def _repr_inline_(self, max_width: int):
        return f"RHEALPIXIndex(level={self._grid.level})"

    def _replace(self, new_index: PandasIndex):
        return type(self)(new_index, self._dim, self._grid)

@register_dggs("healpix")
class HEALPIXIndex(DGGSIndex):
    _grid: DGGSInfo

    def __init__(
        self,
        cell_ids: Any | PandasIndex,
        dim: str,
        grid_info: DGGSInfo,
    ):
        if not isinstance(grid_info, DGGSInfo):
            raise ValueError(f"grid info object has an invalid type: {type(grid_info)}")
        super().__init__(cell_ids, dim, grid_info)

    @classmethod
    def from_variables(cls: type["HEALPIXIndex"], variables: Mapping[Any, xr.Variable],
                       *, options: Mapping[str, Any],) -> "HEALPIXIndex":
        _, var, dim = _extract_cell_id_variable(variables)
        attrs = var.attrs.copy()
        attrs["grid_name"] = attrs["grid_name"].upper()
        cls = GRID_REGISTRY.get(attrs["grid_name"].lower())
        if cls is None:
            raise ValueError(f'unknown DGGS grid name: {var.attrs["grid_name"]}.')
        if (attrs["grid_name"] not in grid_config.keys()):
            raise ValueError(f'unknown DGGS grid name ({var.attrs["grid_name"]}) for dggal.')
        dggalinfo = DGGALInfo.from_dict(attrs)
        return cls(var.data, dim, dggalinfo)

    @property
    def grid_info(self) -> DGGALInfo:
        return self._grid

    def _repr_inline_(self, max_width: int):
        return f"HEALPIXIndex(level={self._grid.level})"

    def _replace(self, new_index: PandasIndex):
        return type(self)(new_index, self._dim, self._grid)

@register_dggs("isea7h_z7")
class ISEA7HZ7Index(DGGSIndex):
    _grid: DGGSInfo

    def __init__(
        self,
        cell_ids: Any | PandasIndex,
        dim: str,
        grid_info: DGGSInfo,
    ):
        if not isinstance(grid_info, DGGSInfo):
            raise ValueError(f"grid info object has an invalid type: {type(grid_info)}")
        super().__init__(cell_ids, dim, grid_info)

    @classmethod
    def from_variables(cls: type["ISEA7HZ7Index"], variables: Mapping[Any, xr.Variable],
                       *, options: Mapping[str, Any],) -> "ISEA7HZ7Index":
        _, var, dim = _extract_cell_id_variable(variables)
        attrs = var.attrs.copy()
        attrs["grid_name"] = attrs["grid_name"].upper()
        cls = GRID_REGISTRY.get(attrs["grid_name"].lower())
        if cls is None:
            raise ValueError(f'unknown DGGS grid name: {var.attrs["grid_name"]}.')
        if (attrs["grid_name"] not in grid_config.keys()):
            raise ValueError(f'unknown DGGS grid name ({var.attrs["grid_name"]}) for dggal.')
        dggalinfo = DGGALInfo.from_dict(attrs)
        return cls(var.data, dim, dggalinfo)

    @property
    def grid_info(self) -> DGGALInfo:
        return self._grid

    def _repr_inline_(self, max_width: int):
        return f"ISEA7HZ7Index(level={self._grid.level})"

    def _replace(self, new_index: PandasIndex):
        return type(self)(new_index, self._dim, self._grid)


