import setuptools

setuptools.setup(
    name="jsonres",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=["flask", "httpz"]
)
