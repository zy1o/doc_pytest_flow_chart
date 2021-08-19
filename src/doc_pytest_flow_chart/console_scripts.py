"""
Contains console scripts to generate different workflow charts
"""
import argparse

from doc_pytest_flow_chart.flow_generator import (
    generate_conftest,
    execute_pytest,
    get_flow_chart_file,
    load_pytest_hook_debug,
    load_hook_order_file,
)


def main():
    """Main entry point. Can be used to generate svg diagrams of pytest hook flow."""
    parser = argparse.ArgumentParser(description="Pytest hook documentation generator")
    parser.add_argument("--out-file", help="path to the output svg file")
    args = parser.parse_args()

    generate_conftest()
    cproc = execute_pytest()
    print(cproc.stdout.decode("utf-8"))
    print(cproc.stderr.decode("utf-8"))
    get_flow_chart_file(args.out_file, load_function=load_hook_order_file)


# testing stuff:
# if __name__ == "__main__":
#     startup_hooks = set(
#         [
#             "pytest_addhooks",
#             "pytest_plugin_registered",
#             "pytest_addoption",
#             "pytest_configure",
#             "pytest_cmdline_parse",
#             "pytest_cmdline_preparse",
#             "pytest_cmdline_main",
#             "pytest_load_initial_conftests",
#             "pytest_sessionstart",
#             "pytest_fixture_setup",
#         ]
#     )
#     collection_hooks = set(
#         [
#             "pytest_fixture_setup",
#             "pytest_fixture_post_finalizer",
#             "pytest_collection",
#             "pytest_collection_modifyitems",
#             "pytest_collection_finish",
#             "pytest_ignore_collect",
#             "pytest_collect_file",
#             "pytest_collectstart",
#             "pytest_itemcollected",
#             "pytest_collectreport",
#             "pytest_deselected",
#             "pytest_make_collect_report",
#             "pytest_pycollect_makemodule",
#             "pytest_pycollect_makeitem",
#             "pytest_pyfunc_call",
#             "pytest_generate_tests",
#             "pytest_make_parametrize_id",
#             "pytest_assertrepr_compare",
#             "pytest_assertion_pass",
#             "pytest_report_teststatus",
#             "pytest_report_header",
#             "pytest_terminal_summary",
#             "pytest_report_collectionfinish",
#         ]
#     )
#     execution_hooks = set()
#     report_hooks = set()
#     generate_conftest()
#     cproc = execute_pytest()
#     print(cproc.stdout.decode("utf-8"))
#     print(cproc.stderr.decode("utf-8"))
#     get_flow_chart_file(
#         "graph1", load_function=load_pytest_hook_debug, hook_filter=startup_hooks
#     )
#     get_flow_chart_file(
#         "graph2", load_function=load_pytest_hook_debug, hook_filter=collection_hooks
#     )

