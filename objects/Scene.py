class Scene:
    def __init__(self):
        """
        None -> None
        """
        this._frames = []

    def add(self, frame):
        """
        Frame -> None
        :param frame: a frame in the scene
        """
        this._frames.append(frame)
