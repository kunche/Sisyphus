# -*- coding: utf-8 -*-
import shelve
import json
import sys
sys.path.append(r'D:\workspace\analol\Sisyphus\src')
import config
from util.con_dict import work_dict, discard_paths


champion_shelve_path = config.get('champion_shelve_path')
champion_json_path = config.get('champion_json_path')

item_shelve_path = config.get('item_shelve_path')
item_json_path = config.get('item_json_path')

item_shelve_at_map11 = config.get('item_shelve_at_map11')

champion_path = "data/"
needless_path_champion = [
    "image", "skins", "lore",
    "blurb", "allytips", "enemytips",
    "info", "recommended"]

needless_path_item = ['image', 'plaintext']


def generate_champion_shelve(json_path, shelve_path, data_path, discard_path):
    def _discard_paths(d, *paths):
        return [_discard(d, path) for path in paths]

    def _discard(d, key):
        tk = key.split('/', 1)
        if len(tk) == 1:
            return d.pop(tk[0], None)
        else:
            return _discard(d[tk[0]], tk[1])

    with open(json_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    with shelve.open(shelve_path) as f:
        target_data = data[data_path.split('/')[0]]
        [_discard_paths(target_data[k], *discard_path)
         for k in target_data.keys()]
        for key in target_data.keys():
            f[key] = target_data[key]


def generate_item_at_map(item_shelve_path):
    with open(item_json_path, 'r', encoding='utf8') as f:
        data = json.load(f)

    with shelve.open(item_shelve_at_map11) as f:
        target_data = data[champion_path.split('/')[0]]
        discard_paths(target_data, *needless_path_item)
        result_keys = []
        for item_key, value in target_data.items():
            is_at_map_11 = work_dict(value, 'maps', '11')
            if is_at_map_11 is None:
                print(item_key)
                continue
            if is_at_map_11:
                result_keys.append(item_key)
        [discard_paths(target_data[k], 'maps') for k in result_keys]
        for k in result_keys:
            f[k] = target_data[k]


if __name__ == '__main__':
    # generate_champion_shelve(
    #     item_json_path, item_shelve_path, champion_path, needless_path_item)
    generate_item_at_map(item_shelve_path)
