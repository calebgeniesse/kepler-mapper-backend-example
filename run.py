# to run the server, please use:
# >>> gunicorn run:server
# or 
# >>> python run.py


### [1] Setup data
import castillo

# Load a single subject
subject = castillo.load_subject(subject=7, batch_size=250)
data, labels = subject.X.to_numpy(), subject.target


### [2] Setup MapperInteractive app
from mappercore import Server
from mappercore.conf import KeplerMapperConfig

# Create kepler mapper config
conf = KeplerMapperConfig(data=data, config="config.json")

# Create server instance
server = Server("Mapper Example", conf=conf)

if __name__ == "__main__":
    server.flask.run()