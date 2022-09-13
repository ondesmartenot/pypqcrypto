import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pqcrypto",
    version="20180314",
    author="PQCRYPTO Project",
    description="Python wrapper library for libpqcrypto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.libpqcrypto.org",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
        "Topic :: Security"
    ],
    requires=["libpqcrypto"],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)

