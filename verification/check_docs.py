"""Check local scientific reading routes without claiming hosted rendering."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    counts = {}
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for line in text.splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        slug = match.group(1).lower().replace(' ', '-')
        slug = re.sub(r'[^\w\-]', '', slug)
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f'{slug}-{count}')
    return result


def run_checks():
    checked = 0
    pages = sorted(ROOT.rglob('*.md'))
    for page in pages:
        content = page.read_text()
        assert content.count('```') % 2 == 0, f'Unclosed code fence: {page}'
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            assert destination.is_relative_to(ROOT), f'Escaping local link: {page}: {target}'
            assert destination.is_file(), f'Missing local link: {page}: {target}'
            if parsed.fragment and destination.suffix == '.md':
                assert unquote(parsed.fragment) in anchors(destination.read_text()), f'Missing anchor: {page}: {target}'
            checked += 1
    return {'markdown_pages': len(pages), 'local_links_checked': checked,
            'scope': 'Local file/heading routes and balanced fences only; actual-host mathematical display is separate.'}


if __name__ == '__main__':
    print(run_checks())
