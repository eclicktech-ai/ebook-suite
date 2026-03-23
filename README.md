# ebook-suite

个人电子书与少量相关资源（如铃声）的整理库，按用途分目录存放。

**文档**：[docs/README.md](./docs/README.md) · [docs/product/README.md](./docs/product/README.md) · [library/README.md](./library/README.md)

---

## 目录里有什么

| 路径 | 内容 |
|------|------|
| [library/expert/](library/expert/) | 主题书单：工程/通识向，按学科分子文件夹 |
| [library/personal/mybooks/](library/personal/mybooks/) | 个人已读/在读 |
| [library/personal/ibooks-iphone/](library/personal/ibooks-iphone/) | EPUB/PDF 为主，便于阅读器导入 |
| [media/ringtones/maplestory-bgm/](media/ringtones/maplestory-bgm/) | 铃声等非图书文件 |

## 仓库结构

```text
ebook-suite/
├── README.md
├── docs/
├── library/
│   ├── expert/
│   ├── personal/
│   │   ├── mybooks/
│   │   └── ibooks-iphone/
│   └── README.md
└── media/
    └── ringtones/
        └── maplestory-bgm/
```

## 各分区说明

### `library/expert/`

工程师与通识向书单，涵盖计算机科学、软件技术、软件工程、创业、思想、数学等；**以子文件夹内实际文件为准**。细分与索引见 [library/expert/README.md](library/expert/README.md)。

### `library/personal/mybooks/`

个人藏书。推荐在 `mybooks/` 下使用 `by-format/`，仅按扩展名归类：

| 扩展名 | 目录 |
|--------|------|
| `.epub` | `by-format/epub/` |
| `.mobi` | `by-format/mobi/` |
| `.pdf` | `by-format/pdf/` |
| `.azw3` | `by-format/azw3/` |

也可全部放在 `mybooks/` 根下，不强制分子目录。

### `library/personal/ibooks-iphone/`

以 EPUB 为主；书单为个人挑选。说明见 [ibooks-iphone/README.md](library/personal/ibooks-iphone/README.md)。

### `media/ringtones/maplestory-bgm/`

与图书分开存放的 `.m4r` 等铃声资源。

---

## 版权与使用

- 请尽量购买**正版图书**；此处文件多用于个人学习与收藏。
- 若认为内容侵权，请通过 Issue 说明，将及时处理。
