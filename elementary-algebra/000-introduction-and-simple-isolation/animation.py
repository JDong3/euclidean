import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
import typesetting.Template as Template
import typesetting.Animator as tAnimator

template = Template()
template.write()

intro_quote_text = 'Things which are equal to the same thing are equal to each other'
intro_quote_author = 'Euclid'

intro_quote = Quote(intro_quote_text, author=intro_quote_author)
quote_anim = tAnimator.fade(intro_quote, 120)
fade_out = tAnimator.fade(intro_quote, 120, reverse=True)
quote_anim.addScene(fade_out)
quote_anim.writeVideo('video')
