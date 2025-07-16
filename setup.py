# setup.py

from setuptools import setup, find_packages

setup(
    name='samurai_bluebird_custos',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'opencv-python',
        'pillow',
        'psutil',
        'numpy',
        'pywin32; platform_system=="Windows"',
        'pynput'
    ],
    entry_points={
        'console_scripts': [
            'samurai-bluebird=samurai_bluebird_custos.core.kernel:main'
        ]
    },
    author='Scurra Labs',
    description='Samurai Bluebird Custos: Cognitive Nervous System Prototype',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ]
)