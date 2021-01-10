import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
	required = f.read().splitlines()

setuptools.setup(
    name="correlaidmatplotlib",
    version="0.1.1",
    author="Marcus Voss",
    author_email="voss.marcus@gmail.com",
    description="A matplotlib style sheet following the CorrelAid style guide",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CorrelAid/correlaid-matplotlib-style",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires= required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
