---
name: yingdao-rpa
description: 影刀RPA平台的Python自动化开发技能。触发：用户提到影刀/xbot/自动化模块/excel网页/OCR，或要求开发新的影刀应用模块、开发xbot自动化脚本。必须激活此skill来处理影刀相关的代码开发任务。
version: 1.0.0
metadata:
  hermes:
    tags: [rpa, automation, yingdao, xbot, python]
    related_skills: []
---

# 影刀XBot RPA 开发技能

## 概述

影刀XBot是企业级RPA平台，提供Python API用于开发自动化脚本。此技能涵盖xbot核心API、代码模板和最佳实践。

**何时使用此技能：**
- 开发影刀xbot自动化流程脚本
- 使用xbot API进行网页自动化（xbot.web）
- Windows桌面应用自动化（xbot.win32）
- 移动端自动化（xbot.mobile）
- Excel/Word文档操作（xbot.excel、xbot.word）
- 数据库操作（xbot.ado）
- AI能力集成（xbot.ai - 阿里云/百度/腾讯）
- PDF文件处理（xbot.pdf）
- FTP文件传输（xbot.ftp）
- 飞书多维表格操作

## 代码模板规范

### 基础模板结构

影刀xbot模块必须遵循以下格式：

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

def main(args):
    # 在此编写自动化逻辑
    pass
```

**重要约束：**
- ❌ 不使用 `if __name__ == "__main__":`
- ✅ 必须使用 `def main(args):` 作为入口函数
- ✅ 必须导入 `xbot` 和 `package` 模块

## 核心API模块

### 1. package - 元素与资源管理

#### 元素选择器
```python
# 获取元素库中的元素
selector = package.selector('元素名称')

# 获取图像库中的图像
image_selector = package.image_selector('图像名称')
```

#### 资源文件操作
```python
# 读取文本资源
text = package.resources.get_text('data.txt', encoding='utf-8')

# 读取二进制资源
data = package.resources.get_bytes('image.png')

# 复制资源文件到本地
package.resources.copy_to('template.xlsx', 'D:\\output.xlsx')

# 添加资源文件到剪切板
package.resources.add_to_clipboard(['file1.txt', 'file2.xml'])
```

### 2. xbot.web - 网页自动化

#### 浏览器操作
```python
# 创建并打开网页
browser = xbot.web.create('https://example.com', mode='cef')

# 获取已打开的网页
browser = xbot.web.get(title='百度一下', url='baidu.com')
browser = xbot.web.get_active()  # 获取当前激活的网页

# 获取所有匹配的网页
browsers = xbot.web.get_all(url='example.com')

# 关闭所有网页
xbot.web.close_all()
```

#### 网页导航
```python
# 跳转
browser.navigate('https://newurl.com')

# 后退/前进
browser.go_back()
browser.go_forward()

# 刷新
browser.reload(ignore_cache=True)

# 获取信息
url = browser.get_url()
title = browser.get_title()
html = browser.get_html()
text = browser.get_text()
```

#### 元素操作
```python
# 查找元素
element = browser.find(package.selector('登录按钮'))
elements = browser.find_all_by_css('input[type="text"]')

# 元素交互
element.click(button='left', simulative=True)
element.input('username', simulative=True, append=False)
element.hover()

# 获取元素信息
text = element.get_text()
value = element.get_value()
attr = element.get_attribute('href')

# 下拉框操作
element.select('选项内容', mode='fuzzy')
element.select_by_index(0)
```

#### Cookie管理
```python
# 获取Cookie
cookies = xbot.web.get_cookies(mode='cef', domain='.example.com')

# 设置Cookie
xbot.web.set_cookie(
    url='https://example.com',
    name='session_id',
    value='abc123',
    expires=3600
)

# 移除Cookie
xbot.web.remove_cookie('https://example.com', 'session_id')
```

#### 对话框处理
```python
# 处理JavaScript对话框
browser.handle_javascript_dialog(dialog_result='ok', text='输入内容')

# 处理下载对话框
xbot.web.handle_save_dialog(
    file_folder='D:\\downloads',
    file_name='report.pdf'
)

# 处理上传对话框
xbot.web.handle_upload_dialog('D:\\files\\upload.pdf')
```

### 3. xbot.win32 - Windows桌面自动化

#### 窗口操作
```python
# 获取窗口
window = xbot.win32.get(title='记事本', class_name='Notepad')
window = xbot.win32.get_by_selector(package.selector('窗口元素'))

# 窗口控制
window.activate()  # 激活
window.set_state('maximize')  # 最大化/最小化/正常
window.move(x=100, y=100)  # 移动
window.resize(width=800, height=600)  # 调整大小
window.close()  # 关闭

# 等待窗口状态
window.wait_active(timeout=20)
window.wait_exists(timeout=20)
window.wait_close(timeout=20)
```

#### 元素操作
```python
# 查找元素
element = window.find(package.selector('按钮元素'))
elements = window.find_all(package.selector('列表项'))

# 元素交互
element.click(button='left', simulative=True)
element.input('输入内容')
element.check(mode='check')  # 复选框
element.select('选项')  # 下拉框
element.hover()

# 拖拽
element.drag_to(simulative=True, top=50, left=100, delay_after=1)
```

#### 鼠标键盘操作
```python
# 鼠标操作
xbot.win32.mouse_move(500, 300, move_speed='fast')
xbot.win32.mouse_click(button='left', click_type='click')
xbot.win32.mouse_wheel(wheel_direction='down', wheel_times=3)

# 键盘操作
xbot.win32.send_keys('Ctrl+C')
xbot.win32.send_keys('Hello World')

# 获取鼠标位置
pos = xbot.win32.get_mouse_position(relative_to='screen')
```

#### 图像识别
```python
# 等待图像出现
xbot.win32.Image.wait_appear(
    image_selectors=[package.image_selector('确认按钮')],
    timeout=20
)

# 点击图像
xbot.win32.Image.click(
    image_selectors=[package.image_selector('图标')],
    button='left'
)

# 图像悬停
xbot.win32.Image.hover([package.image_selector('菜单')])
```

#### 剪切板操作
```python
clipboard = xbot.win32.Clipboard

# 设置/获取文本
clipboard.set_text('复制的内容')
text = clipboard.get_text()

# 清空剪切板
clipboard.clear()

# 设置文件
clipboard.set_file(['D:\\file1.txt', 'D:\\file2.pdf'])
```

#### 截图操作
```python
# 屏幕截图
xbot.win32.Screenshot.save_screen_to_file(
    'D:\\screenshot.png',
    image_format='png'
)
xbot.win32.Screenshot.save_screen_to_clipboard()

# 窗口截图
xbot.win32.Screenshot.save_window_to_file(
    hwnd=window.handle,
    image_path='D:\\window.png',
    image_format='png'
)
```

### 4. xbot.excel - Excel操作

#### 工作簿操作
```python
# 创建Excel
workbook = xbot.excel.create(kind='office', visible=True)

# 打开Excel
workbook = xbot.excel.open('D:\\data.xlsx', kind='office', visible=True)

# 获取活动工作簿
workbook = xbot.excel.get_active_workbook(kind='office')

# 保存/另存
workbook.save()
workbook.save_as('D:\\output.xlsx')

# 关闭
workbook.close()
```

#### 工作表操作
```python
# 获取工作表
sheet = workbook.get_active_sheet()
sheet = workbook.get_sheet_by_name('Sheet1')
sheet = workbook.get_sheet_by_index(1)

# 创建工作表
workbook.create_sheet('新工作表', create_way='last')

# 激活工作表
workbook.active_sheet_by_name('Sheet1')

# 删除/复制/重命名
workbook.delete_sheet('旧工作表')
workbook.copy_sheet('源工作表', '目标工作表')
workbook.rename_sheet('旧名称', '新名称')
```

#### 单元格操作
```python
# 读取单元格
value = sheet.get_cell(1, 'A')  # 行号,列名
row = sheet.get_row(1)  # 获取整行
column = sheet.get_column('A')  # 获取整列
range_data = sheet.get_range(1, 'A', 5, 'C')  # 区域数据

# 写入单元格
sheet.set_cell(1, 'A', '标题')
sheet.set_row(1, ['A', 'B', 'C'], begin_column_name='A')
sheet.set_column('A', [1, 2, 3, 4], begin_row_num=1)
sheet.set_range(1, 'A', [[1, 2], [3, 4]])  # 二维数组

# 追加/插入行
sheet.append_row(['新', '数', '据'])
sheet.insert_row(3, ['插入', '数据'])

# 删除行列
sheet.remove_row(5)
sheet.remove_column('C')

# 清空
sheet.clear()
sheet.clear_range(1, 'A', 10, 'Z')
```

#### 其他功能
```python
# 获取行列数
row_count = sheet.get_row_count()
col_count = sheet.get_column_count()

# 获取第一个空闲行/列
free_row = sheet.get_first_free_row()
free_col = sheet.get_first_free_column()

# 选中区域
sheet.select_range(1, 'A', 10, 'C')

# 复制粘贴
sheet.copy_range(1, 'A', 5, 'C')
sheet.paste_range(1, 'D')
```

### 5. xbot.word - Word操作

#### 文档操作
```python
# 创建Word
doc = xbot.word.create(kind='office', visible=True)

# 打开Word
doc = xbot.word.open(
    'D:\\document.docx',
    kind='office',
    visible=True,
    open_password='',
    edit_password=''
)

# 保存/另存
doc.save()
doc.save_as('D:\\output.docx')

# 导出PDF
doc.export_to_pdf(
    'D:\\output.pdf',
    export_range=0,  # 0=全部, 1=当前页, 2=指定范围
    page_from=1,
    page_to=5
)

# 关闭
doc.close()
```

#### 内容操作
```python
# 获取选择区域
selection = doc.get_selection()

# 写入文本
selection.write_text('Hello World', newline=True)

# 读取文本
text = selection.read_text()

# 插入图片
selection.insert_picture(
    image_source='local',  # local/file_url/clipboard
    image_path='D:\\image.png',
    image_scale=100,  # 缩放百分比
    newline=True
)

# 插入超链接
doc.insert_hyperlink('点击这里', 'https://example.com')

# 插入表格
doc.insert_table(
    table_data=[['A', 'B'], ['1', '2']],
    table_data_format=None,
    grid=True,
    newline=True
)

# 替换文本
selection.replace_text(
    search_text='旧文本',
    replace_text='新文本',
    replace_all=True,
    case_sensitive=False
)

# 移动光标
selection.move_cursor(
    move_direction='right',  # left/right/up/down
    move_count=10,
    press_shift=False
)

# 定位光标
selection.locate_cursor_to_document('end_document')  # start_document/end_document
selection.locate_cursor_to_text('关键词')
doc.locate_cursor_to_bookmark('书签名')
```

### 6. xbot.mobile - 移动端自动化

#### 连接设备
```python
# Appium模式连接
mobile = xbot.mobile.connect(
    appium_url='http://127.0.0.1:4723/wd/hub',
    platform_name='Android',
    platform_version='11',
    device_name=' emulator-5554'
)

# 自定义名称连接
mobile = xbot.mobile.connect_by_custom_name('我的手机')

# 关闭连接
mobile.close()
```

#### 元素操作
```python
# 查找元素
element = mobile.find(package.selector('登录按钮'))
elements = mobile.find_all_by_id('com.app:id/button')
elements = mobile.find_all_by_xpath('//android.widget.Button')

# 元素交互
element.click()
element.input('输入内容')
element.longpress()
element.get_text()
element.get_attribute('text')

# 截图
element.screenshot('D:\\element.png', 'element_screenshot')
```

#### 屏幕操作
```python
# 点击/双击/长按
mobile.click(500, 300)
mobile.dblclick(500, 300)
mobile.longpress(500, 300)

# 滑动
mobile.swipe(
    start_point_x=100, start_point_y=500,
    end_point_x=100, end_point_y=100,
    swipe_time=800
)

# 系统操作
mobile.back()  # 返回
mobile.home()  # 主页
mobile.switchapp()  # 切换应用

# 屏幕方向
orientation = mobile.getoriention()
mobile.setoriention(0)  # 0=横屏, 1=竖屏

# 截图
mobile.screenshot('D:\\screen.png', filename='screenshot')
```

#### 剪切板操作
```python
# 设置/获取剪切板
mobile.set_clipboard_text('复制内容')
text = mobile.get_clipboard_text()
```

### 7. xbot.pdf - PDF操作

```python
# 提取文本
text = xbot.pdf.extract_text(
    path='D:\\document.pdf',
    from_page=1,
    to_page=10,
    password=None
)

# 提取图片
xbot.pdf.extract_images(
    path='D:\\document.pdf',
    from_page=1,
    to_page=5,
    save_to_dir='D:\\images',
    name_prefix='page'
)

# 提取页面
xbot.pdf.extract_pages(
    path='D:\\source.pdf',
    from_page=1,
    to_page=3,
    save_to='D:\\extracted.pdf'
)

# 合并PDF
xbot.pdf.merge_pdfs(
    paths=['file1.pdf', 'file2.pdf'],
    save_to='D:\\merged.pdf',
    passwords=None
)
```

### 8. xbot.ado - 数据库操作

```python
# 连接数据库
db = xbot.ado.Database
db.open('Driver={SQL Server};Server=localhost;Database=test;')

# 执行SQL
db.exec('SELECT * FROM users', timeout_seconds=20)
db.exec('UPDATE users SET name="test" WHERE id=1')

# 关闭连接
db.close()
```

### 9. xbot.ai - AI能力集成

```python
# 阿里云OCR
result = xbot.ai.AliyunAI.ocr_from_file('D:\\image.png')

# 百度OCR
result = xbot.ai.BaiduAI.ocr_from_file('D:\\image.png')

# 腾讯OCR
result = xbot.ai.TencentAI.ocr_from_file('D:\\image.png')
```

### 10. xbot.ftp - FTP操作

```python
# 连接FTP
ftp = xbot.ftp.connect(
    host='ftp.example.com',
    username='user',
    password='pass'
)

# 下载文件
ftp.download_file('D:\\local\\file.txt', 'remote/file.txt')
ftp.download_folder('D:\\local', 'remote/folder')

# 上传文件
ftp.upload_file('D:\\local\\file.txt', 'remote/')
ftp.upload_folder('D:\\local', 'remote/')

# 获取文件列表
files = ftp.get_ftp_files('remote/path')

# 断开连接
ftp.unlogin()
```

### 11. xbot.app - 数据表格与对话框

#### 数据表格操作
```python
# 获取数据表格
databook = xbot.app.databook

# 读取数据
row = databook.get_row(1)  # 获取指定行
cell = databook.get_cell(1, 'A')  # 获取单元格
range_data = databook.get_range(1, 'A', 10, 'C')  # 获取区域
row_count = databook.get_row_count()  # 获取行数

# 写入数据
databook.set_cell(1, 'A', '值')
databook.set_row(1, ['A', 'B', 'C'])
databook.set_column('A', [1, 2, 3])
databook.set_range(1, 'A', [[1, 2], [3, 4]])

# 追加/插入/删除行
databook.append_row(['新', '行'])
databook.insert_row(3, ['插入', '行'])
databook.remove_row(5)

# 清空
databook.clear()
```

#### 对话框操作
```python
# 消息对话框
xbot.app.dialog.show_alert('操作完成', title='提示')

# 确认对话框
result = xbot.app.dialog.show_confirm('确定要删除吗？', title='确认')

# 消息框
xbot.app.dialog.show_message_box(
    title='提示',
    message='操作成功',
    button='ok',
    timeout=5
)

# 数据表格对话框
xbot.app.dialog.show_workbook_dialog('数据确认', '请确认以下数据')

# 通知框
xbot.app.dialog.show_notifycation(
    message='任务完成',
    placement='rightbottom',
    level='info',
    timeout=3
)
```

### 12. xbot.xzip - 压缩解压

```python
# 压缩
xbot.xzip.zip(
    file_folder_path='D:\\source',
    zip_file_path='D:\\archive.zip',
    compress_level=5,  # 1-9
    password='secret'  # 可选
)

# 解压
xbot.xzip.unzip(
    zip_file_path='D:\\archive.zip',
    unzip_dir_path='D:\\extracted',
    password='secret'  # 可选
)
```

## 元素定位原则（重要）

**必须定位到用户可见的元素**，不能只分析form里的元素。

一个页面可能有多个功能相同的元素（如搜索按钮），要通过`display`状态筛选出用户实际看到的：
```javascript
// 分析所有可见元素
document.querySelectorAll("button, input[type='submit'], input[type='button']")
  .filter(el => window.getComputedStyle(el).display !== "none")
  .map(el => ({tag: el.tagName, id: el.id, display: window.getComputedStyle(el).display}))
```

#### 定位方式优先级
1. **影刀客户端捕获**：先录制元素，用选择器名称
2. **xpath定位**：支持绝对xpath和相对xpath
3. **混合定位+容错**：推荐写法

```python
# 混合定位示例
try:
    browser.find_by_xpath("//button[@id='chat-submit-button']").click()
except:
    try:
        browser.find_by_xpath("//input[@id='su']").click()
    except:
        browser.find('搜索按钮').click()
```

#### 常用xpath表达式
| 场景 | xpath表达式 |
|------|------------|
| 按id | `//input[@id='kw']` |
| 按name | `//input[@name='wd']` |
| 按button id | `//button[@id='chat-submit-button']` |
| 按value | `//input[@value='百度一下']` |
| 按class | `//input[@class='s_ipt']` |
| 按placeholder | `//input[@placeholder='搜索']` |
| 组合属性 | `//input[@id='kw' and @name='wd']` |

## 新建影刀模块

### 1. 创建 .py 模块文件
```python
# 使用提醒: ...
from xbot import print
from xbot import excel
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

## 飞书多维表格

**完整指令文档**：`./references/feishu_bitable.md`

调用方式概要：
- 通过 `xbot_visual.process.run(process="xbot_extensions.activity_feishu_bitable.指令名", ...)` 调用
- `package=__name__`，`outputs` 返回元组按声明顺序解构
- 共28个指令：数据表、视图、字段、记录、素材操作

## 通用功能

### 日志输出
```python
from xbot import print, sleep

# 输出日志
print('普通消息')
print('重要信息')

# 延迟
sleep(3)  # 延迟3秒
```

### 全局变量
```python
from .package import variables as glv

# 设置全局变量
glv.set('username', 'admin')

# 获取全局变量
username = glv.get('username')
```

## 资源说明

### references/
- `api_summary.md` - 完整API速查手册（覆盖所有xbot模块）
- `feishu_bitable.md` - 飞书多维表格28个指令详细文档
- `troubleshooting.md` - 11个实战问题解决方案（高频错误+修复方法）
- `sop.md` - 完整RPA开发SOP提示词

### assets/
- `default_module_template.py` - 影刀xbot标准模块模板

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

**参考文档**：`references/sop.md` - 完整SOP提示词

---

## 实战问题速查（11个高频问题）

| # | 问题 | 关键解决方案 |
|---|------|------------|
| 1 | Excel对象断开连接 | 资源只打开一次，try-finally关闭 |
| 2 | Excel API方法不存在 | 用`get_sheet_by_name()`而非`select_sheet_by_name()` |
| 3 | 模块入口设计不合理 | main用于测试，业务逻辑封装为独立函数 |
| 4 | 飞书扩展指令未加载 | 在可视化编辑器拖入飞书指令再删除 |
| 5 | 飞书默认视图名称错误 | 视图名用"表格"而非"默认视图" |
| 6 | _block参数模块名错误 | 第一个元素改为实际模块名称 |
| 7 | 飞书表名匹配失败 | 三重匹配策略：精确→去空格→去全角空格 |
| 8 | 飞书数字字段转换失败 | 空值字段不传输，不写key |
| 9 | 同一表数据未整合 | 按飞书表+Excel表+行范围分组，按行合并 |
| 10 | 批量删除效率低 | 批量删除每次500条，不用逐条 |
| 11 | 日志输出过于冗余 | 精简输出，只保留关键步骤 |

**详细解决方案**：`references/troubleshooting.md`

---

## 注意事项

1. **入口函数规范**：必须使用`def main(args):`，不能使用`if __name__ == "__main__":`
2. **模块导入**：必须导入`xbot`、`print`、`sleep`、`package`和`glv`
3. **元素选择**：使用`package.selector()`获取元素库中的元素
4. **图像识别**：使用`package.image_selector()`获取图像库中的图像
5. **异常处理**：建议添加适当的异常处理逻辑
6. **资源释放**：使用完毕后记得关闭工作簿/浏览器等资源
7. **使用文档中的API**：使用技能文档里的指令代码，不要自己编造方法名称