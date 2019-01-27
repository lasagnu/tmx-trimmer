## xtm_tmx_trimmer

Allows you to trim unnecessary entries in .tmx file generated in XTM (xtm.cloud) based on project name.
~marej <marej.dev@gmail.com>

#Installation

```
git clone https://github.com/lasagnu/tmx-trimmer.git
```

#Usage:

```
tmx_trimmer.py [-h] -s SOURCE -p PROJECTS [-o OUTPUT]
```

#Example

```
python3 tmx_trimmer.py -s example/source.tmx -p example/projects.xml -o output_file.xml
```
