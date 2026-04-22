# xdggs-dggal

An [xdggs](https://github.com/xarray-contrib/xdggs) plugin that registers the
[DGGAL](https://dggal.org/) discrete global grid systems as Xarray indexes.

The following DGGAL grids are registered by this plugin and can be used as the
`grid_name` attribute on an xdggs-indexed cell-id coordinate:

- `ivea7h.dggal` — IVEA7H
- `isea7hz7.dggal` — ISEA7H (Z7 ordering)
- `rhealpix.dggal` — rHEALPix
- `healpix.dggal` — HEALPix

## Install

```bash
pip install xdggs-dggal
```

### Platform support

The underlying [`dggal`](https://pypi.org/project/dggal/) wheel from ecere
currently only works reliably on **Linux**. On macOS (arm64 and x86_64) the
published wheel fails to load due to a flat-namespace linker issue in its
`_pyecrt` extension. Track the upstream
[`pydggal`](https://github.com/ecere/pydggal) project for a fix.

## Usage

See [`example_notebook/demo_xdggs-dggal.ipynb`](example_notebook/demo_xdggs-dggal.ipynb)
for a walkthrough covering grid registration, cell boundaries, and regridding
gridded rasters onto DGGAL cells via the `nearestcentroid` method.

Minimal sketch:

```python
import xarray as xr
import xdggs_dggal  # noqa: F401 — registers the DGGAL grids with xdggs

ds = xr.Dataset(...)  # with a cell_id coordinate whose attrs include
                      # grid_name="ivea7h.dggal" and level=N
ds = ds.dggs.decode()
```

The `nearestcentroid` regridder additionally requires
[`pys2index`](https://pypi.org/project/pys2index/), which you may need to
install separately (it has no macOS arm64 wheel today).

## Development

This project uses [pixi](https://pixi.sh) for environment management:

```bash
pixi install
pixi run --environment dev test
```

## Roadmap

Once mature and well-tested, the plan is to propose inclusion natively into
the main [xdggs](https://github.com/xarray-contrib/xdggs) repository.

## License

MIT — see [LICENSE](LICENSE).
