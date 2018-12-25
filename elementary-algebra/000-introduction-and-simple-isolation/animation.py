import sys
sys.path.insert(0, '../../objects')

import typesetting.Quote as Quote
import typesetting.Template as Template
import typesetting.Animator as tAnimator
import typesetting.Title as Title
import animation.Scene as Scene

def genTemplate():
    template = Template()
    template.write()

def introQuote():
    text = 'Things which are equal to the same thing are equal to each other'
    author = 'Euclid'

    style = {
        'transform': 'scale(2) translate(85 70)'
    }
    quote = Quote(text, author=author, style=style)
    res = tAnimator.fade(quote, 10)
    hold = tAnimator.hold(quote, 10)
    fade_out = tAnimator.fade(quote, 10, reverse=True)
    res.addScene(hold)
    res.addScene(fade_out)
    return res

def mainTitle():
    heading = 'Interpreting Algebra'
    subheading = 'An Introduction To Elementary Algebra'
    style = {
        'transform': 'scale(3) translate(30 15)'
    }
    title = Title(heading, subheading=subheading, style=style)

    fade1 = tAnimator.fade(title, 20)
    hold = tAnimator.hold(title, 20)

    res = Scene()
    res.addScene(fade1)
    res.addScene(hold)
    return res

if __name__ == '__main__':
    # genTemplate()

    s1 = introQuote()
    s2 = mainTitle()
    s1.addScene(s2)
    s1.writeVideo('yvideo', 'maintitle')
