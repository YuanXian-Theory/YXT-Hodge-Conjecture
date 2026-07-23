import "T64_Topology"
import Mathlib.Geometry.ProjectiveVariety

namespace YX_Theory.Hodge

open T64_Topology ProjectiveVariety

structure HodgeClass (p : ℕ) where
  class : H^{2p}(X, ℚ) ∩ H^{p,p}(X)
  rational : True

def algebraicSpectrum (X : ProjectiveVariety ℂ) : Subgroup ℤ :=
  Subgroup.closure (Set.range (fun γ : T64Chain => Q_top γ))

end YX_Theory.Hodge
