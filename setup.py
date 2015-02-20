from setuptools import setup, find_packages

version = '0.0.0'

install_requires = [
    'flask',
    'sqlalchemy'
]

entry_points = """\
[console_scripts]
beefyconn = beefyconnection.beefyflask:app
"""

setup(
    name="beefyconnection",
    version=version,
    author="Scott Williams",
    author_email="vwbusguy@fedoraproject.org",
    maintainer="Scott Williams",
    maintainer_email="wvbusguy@fedoraproject.org",
    description="Kiosk System for Fedora",
    license="TBD",
    keywords="",
    url="https://github.com/vwbusguy/beefy-connection",
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    entry_points=entry_points,
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
