# fb-png2gif

This scripts converts Facebook sticker from png, which includes all frames of the sticker, to gif with custom animation speed

## Prerequisite
- python3
- `$ pip3 -r requirements.txt`


## Usage
- Download sticker image (from any browsers' developer tool)
- Inspect the number of rows(ROW) and columns(COLUMN) of the sticker
- `$ ./run.py -f /path/to/the/sticker -r ROW -c COLUMN -o output.gif -d DURATION`



![image](https://media.tenor.co/images/06447bcaa99945272b9a56149e00122b/tenor.gif)