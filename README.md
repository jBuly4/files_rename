# Renaming files

Simple script for renaming files in target directory.

### Version 1:

Script renames files that satisfy next pattern:  
^\w{2}\d\s-\s\w+[.]\w{3,4} (hope this is correct regular expression =))

Example:
fl1 - Test File.txt
fl2 - Second File to be tested.txt
fl3 - Third file for tests.docx

Data inside files are not changing.

### Usage:
```shell
python main.py [-h] [--d TGT_DIR]

<----- Rename Files ----->

optional arguments:
  -h, --help   show this help message and exit
  --d TGT_DIR  Absolute path to directory where you want to change files. Don't forget slash at the end of path. Example: /path_to_dir/target_dir/

```