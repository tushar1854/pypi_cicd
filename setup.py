from setuptools import setup, find_packages


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='pypi_cicd',
    version='0.5',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
    ],
)
