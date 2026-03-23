# ebook-suite

个人或团队整理的电子书与相关资源（含铃声等非图书文件），按目录存放；**与业务代码无依赖**，可单独 clone、单独维护。

- **是**：主题书单（`library/expert/`）、个人书库（`library/personal/`）、媒体（`media/`）。
- **不是**：后端、前端或 CI 构建的一部分。

细分与分类索引见 [library/expert/README.md](library/expert/README.md)。

---

## 目录里有什么

| 路径 | 内容 |
|------|------|
| [library/expert/](library/expert/) | 主题书单：工程/通识向，按学科分子文件夹 |
| [library/personal/](library/personal/) | 个人藏书：按格式分子目录（`epub/`、`pdf/` 等），见 [library/personal/README.md](library/personal/README.md) |
| [media/ringtones/maplestory-bgm/](media/ringtones/maplestory-bgm/) | 铃声等非图书文件 |

## 仓库结构

```text
ebook-suite/
├── README.md
├── scripts/
│   ├── organize_software_tech.py      # tech-inbox → expert 主题目录
│   └── push-commits-one-by-one.sh    # 分批 push，缓解 GitHub 单次 pack 约 2GiB 限制
├── library/
│   ├── expert/
│   │   ├── tech-inbox/             # 待分类电子书暂放处
│   │   ├── android/ …            # 开发技术类（与「人物传」等同级，见 expert/README.md）
│   │   └── …
│   └── personal/
│       └── epub/  mobi/  pdf/  azw3/   # 个人书按扩展名（含原 ibooks-iphone 合并）
└── media/
    └── ringtones/
        └── maplestory-bgm/
```

## 各分区说明

### `library/expert/`

工程师与通识向书单，涵盖计算机科学、软件技术、软件工程、创业、思想、数学等；**以子文件夹内实际文件为准**。分类目录表见 [library/expert/README.md](library/expert/README.md)。

### `library/personal/`

个人藏书：在 `library/personal/` 下按扩展名直接分子目录（**已去掉** `mybooks/by-format/` 嵌套）：

| 扩展名 | 目录 |
|--------|------|
| `.epub` | `epub/` |
| `.mobi` | `mobi/` |
| `.pdf` | `pdf/` |
| `.azw3` | `azw3/` |

也可把文件放在 `personal/` 根下，不强制分子目录。索引说明见 [library/personal/README.md](library/personal/README.md)。

### `media/ringtones/maplestory-bgm/`

与图书分开存放的 `.m4r` 等铃声资源。

## 大仓库推送到 GitHub

GitHub 对 push 有 **约 2GiB** 的 pack 限制（你看到的 `pack exceeds maximum allowed size (2.00 GiB)`）。要分清两件事：

| 情况 | `scripts/push-commits-one-by-one.sh` 有用吗 |
|------|---------------------------------------------|
| 一次 `git push` 想带上**多个提交**，合成 pack 太大 | **可能有**：改成**每个提交单独 push**，单次 pack 变小。 |
| **某一个提交**里包含的对象太多，**单独 push 那一个**仍报 2GiB | **没用**：必须**把该提交拆成多个更小提交**、或对大文件用 [Git LFS](https://git-lfs.github.com/)、或减少仓库里的二进制体积。脚本不会替你拆提交。 |

```bash
bash scripts/push-commits-one-by-one.sh
```

### 单个提交仍超 2GiB时（脚本救不了）

思路任选其一（或组合）：

1. **拆提交**：例如回到拆分点之前，分批 `git add` 子目录再多次 `git commit`，使每个提交只含一部分文件（可用 `git reset --soft <基线>` 把未推送的改动重新分期提交，再用上面的脚本逐个 push）。操作前请备份或另开分支。
2. **Git LFS**：把 PDF/EPUB 等交给 LFS 跟踪，普通 pack 会小很多（需安装 `git-lfs` 并迁移历史，文档见官网）。
3. **不要把超大资源放在 Git 里**：对象存储 / 网盘链接 + 仓库只留说明。

### 若出现 `remote end hung up` / `Connection closed by remote host`

多为**长时间上传中途断线**（与「pack 超过 2GiB」不同）。可在本机**仅对本仓库**加大缓冲并重试（HTTPS 有效）：

```bash
cd /path/to/ebook-suite
git config http.version HTTP/1.1
git config http.postBuffer 524288000
```

若远程地址是 **SSH**（`git@github.com`），请在 `~/.ssh/config` 为 GitHub 增加保活，再重试 push：

```text
Host github.com
  HostName github.com
  User git
  ServerAliveInterval 30
  ServerAliveCountMax 120
```

仍失败可尝试：**换稳定网络**、**改用另一种协议**（SSH ↔ HTTPS）、或把大文件迁到 **Git LFS** 后推送。

---

## 版权与使用

- 请尽量购买**正版图书**；此处文件多用于个人学习与收藏。
- 若认为内容侵权，请通过 Issue 说明，将及时处理。
