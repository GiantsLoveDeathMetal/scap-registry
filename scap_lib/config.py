import os

import yaml


class Config:

    def __init__(self, config):
        self._config = config

    def __repr__(self):
        return repr(self._config)

    def __getattr__(self, key):
        if key in self._config:
            return self._config[key]


_config = None
def load():
    global _config
    if _config is not None:
        return _config
    data = None
    with open(os.path.join(os.path.dirname(__file__), '..', 'config.yml')) as f:
        data = yaml.load(f)
    # Common is the config common to all flavors
    config = data.get('common', {})
    flavor = os.environ.get('SETTING_FLAVOR', 'dev')
    config.update(data.get(flavor, {}))
    _config = Config(config)
    return _config
