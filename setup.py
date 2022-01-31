from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENCE') as f:
    licence = f.read()

setup(
    name='hwinfo_grapher',
    version='0.1.0',
    description='Plots data from a HWInfo CSV log file.',
    long_description=readme,
    author='Tom Clarke',
    license=licence,
    packages=find_packages(exclude=('tests')),
    install_requires=['matplotlib']
)
