# to run the server, please use:
# >>> gunicorn run:server
# or 
# >>> python run.py
import numpy as np
import pandas as pd
import scipy.stats as stats

### [1] Setup data
import castillo

# Load a single subject
subject = castillo.load_subject(subject=14, batch_size=None)
data, labels = subject.X.to_numpy(), subject.target

# extract sample of featurs
#zscores = stats.zscore(data, axis=0)
#features = np.where(np.mean(np.abs(zscores) > 6, axis=0))
print(data.shape)


### [2] Setup MapperInteractive app
from mappercore import Server
from mappercore.conf import KeplerMapperConfig

# Create kepler mapper config
conf = KeplerMapperConfig(data=data, config="config.json")

# Create server instance
server = Server("Mapper Example", conf=conf)

if __name__ == "__main__":
    server.flask.run()