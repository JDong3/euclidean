import os

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

    def write(self, directory):
        not os.path.exists(directory) and os.makedirs(directory)
        for i, frame in enumerate(self._frames):
            frame.write(f'{directory}/{i:05}.svg')
