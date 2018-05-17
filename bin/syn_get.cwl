import synapseclient
import argparse
from shutil import copyfile

if __name__ == '__main__':

    parser = argparse.ArgumentParser("Gets file from synapse")
    parser.add_argument('--synapse_id', type = str)
    parser.add_argument('--config_file', type = str)
    args = parser.parse_args()
    copyfile(args.config_file,  "./.synapseConfig")
    syn = synapseclient.login()
    syn.get(args.synapse_id, downloadLocation = '.')
