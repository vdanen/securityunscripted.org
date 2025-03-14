AUTHOR = 'Vincent Danen'
SITENAME = 'Security Unscripted'
SITEURL = "https://securityunscripted.org"

PATH = "content"

TIMEZONE = 'America/Edmonton'
DATE_FORMATS = {"en": "%b %d, %Y"}
DEFAULT_LANG = 'en'

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "liquid_tags.youtube",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

STATIC_PATHS = ['covers']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'recent.atom'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Blogroll
#LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#)
#
## Social widget
SOCIAL = (
        ("twitter", "https://x.com/vdanen"),
        ("linkedIn", "https://linkedin.com/in/vdanen"),
        ("youtube", "https://www.youtube.com/playlist?list=PLbkgg0hYLSphsgXABfS_XkAi2fqjGPoQT"),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Appearance
THEME = 'su-dark'
TYPOGRIFY = True
DEFAULT_PAGINATION = 10
#SITE_IMAGE_URL = SITEURL + 'theme/images/logo.png'

SUMMARY_MAX_PARAGRAPHS = 1
SUMMARY_MAX_LENGTH = 100

