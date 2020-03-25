import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="garser", # Replace with your own username
    version="1.1",
    author="GrayHat",
    author_email="garyahthacks10@gmail.com",
    description="A HTML Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grayhat12/garser",
    download_url="https://github.com/GrayHat12/garser/archive/v1.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)