import glob
import json
import sys

def read_config():
    return _build_global_config()


def _build_global_config():
    print("load fuzzer jobs from './config'")
    jobs = []
    for config_file in _load_config_files():
        with open(config_file, "r") as c_file:
            try:
                r = json.load(c_file)
                _validate_config_json(r)

                print(f"load fuzzer job: {r['name']} \n{r['jobs']}")

                jobs.append(r)
            except Exception as e:
                print(f"\033[0;31m>>> error in load fuzzer job from {config_file} \033[0m")
                print(f"\033[0;31m>>> {e} \033[0m")
                sys.exit(1)
    return jobs

def _load_config_files():
    return [f for f in glob.glob("./config/**/*.json", recursive=True)]

def _validate_config_json(config_json):
    if 'name' not in config_json:
        raise Exception("missing property name")
    
    if 'jobs' not in config_json:
        raise Exception("missing property jobs")

    for job in config_json['jobs']:
        if 'exit_codes' not in job:
            raise Exception("missing property exit_codes")

        if 'method' not in job:
            raise Exception("missing property method")

        if 'payload_type' not in job:
            raise Exception("missing property payload_type")

        if 'timeout' not in job:
            raise Exception("missing property timeout")
    
