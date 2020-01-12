#!/usr/bin/python3

import requests
import time
import click
import sys
from lib import Randomness, ConfigReader, Payload, UriParser

def validate_result(response, job):
    if response.status_code in job['exit_codes']:
        print(f"\033[0;31m>>> job target '{response.url}' failed with {response.status_code} \033[0m")
        print(f"\033[0;31m>>> response '{response.__dict__}' \033[0m")
        sys.exit(1)
    else:
        print(f"repsonse: {response.status_code}")

def proccess_post_job(job, uri):
    try:
        payload_builder = Payload.PayloadBuilder(job)

        payload = payload_builder.get_payload()
        headers = payload_builder.get_headers()

        print(f"sending headers: {headers} to {uri}")
        print(f"sending payload: {payload} to {uri}")

        validate_result(requests.put(UriParser.parse_uri(uri), json=payload, headers=headers), job)
    except Exception as e:
        print(f"\033[0;31m>>> job '{job['name']}' failed with internal error")
        print(e)

def proccess_get_job(job, uri):
    try:
        payload_builder = Payload.PayloadBuilder(job)

        payload = payload_builder.get_payload()
        headers = payload_builder.get_headers()

        print(f"sending headers: {headers} to {uri}")
        print(f"sending payload: {payload} to {uri}")

        validate_result(requests.get(UriParser.parse_uri(uri), json=payload, headers=headers), job)
    except Exception as e:
        print(f"\033[0;31m>>> job '{job['name']}' failed with internal error")
        print(e)

def proccess_put_job(job, uri):
    try:
        payload_builder = Payload.PayloadBuilder(job)

        payload = payload_builder.get_payload()
        headers = payload_builder.get_headers()

        print(f"sending headers: {headers} to {uri}")
        print(f"sending payload: {payload} to {uri}")

        validate_result(requests.put(UriParser.parse_uri(uri), json=payload, headers=headers), job)
    except Exception as e:
        print(f"\033[0;31m>>> job '{job['name']}' failed with internal error \033[0m")
        print(e)

def proccess_delete_job(job, uri):
        payload_builder = Payload.PayloadBuilder(job)

        payload = payload_builder.get_payload()
        headers = payload_builder.get_headers()

        print(f"sending headers: {headers} to {uri}")
        print(f"sending payload: {payload} to {uri}")

        validate_result(requests.delete(UriParser.parse_uri(uri), json=payload, headers=headers), job)

@click.command()
@click.option("--uri", help="base api uri from target", required=True)
@click.option("--port", help="port from target", required=True)
@click.option("--rounds", help="number of rounds to fuzz against the api", required=True)
def _FUZZER(uri, port, rounds):

    base_port = port
    base_uri = uri


    for global_jobs in ConfigReader.read_config():
        print(f"process job {global_jobs['name']}")

        for job in global_jobs['jobs']:
            round_counter = 1
            method = job['method'].lower()

            while round_counter <= int(rounds):
        
                if(method == "post"):
                    proccess_post_job(job, f"{base_uri}:{base_port}/{job['path']}")

                elif(method == "get"):
                    proccess_get_job(job, f"{base_uri}:{base_port}/{job['path']}")

                elif(method == "put"):
                    proccess_put_job(job, f"{base_uri}:{base_port}/{job['path']}")

                elif(method == "delete"):
                    proccess_delete_job(job, f"{base_uri}:{base_port}/{job['path']}")

                else:
                    print(f"\033[0;31m>>> method '{method}' is not supported. do you think it's a bug, please report an issue on github \033[0m")

                print(f"round counter: [{round_counter}/{int(rounds)}]")
                round_counter += 1
 
if __name__ == '__main__':
    _FUZZER()
