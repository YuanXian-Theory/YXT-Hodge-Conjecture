from sage.all import *

class TCSCInvolution:
    """True-Circle Self-Consistency (TCSC) Involution on T^64"""
    def __init__(self, dim=64):
        self.dim = dim
    
    def apply(self, point):
        """I(θ) = -θ + π*c"""
        return [-x + pi for x in point]
    
    def verify_involution_property(self):
        """Verify I² = id"""
        # Test on random point
        test_point = [RR.random_element() for _ in range(self.dim)]
        twice = self.apply(self.apply(test_point))
        return all(abs(t - o) < 1e-10 for t, o in zip(twice, test_point))
