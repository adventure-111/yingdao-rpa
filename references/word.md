# Word 模块

## xbot.word

| 方法 | 说明 |
|------|------|
| `create(kind='office', visible=True)` | 创建，kind: office/wps/auto_check |
| `open(file_name, kind='office', visible=True)` | 打开文件 |

## xbot.word.Document

| 方法 | 说明 |
|------|------|
| `get_selection()` | 获取选区 |
| `insert_table(rows, cols)` | 插入表格 |
| `insert_text(text)` | 插入文本 |
| `save()` | 保存 |
| `save_as(path)` | 另存为 |
| `close()` | 关闭 |

## xbot.word.Selection

| 方法 | 说明 |
|------|------|
| `type_text(text)` | 输入文本 |
| `get_text()` | 获取文本 |
| `replace(find, replace)` | 替换文本 |
| `insert_picture(path)` | 插入图片 |
| `break_line()` | 换行 |

## 示例

```python
from xbot import word

# 创建
doc = word.create(kind='office', visible=True)
sel = doc.get_selection()
sel.type_text('Hello Word')

# 打开
doc = word.open('D:\\test.docx')
doc.save()
doc.close()
```
