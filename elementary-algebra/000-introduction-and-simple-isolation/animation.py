import sys
sys.path.insert(0, '../../objects')

import animation.Frame as Frame
import animation.Scene as Scene
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
    text = 'Things which are equal to the same thing are equal to each other'
    author = 'Euclid'

    style = {
        'transform': 'scale(2)'
    }
    position = (170, 140)
    quote = Quote(text, author=author, style=style, position=position)
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
        'transform': 'scale(3)'
    }
    position = (90, 45)
    title = Title(heading, subheading=subheading, style=style,
                  position=position)

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
    genTemplate()

    s1 = introQuote()
    s2 = mainTitle()
    s1.addScene(s2)
    s1.writeVideo('video', 'maintitle5', clean=False)

    # sampleLabel()
    # t = Tex('abc')
    # print(Tex.getGroups(t.node))
