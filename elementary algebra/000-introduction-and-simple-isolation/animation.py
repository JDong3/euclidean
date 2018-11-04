import sys
sys.path.insert(0, '../../objects')

from Tex import Tex

m = Tex('$f(x) = ax$')
m.writeSvg()
