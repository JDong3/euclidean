import subprocess as sp
import os
from hashlib import sha256
from constants import TEMPLATE_FILE

class Tex:
    """
    class for handling objects that need to be typeset in tex
    """

    def __init__(self, content):
        self.content = content

        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        self.name = hashObj.hexdigest()

    def writeSvg(self, cleanup=True):
        self._contentToTex()

        not os.path.exists('aux') and os.mkdir('aux-dir')
        not os.path.exists('out') and os.mkdir('out-dir')

        args = [
            'latex',
            '-aux-directory=aux-dir',
            '-output-directory=out-dir',
            f'{self.name}.tex']
        sp.run(args)

        args = ['dvisvgm', '-n', f'out-dir/{self.name}.dvi']
        sp.run(args)

    def _contentToTex(self):
        """
        writes content in {self.content} to a tex file with name {self.name}
        """
        with open(TEMPLATE_FILE, 'r') as f:
            res = f.readlines()
        res.insert(-1, f'{self.content}\n')
        with open(f'{self.name}.tex', 'w+') as f:
            [f.write(line) for line in res]