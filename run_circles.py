# to run the server, please use:
# >>> gunicorn run:server
# or 
# >>> python run.py


### [1] Setup data
from sklearn import datasets

# Load example data
data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.3)


### [2] Setup MapperInteractive app
from mappercore import Server
from mappercore.conf import KeplerMapperConfig

# Create kepler mapper config
conf = KeplerMapperConfig(data=data, config="config.json")

# Create server instance
server = Server("Mapper Example", conf=conf)

if __name__ == "__main__":
    server.flask.run()