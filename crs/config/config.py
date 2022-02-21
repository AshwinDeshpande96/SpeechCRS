import yaml


class Config:
    def __init__(self, config_file):
        self.opt = self.load_yaml_configs(config_file)

    @staticmethod
    def load_yaml_configs(filename):
        """This function reads ``yaml`` file to build config dictionary

        Args:
            filename (str): path to ``yaml`` config

        Returns:
            dict: config

        """
        config_dict = dict()
        with open(filename, 'r', encoding='utf-8') as f:
            config_dict.update(yaml.safe_load(f.read()))
        return config_dict
