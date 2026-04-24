# 编码版指南

## 模块模板（正确结构）

```python
# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
import xbot_visual
from xbot import print, sleep
from . import package
from .package import variables as glv


def main_business_logic(param1, param2):
    """主要业务逻辑，独立参数便于调用"""
    # 使用glv获取workspace路径
    file_path = glv['workspace'] + '\\' + param1

    # 打开资源（只打开一次）
    resource = xbot.xxx.open(file_path)
    try:
        # 业务逻辑
        ...
    finally:
        resource.close()


def main(args):
    """模块入口函数（用于单元测试）"""
    return main_business_logic(
        args.get("param1", ""),
        args.get("param2", "")
    )
```

**重要约束**：
- ❌ 不使用 `if __name__ == "__main__":`
- ✅ 必须使用 `def main(args):` 作为入口函数
- ✅ 必须导入 `xbot` 和 `package` 模块

## 调用模块（可视化流程）

```python
import xbot_visual

invoke_result = xbot_visual.process.invoke_module(
    module="my_module",
    package=__name__,
    function="my_function",
    params={"key": "value"},
    _block=("main", 1, "步骤名")
)
```

## 调用函数

```python
from . import target_module

result = target_module.get_mean_std(data_list)
```

## 安装第三方库

在「Python包管理」界面安装，或在代码中：

```python
import subprocess
subprocess.run(["pip", "install", "numpy"])
```

## 流程参数

```python
def process_data(web_page):
    text = web_page.find("元素").get_text()
    return text
```

## 实用代码模式

### 重试机制

```python
_xbot_retry_time = 0
while _xbot_retry_time <= 3:
    try:
        web_page = xbot_visual.web.get(title="百度")
        _xbot_retry_time = 5
    except Exception as e:
        if _xbot_retry_time == 3:
            raise e
        xbot_visual.programing.log(type='info', text=str(e))
        _xbot_retry_time += 1
        import time
        time.sleep(3)
```

### 异常追踪

```python
try:
    # 业务逻辑
    element.click()
except Exception as e:
    e = xbot_visual.trace(e)
    xbot_visual.programing.log(type="error", text=str(e))
```

### 列表处理

```python
# 分割文本为列表
数据列表 = xbot_visual.text.split_text_to_list(
    text_to_split=原始文本,
    delimiter_way="standard",
    standard_delimiter="new_line"
)

# 遍历列表
for loop_item_index, loop_item in enumerate(
    xbot_visual.workflow.list_iterator(list=数据列表, start_index=0, loop_count=0)
):
    # 处理每一项
    pass
```

### 日期时间处理

```python
# 日期加减
datetime_instance, _ = xbot_visual.datetime.add(
    datetime=None,
    timeway="decrease",  # decrease=减少, add=增加
    duration="1",
    unit="day"  # day/hour/minute/second
)

# 格式化日期
text = xbot_visual.datetime.to_string(
    datetime=datetime_instance,
    format="%Y/%m/%d"  # 或 "%Y-%m-%d %H:%M:%S"
)
```

### 条件判断

```python
if xbot_visual.workflow.multiconditional_judgment(
    relation="and",  # and/or
    conditionals=[
        {"operand1": "状态", "operator": "==", "operand2": "完成"},
        {"operand1": "时间", "operator": "<=", "operand2": "10"}
    ]
):
    # 执行操作
    pass
```

### 文件对话框

```python
# 选择文件
select_file_dialog = xbot_visual.dialog.show_select_file_dialog(
    title="选择文件",
    file_filter="Excel文件(*.xlsx)",
    initial_directory=""
)

# 保存文件对话框
save_file_dialog = xbot_visual.dialog.show_save_file_dialog(
    title="保存文件",
    file_filter="Excel文件(*.xlsx)",
    default_file_name="导出.xlsx",
    initial_directory=""
)
```

### 日志输出

```python
# 在编码模块中使用
from xbot import print
print("步骤1. 开始处理...")

# 在可视化流程中使用xbot_visual
xbot_visual.programing.log(type='info', text='这是一条日志')
xbot_visual.programing.log(type='error', text='这是一条错误日志')
```

### 睡眠/等待

```python
# 方式1：xbot sleep
from xbot import sleep
sleep(2)  # 秒

# 方式2：xbot_visual
xbot_visual.programing.sleep(seconds=2)
```

### 调用子流程

```python
# 调用子流程
xbot_visual.process.run(
    process="process_name",
    package="__name__"
)

# 等待流程完成
xbot_visual.process.wait_for_process(process_name="子流程名称")
```
