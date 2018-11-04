import sys
sys.path.insert(0, '../../objects')

from Tex import Tex
from Math import Math
from Template import Template

x = Template(['mathtools'])
x.writeTemplate()

t = Tex(Math(r'\sum_{i = 0}^{n} i + i2^i').out)
t.writeSvg()



