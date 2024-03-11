from setuptools import setup, find_packages

setup(
    name="gmail-label-manager",
    version="0.1.2",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for managing Gmail labels.",
    long_description=open('README.md').read(),
    url="https://github.com/SokinjoNS/gmail-label-manager",
    project_urls":{"Source":"https://github.com/SokinjoNS/gmail-label-manager"},
    packages=find_packages(),
    install_requires=[
        'gmail-api-auth>=0.1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
