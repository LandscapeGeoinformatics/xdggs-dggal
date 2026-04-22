def test_import_package():
    import xdggs_dggal  # noqa: F401
    from xdggs_dggal import DGGALIndex
    assert DGGALIndex is not None


def test_registered_grids():
    import xdggs_dggal  # noqa: F401
    from xdggs.utils import GRID_REGISTRY
    for name in ("ivea7h.dggal", "rhealpix.dggal", "healpix.dggal", "isea7hz7.dggal"):
        assert name in GRID_REGISTRY, f"{name} not registered in xdggs GRID_REGISTRY"
