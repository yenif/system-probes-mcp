from setuptools import setup, find_packages

setup(
    name='system-probes-mcp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'fs-mcp=fs_mcp.fs_mcp:main',
            'proc-mcp=proc_mcp.proc_mcp:main',
        ],
    },
    author='Agent Zero',
    author_email='agent-zero@users.noreply.github.com',
    description='A collection of lightweight MCP (Model Context Protocol) tools for filesystem and process inspection.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yenif/system-probes-mcp',
)
