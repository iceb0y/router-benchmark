"""Simple regex router."""
import re
from fixture import register

# stolen from aiohttp
ROUTE_RE = re.compile(r'(\{[_a-zA-Z][^{}]*(?:\{[^{}]*\}[^{}]*)*\})')
DYN = re.compile(r'\{(?P<var>[_a-zA-Z][_a-zA-Z0-9]*)\}')
DYN_WITH_RE = re.compile(r'\{(?P<var>[_a-zA-Z][_a-zA-Z0-9]*):(?P<re>.+)\}')
GOOD = r'[^{}/]+'

class SimpleRegexRouter:
  def __init__(self):
    self.patterns = list()
    self.index = 1
    self.index_to_data = dict()

  def add_route(self, method, url, data):
    prefix = '_' + str(self.index) + '_'
    pattern = '('
    for part in ROUTE_RE.split(url):
      match = DYN.fullmatch(part)
      if match:
        pattern += '(?P<{}>{})'.format(prefix + match.group('var'), GOOD)
        continue
      match = DYN_WITH_RE.fullmatch(part)
      if match:
        pattern += '(?P<{}>{})'.format(prefix + match.group('var'), match.group('re'))
        continue
      pattern += re.escape(part)
    pattern += ')'
    self.patterns.append(pattern)
    self.index_to_data[self.index] = data
    self.index += re.compile(pattern).groups

  def compile(self):
    self.regex = re.compile('|'.join(self.patterns))

  def resolve(self, url):
    m = self.regex.fullmatch(url)
    return self.index_to_data[m.lastindex]

router = SimpleRegexRouter()
register(router.add_route)
router.compile()
for i in range(100000):
  router.resolve('/d/twd2/records-conn/iframe.html')
