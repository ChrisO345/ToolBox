from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="toolbox",
    version="0.0.10",
    description="Useful scripts accumulated",
    # package_dir={"": ""},
    packages=find_packages(include=['toolbox', 'toolbox.*']),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://chriso345.github.io",
    author="ChrisO345",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'hello_test = toolbox.test.hello:hello_world'
        ]}
)