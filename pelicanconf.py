AUTHOR = 'Eric Turgeon'
SITENAME = 'EricBSD'
SITETITLE = 'EricBSD'
SITEURL = ""
PATH = "content"
TIMEZONE = 'America/Moncton'
DEFAULT_LANG = 'en'
THEME = 'theme'

# Copyright
COPYRIGHT_YEAR = 2026
COPYRIGHT_NAME = 'Eric Turgeon'

# Dark mode support
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Static files
STATIC_PATHS = ['images']
SITELOGO = '/images/photo_2020-03-25_14-00-43.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pages
DISPLAY_PAGES_ON_MENU = True

# Projects
LINKS = (
    ("TrueNAS", "https://www.truenas.com/"),
    ("GhostBSD", "https://www.ghostbsd.org/"),
    ("FreeBSD", "https://www.freebsd.org/")
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/ericbsd"),
    ("x-twitter", "https://x.com/ericbsd"),
    ("linkedin", "https://www.linkedin.com/in/eric-turgeon/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
