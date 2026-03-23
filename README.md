# ebook-suite

个人电子书与相关资源的统一存放仓库，由以下三个来源合并整理而来（**未保留原仓库 Git 历史**）。

**文档导航**：[docs/README.md](./docs/README.md) · [docs/product/README.md](./docs/product/README.md)（定位与边界） · [library/README.md](./library/README.md)

---

### 历史与同步（迁移与 GitHub）

**迁移状态（本机已落盘）**：`mybooks`、`ibooks` 已从 `/tmp/ebook-suite-inspect` 拷贝整理；`expert_readed_books` 已从临时完整克隆同步至 `library/expert/`（约 595 个文件）。若你在其他路径有更新版本，可对对应目录做增量覆盖。

**GitHub 同步**：电子书与铃声已纳入 Git 跟踪（已去掉对 `*.pdf` 等的忽略）。因 GitHub **单次接收 pack 约 2GB 上限**，历史上传被拆成多次提交（personal → expert 各分类 → `软件技术` 分两段等）。若以后再次大量新增，请分批 `commit` + `push`。

---

| 原仓库 | 迁入位置 | 说明 |
|--------|-----------|------|
| `eclicktech-ai/expert_readed_books` | `library/expert/` | 专家/主题书单，**保留原仓内所有分类子目录** |
| `eclicktech-ai/mybooks` | `library/personal/mybooks/` | 个人已读/在读，可按格式分子目录 |
| `eclicktech-ai/ibooks` | `library/personal/ibooks-iphone/` + `media/ringtones/maplestory-bgm/` | 根目录电子书与 `ibells` 铃声拆分存放 |

## 目录结构

```text
ebook-suite/
├── README.md
├── library/
│   ├── expert/                 # expert_readed_books 整仓内容（内部子文件夹名不变）
│   ├── personal/
│   │   ├── mybooks/            # mybooks（可选 by-format/ 按扩展名分桶）
│   │   └── ibooks-iphone/      # ibooks 仓库根目录的 epub/pdf 等（不含 ibells）
│   └── README.md               # 可选：expert 与 personal 的说明
└── media/
    └── ringtones/
        └── maplestory-bgm/     # 原 ibooks/ibells 下的 .m4r
```

## 分类与迁移规则

### 1. `library/expert/`（原 expert_readed_books）

- **规则**：**整棵目录迁入**，不拆、不重命名内部的 `计算机科学类/`、`人物传/`、`icons/` 等。
- **操作**：将原仓库除 `.git` 外的全部内容复制到 `library/expert/`。

### 2. `library/personal/mybooks/`（原 mybooks）

- **规则（推荐）**：在 `mybooks/` 下建立 `by-format/`，**仅按文件扩展名**归类：

  | 扩展名 | 目录 |
  |--------|------|
  | `.epub` | `by-format/epub/` |
  | `.mobi` | `by-format/mobi/` |
  | `.pdf` | `by-format/pdf/` |
  | `.azw3` | `by-format/azw3/` |

- **原 README**：放在 `library/personal/mybooks/README.md`。
- **备选**：若不想按格式分，可将原仓库文件**原样**放在 `library/personal/mybooks/`（不建 `by-format/`）。

### 3. `library/personal/ibooks-iphone/` 与 `media/`（原 ibooks）

- **电子书**：原仓库**根目录**下的 `.epub`、`.pdf`（及其他电子书扩展名）→ `library/personal/ibooks-iphone/`。
- **铃声**：原 `ibells/` 下全部 `.m4r` → `media/ringtones/maplestory-bgm/`（与电子书分离）。
- **原 README**：可放在 `ibooks-iphone/README.md` 或合并进本文件，并注明铃声新路径。

## 版权与使用说明

- 请尽量购买**正版图书**；电子书文件多用于个人学习与收藏。
- 若涉及侵权或权利人要求删除，请通过 Issue 说明，将及时处理。

## 迁移后自检（可选）

在已完成的 `ebook-suite` 根目录：

```bash
# 各顶层目录是否存在
test -d library/expert library/personal/mybooks library/personal/ibooks-iphone media/ringtones/maplestory-bgm
```

在原 `mybooks` 克隆根目录迁移前，可先统计扩展名数量（与迁入后对比）：

```bash
printf "epub: "; ls -1 *.epub 2>/dev/null | wc -l
printf "mobi: "; ls -1 *.mobi 2>/dev/null | wc -l
printf "pdf: "; ls -1 *.pdf 2>/dev/null | wc -l
printf "azw3: "; ls -1 *.azw3 2>/dev/null | wc -l
```

## 旧仓库处理建议

合并并推送本仓库后，可将三个旧仓库 **Archive**，并在各旧仓库 README 顶部注明：**内容已迁移至 `eclicktech-ai/ebook-suite`**。
