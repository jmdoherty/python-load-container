# python-load-container
A simple flask app container for testing out monitoring by generating cpu/memory/errors/latency

Listens on port 3333

Routes: <br>
/ - Generates a hello world reply <br>
/error/\<int:number\> - Same as /, except there is a 1 in _number_ chance it generates a 418 error <br>
/loop/\<int:number\> - Same as /, except it loops 1M x _number_ times before completing request <br>
/memory/\<int:number\> - Same as /, except it tries to create a _number_ MB string in memory before it does so, in increments of 1MB <br>
/slow/\<int:number\> - Same as /, except it randomally sleeps for up to _number_ ms before completing the request <br>
