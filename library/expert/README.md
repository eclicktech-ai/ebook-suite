# `library/expert/` 专家书单

面向工程师与通识阅读的**主题书单**，按文件夹分类；含本说明、`icons/`、`list.png` 与各分类子目录。

总览与版权：见 [仓库根 README](../../README.md)。

## 通识与人文等（中文目录名）

| 分类 | 路径 |
|------|------|
| 人物传 | [人物传](./人物传/) |
| 创业类 | [创业类](./创业类/) |
| 历史类 | [历史类](./历史类/) |
| 哲学类 | [哲学类](./哲学类/) |
| 大佬书籍 | [大佬书籍](./大佬书籍/) |
| 小说类 | [小说类](./小说类/) |
| 数学类 | [数学类](./数学类/) |
| 经济类 | [经济类](./经济类/) |
| 编程思想类 | [编程思想类](./编程思想类/) |
| 计算机科学 | [计算机科学](./计算机科学/) |
| 软件工程 | [软件工程](./软件工程/) |

## 开发技术（英文目录名，与上表同级）

以下目录**直接位于** `library/expert/`，不再套一层「软件技术」。新文件可先放入 [tech-inbox](./tech-inbox/)，再运行 [`scripts/organize_software_tech.py`](../../scripts/organize_software_tech.py) 按文件名归类。

| 目录 | 含义（示例） |
|------|----------------|
| [android](./android/) | Android 开发 |
| [bigdata](./bigdata/) | Hadoop、Hive、HBase、Elasticsearch 等 |
| [c-cpp](./c-cpp/) | C / C++（含 `thinkinginC++/` 等子文件夹） |
| [cloud-virtualization](./cloud-virtualization/) | OpenStack、KVM 等 |
| [data-ml](./data-ml/) | 机器学习、算法类 |
| [database](./database/) | MySQL、Redis、MongoDB 等 |
| [devops](./devops/) | Linux、Docker、命令行与内核注释等 |
| [distributed-messaging](./distributed-messaging/) | Kafka、ZooKeeper、Spring Cloud、微服务 |
| [dotnet-web](./dotnet-web/) | ASP.NET、.NET 面试等 |
| [embedded](./embedded/) | 嵌入式、RFID、J2ME、Qt 嵌入式等 |
| [java](./java/) | Java |
| [matlab](./matlab/) | MATLAB（含 `matlab教程电子书/` 等） |
| [networking](./networking/) | Nginx、网络方案、压测等 |
| [php](./php/) | PHP |
| [security](./security/) | 安全脚本类 |
| [other](./other/) | 难以从文件名自动归类或通用面试书等 |

归类脚本若根据文件名匹配到新主题（例如 `python/`、`javascript-web/`），会在 `library/expert/` 下**自动创建**对应目录。

书目以本目录下**实际文件**为准；阅读请优先购买正版。
