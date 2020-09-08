import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="respond",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=["flask"],
    author="Julian Nash",
    author_email="julianjamesnash@gmail.com",
    description="A lightweight and useful wrapper around Flask's make_response and jsonify",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="flask http request parser json rest",
    url="https://github.com/Julian-Nash/respond",
    project_urls={
        "Bug Tracker": "https://github.com/Julian-Nash/respond",
        "Documentation": "https://github.com/Julian-Nash/respond",
        "Source Code": "https://github.com/Julian-Nash/respond",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
