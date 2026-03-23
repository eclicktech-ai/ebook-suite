# ebook-suite

个人电子书与相关资源的统一存放仓库，由以下三个来源合并整理而来（**未保留原仓库 Git 历史**）。

**文档导航**：[docs/README.md](./docs/README.md) · [docs/product/README.md](./docs/product/README.md)（定位与边界） · [library/README.md](./library/README.md)

---

## 各分区说明（合并自原各目录 README）

### `library/expert/`（专家书单）

推荐工程师与一般通识阅读的读本，涵盖计算机科学、软件技术、软件工程、创业、思想、数学等方向；**以本目录下子文件夹中的文件为准**。

- 喜欢的书请购买**正版**；电子书仅便于收藏与检索，不能替代对知识的系统学习。
- 若认为内容侵权，请通过 Issue 说明，将及时处理。

### `library/personal/mybooks/`

个人已读/在读收藏；当前推荐按 `by-format/{epub,mobi,pdf,azw3}` 存放（详见下文「分类与迁移规则」）。

### `library/personal/ibooks-iphone/`（原 ibooks）

- 以 **EPUB** 为主，便于导入 iPhone iBooks；若需 Kindle 等格式可自行转换。
- 书单为个人挑选、读完后觉得有意思的书。
- 原仓库 **`ibells/` 铃声**（冒险岛 BGM 等）已单独放在 [`media/ringtones/maplestory-bgm/`](./media/ringtones/maplestory-bgm/)，与电子书分离。

---

### 历史与同步（迁移与 GitHub）

**迁移状态（本机已落盘）**：`mybooks`、`ibooks` 已从临时克隆目录拷贝整理；`expert_readed_books` 已同步至 `library/expert/`（约 595 个文件级对象）。若你在其他路径有更新版本，可对对应目录做增量覆盖。

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
├── docs/
├── library/
│   ├── expert/                 # expert_readed_books；见 expert/README.md
│   ├── personal/
│   │   ├── mybooks/
│   │   └── ibooks-iphone/
│   └── README.md
└── media/
    └── ringtones/
        └── maplestory-bgm/
```

## 分类与迁移规则

### 1. `library/expert/`（原 expert_readed_books）

- **规则**：**整棵目录迁入**，不拆、不重命名内部的各分类目录与 `icons/` 等。
- **操作**：将原仓库除 `.git` 外的全部内容复制到 `library/expert/`。

### 2. `library/personal/mybooks/`（原 mybooks）

- **规则（推荐）**：在 `mybooks/` 下建立 `by-format/`，**仅按文件扩展名**归类：

  | 扩展名 | 目录 |
  |--------|------|
  | `.epub` | `by-format/epub/` |
  | `.mobi` | `by-format/mobi/` |
  | `.pdf` | `by-format/pdf/` |
  | `.azw3` | `by-format/azw3/` |

- **原 README**：`library/personal/mybooks/README.md`（若保留简短说明可指向本文件）。
- **备选**：若不想按格式分，可将原仓库文件**原样**放在 `library/personal/mybooks/`（不建 `by-format/`）。

### 3. `library/personal/ibooks-iphone/` 与 `media/`（原 ibooks）

- **电子书**：原仓库**根目录**下的 `.epub`、`.pdf`（及其他电子书扩展名）→ `library/personal/ibooks-iphone/`。
- **铃声**：原 `ibells/` 下全部 `.m4r` → `media/ringtones/maplestory-bgm/`。

## 版权与使用说明

- 请尽量购买**正版图书**；电子书文件多用于个人学习与收藏。
- 若涉及侵权或权利人要求删除，请通过 Issue 说明，将及时处理。

## 迁移后自检（可选）

在已完成的 `ebook-suite` 根目录：

```bash
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
