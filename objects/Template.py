from constants import TEMPLATE_FILE

class Template:
    def __init__(self, packages=[]):
        self.packages = packages

    def writeTemplate(self, name=TEMPLATE_FILE):
        res = []
        res.append(r'\documentclass{article}')

        body = [
            r'\begin{document}',
            r'\end{document}'
        ]

        for i, package in enumerate(self.packages):
            self.packages[i] = r'\usepackage{' + package + '}'

        [res.append(package) for package in self.packages]

        res.extend(body)

        with open(TEMPLATE_FILE, 'w+') as f:
            [f.write(f'{line}\n') for line in res]


t = Template(['amsfonts','tikz'])
t.writeTemplate()