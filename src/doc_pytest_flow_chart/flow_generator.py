import pathlib
import subprocess
import graphviz
from doc_pytest_flow_chart import hookspec_generator


def generate_conftest() -> None:
    """Creates a new conftest file in the dummy project
    directory"""
    current_dir = pathlib.Path(__file__).parent
    conftest_path = current_dir / "dummy_test_project" / "conftest.py"

    with conftest_path.open("wt") as conftest_file:
        conftest_file.write(hookspec_generator.get_conftest_file())


def execute_pytest() -> subprocess.CompletedProcess:
    """Runs pytest as a subprocess for the dummy test project
    added here. All the hooks will be logged to a text file.
    In addtion, pytest is launched with ``--debug`` flag, so that
    the hook order is also available with a pluggy feature.
    """
    current_dir = pathlib.Path(__file__).parent
    test_project_root = current_dir / "dummy_test_project"
    cproc = subprocess.run(
        ["pytest", str(test_project_root), "-vs", "--debug"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return cproc


def load_hook_order_file() -> list[str]:
    """Reads out the hook order from a text file. The file name is hardcoded
    to match the name hardcoded in the project"""
    with open("hooks_order.txt", "rt") as hooks:
        data = hooks.read()

    return data.splitlines()


def get_flow_chart_file(hook_filter: set = None) -> None:
    """Renders aflow chart for selected hooks to a .svg file. The resulting
    .svg contains links to the latest version of the pytest documentation.
    This isn't great as the documentation might get outdated or modified resulting
    with non functional links."""
    hook_order = load_hook_order_file()

    # using a set so that each hook appears once
    unique_hooks = set(hook_order)

    # optional filtering
    if hook_filter:
        unique_hooks = unique_hooks & hook_filter
        hook_order = [h for h in hook_order if h in hook_filter]

    dot = graphviz.Digraph(format="gv", strict=True)
    dot.attr("node", shape="rect", width="5", ordering="out")

    for h in unique_hooks:
        dot.node(
            h,
            label=h,
            href=f"https://docs.pytest.org/en/latest/reference.html#pytest.hookspec.{h}",
            target="_blank",
        )

    for edge_begin, edge_end in zip(hook_order, hook_order[1:]):
        dot.edge(edge_begin, edge_end)

    dot.render("graph.svg", format="svg")


def get_flow_chart_pluggy(hook_filter: set = None) -> None:
    """Renders aflow chart for selected hooks to a .svg file based on
    the pluggy output."""
    pass
