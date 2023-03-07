from setuptools import setup, find_packages

setup(
    name="hoobly_pkg",
    version="0.0.0",
    packages=find_packages(),
    install_requires=["Selenium",
                      "webdriver-manager",
                      ],
    entry_points={
        'console_scripts': ['hoobly_pkg = hoobly_pkg.__main__:main']
    },
)
