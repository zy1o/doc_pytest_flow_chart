import pytest
import _pytest.hookspec
from doc_pytest_flow_chart import hookspec_generator


def test_hookspec(monkeypatch):
    def pytest_cmdline_preparse(
        plugin: "_PluggyPlugin", manager: "PytestPluginManager"
    ) -> None:
        pass

    monkeypatch.setattr(
        _pytest.hookspec, "pytest_cmdline_preparse", pytest_cmdline_preparse
    )

    assert (
        "def pytest_cmdline_preparse(plugin, manager)"
        in hookspec_generator.get_conftest_file()
    )
