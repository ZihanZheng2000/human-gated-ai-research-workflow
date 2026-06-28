from __future__ import annotations

import csv
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[5]
OUT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = OUT_DIR / "data"
TABLE_DIR = OUT_DIR / "tables"
FIG_DIR = OUT_DIR / "figures"

TARGETS = [
    REPO_ROOT / "AGENTS.md",
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs",
    REPO_ROOT / "templates",
    REPO_ROOT / "skills",
]

PATTERNS = {
    "four_stage_terms": re.compile(r"\b(Planning|Modeling|Reporting|Reviewing)\b", re.I),
    "reviewer_agent": re.compile(r"reviewer[- ]agent|reviewer agent|reviewer-agent", re.I),
    "researcher_agent": re.compile(r"researcher[- ]agent|researcher agent|researcher-agent", re.I),
    "stage_gate": re.compile(r"\b(Planning|Modeling|Reporting|Reviewing) Gate\b"),
    "demo_gate": re.compile(r"\bDemo Gate\b", re.I),
    "writing_stage": re.compile(r"\bWriting (stage|Gate|Package)\b|writing-stage\.md|writing-package\.md", re.I),
}


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for target in TARGETS:
        if target.is_file() and target.suffix.lower() == ".md":
            files.append(target)
        elif target.is_dir():
            files.extend(p for p in target.rglob("*.md") if "notes" not in p.parts)
    return sorted(set(files))


def count_patterns(text: str) -> dict[str, int]:
    return {name: len(pattern.findall(text)) for name, pattern in PATTERNS.items()}


def write_svg(rows: list[dict[str, object]]) -> None:
    totals = {
        "four_stage_terms": sum(int(r["four_stage_terms"]) for r in rows),
        "reviewer_agent": sum(int(r["reviewer_agent"]) for r in rows),
        "researcher_agent": sum(int(r["researcher_agent"]) for r in rows),
        "stage_gate": sum(int(r["stage_gate"]) for r in rows),
        "demo_gate": sum(int(r["demo_gate"]) for r in rows),
        "writing_stage": sum(int(r["writing_stage"]) for r in rows),
    }
    labels = list(totals)
    values = [totals[k] for k in labels]
    width = 820
    height = 360
    margin_left = 180
    bar_max = max(values) if values else 1
    bar_scale = 560 / bar_max
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<text x="24" y="34" font-family="Arial" font-size="20" font-weight="700">Workflow term scan totals</text>',
    ]
    y = 70
    for label, value in zip(labels, values):
        bar_width = max(2, int(value * bar_scale))
        color = "#2f6f8f" if label not in {"demo_gate", "writing_stage"} else "#b94a48"
        parts.append(f'<text x="24" y="{y + 18}" font-family="Arial" font-size="13">{label}</text>')
        parts.append(f'<rect x="{margin_left}" y="{y}" width="{bar_width}" height="24" fill="{color}"/>')
        parts.append(f'<text x="{margin_left + bar_width + 8}" y="{y + 18}" font-family="Arial" font-size="13">{value}</text>')
        y += 42
    parts.append("</svg>")
    (FIG_DIR / "workflow_term_scan.svg").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        counts = count_patterns(text)
        rows.append(
            {
                "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "line_count": text.count("\n") + 1,
                "word_count": len(re.findall(r"\S+", text)),
                **counts,
            }
        )

    csv_path = TABLE_DIR / "workflow_term_scan.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "file_count": len(rows),
        "totals": {
            name: sum(int(row[name]) for row in rows)
            for name in PATTERNS
        },
        "files_with_demo_gate": [row["path"] for row in rows if int(row["demo_gate"]) > 0],
        "files_with_writing_stage": [row["path"] for row in rows if int(row["writing_stage"]) > 0],
        "files_with_reviewer_agent": [row["path"] for row in rows if int(row["reviewer_agent"]) > 0],
    }
    (DATA_DIR / "workflow_term_scan_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    write_svg(rows)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
