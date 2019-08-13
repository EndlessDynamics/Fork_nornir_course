from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks import networking


def file_copy(task):

    host = task.host
    platform = host.platform
    filename = host["file_name"]
    source_file = f"{platform}/{filename}"

    # SCP Transfer the file
    task.run(
        task=networking.netmiko_file_transfer,
        source_file=source_file,
        dest_file=filename,
        overwrite_file=True,
        direction="put",
    )

    # Verify file contents are correct
    cmd = f"more flash:/{filename}"
    multi_result = task.run(task=networking.netmiko_send_command, command_string=cmd)
    output = multi_result[0].result

    print()
    print("-" * 40)
    print(f"{host}:")
    print(output)
    print("-" * 40)
    print()


def main():
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(F(groups__contains="eos"))
    nr.run(task=file_copy)


if __name__ == "__main__":
    main()
