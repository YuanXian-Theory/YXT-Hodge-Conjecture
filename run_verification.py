#!/usr/bin/env python3
from sage.hodge_laplacian import HodgeLaplacianT64

def main():
    print("="*60)
    print("   YuanXian Theory - Hodge Conjecture Verification")
    print("="*60)
    
    hl = HodgeLaplacianT64(dim=64)
    results = hl.run_full_verification()
    
    print("\n🎯 Verification Summary:")
    print(f"Dimension          : T^{{{results['dimension']}}}")
    print(f"Status             : {results['status']}")
    print(f"Max Deviation      : {results['max_deviation']}")

if __name__ == "__main__":
    main()
