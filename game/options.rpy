
# This file is created by your AI Lead Developer ✨
define config.name = "Eleanor: The Mansion Mysteries"
define config.version = "0.1"

# Window size and settings
define config.screen_width = 1920
define config.screen_height = 1080

# Basic game options

# ---------------------------------------------------------------------------
# BUILD / DISTRIBUTION CONFIGURATION
# ---------------------------------------------------------------------------
init python:

    build.name = "EleanorMansionMysteries"

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/images/**.png', 'archive')
    build.classify('game/images/**.jpg', 'archive')
    build.classify('game/images/**.webp', 'archive')
    build.classify('game/audio/**.ogg', 'archive')
    build.classify('game/audio/**.mp3', 'archive')
    build.classify('game/audio/**.wav', 'archive')
    build.classify('game/gui/**.png', 'archive')
    build.classify('game/gui/**.jpg', 'archive')
    build.classify('game/gui/**.webp', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('README*')
