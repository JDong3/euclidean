import os
import subprocess as sp
from .styles import RESOLUTION
from .constants import DEFAULT_BACKGROUND
from glob import glob
import multiprocessing as mp

NUM_PROCESSES = 6

class Scene:
    def __init__(self, frames=[]):
        """
        None -> None
        """
        self._frames = frames

    def addFrame(self, frame):
        """
        Frame -> None
        :param frame: a frame in the scene
        """
        self._frames.append(frame)

    def addScene(self, scene):
        self._frames.extend(scene._frames)

    def writeSvgs(self, directory):
        if not os.path.exists(directory):
             os.makedirs(directory)
        for i, frame in enumerate(self._frames):
            frame.write(f'{directory}/{i:07}.svg')

    def svgsToPngs(self, directory):
        argss = []
        pool = mp.Pool(processes=NUM_PROCESSES)
        for i in range(len(self._frames)):
            args = [
                'inkscape',
                '-z', f'{directory}/{i:07}.svg',
                '-e', f'{directory}/{i:07}.png',
                '-b', DEFAULT_BACKGROUND
            ]
            argss.append(args)
        pool.map_async(sp.run, argss)
        pool.close()
        pool.join()

    def writeVideo(self, directory, file, clean=True, view=False):
        self.writeSvgs(directory)
        self.svgsToPngs(directory)

        path = f'{directory}/{file}.mp4'
        new_path = path
        i = 2
        while os.path.isfile(new_path):
            new_path = f'{path[:-4]} ({str(i)}).mp4'
            i += 1

        args = [
            'ffmpeg',
            '-framerate',
            '60',
            '-i',
            f'{directory}/%07d.png',
            '-pix_fmt',
            'yuv420p',
            new_path
        ]
        sp.run(args)

        if clean:
            self.clean(directory)

        if view:
            args = [
                'vlc',
                '-f',
                '-L',
                new_path
            ]
            sp.run(args)

    def clean(self, directory):
        for file in glob(f'{directory}/*.png'):
            os.remove(file)
        for file in glob(f'{directory}/*.svg'):
            os.remove(file)

    @staticmethod
    def fromNodeList(lst):
        for i, element in enumerate(lst):
            frame = Frame(RESOLUTION)
            frame.addFrame(lst[i])
            lst[i] = frame

        scene = Scene()
        for i, frame in enumerate(lst):
            scene.addFrame(frame)
        return scene

# convert *.svg out_%05d.png
# ffmpeg -framerate 60 -i out_%05d.png -pix_fmt yuv420p out.mp4
