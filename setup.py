import setuptools


repo_name = "End-to-end-machine-learning-project-with-mlflow"
author_user_name = "AmitKumarSinghAI",
author_email = "amitkumarsinghkurmi123@gmail.com",
src_name = "mlProject"
__version__ = "0.0.0"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=src_name,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    src_name = src_name,
    description="A small python package for ml app",
    long_description="long_description",
    long_description_content="text/markdown",
    url=f"https://github.com/{author_user_name}/{repo_name}",
    project_urls={
        "Bug tracker" :f"https://github.com/{author_user_name}/{repo_name}/issues"
    },
    package_dir={
        "":"src"
    },
    packages=setuptools.find_packages(where="src")
)