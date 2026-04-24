# 影刀 RPA 技能库

影刀 XBot 的 Python 自动化开发技能模板与 API 参考。

## 内容结构

```
yingdao-rpa/
├── SKILL.md              # 主技能文件（供 Hermes Agent 使用）
├── README.md             # 本文件
├── assets/
│   └── default_module_template.py   # 标准模块模板
└── references/
    ├── _index.md         # 全部 API 索引（306个指令）
    ├── api_summary.md    # 完整 API 速查手册
    ├── feishu_bitable.md # 飞书多维表格（28个指令）
    ├── troubleshooting.md # 11个高频问题与解法
    ├── sop.md            # RPA开发SOP提示词
    ├── web.md            # xbot.web 详解
    ├── win32.md          # xbot.win32 详解
    ├── excel.md          # xbot.excel 详解
    ├── word.md           # xbot.word 详解
    ├── mobile.md         # xbot.mobile 详解
    ├── app.md            # xbot.app（数据表格/对话框）详解
    ├── ai.md             # AI能力（OCR）详解
    ├── guides.md         # 开发指南
    └── other.md          # 剩余模块（ado/ftp/pdf/xzip）
```

## 快速开始

### 1. 新建一个影刀模块

复制 `assets/default_module_template.py` 到你的影刀项目，作为新模块的起点。

### 2. 核心规则

- **入口函数**：`def main(args):`，不能用 `if __name__ == "__main__":`
- **必须导入**：`xbot`、`print`、`sleep`、`package`
- **查找指令**：完整清单见 `references/_index.md`，详细用法见对应 reference 文件
- **元素选择**：用 `package.selector('元素名称')`，不要硬编码 xpath

### 3. 常用模块一览

| 模块 | 用途 |
|------|------|
| `xbot.web` | 网页自动化（浏览器控制、元素操作） |
| `xbot.win32` | Windows 桌面应用自动化 |
| `xbot.excel` | Excel 读、写、格式、公式 |
| `xbot.word` | Word 文档操作 |
| `xbot.mobile` | Android/iOS 移动端自动化 |
| `xbot.app.databook` | 影刀数据表格读写 |
| `xbot.app.dialog` | 消息/确认/通知对话框 |
| `xbot.ai.*` | 阿里云/百度/腾讯 OCR |
| `xbot.pdf` | PDF 文本提取、合并 |
| `xbot.ftp` | FTP 文件上传下载 |
| `xbot.xzip` | 文件压缩解压 |
| `xbot.ado` | 数据库 SQL 执行 |
| `xbot_extensions.activity_feishu_bitable` | 飞书多维表格（28指令） |

## 示例

```python
import xbot
from xbot import print, sleep
from . import package
from .package import variables as glv

def main(args):
    # 打开 Excel 并读取数据
    workbook = xbot.excel.open('D:\\data.xlsx', kind='office', visible=True)
    try:
        sheet = workbook.get_sheet_by_name('Sheet1')
        value = sheet.get_cell(1, 'A')
        print(f"读取到: {value}")
        workbook.save()
    finally:
        workbook.close()
```

## 查看完整指令清单

所有 306 个指令的完整索引在 `references/_index.md`，包含每个指令的名称、参数和简要说明。

## 官方文档

https://www.yingdao.com/yddoc/rpa/zh-CN/
