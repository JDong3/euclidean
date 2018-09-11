STD_WIDTH = 1920
STD_HEIGHT = 1080
STD_COLOR = 'black'

STD_STROKE_WIDTH = round(STD_WIDTH/500)
STD_POINT_RADIUS = STD_STROKE_WIDTH

point = {
    'r': str(STD_POINT_RADIUS)
}

line = {
    'stroke': STD_COLOR,
    'stroke-width': str(STD_STROKE_WIDTH)
}

resolution = {
    'height': str(STD_WIDTH),
    'width': str(STD_HEIGHT)
}

circle = {
    'stroke': STD_COLOR,
    'stroke-width': str(STD_STROKE_WIDTH)
}
