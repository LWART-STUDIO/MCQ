from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="LIFEWAY",
    author_email="someeamail",
    install_requres=["huggingface_hub","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)