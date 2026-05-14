'''

# Customized Probe Creation
**Authors:** Luca Pugnetti, Mattia Fornari\
**License:** [The MIT License](https://opensource.org/license/mit)

Copyright (c) 2025 Mattia Fornari, Luca Pugnetti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

'''


import json
from itertools import islice
import pandas as pd
import os

def read_garak_jsonl(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            if entry.get('entry_type') == 'digest':
              digest = entry
              #print('trovata')
              #if digest.get('eval'):
                #print('trovato eval')
                # Estrai i punteggi assoluti e relativi
                #absolute_score = entry.get('absolute_score')
                #relative_score = entry.get('relative_score')
                #print(f"Absolute Score: {absolute_score}, Relative Score: {relative_score}")

              return digest

def read_json(report_json): # output dataframe

  #1. Lettura entry_type = digest
  digest_row = read_garak_jsonl(report_json)

  print(digest_row)

  #2. get eval
  eval = digest_row.get('eval')
  #print(eval.keys())

  #3.
  probe_s = eval.get(list(eval.keys())[0])
  #print('1', list(probe_s.keys())[1])

  #4. per detector
  probe = probe_s.get(list(probe_s.keys())[1])
  #print(probe.keys())

  #5. per probe attacco
  probe_name = list(probe_s.keys())[1] # stringa

  #6.
  detector_name = {}
  for k in probe.keys():
    if k != '_summary':
      #print('detector trovato')
      detector_name[k] = probe.get(k).get('detector_name')

  #print(detector_name)

  #7.
  dim = len(detector_name)

  #8.
  absolute_score = {}
  for k in probe.keys():
    if k != '_summary':
      #print('detector trovato')
      absolute_score[k] = probe.get(k).get('absolute_score')

  #9.
  relative_score = {}
  for k in probe.keys():
    if k != '_summary':
      #print('detector trovato')
      relative_score[k] = probe.get(k).get('relative_score')

  meta = digest_row.get('meta')
  nome_modello = meta.get('target_name')


  #10. Creazione DataFrame
  data = {
    "Modello": nome_modello,
    "Probe": probe_name,
    "Detector": detector_name,
    "AbsoluteScore": absolute_score,
    "RelativeScore": relative_score,
  }

  df = pd.DataFrame(data)

  df = df.reset_index(drop=True)

  return df

