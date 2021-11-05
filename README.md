Setup: run `make`

Usage: `cacheSim [latD] [latP] [latS] [capD] [capP] [n] [s]`
- latD: relative latency of DRAM
- latP: relative latency of PMEM
- latS: relative latency of SSD
- capD: # items DRAM can hold
- capP: # items PMEM can hold
- n: total # items to be accessed
- s: zipf parameter "s" ([Wikipedia](https://en.wikipedia.org/wiki/Zipf%27s_law))