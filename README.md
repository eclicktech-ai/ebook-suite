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
| [library/personal/mybooks/](library/personal/mybooks/) | 个人已读/在读 |
| [library/personal/ibooks-iphone/](library/personal/ibooks-iphone/) | EPUB/PDF 为主，便于阅读器导入 |
| [media/ringtones/maplestory-bgm/](media/ringtones/maplestory-bgm/) | 铃声等非图书文件 |

## 仓库结构

```text
ebook-suite/
├── README.md
├── library/
│   ├── expert/
│   └── personal/
│       ├── mybooks/
│       └── ibooks-iphone/
└── media/
    └── ringtones/
        └── maplestory-bgm/
```

## 各分区说明

### `library/expert/`

工程师与通识向书单，涵盖计算机科学、软件技术、软件工程、创业、思想、数学等；**以子文件夹内实际文件为准**。分类目录表见 [library/expert/README.md](library/expert/README.md)。

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

以 EPUB 为主；书单为个人挑选（如 2012–2018 期间收集）。铃声放在 `media/ringtones/maplestory-bgm/`，与图书分开。

### `media/ringtones/maplestory-bgm/`

与图书分开存放的 `.m4r` 等铃声资源。

---

## 版权与使用

- 请尽量购买**正版图书**；此处文件多用于个人学习与收藏。
- 若认为内容侵权，请通过 Issue 说明，将及时处理。
