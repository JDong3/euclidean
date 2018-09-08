import styles

class Line:
    __init__(self, a, b, style_update=dict()):
        """
        point, point, dict -> None
        :param a: a point on the line
        :param b: a point on the line
        :param [style_update]: the updated style of the line
        """
        let default = styles.line

        self.a = a
        self.b = b
