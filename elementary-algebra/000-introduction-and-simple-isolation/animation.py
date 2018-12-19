import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
import typesetting.Template as Template
import typesetting.Animator as tAnimator


def genTemplate():
    template = Template()
    template.write()

def genIntroQuote():
    intro_quote_text = 'Things which are equal to the same thing are equal to each other'
    intro_quote_author = 'Euclid'

    intro_quote = Quote(intro_quote_text, author=intro_quote_author,
                        transform='scale(2) translate(80 70)')
    res = tAnimator.fade(intro_quote, 120)
    hold = tAnimator.hold(intro_quote, 120)
    fade_out = tAnimator.fade(intro_quote, 120, reverse=True)
    res.addScene(hold)
    res.addScene(fade_out)
    return res


if __name__ == '__main__':
    intro_quote = genIntroQuote()
    intro_quote.writeVideo('video')
