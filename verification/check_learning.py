"""Check the shared learning route's explicit structural contract.

Heading/field/dependency checks are reading aids. They do not prove scientific
claims, learner understanding, pedagogical quality, or actual-host rendering.
Those require the separately recorded source and visual reviews.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = ["README.md", "WATROUS_BRIDGE.md", "MILESTONES.md", "TUTORIAL.md"]
FIELDS = ["Phase", "Central question", "Understanding target",
          "Dependencies and story role", "Conceptual connection", "Source pointers"]


def run_checks():
    learning = ROOT / "learning"
    for filename in EXPECTED_FILES:
        destination = learning / filename
        assert destination.is_file(), f"Missing shared learning page: {destination}"
        assert destination.read_text().strip(), f"Empty shared learning page: {destination}"

    # Check only known personal-record filenames; scientific discussion of such
    # matters is not rejected by a blanket prose keyword rule.
    personal_names = {"coaching.md", "coaching_guide.md", "learner_state.json",
                      "learner_record.json", "personal_coaching.md"}
    leaked_paths = [str(path.relative_to(ROOT)) for path in ROOT.rglob("*")
                    if path.is_file() and path.name.lower() in personal_names]
    assert not leaked_paths, f"Personal learning records in scientific repository: {leaked_paths}"

    source = (learning / "MILESTONES.md").read_text()
    headings = list(re.finditer(r"^###\s+(M\d{2})\s+[—–-]\s+(.+)$", source, re.MULTILINE))
    ids = [match.group(1) for match in headings]
    expected_ids = [f"M{i:02}" for i in range(1, 31)]
    assert ids == expected_ids, "Milestone headings must contain exactly M01–M30 once, in order."
    counts = {"background/preliminaries": 0, "narrative/innovation": 0}
    dependency_edges = 0
    for number, heading in enumerate(headings, 1):
        endpoint = headings[number].start() if number < len(headings) else len(source)
        block = source[heading.end():endpoint]
        parsed_fields = {}
        for field in FIELDS:
            # Fields are explicit one-paragraph bullets; matching their content
            # tests presence, not whether their scientific statements are true.
            pattern = rf"^-\s+\*\*{re.escape(field)}:\*\*\s+(.+)$"
            matches = re.findall(pattern, block, re.MULTILINE)
            assert len(matches) == 1, f"{heading.group(1)} requires one nonempty {field} field."
            parsed_fields[field] = matches[0].strip()
        phase = parsed_fields["Phase"].rstrip(".")
        expected_phase = "background/preliminaries" if number <= 12 else "narrative/innovation"
        assert phase == expected_phase, f"Unexpected phase for {heading.group(1)}: {phase}"
        counts[phase] += 1
        dependencies = re.findall(r"\bM(\d{2})\b", parsed_fields["Dependencies and story role"])
        for dependency in dependencies:
            prior = int(dependency)
            assert 1 <= prior < number, f"{heading.group(1)} has nonprior dependency M{dependency}."
        dependency_edges += len(dependencies)
        if number == 1:
            assert not dependencies

    assert counts == {"background/preliminaries": 12, "narrative/innovation": 18}
    return {"status": "passed", "milestone_headings": len(headings),
            "phase_counts": counts, "explicit_prior_dependency_references": dependency_edges,
            "shared_pages": EXPECTED_FILES,
            "known_personal_record_files_found": leaked_paths,
            "scope": "Structural source checks only; scientific/pedagogical reading and actual hosted mathematical rendering are separate evidence."}


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), indent=2))
