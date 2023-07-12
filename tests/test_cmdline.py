from click.testing import CliRunner

from sample_python_project import cmdline


def test_main():
    runner = CliRunner()
    result = runner.invoke(cmdline.main)
    assert 'Hello world!' in result.output
