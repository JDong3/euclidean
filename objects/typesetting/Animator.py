from .Tex import Tex
import animation.Easings as Easings
import copy
import animation.Frame as Frame
import animation.Scene as Scene

class Animator:
    @staticmethod
    def fade(tex, frame_count, easing=Easings.linear, reverse=False):
        res = []
        node = tex.node

        if reverse:
            opacities = easing(1, 0, frame_count)
        else:
            opacities = easing(0, 1, frame_count)

        for opacity in opacities:
            style={
                'opacity': opacity
            }
            t = tex.partialCopy(style=style)
            res.append(t.frame)

        res = Scene(res)
        return res

    @staticmethod
    def hold(tex, frame_count):
        res = []

        for i in range(frame_count):
            t = copy.copy(tex)
            res.append(t.frame)

        res = Scene(res)
        return res
