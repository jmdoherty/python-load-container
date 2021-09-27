# python-load-container
A simple flask app container for testing out monitoring by generating cpu/memory/errors/latency

Listens on port 3333

Routes:
/ - Geneates a hello world reply
/error/<int:number> - Same as /, except 1 in _number_ it generates a 418 error
/loop/<int:number> - Same as /, except it loops 1M x _number_ times before completing request
/memory/<int:number> - Same as /, except it tries to create a _number_ MB string in memory before it does so, in increments of 1MB
/slow/<int:number> - Same as /, except it randomally sleeps for up to _number_ ms before completing the request
