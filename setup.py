"""
Interact with your Hadoop cluster from the convenience of your local command line.
"""
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='athena',
    version='0.1.0',
    url='https://github.com/datadudes/athena',
    license='MIT',
    author='Daan Debie',
    author_email='debie.daan@gmail.com',
    description='Interact with your Hadoop cluster from the convenience of your local command line.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'athena = athena.cli:main',
            ],
        },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
