from setuptools import setup

setup(
    name="allocation_language",
    version="0.0.1",
    description="Language intented to construct the financial behaviour of (re)insurance contracts.",
    py_modules=[
        "allocation_language",
        "alloc_lang_data_containers/csv_to_event_list",
        "alloc_lang_data_containers/converters",
        ],
    install_requires=[
        "rply"
    ],
    package_dir={"": "src"},
    author="Mammen Joseph",
    author_email="tmammenjoseph@gmail.com",
    maintainer="Mammen Joseph",
    maintainer_email="tmammenjoseph@gmail.com",
    url=""
)
