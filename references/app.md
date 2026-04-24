# APP 模块

## xbot.app.databook

影刀内置数据表格

| 方法 | 说明 |
|------|------|
| `get_row(row_num)` | 获取行（从1开始） |
| `set_row(row_num, values, 'A')` | 写入行 |
| `get_column(column_name)` | 获取列 |
| `set_column(column_name, values)` | 写入列 |
| `get_row_count()` | 获取总行数 |
| `clear()` | 清空 |

## xbot.app.dialog

| 方法 | 说明 |
|------|------|
| `message(msg, title)` | 消息框 |
| `confirm(msg, title)` | 确认框，返回bool |
| `input(title, default)` | 输入框，返回输入内容 |

## 示例

```python
from xbot import app

# 数据表格
app.databook.set_row(1, ['a', 'b', 'c'])
data = app.databook.get_row(1)

# 对话框
app.dialog.message('操作完成')
result = app.dialog.confirm('是否继续？')
value = app.dialog.input('请输入：', '默认值')
```
