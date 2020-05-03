import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonres",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=["flask", "httpz"],
    author="Julian Nash",
    author_email="julianjamesnash@gmail.com",
    description="A lightweight and useful wrapper around Flask's make_response and jsonify",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="flask http request parser json rest",
    url="https://github.com/Julian-Nash/jsonres",
    project_urls={
        "Bug Tracker": "https://github.com/Julian-Nash/jsonres",
        "Documentation": "https://github.com/Julian-Nash/jsonres",
        "Source Code": "https://github.com/Julian-Nash/jsonres",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
