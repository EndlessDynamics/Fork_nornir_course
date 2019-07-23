import os
import subprocess


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_class3_ex1a():
    base_path = "../class3/exercises/exercise1/1a/"
    cmd_list = ["python", "exercise1a.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "{'role': 'AGG'}" in std_out
    assert (
        "dict_items([('role', 'AGG'), ('timezone', 'CET'), ('state', 'WA')])" in std_out
    )
    assert std_err == ""


def test_class3_ex1b():
    base_path = "../class3/exercises/exercise1/1b/"
    cmd_list = ["python", "exercise1b.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_out.count("CET") == 2
    assert std_out.count("PST") == 3
    assert "{'role': 'AGG'}" in std_out
    assert (
        "dict_items([('role', 'AGG'), ('state', 'WA'), ('timezone', 'PST'), ('dns', '8.8.8.8')])"
        in std_out
    )
    assert std_err == ""


def test_class3_ex2():
    base_path = "../class3/exercises/exercise2/"
    cmd_list = ["python", "exercise2.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert std_out.count("{'arista1': Host: arista1}") == 3
    assert "{'arista1': Host: arista1, 'arista2': Host: arista2}" in std_out
    assert "{'arista2': Host: arista2}" in std_out
    assert std_err == ""


def test_class3_ex3():
    base_path = "../class3/exercises/exercise3/"
    cmd_list = ["python", "exercise3.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "{'arista3': Host: arista3}" in std_out
    assert std_out.count("{'arista2': Host: arista2}") == 2
    assert (
        "{'arista1': Host: arista1, 'arista2': Host: arista2, 'arista3': Host: arista3}"
        in std_out
    )
    assert "{'arista1': Host: arista1}" in std_out
    assert std_err == ""


def test_class3_ex4():
    base_path = "../class3/exercises/exercise4/"
    cmd_list = ["python", "exercise4.py"]

    os.environ["PYTHONWARNINGS"] = "ignore::Warning"
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "{'arista1': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista2': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista3': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista4': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert std_err == ""


def test_class3_ex5():
    base_path = "../class3/exercises/exercise5/"
    cmd_list = ["python", "exercise4.py"]

    os.environ["PYTHONWARNINGS"] = "ignore::Warning"
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "{'arista1': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista2': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista3': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert "'arista4': {'Et1': {'status': 'connected', 'vlan': '1'}," in std_out
    assert std_err == ""


def test_class3_ex6():
    base_path = "../class3/exercises/exercise6/"
    cmd_list = ["python", "exercise6.py"]

    os.environ["PYTHONWARNINGS"] = "ignore::Warning"
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)
    assert return_code == 0
    assert "{'nxos1': {'model': 'Nexus9000 9000v Chassis'" in std_out
    assert "'nxos2': {'model': 'Nexus9000 9000v Chassis'," in std_out
    assert std_err == ""