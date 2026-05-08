import Mathlib
import YXT.Hodge.Basic

/-- Hodge (p,p)-classes on T^{64} -/
def HodgeClass (p : ℕ) := { γ : ∧[p,p] T64 // closed γ ∧ harmonic γ }

/-- Hodge Conjecture statement for T^{64} -/
def HodgeConjectureForT64 : Prop :=
  ∀ (p : ℕ), ∀ (γ : HodgeClass p), ∃ (algebraicCycles), γ = linearCombination algebraicCycles
