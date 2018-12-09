from .constants import TEMPLATE_FILE, FONT_SIZE, PACKAGES
import os


class Template:
    def __init__(self, packages=PACKAGES):
        self.packages = packages

    def write(self, name=TEMPLATE_FILE):
        res = []
        res.append(r'\documentclass[{FONT_SIZE}]{article}')

        body = [
            r'\usepackage[margin=1in]{geometry}',
            r'\begin{document}',
            r'\end{document}'
        ]

        for i, package in enumerate(self.packages):
            self.packages[i] = r'\usepackage{' + package + '}'

        [res.append(package) for package in self.packages]

        res.extend(body)

        with open(TEMPLATE_FILE, 'w+') as f:
            [f.write(f'{line}\n') for line in res]
