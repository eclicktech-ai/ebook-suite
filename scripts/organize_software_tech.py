#!/usr/bin/env python3
"""Classify files in library/expert/软件技术/ by filename; print git mv commands. Run from ebook-suite root."""
import os
import subprocess
import sys

BASE = os.path.join("library", "expert", "软件技术")


def bucket(name: str) -> str:
    s = name.lower()
    n = name
    nl = n.casefold()

    if "javascript" in s or "node.js" in s or " node" in s or "react" in s or "vue" in s or "angular" in s:
        return "javascript-web"
    if "android" in s or "andord" in s:
        return "android"
    if "ios" in s or "swift" in s:
        return "mobile-ios"
    if "php" in s:
        return "php"
    if "asp.net" in s or "+mvc+" in s or ".net程序员" in n:
        return "dotnet-web"
    if "html" in s or "css" in s or "w3c" in s:
        return "web-frontend"

    if "docker" in s or "kubernetes" in s or "k8s" in s:
        return "devops"
    if "linux" in s or "ubuntu" in s or "command line" in s or "shell" in s or "bash" in s or "apress.beginning.the.linux" in s:
        return "devops"
    if "openstack" in s or "kvm" in s or "深度实践kvm" in n or "《深度实践kvm》" in n:
        return "cloud-virtualization"
    if "nginx" in s:
        return "networking"
    if "memcached" in s or "haproxy" in s or "loadrunner" in s:
        return "networking"

    if "mysql" in s or "redis" in s or "mongo" in s or "postgresql" in s:
        return "database"
    if "sql" in s and "mysql" not in s and "hbase" not in s:
        pass

    if "hadoop" in s or "hive" in s or "hbase" in s or "spark" in s or "flink" in s or "elasticsearch" in s or "fastdfs" in s:
        return "bigdata"

    if "kafka" in s or "zookeeper" in s or "paxos" in s:
        return "distributed-messaging"
    if "zeromq" in s or "zmq" in s:
        return "distributed-messaging"
    if "spring" in s or "微服务" in n:
        return "distributed-messaging"

    if "java" in s and "javascript" not in s and "jsp" not in s:
        return "java"
    if "python" in s:
        return "python"
    if "go语言" in n or "golang" in s:
        return "golang"
    if "rust" in s:
        return "rust"

    if "matlab" in s:
        return "matlab"

    if (
        "c++" in n
        or "c++" in s
        or "c语言" in nl
        or "c程序" in nl
        or "c和" in nl
        or "c陷阱" in nl
        or "c.primer" in s
        or "c primer" in s
        or "c和指针" in nl
        or "stl" in s
        or "codeguru" in s
        or n.startswith("c ")
        or n.startswith("c.")
        or n.startswith("C ")
        or n.startswith("C.")
        or "cmd命令" in n
        or "高质量c" in s
        or "彻底搞定c指针" in nl
    ):
        return "c-cpp"
    if "vc++" in s or "vc6" in s or "codeguru" in s:
        return "c-cpp"

    if "windows" in s or "wince" in s or "win32" in s:
        return "windows-systems"
    if "ucos" in s or "j2me" in s or "rfid" in s or "d3_rfid" in s or "qt4" in s or "qtopia" in s or "6410" in s:
        return "embedded"
    if "opencv" in s or "数字图像" in n:
        return "graphics-cv"

    if "机器学习" in n or "与r语言" in n:
        return "data-ml"
    if "经典算法" in n:
        return "data-ml"

    if "区块链" in n:
        return "networking"
    if "网络详细" in n or "网络工程师" in n or "实施方案" in n:
        return "networking"

    if "微服务设计" in n:
        return "distributed-messaging"
    if ".net程序员面试" in nl:
        return "dotnet-web"
    if "面试宝典" in n or "疯狂的程序员" in n:
        return "other"
    if "脚本黑客" in n or "精通脚本" in n:
        return "security"
    if "黑客" in n:
        return "security"

    return "other"


def main() -> None:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    tech = os.path.join(root, BASE)
    os.chdir(root)

    moves: list[tuple[str, str]] = []
    for name in os.listdir(tech):
        src = os.path.join(tech, name)
        if not os.path.isfile(src):
            continue
        b = bucket(name)
        dst_dir = os.path.join(tech, b)
        dst = os.path.join(dst_dir, name)
        if os.path.exists(dst):
            print(f"skip exists: {dst}", file=sys.stderr)
            continue
        moves.append((os.path.relpath(src, root), os.path.relpath(dst, root)))

    moves.sort(key=lambda x: x[0])
    for a, b in moves:
        os.makedirs(os.path.dirname(os.path.join(root, b)), exist_ok=True)
        subprocess.run(["git", "mv", a, b], check=True, cwd=root)
        print(f"mv {a} -> {b}")


if __name__ == "__main__":
    main()
