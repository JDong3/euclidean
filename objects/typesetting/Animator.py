from .Tex import Tex
import animation.Easings as Easings
import copy
import animation.Frame as Frame
import animation.Scene as Scene

class Animator:
    @staticmethod
    def fade(tex, frame_count, easing=Easings.linear):
        res = []
        node = tex.getNode()
        opacities = easing(0, 1, frame_count)
        for opacity in opacities:
            node_copy = copy.deepcopy(node)
            root = node.getroot()
            root.set('opacity', str(opacity))
            res.append(node_copy)
        return res
