# Excel 模块

## 常见错误（必须避免）

| 错误写法 | 正确写法 | 说明 |
|---------|---------|------|
| `workbook.select_sheet_by_name()` | `workbook.get_sheet_by_name()` | API方法名不同 |
| `workbook.get_cell_value(row, col)` | `sheet.get_cell(row, 'A')` | 方法在sheet上，非workbook |
| `workbook.get_last_row()` | `sheet.get_row_count()` | 方法名不同 |
| 循环中重复open/close | 只open一次，try-finally close | 避免对象断开连接 |

## xbot.excel

### 方法

| 方法 | 说明 |
|------|------|
| `create(kind='office', visible=True)` | 创建Excel，kind: office/wps/openpyxl/auto_check |
| `open(file_name, kind='office', visible=True)` | 打开文件 |
| `get_active_workbook(kind)` | 获取激活的Excel |

## xbot.excel.WorkBook

| 方法 | 说明 |
|------|------|
| `get_active_sheet()` | 获取当前sheet |
| `get_sheet_by_index(index)` | 按索引获取（从1开始） |
| `get_sheet_by_name(name)` | 按名称获取 |
| `create_sheet(name, 'first'/'last')` | 创建sheet |
| `active_sheet_by_index/index/name` | 激活sheet |
| `save()` | 保存 |
| `save_as(filename)` | 另存为 |
| `close()` | 关闭（office/wps模式） |
| `execute_macro(name)` | 执行宏 |
| `delete_sheet(name)` | 删除sheet |
| `copy_sheet(name, new_name)` | 复制sheet |
| `rename_sheet(name, new_name)` | 重命名sheet |
| `export_to_pdf(name, sheet, all_sheets)` | 导出PDF |

## xbot.excel.WorkSheet

| 方法 | 说明 |
|------|------|
| `get_cell(row, 'A')` | 读单元格（行从1，列名'A'） |
| `set_cell(row, 'A', value)` | 写单元格 |
| `get_row(row_num)` | 读整行 |
| `get_column('A')` | 读整列 |
| `get_range(r1,'A',r2,'B')` | 读区域 |
| `set_row(row, [values], 'A')` | 写整行 |
| `set_column('A', [values])` | 写整列 |
| `set_range(row, 'A', [[]]) | 写区域（二维数组） |
| `append_row([values], 'A')` | 追加行 |
| `insert_row(row, [values], 'A')` | 插入行 |
| `remove_row(row)` | 删除行 |
| `remove_column('A')` | 删除列 |
| `clear()` | 清空sheet |
| `get_row_count()` | 获取总行数 |
| `get_column_count()` | 获取总列数 |
| `get_first_free_row()` | 获取第一个空行 |
| `get_first_free_column()` | 获取第一个空列 |

## 示例

```python
from xbot import excel

# 创建
wb = excel.create(kind='openpyxl', visible=False)
ws = wb.get_active_sheet()
ws.set_cell(1, 'A', '姓名')
ws.set_cell(1, 'B', '年龄')
wb.save_as('D:\\test.xlsx')

# 打开
wb = excel.open('D:\\test.xlsx', kind='openpyxl')
ws = wb.get_active_sheet()
value = ws.get_cell(1, 'A')
wb.save()
```
