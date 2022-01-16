from setuptools import setup, find_packages

version = '5.0.0'

setup(
    name="alerta-influxdb2",
    version=version,
    description='Alerta webhook for InfluxDB2',
    url='https://github.com/alerta/alerta-contrib',
    license='MIT',
    author='Renan de Souza Polisciuc',
    author_email='renan.de.souza@outlook.com',
    packages=find_packages(),
    py_modules=['alerta_influxdb2'],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'influxdb2 = alerta_influxdb2:InfluxDB2Webhook'
        ]
    }
)
