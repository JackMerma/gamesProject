WHITE = (250, 250, 250)
BLACK = (33, 33, 33)
LIGHTGRAY = (238, 238, 238)
GRAY = (189, 189, 189)
DARKGRAY = (97, 97, 97)
BACKGROUND_COLOR = (118, 215, 196)

color = {
  '_': LIGHTGRAY,
  '=': GRAY,
  '.': WHITE,
  '@': BLACK,
  '#': DARKGRAY,
  ' ': BACKGROUND_COLOR,
}
inverter = {
  '_': '=',
  '=': '_',
  '.': '@',
  '@': '.',
}
