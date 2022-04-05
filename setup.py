from setuptools import setup, find_packages

setup(
    name='media_cli',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    media=media_cli:media_cli
    '''
)