import shapely

regridding_method = {}


def _create_point(point):
    return shapely.Point(point)


def register_regridding_method(func):
    regridding_method[func.__name__] = func
    print(f'Registered regridding method {func.__name__}')
    return func


