import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mov2gif",
    version="0.0.4",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="MP4/AVI format movie file to animated GIF file converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/mov2gif",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'mov2gif=mov2gif.mov2gif:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    setup_requires=["setuptools"],
    install_requires=["Pillow","opencv-python"],
)
