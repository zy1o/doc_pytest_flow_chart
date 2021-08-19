"""
Contains console scripts to generate different workflow charts
"""
import argparse

from doc_pytest_flow_chart.flow_generator import (
    generate_conftest,
    execute_pytest,
    get_flow_chart_file,
)


def main():
    parser = argparse.ArgumentParser(description="Pytest hook documentation generator")
    parser.add_argument("--out-file", help="path to the output svg file")
    args = parser.parse_args()

    generate_conftest()
    cproc = execute_pytest()
    print(cproc.stdout.decode("utf-8"))
    print(cproc.stderr.decode("utf-8"))
    get_flow_chart_file(args.out_file)
