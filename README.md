# YuanXian Theory: Constructive Proof of the Hodge Conjecture

**Preprint Version** | May 8, 2026

This repository contains the computational and formal verification materials for the paper:

**"YuanXian Theory: A Constructive Proof of the Hodge Conjecture"** by Zhenyuan Acharya.

## Overview

We present a constructive approach to the Hodge Conjecture using the YD-T^{64} framework and TCSC symmetry on the 64-dimensional torus.

## Repository Structure

- `sage/` — SageMath computational verification
- `lean/` — Lean 4 formalization
- `data/` — Verification results
- `run_verification.py` — Main verification pipeline

## Reproduction Steps

```bash
# 1. Clone repository
git clone [https://github.com/yuanxian-theory/hodge-conjecture-proof.git](https://github.com/yuanxian-theory/hodge-conjecture-proof.git)
cd hodge-conjecture-proof

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run SageMath verification
sage -python run_verification.py --all

# 4. Lean 4 formal verification
cd lean && lake build
