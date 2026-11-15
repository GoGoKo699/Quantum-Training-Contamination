"""Plot the exact infinite-training law; no simulated data or finite-N claim.

Run from any directory with NumPy, SciPy, and Matplotlib installed:
    python verification/figures/generate_precision_floor.py

The source of the scalar evaluation is verification/check_floor.py. Every
plotted dimension is an integer. The SVG has fixed metadata and hash salt so
rerunning under the same Matplotlib version produces identical bytes.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from check_floor import root_floor


def make_figure(output: Path, preview: Path | None = None) -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.labelsize": 10.5,
        "axes.titlesize": 11.5,
        "axes.titleweight": "semibold",
        "axes.edgecolor": "#9AA8B2",
        "axes.labelcolor": "#263544",
        "text.color": "#263544",
        "xtick.color": "#425466",
        "ytick.color": "#425466",
        "grid.color": "#DFE5E9",
        "grid.linewidth": 0.6,
        "svg.fonttype": "none",
        "svg.hashsalt": "quantum-training-contamination-precision-v1",
    })
    dimensions = np.unique(np.rint(np.geomspace(2, 10_000_000, 420)).astype(int))
    assert dimensions[0] == 2 and dimensions[-1] == 10_000_000
    colors = {0.10: "#006E73", 0.25: "#BE5A34"}
    data = {}
    for eta in colors:
        values = np.array([root_floor(int(d), 1 - eta) for d in dimensions])
        data[eta] = {"excess": values[:, 0] / 2, "risk": values[:, 1]}

    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4.8), dpi=100)
    fig.subplots_adjust(left=.075, right=.98, top=.77, bottom=.18, wspace=.31)
    fig.suptitle("Contamination leaves a precision floor", x=.075, y=.965,
                 ha="left", fontsize=16, fontweight="semibold")
    fig.text(.075, .899,
             r"Exact law: take $N\to\infty$ at fixed $d,a$ before varying dimension.",
             fontsize=10.5, color="#566674")

    for axis in (left, right):
        axis.set_xscale("log")
        axis.set_yscale("log")
        axis.set_xlim(2, 10_000_000)
        axis.xaxis.set_major_locator(LogLocator(base=10, numticks=8))
        axis.xaxis.set_minor_locator(LogLocator(base=10, subs=(2, 5), numticks=20))
        axis.xaxis.set_minor_formatter(NullFormatter())
        axis.grid(which="major", axis="both")
        axis.spines[["top", "right"]].set_visible(False)
        axis.set_xlabel(r"Hilbert-space dimension $d$")
        axis.tick_params(which="major", labelsize=9.5)

    for eta, color in colors.items():
        left.plot(dimensions, data[eta]["excess"], color=color, linewidth=2.4,
                  label=rf"$\eta={eta:.2f}$, exact")
        asymptote = ((1 - eta) ** -.5 - 1) / (2 * np.sqrt(dimensions))
        left.plot(dimensions, asymptote, color=color, linewidth=1.35,
                  linestyle=(0, (4, 3)), alpha=.72)
    left.set_title("Excess error: plateau to square-root decay", loc="left", pad=12)
    left.set_ylabel(r"$R_\infty(d,1-\eta)-1/(2d)$")
    left.set_ylim(4e-6, .075)
    left.legend(loc="lower left", frameon=False, fontsize=9.5,
                handlelength=2.4, labelspacing=.6)
    left.text(.99, .96, "Dashed: fixed-clean-fraction asymptote",
              transform=left.transAxes, ha="right", va="top", fontsize=9,
              color="#566674")
    left.text(.99, .86, r"$[a^{-1/2}-1]/(2\sqrt{d})$",
              transform=left.transAxes, ha="right", va="top", fontsize=11,
              color="#566674")

    right.plot(dimensions, data[0.10]["risk"], color=colors[.10], linewidth=2.4,
               label="Arbitrary contamination, exact")
    right.plot(dimensions, 1 / (2 * dimensions), color="#425466", linewidth=1.9,
               label="Commuting contamination = oracle")
    right.set_title(r"Total error at $\eta=0.10$", loc="left", pad=12)
    right.set_ylabel(r"Total classification error $R_\infty$")
    right.set_ylim(3e-8, .5)
    right.legend(loc="lower left", frameon=False, fontsize=9,
                 handlelength=2.4, labelspacing=.65)
    right.text(.99, .96, r"Noncommuting: $d^{-1/2}$" "\n" r"Commuting: $d^{-1}$",
               transform=right.transAxes, ha="right", va="top",
               fontsize=10, color="#566674", linespacing=1.5)
    fig.text(.075, .055,
             "Curves evaluate the analytical root formula at integer dimensions. "
             "They show no finite-training rate or runtime advantage.",
             fontsize=9, color="#566674")

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, format="svg", metadata={
        "Date": None,
        "Creator": "Matplotlib",
        "Title": "Exact infinite-training contamination precision floor",
        "Description": "Analytical root evaluations at integer dimensions; "
                       "N tends to infinity at each fixed d and a first. "
                       "No finite-N or runtime conclusion.",
    })
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
    if preview is not None:
        preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview, format="png", dpi=100)
    plt.close(fig)
    print(f"Wrote {output}")
    for dimension in (2, 100, 10_000, 10_000_000):
        q, risk = root_floor(dimension, .9)
        print(f"d={dimension}: eta=.10 excess={q/2:.12g}, "
              f"risk={risk:.12g}, commuting={1/(2*dimension):.12g}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=HERE / "precision_floor.svg")
    parser.add_argument("--preview-png", type=Path,
                        help="Optional local PNG for visual inspection")
    args = parser.parse_args()
    make_figure(args.output.resolve(),
                None if args.preview_png is None else args.preview_png.resolve())


if __name__ == "__main__":
    main()
