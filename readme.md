# MaoGaiPlot
## What is this tiny little thing? 
This is a tiny tool created for my 
non-programmer team-mates on the 
MaoGai class to plot some figures for the presentation. 

It is  written in Python3 with Numpy and Matplotlib. 
Anyone can use this tool for any use. 

## How to use it? 
A simple example is given as ```main.py```. 
I believe it is human-readable and can easily be understood without reading 
```Plotr.py```. Note that ```log_sc``` means whether to 
use log-scale for y-axis. 

I have posed some constraints on the ```*.csv``` file. 
The first column of the matrix should be years. The following
columns should be the certain value in that year for each of the regions in the same
order as listed in ```self.set_regions```. 