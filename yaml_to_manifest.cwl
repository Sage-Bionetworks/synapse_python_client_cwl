#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

baseCommand: [ python, /usr/local/bin/yaml_to_manifest.py ]

hints:
  DockerRequirement:
    dockerPull: quay.io/andrewelamb/synapse_python_client

inputs:

  output_file_string:
    type: string
    default: 'manifest.tsv'
    inputBinding:
      prefix: "--output_file_string"
      
  yaml_config_file:
    type: File
    inputBinding:
      prefix: "--config_file"

outputs:

  output:
    type: File
    outputBinding:
      glob: inputs.output_file_string