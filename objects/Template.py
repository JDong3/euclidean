from constants import TEMPLATE

class Template:
    def __init__(self, mods=[], color=None):
        pass

    def writeTemplte(self, name=TEMPLATE):
        lines = [
        '\documentclass{article}',
        '\begin{document}',
        '\end{document}'
        ]
        with open('name', 'w+') as f:
            [f.write[f'{line}\n'] for line in lines]
