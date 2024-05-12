import importlib.metadata as data
def verify(pkg):
    version = data.version(pkg)
    return version