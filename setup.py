from setuptools import setup, find_packages

setup(
    name='ucalcx',
    version='0.0.1-alpha',
    packages=find_packages(include=['ucalcx', 'ucalcx.*']),
    install_requires=[
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'ucx = ucalcx.main:main',
        ],
    },
    test_suite='test',
    tests_require=[
        'unittest',
    ],
)