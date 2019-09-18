import setuptools

setuptools.setup(
    name="gateways19-tutorial-django-app",
    version="0.0.1",
    description="Custom output viewer and django app for Gateways 2019 Tutorial",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16',
        'cclib',
        'numpy',
        'matplotlib'
    ],
    entry_points="""
""",
)
