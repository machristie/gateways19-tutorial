import setuptools

setuptools.setup(
    name="gateways19-tutorial-django-app",
    version="0.0.1",
    description="Custom output viewer and django app for Gateways 2019 Tutorial",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16',
        'numpy',
        'matplotlib'
    ],
    entry_points="""
[airavata.output_view_providers]
gaussian-log-image = gateways19_tutorial.output_views:GaussianLogViewProvider
[airavata.djangoapp]
gateways19_tutorial = gateways19_tutorial.apps:Gateways19TutorialAppConfig
""",
)
