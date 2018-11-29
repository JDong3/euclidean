import subprocess as sp
import os
from hashlib import sha256
from .constants import TEMPLATE_FILE, TEX_OUTPUT, TEX_AUXILIARY

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

        if not os.path.exists(TEX_AUXILIARY):
            os.mkdir(TEX_AUXILIARY)
        if not os.path.exists(TEX_OUTPUT):
            os.mkdir(TEX_OUTPUT)

        args = [
            'latex',
            f'-aux-directory={TEX_AUXILIARY}',
            f'-output-directory={TEX_OUTPUT}',
            f'{self.name}.tex']
        sp.run(args)

        args = ['dvisvgm', '-n', f'{TEX_OUTPUT}/{self.name}.dvi']
        sp.run(args)

        self.clean()

    def _contentToTex(self):
        """
        writes content in {self.content} to a tex file with name {self.name}
        """
        with open(TEMPLATE_FILE, 'r') as f:
            res = f.readlines()
        res.insert(-1, f'{self.content}\n')
        with open(f'{self.name}.tex', 'w+') as f:
            [f.write(line) for line in res]

    def clean(self, svg=False):
        """
        cleans up the files that are created after calling writeSvg
        """
        args = [
            'rm',
            '-r',
            TEX_AUXILIARY,
            TEX_OUTPUT,
            f'{self.name}.tex',
        ]

        if svg:
            args.append(f'{self.name}.svg')

        sp.run(args)
