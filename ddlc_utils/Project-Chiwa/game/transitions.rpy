
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_white_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#FFF"), Pause(0.2),
    Solid("#FFF"), Dissolve(1.0),
    True])

define trans1 = ImageDissolve("trans/1.jpg", 1.0, 8)
define trans2 = ImageDissolve("trans/2.png", .4, 8)

define trans1_scene = MultipleTransition([
    False, ImageDissolve("trans/1.jpg", 1.0, 8),
    Solid("#000"), Pause(0.6),
    Solid("#000"), ImageDissolve("trans/1.jpg", 1.0, 8),
    True])