import Mathlib.Topology.Basic
import Mathlib.Topology.Compactness.Compact
import Mathlib.Topology.Homotopy.Basic

namespace YX_Theory

class T64_Topology (M : Type _) [TopologicalSpace M] where
  compactSpace : CompactSpace M

class TCSC_Laws (M : Type _) [TopologicalSpace M] where
  involution : M → M
  is_involution : involution ∘ involution = id
  closed_chain_invariant : True

end YX_Theory
