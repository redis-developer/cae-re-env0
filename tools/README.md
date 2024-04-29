 
## How to generate the env0 client

1. Download fresh spec if needed from https://docs.env0.com/openapi and save it to `env0_spec.json`. 
   Currently, we use v8 spec. 
2. Switch current dir to `tools` and run `python3 fix_spec.py`
3. Run `./env0_client_generator.sh`
