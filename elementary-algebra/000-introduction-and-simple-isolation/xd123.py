import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
import typesetting.Template as Template
import typesetting.Animator as tAnimator

t = Template()
t.write()

q = Quote('Two things that are equal to a third are equal to each other.', 'Euclid')
# q.write()
