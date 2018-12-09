import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
import typesetting.Template as Template
import typesetting.Animator as tAnimator

t = Template()
t.write()

quote_text = 'Two things that are equal to a thrid are equal to each other'
author = 'Euclid'

q = Quote(quote_text, author=author)
lst = tAnimator.fade(q, 10)
for l in lst:
    root = l.getroot()
    print(root.items())
