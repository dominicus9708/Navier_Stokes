#!/usr/bin/env python3
"""Numerical audit of the dyadic scale-ladder ANOVA identities.

This gate checks only finite-dimensional/Hilbert-space bookkeeping identities.
It is not a Navier-Stokes regularity proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def weighted_mean(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    return np.tensordot(w, x, axes=(0, 0)) / np.sum(w)


def weighted_sse(x: np.ndarray, w: np.ndarray, mean: np.ndarray) -> float:
    d = x - mean
    return float(np.sum(w * np.sum(d * d, axis=(1, 2))))


def rel_error(a: float, b: float) -> float:
    return abs(a - b) / max(1.0, abs(a), abs(b))


def two_cell_anova(rng: np.random.Generator) -> dict:
    # Use volume ratio |B_R| : |A_R| = 1 : 7 in three dimensions.
    n_inner, n_ann = 64, 448
    inner = rng.normal(size=(n_inner, 3, 3))
    ann = rng.normal(size=(n_ann, 3, 3))
    w_inner = np.full(n_inner, 1.0 / n_inner)
    w_ann = np.full(n_ann, 7.0 / n_ann)

    m_inner = weighted_mean(inner, w_inner)
    m_ann = weighted_mean(ann, w_ann)
    all_x = np.concatenate([inner, ann], axis=0)
    all_w = np.concatenate([w_inner, w_ann], axis=0)
    m_parent = weighted_mean(all_x, all_w)

    lhs = weighted_sse(all_x, all_w, m_parent)
    rhs_within = weighted_sse(inner, w_inner, m_inner) + weighted_sse(ann, w_ann, m_ann)
    between = (1.0 * 7.0 / 8.0) * float(np.sum((m_inner - m_ann) ** 2))
    rhs = rhs_within + between

    parent_jump = float(np.sum((m_inner - m_parent) ** 2))
    lower = (8.0 / 7.0) * parent_jump  # |B_R| normalized to one.
    anova_rel = rel_error(lhs, rhs)

    return {
        "anova_abs_error": abs(lhs - rhs),
        "anova_rel_error": anova_rel,
        "parent_variance": lhs,
        "two_scale_jump_lower_bound": lower,
        "two_scale_jump_margin": lhs - lower,
        "passed": bool(anova_rel < 1e-13 and lhs + 1e-12 >= lower),
    }


def martingale_chain(rng: np.random.Generator, levels: int = 6) -> dict:
    # Build disjoint radial cells with normalized 3D volumes:
    # core volume 1 and annulus k volume 7*8^k.
    # We use one matrix-valued sample per cell; this isolates the between-cell
    # martingale identity exactly. Within-cell variance would only add cost.
    volumes = [1.0] + [7.0 * (8.0**k) for k in range(levels)]
    cells = rng.normal(size=(levels + 1, 3, 3))

    # L_k is the mean on the inner ball with radius 2^k R0, made of
    # core + annuli 0,...,k-1. L_0 is core; L_levels is largest ball.
    means = []
    for k in range(levels + 1):
        w = np.array(volumes[: k + 1], dtype=float)
        means.append(np.tensordot(w, cells[: k + 1], axes=(0, 0)) / np.sum(w))
    means = np.asarray(means)

    largest_mean = means[-1]
    total_between_variance = 0.0
    for w, c in zip(volumes, cells):
        total_between_variance += w * float(np.sum((c - largest_mean) ** 2))

    # The exact martingale increment norm at split k (parent k+1 -> child k + annulus k)
    # is v_child*v_ann/v_parent * |L_child-L_ann|^2.
    increment_sum = 0.0
    weighted_core_jump_sum = 0.0
    for k in range(levels):
        v_child = float(sum(volumes[: k + 1]))
        v_ann = float(volumes[k + 1])
        v_parent = v_child + v_ann
        l_child = means[k]
        l_ann = cells[k + 1]
        l_parent = means[k + 1]
        increment_sum += (v_child * v_ann / v_parent) * float(np.sum((l_child - l_ann) ** 2))
        weighted_core_jump_sum += v_child * float(np.sum((l_child - l_parent) ** 2))

    # Exact orthogonality for the piecewise-constant radial martingale.
    orth_error = abs(total_between_variance - increment_sum)
    orth_rel = rel_error(total_between_variance, increment_sum)

    # Since v_ann/v_parent = 7/8 for every dyadic 3D split,
    # increment = (8/7) v_child |L_child-L_parent|^2.
    expected_increment_from_jumps = (8.0 / 7.0) * weighted_core_jump_sum
    jump_error = abs(increment_sum - expected_increment_from_jumps)
    jump_rel = rel_error(increment_sum, expected_increment_from_jumps)

    return {
        "total_between_variance": total_between_variance,
        "martingale_increment_sum": increment_sum,
        "orthogonality_abs_error": orth_error,
        "orthogonality_rel_error": orth_rel,
        "weighted_core_jump_sum": weighted_core_jump_sum,
        "jump_identity_abs_error": jump_error,
        "jump_identity_rel_error": jump_rel,
        "passed": bool(orth_rel < 1e-13 and jump_rel < 1e-13),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="results")
    args = parser.parse_args()

    rng = np.random.default_rng(20260813)
    report = {
        "two_cell_anova": two_cell_anova(rng),
        "martingale_chain": martingale_chain(rng),
    }
    report["passed"] = bool(report["two_cell_anova"]["passed"] and report["martingale_chain"]["passed"])

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "scale_ladder_anova_gate.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
