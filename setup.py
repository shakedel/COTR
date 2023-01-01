from setuptools import setup, find_packages

setup(
    name='COTR',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'torch',
        'numpy',
        'opencv-python',
        'imageio',
        'Pillow',
        'tables',
        'torchvision',
        'tensorboardX',
        'matplotlib'
    ],
)
