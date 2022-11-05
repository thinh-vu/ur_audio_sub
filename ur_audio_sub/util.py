import os

# Working with file systems
def lmt_detect():
    """Detect the running OS and return file path delimiter"""
    if os.name == 'nt':
        lmt = '\\'
    else:
        lmt = '/'
    return lmt

ROOT_DIR = os.path.abspath(os.curdir)
LMT = lmt_detect()

def file_ls(directory=ROOT_DIR):
    """List all file in the root directory"""
    data = []
    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            data.append(entry)
    return data

def subdir_ls(basepath=ROOT_DIR):
    """List all subdirectories in the root folder"""
    data = []
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            data.append(entry)
    return data

# Data loading
def read_txt(path_to_file):
    """Read a plain text file"""
    with open(path_to_file) as f:
        content = f.read()
    return content

# Cleaning
def memory_cleaner():
    """Free up memory from large model data"""
    import gc
    import torch
    gc.collect()
    torch.cuda.empty_cache()