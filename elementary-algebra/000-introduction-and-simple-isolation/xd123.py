import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
q = Quote('abc')
print(q.content)
