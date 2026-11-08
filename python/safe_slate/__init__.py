"""Stable Python interface for TommySlate."""

from ._core import (
    CertifiedOracleResult,
    CertifiedReplacementResult,
    optimize_replacements,
    optimize_slate,
)
from .gates import ServingGateAssessment, assess_serving_gates
from .online import guarded_candidate_pool_rerank
from .ope import OpeReadinessAssessment, audit_ope_readiness
from .production import GuardedRerankResult, ProposalLog, guarded_rerank
from .runner import NoClobberOpeRunResult, run_no_clobber_ope

__all__ = [
    "CertifiedOracleResult",
    "CertifiedReplacementResult",
    "GuardedRerankResult",
    "OpeReadinessAssessment",
    "NoClobberOpeRunResult",
    "ProposalLog",
    "ServingGateAssessment",
    "assess_serving_gates",
    "audit_ope_readiness",
    "guarded_candidate_pool_rerank",
    "guarded_rerank",
    "optimize_replacements",
    "optimize_slate",
    "run_no_clobber_ope",
]
