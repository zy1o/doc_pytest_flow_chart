import pathlib
import subprocess
import graphviz
from doc_pytest_flow_chart import hookspec_generator


def generate_conftest() -> None:
    """ Creates a new conftest file in the dummy project
    directory """
    current_dir = pathlib.Path(__file__).parent
    conftest_path = current_dir / "dummy_test_project" / "conftest.py"

    
    with conftest_path.open("wt") as conftest_file:
        conftest_file.write(hookspec_generator.get_conftest_file())


def execute_pytest() -> subprocess.CompletedProcess:
    """ Runs pytest as a subprocess for the dummy test project
    added here. All the hooks will result with a file
    """
    current_dir = pathlib.Path(__file__).parent
    test_project_root = current_dir / "dummy_test_project"
    cproc = subprocess.run(["pytest", str(test_project_root), "-vs"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return cproc


def load_hook_order_file() -> list[str]:
    """ Reads out the hook order from a text file."""
    with open("hooks_order.txt", "rt") as hooks:
        data = hooks.read()

    return data.splitlines()


def get_flow_chart():
    """ Renders flow chart to a .svg file"""
    hook_order = load_hook_order_file()

    unique_hooks = set(hook_order)

    dot = graphviz.Digraph(format='gv', strict=True)
    dot.attr("node", shape="rect", width="5", ordering="out")

    for h in unique_hooks:
        dot.node(h, label=h, href=f"https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.{h}")
    
    for edge_begin, edge_end in zip(hook_order, hook_order[1:]):
        dot.edge(edge_begin, edge_end)

    dot.render("graph", format="svg", view=True)


if __name__ == "__main__":
    generate_conftest()
    execute_pytest()
    get_flow_chart()
