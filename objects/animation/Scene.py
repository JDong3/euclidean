import os
import subprocess as sp
from .styles import RESOLUTION
from glob import glob

class Scene:
    def __init__(self):
        """
        None -> None
        """
        self._frames = []

    def add(self, frame):
        """
        Frame -> None
        :param frame: a frame in the scene
        """
        self._frames.append(frame)

    def writeSvg(self, directory):
        if not os.path.exists(directory):
             os.makedirs(directory)
        for i, frame in enumerate(self._frames):
            frame.write(f'{directory}/{i:07}.svg')

    def writeVideo(self, directory, clean=True):
        self.writeSvg(directory)

        args = [
            'magick',
            f'{directory}/*.svg',
            f'{directory}/out_%07d.png'
        ]
        sp.run(args)

        args = [
            'ffmpeg',
            '-framerate',
            '60',
            '-i',
            f'{directory}/out_%07d.png',
            '-pix_fmt',
            'yuv420p',
            f'{directory}/out.mp4'
        ]
        sp.run(args)

        if clean:
            self.clean(directory)

    def clean(self, directory):
        for file in glob(f'{directory}/*.png'):
            os.remove(file)
        for file in glob(f'{directory}/*.svg'):
            os.remove(file)

    @staticmethod
    def fromNodeList(lst):
        for i, element in enumerate(lst):
            frame = Frame(RESOLUTION)
            frame.add(lst[i])
            lst[i] = frame

        scene = Scene()
        for i, frame in enumerate(lst):
            scene.add(frame)
        return scene

# convert *.svg out_%05d.png
# ffmpeg -framerate 60 -i out_%05d.png -pix_fmt yuv420p out.mp4
