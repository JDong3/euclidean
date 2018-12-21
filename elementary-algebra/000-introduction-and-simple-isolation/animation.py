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

    quote = Quote(text, author=author,
                        transform='scale(2) translate(85 70)')
    res = tAnimator.fade(quote, 120)
    hold = tAnimator.hold(quote, 120)
    fade_out = tAnimator.fade(quote, 120, reverse=True)
    res.addScene(hold)
    res.addScene(fade_out)
    return res

def mainTitle():
    heading = 'Interpreting Algebra'
    subheading = 'An Introduction To Elementary Algebra'
    title = Title(heading, subheading=subheading,
                  transform='scale(3) translate(30 15)')

    fade1 = tAnimator.fade(title, 20)
    hold = tAnimator.hold(title, 200)

    res = Scene()
    res.addScene(fade1)
    res.addScene(hold)
    return res

if __name__ == '__main__':
    # genTemplate()

    s1 = introQuote()
    s2 = mainTitle()
    s1.addScene(s2)
    s1.writeVideo('video', 'v')
