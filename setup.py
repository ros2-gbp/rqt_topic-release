from setuptools import setup

package_name = 'rqt_topic'
setup(
    name=package_name,
    version='0.4.9',
    package_dir={'': 'src'},
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource', ['resource/TopicWidget.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('lib/' + package_name, ['scripts/rqt_topic'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dorian Scholz',
    maintainer='Dirk Thomas, Dorian Scholz',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'rqt_topic provides a GUI plugin for displaying debug information about ROS topics '
        'including publishers, subscribers, publishing rate, and ROS Messages.'
    ),
    license='BSD',
    scripts=['scripts/rqt_topic'],
)