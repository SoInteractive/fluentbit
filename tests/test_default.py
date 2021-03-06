
from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/etc/td-agent-bit"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/td-agent-bit/td-agent-bit.conf",
        "/etc/rsyslog.d/90-logforwarder.conf"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "td-agent-bit"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(host):
    present = [
        "td-agent-bit",
        "rsyslog"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed
