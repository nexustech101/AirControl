"""Setup configuration for AirControl package."""
from setuptools import setup, find_packages

setup(
    name="air_control",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5.0",
        "mediapipe>=0.8.0",
        "pyautogui>=0.9.0",
        "numpy>=1.19.0",
    ],
    author="nexustech101",
    description="Hand gesture-based mouse control using computer vision",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="computer-vision, hand-tracking, gesture-control, mouse-control",
    url="https://github.com/nexustech101/AirControl",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
