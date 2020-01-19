from setuptools import setup

setup(
    name="worker",
    version="1.0.0",
    author="Eugen Ciur",
    author_email="eugen@papermerge.com",
    url="https://github.com/ciur/papermerge-worker",
    description=("Worker - extract OCR text documents"),
    long_description="long_description",
    long_description_content_type="text/markdown",
    license="Apache 2.0 License",
    keywords="tesseract documentation tutorial",
    packages=['worker'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
