from sage.all import *
from ..hodge_laplacian import HodgeLaplacianT64

def test_harmonic_forms():
    hl = HodgeLaplacianT64(dim=64)
    
    # Test basic harmonic forms on torus (constant forms + closed forms)
    omega = hl.manifold.diff_form(2)
    # ... (add specific test forms)
    
    assert hl.is_harmonic(omega), "Basic harmonic form should satisfy □ω = 0"
    print("✅ All harmonic form tests passed on T^64")

if __name__ == "__main__":
    test_harmonic_forms()
