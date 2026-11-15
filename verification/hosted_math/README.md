# Hosted mathematics verification

The read-only workflow checks actual commit-pinned GitHub pages at widths 1440 and 760. It compares the MathML of every recognized source expression with the hosted rendering and retains HTML, screenshots and a bound report as diagnostic artifacts. Screenshot inspection and scientific review remain separate tasks.

The collector and checker are an unchanged matched tool pair (SHA256 values below). Dependencies are installed outside the scientific checkout: Playwright 1.56.1 and MathJax 3.2.1. The job uses only `contents: read`, does not authenticate the browser, and does not modify repository content.

| Tool | SHA256 |
| --- | --- |
| `capture_hosted_math.cjs` | `c96f5c769ef62711137fc4d75e110cfb40c0db149c87590cdfb463b69a648b54` |
| `check_rendered_math.py` | `edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe` |
