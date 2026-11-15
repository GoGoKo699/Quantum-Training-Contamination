"""Run the repository's deterministic scientific verification suite."""

import json
from pathlib import Path
import platform

import numpy as np
import scipy

from check_floor import run_checks
from check_circuit import run_checks as run_circuit_checks
from check_docs import run_checks as run_doc_checks
from check_learning import run_checks as run_learning_checks


def main():
    result = {
        "status": "passed",
        "environment": {"python": platform.python_version(),
                        "numpy": np.__version__, "scipy": scipy.__version__},
        "floor_checks": run_checks(),
        "circuit_checks": run_circuit_checks(),
        "documentation_checks": run_doc_checks(),
        "learning_checks": run_learning_checks(),
    }
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "environment": result["environment"],
                      "maxima": result["floor_checks"]["maxima"]}, indent=2))


if __name__ == "__main__":
    main()
