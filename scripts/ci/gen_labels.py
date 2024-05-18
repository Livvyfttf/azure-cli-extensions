#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
import os
import re
import json

base_meta_path = os.environ.get('base_meta_path', None)
diff_meta_path = os.environ.get('diff_meta_path', None)
result_path = os.environ.get('diff_meta_path', None)
output_file = os.environ.get('output_file', None)
add_labels_file = os.environ.get('add_labels_file', None)
remove_labels_file = os.environ.get('remove_labels_file', None)
changed_module_list = os.environ.get('changed_module_list', "").split()
diff_code_file = os.environ.get('diff_code_file', "")
print("diff_code_file:", diff_code_file)
pr_label_list = os.environ.get('pr_label_list', "").split()
pr_label_list = [name.lower().strip().strip('"').strip("'") for name in pr_label_list]

block_pr = 0

def save_gh_output():
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'BlockPR={block_pr}', file=fh)

add_label_dict = {
    "labels": ["lab1", "lab30"]
}

def save_add_label_file():
    with open(result_path + "/" + add_labels_file, "w") as f:
        json.dump(add_label_dict, f)

def save_remove_label_file():
    with open(result_path + "/" + remove_labels_file, "w") as f:
        f.write("lab2" + "\n")
        f.write("lab3" + "\n")

def main():
    print("Start calculate release version ...\n")
    print("base_meta_path: ", base_meta_path)
    print("diff_meta_path: ", diff_meta_path)
    print("output_file: ", output_file)
    print("remove_labels_file: ", remove_labels_file)
    print("add_labels_file: ", add_labels_file)
    print("changed_module_list: ", changed_module_list)
    print("pr_label_list: ", pr_label_list)
    print("block_pr:", block_pr)
    save_gh_output()
    save_add_label_file()
    save_remove_label_file()


if __name__ == '__main__':
    main()
