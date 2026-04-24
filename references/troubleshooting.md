# 影刀RPA实战问题解决方案

> 基于实际项目开发经验总结，持续更新

## 问题1：Excel对象断开连接

**错误信息**：
```
❌ 同步失败：(-2147417848, '被调用的对象已与其客户端断开连接。', None, None)
❌ 同步失败：'NoneType' object has no attribute 'Close'
```

**原因**：每个配置循环中重复打开/关闭Excel文件

**解决方案**：
```python
# ❌ 错误：循环中重复打开关闭
for config in config_list:
    workbook = xbot.excel.open(...)
    ...
    workbook.close()

# ✅ 正确：只打开一次，最后关闭
workbook = xbot.excel.open(excel_file_path, kind='office', visible=False)
try:
    for config in config_list:
        result = sync_sheet_to_feishu(bitable_instance, workbook, config)
finally:
    workbook.close()
```

---

## 问题2：Excel API方法不存在

**错误信息**：
```
"OfficeWorkBook" 没有 "select_sheet_by_name" 属性或方法
```

**原因**：使用了错误的API方法名

**解决方案**：
```python
# ❌ 错误：不存在的方法
workbook.select_sheet_by_name("Sheet1")
workbook.get_cell_value(row, col)
workbook.get_last_row()

# ✅ 正确：影刀标准API
sheet = workbook.get_sheet_by_name("Sheet1")
value = sheet.get_cell(row, 'A')
total_rows = sheet.get_row_count()
```

---

## 问题3：模块入口设计不合理

**问题描述**：main函数接收args字典，不便于主流程调用

**解决方案**：
```python
# 主要业务逻辑封装为独立函数，使用独立参数
def sync_excel_to_feishu(excel_file_path, feishu_app_id, feishu_app_secret, feishu_bitable_token):
    excel_file_path = glv['workspace'] + '\\' + excel_file_path
    ...

# main函数用于单元测试
def main(args):
    # 测试数据
    excel_file_path = ""
    ...
    return sync_excel_to_feishu(
        excel_file_path,
        feishu_app_id,
        feishu_app_secret,
        feishu_bitable_token
    )
```

---

## 问题4：飞书扩展指令未加载

**错误信息**：调用飞书指令时报错，指令不可用

**原因**：影刀不会自动加载飞书扩展指令

**解决方案**：
1. 在影刀可视化编辑器中，从指令面板拖入任意一个飞书多维表格操作指令
2. 删除该指令（只是触发加载）
3. 此后可在代码中使用`xbot_visual.process.run`调用飞书指令

---

## 问题5：飞书默认视图名称错误

**错误信息**：视图不存在

**原因**：文档示例使用`"默认视图"`，但实际飞书默认视图名称是`"表格"`

**解决方案**：
```python
# ❌ 错误
"view_identity": "默认视图"

# ✅ 正确
"view_identity": "表格"

# 最佳实践：先获取视图列表
views_id, views_name, _ = get_views(...)
```

---

## 问题6：_block参数模块名错误

**问题描述**：`_block=("main", 21, "删除记录")`中模块名固定为main

**解决方案**：
```python
# ❌ 错误
_block=("main", 21, "删除记录")

# ✅ 正确：使用实际模块名称
_block=("飞书多维表格同步模块", 21, "删除记录")
```

---

## 问题7：飞书表名匹配失败

**错误信息**：
```
❌ 写入失败：未找到数据表 W2 达成 - 数据表
```

**原因**：
- 表名有空格差异
- 副本表命名差异
- API返回的表列表可能不完整

**解决方案**：
```python
# 多重匹配策略
def get_table_id(bitable_instance, table_name):
    tables_id, tables_name, _ = get_tables(...)
    
    for i, name in enumerate(tables_name):
        # 1. 精确匹配
        if name == table_name:
            return tables_id[i]
        # 2. 忽略前后空格
        if name.strip() == table_name.strip():
            return tables_id[i]
        # 3. 去掉所有空格（包括全角空格）
        if name.replace(" ", "").replace("\u3000", "") == table_name.replace(" ", "").replace("\u3000", ""):
            return tables_id[i]
    
    # 优先使用表ID进行后续操作
    return None
```

---

## 问题8：飞书数字字段转换失败

**错误信息**：
```
❌ 写入失败：错误码：1254061; 错误信息：NumberFieldConvFail
the value of 'Number' must be a number
```

**原因**：Excel中的空值转换为空字符串`""`，飞书数字字段不接受空字符串

**解决方案**：
```python
# 空值字段不传输
def merge_records_by_row(...):
    for row_idx in range(start_row, end_row + 1):
        merged_record = {}
        
        for config in configs:
            ...
            converted_value = convert_value_for_feishu(cell_value)
            
            # 空值不传输该字段
            if converted_value != "":
                merged_record[field_name] = converted_value
        
        records.append(merged_record)
```

---

## 问题9：同一个飞书表的数据未整合

**问题描述**：同一个飞书表的多个Excel区域配置，生成了多条独立记录，应该合并为一条

**原因**：分组逻辑只按飞书表名分组，没有按行范围分组

**解决方案**：
```python
# 按飞书表名 + Excel表名 + 行范围分组
def group_by_feishu_table(config_list):
    grouped = {}
    
    for config in config_list:
        key = (
            config["feishu_table"],
            config["excel_sheet"],
            config["start_row"],
            config["end_row"]
        )
        
        if key not in grouped:
            grouped[key] = {"configs": []}
        grouped[key]["configs"].append(config)
    
    return grouped

# 按行合并多个配置的数据
def merge_records_by_row(workbook, configs, start_row, end_row):
    for row_idx in range(start_row, end_row + 1):
        merged_record = {}
        
        for config in configs:
            # 读取每个配置的列数据，合并到同一条记录
            ...
        
        records.append(merged_record)
```

---

## 问题10：批量删除效率低

**问题描述**：逐条删除记录，API调用次数过多

**解决方案**：
```python
# ❌ 错误：逐条删除
for record_id in records_id:
    xbot_visual.process.run(
        process="...delete_record",
        inputs={"record_id": record_id},
        ...
    )

# ✅ 正确：批量删除（每次最多500条）
batch_size = 500
for i in range(0, len(records_id), batch_size):
    batch_ids = records_id[i:i+batch_size]
    xbot_visual.process.run(
        process="...batch_delete_record",
        inputs={"record_ids": batch_ids},
        ...
    )
```

---

## 问题11：日志输出过于冗余

**问题描述**：每条操作都输出详细日志，信息过多

**解决方案**：
```python
# ❌ 错误：过于冗余
print(f"🔗 正在连接飞书多维表格...")
print(f"  ✅ 飞书多维表格连接成功")
print(f"📖 打开Excel文件...")
print(f"  ✅ Excel文件打开成功")

# ✅ 正确：精简输出
print(f"🔗 连接飞书多维表格...")
print(f"📖 打开Excel...")
print(f"✅ 读取到 {len(config_list)} 条配置")
```

---

## 快速排查表

### Excel相关

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `'NoneType' object has no attribute 'Close'` | 重复关闭Excel | 确保只关闭一次，使用try-finally |
| `被调用的对象已与其客户端断开连接` | Excel对象失效 | 不要重复打开/关闭，保持workbook对象引用 |
| `未找到工作表` | 表名不匹配 | 检查表名是否有空格、大小写 |
| `select_sheet_by_name 不存在` | API方法错误 | 使用`get_sheet_by_name()` |

### 飞书相关

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `NumberFieldConvFail` | 数字字段传入空字符串 | 空值字段不传输到飞书 |
| `未找到数据表` | 表名不匹配 | 使用表ID而非表名，或先获取表列表匹配 |
| `视图不存在` | 视图名称错误 | 默认视图名称是"表格"不是"默认视图" |
| `飞书指令不可用` | 扩展未加载 | 在可视化编辑器中拖入飞书指令再删除 |

### 影刀规范

| 问题 | 解决方案 |
|------|----------|
| `_block`报错 | 第一个元素改为模块名称 |
| 模块调用不便 | main用于测试，业务逻辑封装为独立函数 |
