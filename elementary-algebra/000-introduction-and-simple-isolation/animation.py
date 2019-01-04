import sys
sys.path.insert(0, '../../objects')

import animation.Frame as Frame
import animation.Scene as Scene
import numpy as np
import typesetting.Label as Label
import typesetting.Quote as Quote
import typesetting.Animator as tAnimator
import typesetting.Template as Template
import typesetting.Tex as Tex
import typesetting.Title as Title

def genTemplate():
    template = Template()
    template.write()

def introQuote():
    config = {
        'quote': 'Things which are equal to the same thing are equal to each other',
        'author': 'Euclid',
        'style' : {
            'transform': '',
            'fill': '#ffffff'
        },
        'size': (1920, 1080)
    }
    quote = Quote(config)
    res = tAnimator.fade(quote, 100)
    hold = tAnimator.hold(quote, 100)
    fade_out = tAnimator.fade(quote, 100, reverse=True)
    res.addScene(hold)
    res.addScene(fade_out)

    return res

def mainTitle():

    config = {
        'heading': 'Interpreting Algebra',
        'subheading': 'An Introduction To Elementary Algebra',
        'style': {
            'transform': 'translate(90 45)',
            'fill': '#ffffff'
        },
        'size': (1920, 1080)
    }

    title = Title(config)

    fade1 = tAnimator.fade(title, 20)
    hold = tAnimator.hold(title, 20)

    res = Scene()
    res.addScene(fade1)
    res.addScene(hold)
    return res

def sampleLabel():
    l = Label('abc', (0, 0))
    f = Frame(l.node)
    f.write('sampleLabel.svg')

if __name__ == '__main__':
    # genTemplate()

    # s1 = introQuote()
    # s2 = mainTitle()
    # s1.addScene(s2)
    # s1.writeVideo('video', 'bug2')

    t = Tex({'content': 'abc'})
