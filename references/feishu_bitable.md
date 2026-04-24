# 飞书多维表格（Bitable）指令手册

> 基于 `xbot_extensions.activity_feishu_bitable` 扩展包，共28个指令  
> 调用方式：`xbot_visual.process.run(process="xbot_extensions.activity_feishu_bitable.指令名", package=__name__, inputs={...}, outputs=[...], _block=(...))`

---

## 调用规范

| 参数 | 说明 |
|------|------|
| `process` | `xbot_extensions.activity_feishu_bitable.指令名` |
| `package` | 固定 `__name__` |
| `outputs` | 返回元组，按声明顺序解构 |
| `_block` | `("实际模块名称", 步骤序号, "步骤描述")` |

**重要**：
- ❌ `_block` 第一个元素不要写死为 `"main"`，应改为实际模块名称
- ✅ 例如：`_block=("飞书多维表格同步模块", 1, "建立连接")`
- 飞书扩展指令使用前需先在可视化编辑器拖入飞书指令再删除，触发加载
- ⚠️ 飞书默认视图名称是 `"表格"`，不是 `"默认视图"`

---

## 1. create_instance — 建立连接

建立与飞书多维表格的连接，返回 Bitable 实例。

**inputs**

| 参数 | 类型 | 说明 |
|------|------|------|
| `app_id` | str | 飞书应用 ID (cli_xxx) |
| `app_secret` | str | 飞书应用密钥 |
| `bitable` | str | 多维表格链接或 token |
| `host` | str | 主机地址，空值默认 open.feishu.cn |
| `apikey` | str | API Key（可选） |
| `is_tenant` | bool | 是否 tenant 模式，默认 True |
| `is_wiki` | bool | 是否知识库多维表格，默认 False |

**outputs**: `bitable_instance`

```python
bitable_instance = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.create_instance",
    package=__name__,
    inputs={
        "app_id": "cli_xxx",
        "app_secret": "飞书应用密钥",
        "bitable": "多维表格token",
        "host": "",
        "apikey": "",
        "is_tenant": True,
        "is_wiki": False
    },
    outputs=["bitable_instance"],
    _block=("模块名", 1, "建立多维表格连接")
)
```

---

## 2. get_tables — 获取数据表

**inputs**: `bitable_instance`

**outputs**: `tables_id, tables_name, tables_info`

```python
tables_id, tables_name, tables_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_tables",
    package=__name__,
    inputs={"bitable_instance": bitable_instance},
    outputs=["tables_id", "tables_name", "tables_info"],
    _block=("模块名", 2, "列出数据表")
)
```

---

## 3. add_table — 新增数据表

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `name` | 数据表名称 |
| `default_view_name` | 默认视图名称（可选） |

**outputs**: `table_id, table_info`

```python
table_id, table_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.add_table",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "name": "新数据表",
        "default_view_name": ""
    },
    outputs=["table_id", "table_info"],
    _block=("模块名", 3, "添加数据表")
)
```

---

## 4. delete_table — 删除数据表

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.delete_table",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名"
    },
    outputs=[],
    _block=("模块名", 4, "删除数据表")
)
```

---

## 5. update_table — 更新数据表

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `new_name` | 新名称 |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.update_table",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "new_name": "新表名"
    },
    outputs=[],
    _block=("模块名", 5, "更新数据表")
)
```

---

## 6. get_views — 获取视图

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_identity_kind` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |

**outputs**: `views_id, views_name, views_info`

```python
views_id, views_name, views_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_views",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_identity_kind": "NAME",
        "table_identity": "表名"
    },
    outputs=["views_id", "views_name", "views_info"],
    _block=("模块名", 6, "列出视图")
)
```

---

## 7. add_view — 新增视图

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_kind` | 视图类型：`GRID`/`KANBAN`/`GALLERY`/`GANTT`/`FORM` |
| `view_name` | 视图名称 |

**outputs**: `view_id, view_info`

```python
view_id, view_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.add_view",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "view_kind": "GRID",
        "view_name": "新视图"
    },
    outputs=["view_id", "view_info"],
    _block=("模块名", 7, "添加视图")
)
```

---

## 8. delete_view — 删除视图

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_identity_kind` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_identity_kind` | `NAME` 或 `ID` |
| `view_identity` | 视图名或视图ID |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.delete_view",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_identity_kind": "NAME",
        "table_identity": "表名",
        "view_identity_kind": "NAME",
        "view_identity": "视图名"
    },
    outputs=[],
    _block=("模块名", 8, "删除视图")
)
```

---

## 9. update_view — 更新视图

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_identity_kind` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_identity_kind` | `NAME` 或 `ID` |
| `view_identity` | 视图名或视图ID |
| `new_view_name` | 新视图名称 |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.update_view",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_identity_kind": "NAME",
        "table_identity": "表名",
        "view_identity_kind": "NAME",
        "view_identity": "视图名",
        "new_view_name": "新视图名"
    },
    outputs=[],
    _block=("模块名", 9, "更新视图")
)
```

---

## 10. get_fields — 获取字段

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |

**outputs**: `fields_info, fields_name, fields_id`

```python
fields_info, fields_name, fields_id = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_fields",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名"
    },
    outputs=["fields_info", "fields_name", "fields_id"],
    _block=("模块名", 10, "列出字段")
)
```

---

## 11. add_fields — 新增字段

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `field_name` | 字段名称 |
| `field_type` | 字段类型（1=文本，2=数字等） |
| `field_description` | 字段描述 |
| `property_dict` | 属性字典，可为空 `{}` |

**outputs**: `field_id`

```python
field_id = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.add_fields",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "field_name": "新字段",
        "field_type": "1",
        "field_description": "字段描述",
        "property_dict": {}
    },
    outputs=["field_id"],
    _block=("模块名", 11, "添加字段")
)
```

---

## 12. update_fields — 更新字段

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `field_kind_identity` | `NAME` 或 `ID` |
| `field_identity` | 字段名或字段ID |
| `new_field_name` | 新字段名称 |
| `new_field_type` | 新字段类型 |
| `new_field_description` | 新字段描述 |
| `property_dict` | 属性字典（字符串或字典） |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.update_fields",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "field_kind_identity": "NAME",
        "field_identity": "字段名",
        "new_field_name": "新字段名",
        "new_field_type": "1",
        "new_field_description": "新描述",
        "property_dict": ""
    },
    outputs=[],
    _block=("模块名", 12, "更新字段")
)
```

---

## 13. delete_fields — 删除字段

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `field_kind_identity` | `NAME` 或 `ID` |
| `field_identity` | 字段名或字段ID |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.delete_fields",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "field_kind_identity": "NAME",
        "field_identity": "字段名"
    },
    outputs=[],
    _block=("模块名", 13, "删除字段")
)
```

---

## 14. get_records_by_view — 获取记录（按视图）

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_kind_identity` | `NAME` 或 `ID` |
| `view_identity` | 视图名或视图ID |
| `count` | 返回数量，-1 表示全部 |

**outputs**: `records_id, records_info`

```python
records_id, records_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_records_by_view",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "view_kind_identity": "NAME",
        "view_identity": "视图名",
        "count": -1
    },
    outputs=["records_id", "records_info"],
    _block=("模块名", 14, "列出记录(视图)")
)
```

---

## 15. get_records_by_view_v2 — 获取记录v2（高级查询）

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_kind_identity` | `NAME` 或 `ID` |
| `view_identity` | 视图名或视图ID |
| `filter_info` | 筛选条件字典，可为空 `{}` |

**outputs**: `records_id, records_info`

```python
records_id, records_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_records_by_view_v2",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "view_kind_identity": "NAME",
        "view_identity": "视图名",
        "filter_info": {}
    },
    outputs=["records_id", "records_info"],
    _block=("模块名", 15, "查询记录(视图)")
)
```

---

## 16. get_record_by_id — 按ID获取记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `record_id` | 记录ID |

**outputs**: `record_info`

```python
record_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_record_by_id",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "record_id": "记录ID"
    },
    outputs=["record_info"],
    _block=("模块名", 16, "检索记录")
)
```

---

## 17. get_record_by_filter — 筛选获取记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `view_kind_identity` | `NAME` 或 `ID` |
| `view_identity` | 视图名或视图ID |
| `filter_formula` | 筛选公式 |
| `field_names` | 字段名称列表 |

**outputs**: `records_info, records_id`

```python
records_info, records_id = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.get_record_by_filter",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "view_kind_identity": "NAME",
        "view_identity": "视图名",
        "filter_formula": 'CurrentValue.[日期] = TODATE("2025-1-1")',
        "field_names": ""
    },
    outputs=["records_info", "records_id"],
    _block=("模块名", 17, "列出记录(筛选)")
)
```

---

## 18. add_record — 新增记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `payload` | 字段值字典 `{"字段名": "值"}` |

**outputs**: `record_id`

```python
record_id = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.add_record",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "payload": {"字段名": "值"}
    },
    outputs=["record_id"],
    _block=("模块名", 18, "添加记录")
)
```

---

## 19. add_records — 批量新增记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `payload` | 记录列表 `[{"字段名": "值"}, ...]` |

**outputs**: `record_id`（批量返回时为列表）

```python
record_id = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.add_records",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "payload": [{"字段名": "值1"}, {"字段名": "值2"}]
    },
    outputs=["record_id"],
    _block=("模块名", 19, "批量添加记录")
)
```

---

## 20. update_record — 更新记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `record_id` | 记录ID |
| `payload` | 字段值字典 `{"字段名": "新值"}` |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.update_record",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "record_id": record_id,
        "payload": {"字段名": "新值"}
    },
    outputs=[],
    _block=("模块名", 20, "更新记录")
)
```

---

## 21. delete_record — 删除记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `record_id` | 记录ID |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.delete_record",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "record_id": record_id
    },
    outputs=[],
    _block=("模块名", 21, "删除记录")
)
```

---

## 22. batch_delete_record — 批量删除记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `record_ids` | 记录ID列表 `[]` |

**outputs**: 无

```python
xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.batch_delete_record",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "record_ids": ["记录ID1", "记录ID2"]
    },
    outputs=[],
    _block=("模块名", 22, "批量删除记录")
)
```

---

## 23. batch_get_record — 批量获取记录

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `table_kind_identity` | `NAME` 或 `ID` |
| `table_identity` | 表名或表ID |
| `record_ids` | 记录ID列表 |
| `user_id_type` | 用户ID类型，默认 `user_id` |
| `automatic_fields` | 是否获取自动字段，默认 False |
| `with_shared_url` | 是否获取共享链接，默认 False |

**outputs**: `record_info`

```python
record_info = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.batch_get_record",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "table_kind_identity": "NAME",
        "table_identity": "表名",
        "record_ids": ["ID1", "ID2"],
        "user_id_type": "user_id",
        "automatic_fields": False,
        "with_shared_url": False
    },
    outputs=["record_info"],
    _block=("模块名", 23, "批量获取记录")
)
```

---

## 24. download_media — 下载素材

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例 |
| `file_token` | 文件token |
| `save_dir` | 保存目录 |
| `extra` | 额外参数（可选） |

**outputs**: `file_path`

```python
file_path = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.download_media",
    package=__name__,
    inputs={
        "bitable_instance": bitable_instance,
        "file_token": "文件token",
        "save_dir": "C:\\Users\\Downloads",
        "extra": ""
    },
    outputs=["file_path"],
    _block=("模块名", 24, "下载素材")
)
```

---

## 25. upload_media — 上传素材

**inputs**

| 参数 | 说明 |
|------|------|
| `bitable_instance` | Bitable 实例（可为 None） |
| `file_path` | 本地文件路径 |
| `parent_type` | 父节点类型：`bitable_image` 或 `bitable_file` |

**outputs**: `file_token`

```python
file_token = xbot_visual.process.run(
    process="xbot_extensions.activity_feishu_bitable.upload_media",
    package=__name__,
    inputs={
        "bitable_instance": None,
        "file_path": "C:\\Users\\test.png",
        "parent_type": "bitable_image"
    },
    outputs=["file_token"],
    _block=("模块名", 25, "上传素材")
)
```

---

## 26. get_meta_info — 获取元信息

**inputs**: `bitable_instance`

**outputs**: 根据实际返回而定

---

## 27. update_meta_info — 更新元信息

**inputs**: 根据实际返回而定

**outputs**: 根据实际返回而定

---

## 28. get_wiki_token — 知识库Token转换

将知识库多维表格的token转换为普通token。

**inputs**: `bitable_instance`

**outputs**: 根据实际返回而定

---

## 字段类型参考

| type值 | 类型 |
|-------|------|
| 1 | 文本 |
| 2 | 数字 |
| 3 | 单选 |
| 4 | 多选 |
| 5 | 日期 |
| 7 | 复选框 |
| 11 | 人员 |
| 13 | 附件 |
| 15 | 链接 |
| 17 | 公式 |

## 视图类型参考

| view_kind | 说明 |
|-----------|------|
| `GRID` | 表格视图 |
| `KANBAN` | 看板视图 |
| `GALLERY` | 画册视图 |
| `GANTT` | 甘特视图 |
| `FORM` | 表单视图 |
