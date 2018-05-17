import synapseclient
import argparse
from shutil import copyfile

if __name__ == '__main__':

    parser = argparse.ArgumentParser("Uploads files to synapse")
    parser.add_argument('--manifest_file', type = str)
    parser.add_argument('--config_file', type = str)
    args = parser.parse_args()
    copyfile(args.config_file,  "./.synapseConfig")
    syn = synapseclient.login()
    syn.syncToSynapse(args.manifest_file)
