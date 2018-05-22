import argparse
import yaml
import pandas as pd
import synapseclient
import synapseutils
from shutil import copyfile

if __name__ == '__main__':
 
    parser = argparse.ArgumentParser("Creates manifest file and syncs to synapse")
    
    parser.add_argument('--synapse_config_file', type = str)
    parser.add_argument('--paths', type = str, nargs = '+')
    parser.add_argument('--parent', type = str)
    parser.add_argument('--used', 
                        type = str,
                        nargs = '+',
                        default = None, 
                        required = False)
    parser.add_argument('--executed', 
                        type = str,
                        nargs = '+',
                        default = None, 
                        required = False)
    parser.add_argument('--activity_name', 
                        type = str,
                        default = None, 
                        required = False)
    parser.add_argument('--activity_description', 
                        type = str,
                        default = None, 
                        required = False)
    parser.add_argument('--yaml_config_file', 
                        type = str, 
                        default = None, 
                        required = False)
    parser.add_argument('--manifest_string', 
                        type = str, 
                        default = 'manifest.tsv', 
                        required = False)
    args = parser.parse_args()
    
    manifest_dict = {"path": args.paths, 
                     "parent": args.parent}
    
    if args.used is not None:
        manifest_dict["used"] = ";".join(args.used)
    
    if args.executed is not None:
        manifest_dict["executed"] = ";".join(args.executed)
    
    if args.activity_name is not None:
        manifest_dict["activityName"] = args.activity_name
    
    if args.activity_description is not None:
        manifest_dict["activityDescription"] = args.activity_description
    
    if args.yaml_config_file is not None:
        with open(args.yaml_config_file, 'r') as stream:
            dict = (yaml.load(stream))
            if "annotations" in dict:
                annotations = dict["annotations"]
                for key in annotations.keys():
                    manifest_dict[key] = annotations[key]
    
    df = pd.DataFrame(data = manifest_dict)
    df.to_csv(args.manifest_string, sep = "\t", index = False)
    
    copyfile(args.synapse_config_file,  "./.synapseConfig")
    syn = synapseclient.login()
    synapseutils.sync.syncToSynapse(syn, args.manifest_string)
