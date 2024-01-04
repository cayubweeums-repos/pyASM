# pyASM
An ASM tool that has both a CLI and web interface. Can launch attacks and score the network &amp; individual devices ability to detect, block, and alert on those attacks

## Dev Setup
```
cd pyasm/
poetry install
poetry shell # for a shell environment to debug
```

Commitizen was used for commits to be standardized. Install with:
```
npm install commitizen -g
```
Make all commits with:
```
git cz
```


## Usage

#### Web UI
```
flet run flet/main.py -d -w -vv
```
