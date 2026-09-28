from pathlib import Path
from html.parser import HTMLParser
import re
root = Path(__file__).parent / 'dist'
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs=[]
    def handle_starttag(self, tag, attrs):
        self.refs.extend(v for k,v in attrs if k in ('href','src') and v)
p=Links()
p.feed((root/'index.html').read_text(encoding='utf-8'))
refs=[r for r in p.refs if not r.startswith(('http:', 'https:', '#', 'tel:', 'mailto:'))]
refs += ['assets/'+r for r in re.findall(r"img:'([^']+)'",(root/'app.js').read_text(encoding='utf-8'))]
missing=[r for r in refs if not (root/r).is_file()]
assert not missing, missing
print(f'OK: {len(refs)} local asset references; no missing files.')
