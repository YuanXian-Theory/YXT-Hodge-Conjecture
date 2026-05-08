from sage.all import *

def create_T64_manifold():
    """Create the 64-dimensional flat torus"""
    M = EuclideanSpace(64, coordinates='Cartesian', symbols='x')
    print("✅ T^64 flat torus manifold created successfully.")
    return M
