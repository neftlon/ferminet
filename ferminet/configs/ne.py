from ferminet import base_config
from ferminet.utils import system

# Settings in a config files are loaded by executing the the get_config
# function.
def get_config():
  # Get default options.
  cfg = base_config.default()
  # Set up molecule
  cfg.system.electrons = (5,5)
  cfg.system.molecule = [system.Atom('Ne', (0, 0, 0))]

  # Set training hyperparameters
  cfg.batch_size = 256
  cfg.pretrain.iterations = 100

  # NOTE(johannes): fix the number to a small value for testing
  cfg.optim.iterations = 20000

  return cfg