# `tech-inbox/` 待分类电子书

将**尚未归类**的电子书文件放在此目录（仅文件，不要套一层子文件夹），在仓库根目录执行：

```bash
python3 scripts/organize_software_tech.py
```

脚本会按**文件名关键词**移动到 `library/expert/` 下对应主题目录（如 `android/`、`java/`、`c-cpp/` 等）。规则见 [`scripts/organize_software_tech.py`](../../scripts/organize_software_tech.py)。
