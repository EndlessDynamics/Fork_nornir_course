from glob import glob
import os
import subprocess


NORNIR_LOGGING = {"enabled": False}


def gen_inventory_dict(base_path):
    """Dynamically create an inventory dictionary using exercise path."""
    # BASE_PATH = "../class1/exercises/exercise1/"
    NORNIR_HOSTS = f"{base_path}/hosts.yaml"
    NORNIR_GROUPS = f"{base_path}/groups.yaml"
    NORNIR_DEFAULTS = f"{base_path}/defaults.yaml"
    NORNIR_INVENTORY = {
        "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
        "options": {
            "host_file": NORNIR_HOSTS,
            "group_file": NORNIR_GROUPS,
            "defaults_file": NORNIR_DEFAULTS,
        },
    }
    return NORNIR_INVENTORY


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def remove_log_files(exercise_dir):
    log_files = glob(f"{exercise_dir}/*.log")
    for file in log_files:
        os.remove(file)


def test_class6_ex1():
    base_path = "../class6/exercises/exercise1/"
    cmd_list = ["python", "exercise1.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_out.count("syntax error, expecting <command>.") == 2
    assert std_out.count("ValueError") == 2
    assert std_err.count("ValueError") == 2


def test_class6_ex2a():
    base_path = "../class6/exercises/exercise2/exercise2a/"
    cmd_list = ["python", "exercise2.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "  ip address 1.2.3.1 255.255.255.255" in std_out
    assert "  ip address 1.3.2.1 255.255.255.255" in std_out
    assert std_err == ""


def test_class6_ex2b():
    base_path = "../class6/exercises/exercise2/exercise2b_2c/"
    cmd_list = ["python", "exercise2b.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "  ip address 1.2.3.1 255.255.255.255" in std_out
    assert "Eh, its okay...." in std_out
    assert "Host 'nxos2': task 'template_file' failed with traceback:" in std_err
    assert "jinja2.exceptions.UndefinedError: 'loopbacks' is undefined" in std_err


def test_class6_ex2c():
    base_path = "../class6/exercises/exercise2/exercise2b_2c/"
    cmd_list = ["python", "exercise2c.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "  ip address 1.2.3.1 255.255.255.255" in std_out
    assert "Encountered Jinja2 error Undefined Variable" in std_out
    assert "Host 'nxos2': task 'template_file' failed with traceback:" in std_err
    assert "jinja2.exceptions.UndefinedError: 'loopbacks' is undefined" in std_err


def test_class6_ex3():
    base_path = "../class6/exercises/exercise3/"
    cmd_list = ["python", "exercise3.py"]

    os.environ["NORNIR_PASSWORD"] = "88newclass"
    remove_log_files(base_path)
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    remove_log_files(base_path)
    assert return_code == 0
    assert std_err == ""
