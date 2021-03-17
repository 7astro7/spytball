
from constants import VERSION

setup(
    name = "spytball",
    packages = ["spytball"],
    entry_points = pass, # do this
    version = VERSION,
    author = "Zachary A. Kraehling",
    author_email = "zaknyy@protonmail.com",
    description = "An encrypted-archiving utility using GPG",
    long_description = "", # do this
    license = "GPLv3",
    url = "https://github.com/7astro7/spytball",
    package_data = None,
    install_requires = ["docopt",""] # add to this
    python_requires = ">=3.8", # test this
    classifiers = [], # do this
    )
