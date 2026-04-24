---
name: yingdao-rpa
description: 影刀RPA平台的Python自动化开发技能。触发：用户提到影刀/xbot/自动化模块/excel网页/OCR，或要求开发新的影刀应用模块、开发xbot自动化脚本。必须激活此skill来处理影刀相关的代码开发任务。
version: 1.1.0
metadata:
  hermes:
    tags: [rpa, automation, yingdao, xbot, python]
    related_skills: []
---

# 影刀XBot RPA 开发技能

## 概述

影刀XBot是企业级RPA平台，提供Python API用于开发自动化脚本。

**何时使用此技能：**
- 开发影刀xbot自动化流程脚本
- 使用xbot API进行网页自动化（xbot.web）
- Windows桌面应用自动化（xbot.win32）
- Excel/Word文档操作（xbot.excel、xbot.word）
- 数据库操作（xbot.ado）、FTP、PDF等
- AI能力集成（OCR）、飞书多维表格操作

**所有API指令索引**：`references/_index.md`（含完整指令列表和说明）

---

## RPA开发SOP工作流

开发影刀RPA必须遵循"需求沟通 → 流程设计 → 程序开发"三步SOP。每步必须等用户确认后才能进入下一步。

### 第一步：需求沟通
- 主动提问：触发条件、分支逻辑、数据来源与去向、异常处理、权限与环境、业务规则确认
- 输出需求文档，明确请求用户确认

### 第二步：流程设计
- 提供Mermaid格式流程图 + 缩进式文本流程图
- 标注开始/结束、主流程、判断节点、异常处理、回滚节点
- 等用户确认后再开发

### 第三步：程序开发
- 严格使用xbot指令集，不用伪代码
- 日志精简，只记录关键步骤
- 异常处理用捕获异常块+重试
- 配置参数外置
- 输出代码 + 用户操作说明（含常见问题表）

**参考文档**：`references/sop.md`

---

## 常用API（高频指令）

完整指令清单见 `references/_index.md`，详细用法见对应reference文件。

### package - 元素与资源管理

```python
# 获取元素选择器
selector = package.selector('元素名称')

# 读取资源文件
text = package.resources.get_text('data.txt', encoding='utf-8')
package.resources.copy_to('template.xlsx', 'D:\\output.xlsx')
```

### xbot.web - 网页自动化

```python
browser = xbot.web.create('https://example.com', mode='cef')
browser = xbot.web.get(title='标题', url='baidu.com')

element = browser.find(package.selector('登录按钮'))
element.click()
element.input('内容', simulative=True)

browser.navigate('https://newurl.com')
```

### xbot.excel - Excel操作

```python
workbook = xbot.excel.open('D:\\data.xlsx', kind='office', visible=True)
sheet = workbook.get_sheet_by_name('Sheet1')

value = sheet.get_cell(1, 'A')
sheet.set_cell(1, 'A', '值')
sheet.set_range(1, 'A', [[1, 2], [3, 4]])  # 二维数组

workbook.save()
workbook.close()
```

### xbot.win32 - Windows桌面自动化

```python
window = xbot.win32.get(title='记事本', class_name='Notepad')
window.activate()
window.set_state('maximize')

element = window.find(package.selector('按钮'))
element.click()

xbot.win32.send_keys('Ctrl+C')
```

### xbot.word - Word操作

```python
doc = xbot.word.open('D:\\doc.docx', kind='office', visible=True)
selection = doc.get_selection()
selection.write_text('内容', newline=True)
doc.save()
doc.close()
```

### xbot.app.dialog - 对话框

```python
xbot.app.dialog.show_alert('完成', title='提示')
result = xbot.app.dialog.show_confirm('确定？', title='确认')
xbot.app.dialog.show_notifycation('任务完成', level='info')
```

---

## 元素定位原则

**必须定位到用户可见的元素**。

```python
# 混合定位（推荐）
try:
    browser.find_by_xpath("//button[@id='submit']").click()
except:
    browser.find(package.selector('提交按钮')).click()
```

常用xpath：
| 场景 | xpath |
|------|-------|
| 按id | `//input[@id='kw']` |
| 按name | `//input[@name='wd']` |
| 按value | `//input[@value='搜索']` |
| 组合 | `//input[@id='kw' and @name='wd']` |

---

## 新建影刀模块

### 1. 创建 .py 模块文件

```python
# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from . import package
from .package import variables as glv

def my_function():
    print("执行任务")
    # 业务逻辑
    pass

def main(args):
    my_function()
```

### 2. 更新 .dev/main.flow.json（追加到 blocks 数组）
```json
{
  "id": "新UUID",
  "name": "process.invoke_module",
  "isEnabled": true,
  "inputs": {
    "module": { "value": "10:my_module", "display": "my_module" },
    "function": { "value": "10:my_function" },
    "params": { "value": "16:[]" },
    "returnType": { "value": "10:any" }
  },
  "outputs": {
    "invoke_result": { "name": "invoke_result", "type": "any", "isEnable": true }
  }
}
```

### 3. 更新 package.json（追加到 flows 数组）
```json
{
  "name": "my_module",
  "filename": "my_module",
  "kind": "Code",
  "opened": false,
  "groupName": null,
  "enableCopilot": false
}
```

### 代码中调用模块
```python
import xbot_visual

invoke_result = xbot_visual.process.invoke_module(
    module="my_module",
    package=__name__,
    function="my_function",
    params={},
    _block=("main", 1, "步骤名称")
)
```

---

## 飞书多维表格

**完整指令文档**：`references/feishu_bitable.md`

调用方式：
- 通过 `xbot_visual.process.run(process="xbot_extensions.activity_feishu_bitable.指令名", ...)` 调用
- `package=__name__`，`outputs` 返回元组按声明顺序解构

---

## 通用功能

```python
from xbot import print, sleep

print('日志输出')
sleep(3)  # 延迟3秒

from .package import variables as glv
glv.set('key', 'value')
val = glv.get('key')
```

---

## 实战问题速查

| # | 问题 | 关键解决方案 |
|---|------|------------|
| 1 | Excel对象断开连接 | 资源只打开一次，try-finally关闭 |
| 2 | Excel API方法不存在 | 用`get_sheet_by_name()`而非`select_sheet_by_name()` |
| 3 | 模块入口设计不合理 | main用于测试，业务逻辑封装为独立函数 |
| 4 | 飞书扩展指令未加载 | 在可视化编辑器拖入飞书指令再删除 |
| 5 | 飞书默认视图名称错误 | 视图名用"表格"而非"默认视图" |
| 6 | 飞书表名匹配失败 | 三重匹配策略：精确→去空格→去全角空格 |
| 7 | 批量删除效率低 | 批量删除每次500条，不用逐条 |

**详细解决方案**：`references/troubleshooting.md`

---

## 注意事项

1. **入口函数**：必须使用`def main(args):`，不能用`if __name__ == "__main__":`
2. **必须导入**：`xbot`、`print`、`sleep`、`package`
3. **元素选择**：用`package.selector()`，不要硬编码
4. **资源释放**：用完记得`workbook.close()`、`browser.quit()`
5. **查指令**：完整清单在`references/_index.md`，详细用法在对应reference文件
