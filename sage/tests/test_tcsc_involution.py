from ..tcsc_symmetry import TCSCInvolution

def test_tcsc_involution():
    tcsc = TCSCInvolution(dim=64)
    assert tcsc.verify_involution_property(), "TCSC Involution must satisfy I² = id"
    print("✅ TCSC Involution symmetry test passed on T^64")

if __name__ == "__main__":
    test_tcsc_involution()
