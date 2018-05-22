import synapseclient
import synapseutils
import argparse
from shutil import copyfile

if __name__ == '__main__':

    parser = argparse.ArgumentParser("Uploads files to synapse")
    parser.add_argument('--manifest_file', type = str)
    parser.add_argument('--synapse_config_file', type = str)
    args = parser.parse_args()
    copyfile(args.synapse_config_file,  "./.synapseConfig")
    syn = synapseclient.login()
    synapseutils.sync.syncToSynapse(syn, args.manifest_file)
