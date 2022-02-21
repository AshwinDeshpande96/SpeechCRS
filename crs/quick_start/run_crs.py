from crs.data import get_dataset, get_dataloader
from crs.system import get_system


def run_crslab(config):
    CRS_dataset = get_dataset(config, config['tokenize'])
    side_data = CRS_dataset.side_data
    vocab = CRS_dataset.vocab

    train_dataloader = get_dataloader(config, CRS_dataset.train_data, vocab)
    valid_dataloader = get_dataloader(config, CRS_dataset.valid_data, vocab)
    test_dataloader = get_dataloader(config, CRS_dataset.test_data, vocab)

    # system
    CRS = get_system(config, train_dataloader, valid_dataloader, test_dataloader, vocab, side_data)
    CRS.fit()
