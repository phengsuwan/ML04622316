import wget
import os
import json

from pyrengine.objectlist import OBJECTLIST, ARRAY
from pyrengine.op import OP
from pyrengine.lookup import LOOKUP
from pyrengine.ruleutils import convert

def download_tables(ld, bt, lts): 
  if not os.path.exists(ld):
    os.mkdir(ld)
    wget.download(bt[1], bt[0])
    for lt in lts:
      wget.download(lt[1], lt[0])

def read_tx(path: str) -> dict: 
    with open(path) as f: 
        tx = json.load(f)
    return tx

def load_bigtable_fields(bt):
    bt_json = read_tx(bt[0])
    bt = convert(bt_json)
    btf = [f"{k} = '{bt[k]}'" if type(bt[k]) is str else f"{k} = {bt[k]}" for k in bt.keys()]
    return btf

def load_bigtable_fields_v2(bt): 
  bt_json = read_tx(bt)
  bt = convert(bt_json)
  btf = [f"{k} = '{bt[k]}'" if type(bt[k]) is str else f"{k} = {bt[k]}" for k in bt.keys()]
  return btf