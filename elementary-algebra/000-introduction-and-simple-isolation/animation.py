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
import typesetting.tatr as tatr

def genTemplate():
    template = Template()
    template.write()

def introQuote():
    config = {
        tatr.quote: 'Things which are equal to the same thing are equal to '
                    'each other',
        tatr.author: 'Euclid',
        tatr.fill: '#ffffff',
        tatr.position: (200, 190),
        tatr.size: (1920*0.8, 1080*0.8)
    }
    quote = Quote(config)
    res = tAnimator.fade(quote, 20)
    hold = tAnimator.hold(quote, 20)
    fade_out = tAnimator.fade(quote, 20, reverse=True)
    res.addScene(hold)
    res.addScene(fade_out)

    return res

def mainTitle():

    config = {
        tatr.heading: 'Interpreting Algebra',
        tatr.subheading: 'An Introduction To Elementary Algebra',
        tatr.fill: '#ffffff',
        tatr.size: (1920*0.8, 1080*0.8),
        tatr.position: (190, 100)
    }

    title = Title(config)

    fade1 = tAnimator.fade(title, 20)
    hold = tAnimator.hold(title, 20)

    res = Scene()
    res.addScene(fade1)
    res.addScene(hold)
    return res

def sampleLabel():
    config = {
        tatr.content: 'abc',
        tatr.position: (0, 0),
        tatr.radian: 1.75 * np.pi,
        tatr.distance: 200,
        tatr.size: (sys.maxsize, 400)
    }
    l = Label(config)
    l.frame.write('sampleLabel', png=True)

if __name__ == '__main__':
    sampleLabel()
