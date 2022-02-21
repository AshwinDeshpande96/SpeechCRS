import argparse
import warnings

import torch

from crs.config import Config
from crs.quick_start import run_crslab

torch.cuda.current_device()
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # parse args
    parser = argparse.ArgumentParser()
    args, _ = parser.parse_known_args()
    config = Config(args.config)

    run_crslab(config)
