
from constants import VERSION

setup(
    name = "spytball",
    packages = ["spytball"],
    entry_points = {
        "console_scripts": [
            "spytball=spytball.cli:main",
            ]
        },
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
    classifiers = [
        "Development Status :: -- :: Dev1",
        "Environment :: Console",
        "Intended Audience :: -"
        "Topic :: - :: -",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: ----", 
        ], # add to this
    )
