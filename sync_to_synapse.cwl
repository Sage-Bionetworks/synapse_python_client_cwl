#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: synapse_python
    
baseCommand: [ python, /usr/local/bin/sync_to_synapse.py ]

inputs:
 
  manifest_file:
    type: File
    inputBinding:
      prefix: "--manifest_file"
      
  config_file:
    type: File
    inputBinding:
      prefix: "--config_file"