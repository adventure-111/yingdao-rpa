# XBot API 速查手册

## 目录
- [package](#package)
- [xbot.ado](#xbotado)
- [xbot.ai](#xbotai)
- [xbot.app](#xbotapp)
- [xbot.excel](#xbotexcel)
- [xbot.ftp](#xbotftp)
- [xbot.mobile](#xbotmobile)
- [xbot.pdf](#xbotpdf)
- [xbot.web](#xbotweb)
- [xbot.win32](#xbotwin32)
- [xbot.word](#xbotword)
- [xbot.xzip](#xbotxzip)

## package

### selector()
根据元素名称返回元素选择器对象
```python
def selector(name)
```
**参数:**
- name: 选择器名称，即元素库中元素的名称

### image_selector()
根据图像库中图像元素的名称返回图像选择器对象
```python
def image_selector(name)
```
**参数:**
- name: 图像选择器名称，即图像库中图像元素的名称

### resources.get_text()
获取资源文件的文本内容
```python
def get_text(self, filename, encoding='utf-8')
```
**参数:**
- filename: 资源文件名
- encoding: 读取文件时的编码格式，默认为'utf-8'

### resources.get_bytes()
获取资源文件的二进制信息
```python
get_bytes(self, filename)
```
**参数:**
- filename: 资源文件名

### resources.copy_to()
将资源文件的内容拷贝到目标文件中
```python
copy_to(self, filename, dest_filename)
```
**参数:**
- filename: 资源文件名
- dest_filename: 资源文件内容最终拷贝到的位置（为文件绝对路径）

### resources.add_to_clipboard()
将资源文件添加到剪切板
```python
add_to_clipboard(self, filenames)
```
**参数:**
- filenames: 资源文件名列表

## xbot.ado

### Database.open()
连接数据库
```python
open(self, conn_str)
```
**参数:**
- conn_str: 数据库连接字符串

### Database.exec()
执行SQL语句
```python
exec(self, sql, timeout_seconds=20)
```
**参数:**
- sql: SQL语句
- timeout_seconds: SQL语句执行超时时间，默认超时时间为20s

### Database.close()
关闭数据库连接
```python
close(self)
```

## xbot.ai

### AliyunAI.ocr_from_file()
识别文件内容
```python
ocr_from_file(self, image_path)
```
**参数:**
- image_path: 识别文件的路径

### BaiduAI.ocr_from_file()
识别文件内容
```python
ocr_from_file(self, image_path)
```
**参数:**
- image_path: 识别文件的路径

### TencentAI.ocr_from_file()
识别文件内容
```python
ocr_from_file(self, image_path)
```
**参数:**
- image_path: 识别文件的路径

## xbot.app

### databook.get_row()
获取数据表格指定行内容
```python
get_row(row_num)
```
**参数:**
- row_num: 指定行号，行号从1开始

### databook.set_row()
向数据表格指定列写入行内容
```python
set_row(row_num, values, begin_column_name = 'A')
```
**参数:**
- row_num: 要设置的数据表格行号，行号从1开始
- values: 要设置的值，必须是一个字符列表类型
- begin_column_name: 要写入数据的起始列名，默认值为"A"

### databook.append_row()
在数据表格追加一行内容
```python
append_row(values, begin_column_name = 'A')
```
**参数:**
- values: 要设置的值, 必须是一个列表类型
- begin_column_name: 设置开始的单元格列名，默认值为"A"

### databook.insert_row()
往数据表格中插入一行内容
```python
insert_row(row_num, values, begin_column_name = 'A')
```
**参数:**
- row_num: 插入位置的行号，行号从1开始
- values: 要设置的值，必须是一个列表类型
- begin_column_name: 起始开始的单元格列名，默认值为"A"

### databook.remove_row()
删除数据表格指定行内容
```python
remove_row(row_num)
```
**参数:**
- row_num: 要移除的行号

### databook.get_cell()
获取数据表格指定单元格内容
```python
get_cell(row_num, col_name)
```
**参数:**
- row_num: 指定单元格的行号
- col_name: 指定单元格的列名

### databook.set_cell()
在数据表格指定单元格写入内容
```python
set_cell(row_num, col_name, value)
```
**参数:**
- row_num: 单元格行号
- col_name: 单元格列名
- value: 要写入到单元格中的内容

### databook.set_column()
在数据表格指定列中写入内容
```python
set_column(col_name, values, begin_row_num = 1)
```
**参数:**
- col_name: 列名，指要写入内容的列位置
- values: 写入的值, 必须是一个列表类型
- begin_row_num: 写入列内容的起始行号，默认行号为1

### databook.clear()
清空数据表格内容
```python
clear()
```

### databook.get_row_count()
获取数据表格的总行数
```python
get_row_count()
```

### databook.get_range()
获取数据表格指定区域的内容
```python
get_range(area_begin_row_num, area_begin_column_name, area_end_row_num, area_end_column_name)
```
**参数:**
- area_begin_row_num: 起始单元格行号，行号从1开始
- area_begin_column_name: 起始单元格列名，列名从A开始
- area_end_row_num: 结束单元格行号, 行号从1开始
- area_end_column_name: 结束单元格列名，列名从A开始

### databook.set_range()
向数据表格指定区域写入内容
```python
set_range(row_num, col_name, values)
```
**参数:**
- row_num: 写入区域内容的起始行号，行号从1开始
- col_name: 写入区域内容的起始列名，列名从A开始
- values: 要设置的内容，必须是一个二维数组

### dialog.show_alert()
打开消息对话框
```python
show_alert(message, title='提示')
```
**参数:**
- message: 需要在消息对话框中展示的内容
- title: 消息对话框标题，默认为"提示"

### dialog.show_confirm()
打开确认对话框
```python
show_confirm(message, title='请确认')
```
**参数:**
- message: 需要在确认对话框中展示的内容
- title: 确认对话框标题，默认为"请确认"

### dialog.show_custom_dialog()
打开自定义对话框
```python
show_custom_dialog(settings)
```
**参数:**
- settings: 自定义对话框配置json串

### dialog.show_message_box()
打开消息对话框
```python
show_message_box(title, message, button='ok', *, timeout=-1, default_button=None)
```
**参数:**
- title: 消息对话框标题
- message: 消息对话框要展示的信息
- button: 消息对话框中的按钮
- timeout: 对话框等待点击超时时间
- default_button: 超时时默认点击的按钮

### dialog.show_workbook_dialog()
打开数据表格对话框
```python
show_workbook_dialog(title, message)
```
**参数:**
- title: 数据表格对话框标题
- message: 数据表格对话框提示信息

### dialog.show_notifycation()
打开消息通知框
```python
show_notifycation(message, placement='rightbottom' , level='info', timeout=3)
```
**参数:**
- message: 消息通知框的通知内容
- placement: 通知消息在屏幕上的显示位置，默认为"rightbottom"
- level: 通知消息的消息级别，默认为"info"
- timeout: 通知消息框显示时长，默认为3秒

## xbot.excel

### create()
创建并返回excel对象
```python
create(kind='office', visible=True)
```
**参数:**
- kind: 创建方式，可选'office'、'wps'、'openpyxl'或'auto_check'
- visible: 用于控制自动化操作是否用户级可见

### open()
打开excel文件并返回excel对象
```python
open(file_name, kind='office', visible=True)
```
**参数:**
- file_name: excel文件路径
- kind: 打开方式，可选'office'、'wps'、'openpyxl'或'auto_check'
- visible: 用于控制自动化操作是否用户级可见

### get_active_workbook()
获取当前激活的excel
```python
get_active_workbook(kind)
```
**参数:**
- kind: 打开方式，可选'office'、'wps'、'openpyxl'或'auto_check'

### WorkBook.get_active_sheet()
获取工作簿中激活的sheet页
```python
get_active_sheet(self)
```

### WorkBook.get_sheet_by_index()
获取工作簿中指定位置的sheet页
```python
get_sheet_by_index(self, index)
```
**参数:**
- index: 目标sheet页在工作簿中的索引位置，从1开始计数

### WorkBook.get_sheet_by_name()
获取工作簿中指定名称的sheet页
```python
get_sheet_by_name(self, name)
```
**参数:**
- name: 目标sheet页的名称

### WorkBook.create_sheet()
在工作簿中创建新的sheet页
```python
create_sheet(self, name, create_way)
```
**参数:**
- name: sheet页名称
- create_way: 添加方式，可选择'first'或'last'

### WorkBook.active_sheet_by_index()
激活工作簿中指定位置的sheet页
```python
active_sheet_by_index(self, index)
```
**参数:**
- index: 目标sheet页在工作簿中的索引位置，从1开始计数

### WorkBook.active_sheet_by_name()
激活工作簿中指定名称的sheet页
```python
active_sheet_by_name(self, name)
```
**参数:**
- name: 目标sheet页的名称

### WorkBook.save()
将工作簿保存为excel文件
```python
save(self)
```

### WorkBook.save_as()
将工作簿另存为excel文件
```python
save_as(self, filename)
```
**参数:**
- filename: 另存为路径

### WorkBook.close()
关闭工作簿
```python
close(self)
```

### WorkBook.execute_macro()
执行宏
```python
execute_macro(self, macro)
```
**参数:**
- macro: 宏名称

### WorkBook.get_all_sheets()
获取所有的Sheet页
```python
get_all_sheets(self)
```

### WorkBook.delete_sheet()
删除Sheet页
```python
delete_sheet(self, name)
```
**参数:**
- name: Sheet页名称

### WorkBook.copy_sheet()
拷贝Sheet页
```python
copy_sheet(self, name, new_name)
```
**参数:**
- name: 待拷贝的Sheet页名称
- new_name: 新的Sheet页名称

### WorkBook.copy_sheet_to_workbook()
拷贝Sheet页到指定Workbook
```python
copy_sheet_to_workbook(self, name, workbook, new_name)
```
**参数:**
- name: 待拷贝的Sheet页名称
- workbook: 目标Workbook名称
- new_name: 新的Sheet页名称

### WorkBook.get_selected_range()
获取当前页的选中区域
```python
get_selected_range(self)
```

### WorkBook.rename_sheet()
重命名Sheet页
```python
rename_sheet(self, name, new_name)
```
**参数:**
- name: 待修改的Sheet页名称
- new_name: 修改后的Sheet页名称

### WorkBook.refresh_data()
刷新数据
```python
refresh_data(self)
```

### WorkBook.create_pivot_table()
创建数据透视表
```python
create_pivot_table(self, setting, source)
```
**参数:**
- setting: 数据透视表配置
- source: 数据透视表数据来源

### WorkBook.refresh_pivot_table()
刷新数据透视表
```python
refresh_pivot_table(self, name_or_index, sheet_name=None)
```
**参数:**
- name_or_index: 数据透视表名称或位置（从1开始）
- sheet_name: 透视表所在Sheet页名称, 默认为当前激活的Sheet页

### WorkBook.filter_pivot_table()
筛选数据透视表
```python
filter_pivot_table(self, sheet_name, name_or_index, field_name, select_type, filter_value_list)
```
**参数:**
- sheet_name: 透视表所在Sheet页名称
- name_or_index: 数据透视表名称或位置（从1开始）
- field_name: 透视表筛选器字段名称
- select_type: 选择方式，包括'all' 'none' 和 'partial'
- filter_value_list: 透视表筛选器选择项内容

### WorkBook.export_to_pdf()
导出PDF文件
```python
export_to_pdf(self, pdf_name, sheet_name=None, all_sheets=False, override=True)
```
**参数:**
- pdf_name: 透视表所在Sheet页名称
- sheet_name: 要导出的Sheet页，默认为当前激活的Sheet名称
- all_sheets: 是否导出全部Sheet页，默认为False
- override: 若导出的PDF文件已存在，是否选择覆盖，默认为True

### WorkSheet.get_cell()
获取工作表中指定单元格的内容
```python
get_cell(self, row_num, col_name)
```
**参数:**
- row_num: 指定单元格的行号，行号从 1 开始
- col_name: 指定单元格的列名，列名从'A'开始

### WorkSheet.get_row()
获取工作表中指定行内容
```python
get_row(self, row_num)
```
**参数:**
- row_num: 指定行号，行号从1开始

### WorkSheet.get_column()
获取工作表中指定列内容
```python
get_column(self, col_name)
```
**参数:**
- col_name: 指定列名，列名从'A'开始

### WorkSheet.get_range()
获取工作表中指定区域的内容
```python
get_range(self, begin_row_num, begin_column_name, end_row_num, end_column_name)
```
**参数:**
- begin_row_num: 起始单元格行号，行号从1开始
- begin_column_name: 起始单元格列名，列名从A开始
- end_row_num: 结束单元格行号, 行号从1开始
- end_column_name: 结束单元格列名，列名从A开始

### WorkSheet.set_cell()
在工作表指定单元格写入内容
```python
set_cell(self, row_num, col_name, value)
```
**参数:**
- row_num: 指定单元格的行号
- col_name: 指定单元格的列名
- value: 要写入到单元格中的内容

### WorkSheet.set_row()
设置工作表行内容
```python
set_row(self, row_num, values, begin_column_name = 'A')
```
**参数:**
- row_num: 指定要写入内容的行号，行号从 1 开始
- values: 要写入的内容，必须是一个列表类型
- begin_column_name: 指定写入内容的开始列名，默认值为 'A'

### WorkSheet.set_column()
向工作表写入列内容
```python
set_column(selef, col_name, values, begin_row_num = 1)
```
**参数:**
- col_name: 指定要写入内容的列名
- values: 要写入的内容，必须是一个列表类型
- begin_row_num: 指定写入内容的开始行号，默认值为 1

### WorkSheet.set_range()
向工作表指定区域写入内容
```python
set_range(self, row_num, col_name, values)
```
**参数:**
- row_num: 写入区域起始行号，行号从1开始
- col_name: 写入区域起始列名，列名从A开始
- values: 要写入的内容，必须是一个二维数组

### WorkSheet.append_row()
在工作表的最后追加一行内容
```python
append_row(self, values, begin_column_name = 'A')
```
**参数:**
- values: 要写入的值, 必须是一个列表类型
- begin_column_name: 设置开始的单元格列名, 默认值为 A

### WorkSheet.insert_row()
在工作表中插入一行内容
```python
insert_row(self, row_num, values, begin_column_name = 'A')
```
**参数:**
- row_num: 插入位置的行号，行号从1开始
- values: 要插入的值，必须是一个列表类型
- begin_column_name: 插入内容的起始列名，默认值为 A

### WorkSheet.remove_row()
移除工作表的某一行内容
```python
remove_row(self, row_num)
```
**参数:**
- row_num: 要移除的行号

### WorkSheet.remove_column()
移除工作表的某一列内容
```python
remove_column(self, column_name)
```
**参数:**
- column_name: 要移除的列名

### WorkSheet.clear()
清空工作表内容
```python
clear(self)
```

### WorkSheet.get_row_count()
获取工作表的总行数
```python
get_row_count(self)
```

### WorkSheet.get_column_count()
获取工作表的总列数
```python
get_column_count(self)
```

### WorkSheet.select_range()
选中工作表的指定内容区域
```python
select_range(self, begin_row_num, begin_column_name, end_row_num, end_column_name)
```
**参数:**
- begin_row_num: 起始单元格行号，行号从1开始
- begin_column_name: 起始单元格列名，列名从A开始
- end_row_num: 结束单元格行号, 行号从1开始
- end_column_name: 结束单元格列名，列名从A开始

### WorkSheet.get_name()
获取工作表的名称
```python
get_name(self)
```

### WorkSheet.insert()
插入列
```python
select_range(self, column_name, values, begin_row_index = 1)
```
**参数:**
- column_name: 插入数据的起始列名
- values: 插入数据
- begin_row_index: 开始插入的行号

### WorkSheet.get_first_free_column()
获取第一个可用列
```python
get_first_free_column(self)
```

### WorkSheet.get_first_free_column_on_row()
获取行的第一个可用列
```python
get_first_free_column_on_row(self, row_num)
```
**参数:**
- row_num: 行号

### WorkSheet.get_first_free_row()
获取第一个可用行
```python
get_first_free_row(self)
```

### WorkSheet.get_first_free_row_on_column()
获取列的第一个可用行
```python
get_first_free_row_on_column(self, column_name)
```
**参数:**
- column_name: 列名

### WorkSheet.copy_range()
拷贝指定的区域内容到剪切板
```python
copy_range(self, begin_row_num, begin_column_name, end_row_num, end_column_name)
```
**参数:**
- begin_row_num: 起始单元格行号，行号从1开始
- begin_column_name: 起始单元格列名，列名从A开始
- end_row_num: 结束单元格行号, 行号从1开始
- end_column_name: 结束单元格列名，列名从A开始

### WorkSheet.paste_range()
从指定的起始单元格粘贴剪切板数据
```python
paste_range(self, row_num, column_name)
```
**参数:**
- row_num: 起始单元格行号，行号从1开始
- column_name: 起始单元格列名，列名从A开始

### WorkSheet.paste_range_ex()
从指定的起始单元格粘贴剪切板数据，扩展选择性粘贴功能
```python
paste_range_ex(self, row_num, column_name, paste_type, paste_special_operation, skip_blanks, transpose)
```
**参数:**
- row_num: 起始单元格行号，行号从1开始
- column_name: 起始单元格列名，列名从A开始
- paste_type: 粘贴类型
- paste_special_operation: 粘贴运算
- skip_blanks: 是否跳过空单元，默认为False
- transpose: 是否选择转置，默认为False

### WorkSheet.clear_range()
清空指定的区域内容
```python
clear_range(self, begin_row_num, begin_column_name, end_row_num, end_column_name)
```
**参数:**
- begin_row_num: 起始单元格行号，行号从1开始
- begin_column_name: 起始单元格列名，列名从A开始
- end_row_num: 结束单元格行号, 行号从1开始
- end_column_name: 结束单元格列名，列名从A开始

### WorkSheet.set_row_hidden()
设置行隐藏属性
```python
set_row_hidden(self, row_num, hidden = False)
```
**参数:**
- row_num: 行号，list，行号从1开始
- hidden: 隐藏属性，默认为False

### WorkSheet.set_column_hidden()
设置列隐藏属性
```python
set_column_hidden(self, column_name, hidden = False)
```
**参数:**
- column_name: 列名列表，列名从A开始
- hidden: 隐藏属性，默认为False

## xbot.ftp

### connect()
连接FTP服务器
```python
connect(host, username, password)
```
**参数:**
- host: FTP服务器地址
- username: 用户名
- password: 密码

### FTPBase.unlogin()
退出登录，断开当前连接
```python
unlogin(self)
```

### FTPBase.get_ftp_files()
获取文件服务器上当前连接路径下的全部文件信息
```python
get_ftp_files(self, remote_path="")
```
**参数:**
- remote_path: 需要获取文件信息远程路径，默认值为空

### FTPBase.download_file()
下载文件服务器上指令路径下的文件到本地
```python
download_file(self, local_path, remote_file, download_mode='overwrite')
```
**参数:**
- local_path: 远程文件要下载到本地的路径
- remote_file: 服务器上相对当前连接的工作路径需要下载的文件路径
- download_mode: 当本地路径下存在同名文件时的处理方式

### FTPBase.download_files()
从远程目录下载多个文件到本地目录
```python
download_files(self, local_path, download_files, download_mode='overwrite')
```
**参数:**
- local_path: 远程文件要下载到本地的路径
- download_files: 服务器上相对当前连接的工作路径需要下载的文件列表
- download_mode: 当本地路径下存在同名文件时的处理方式

### FTPBase.download_folder()
从远程目录下载文件到指定的本地目录
```python
download_folder(self, local_path, remote_path, download_mode = 'overwrite')
```
**参数:**
- local_path: 远程文件要下载到本地的路径
- remote_path: 需要获取文件夹的远程目录
- download_mode: 当本地路径下存在同名文件时的处理方式

### FTPBase.download_folders()
从远程目录下载文件到指定的本地目录
```python
download_folders(self, local_path, remote_paths, download_mode = 'overwrite')
```
**参数:**
- local_path: 远程文件要下载到本地的路径
- remote_paths: 远程文件夹路径列表
- download_mode: 当本地路径下存在同名文件时的处理方式

### FTPBase.upload_file()
上传本地文件到远程服务器
```python
upload_file(self, local_file, remote_path='', upload_mode='overwrite')
```
**参数:**
- local_file: 需要上传的本地文件
- remote_path: 本地文件将要上传到的远程文件夹，默认为空
- upload_mode: 远程目标路径下存在和需要上传的文件同名的文件时的上传模式

### FTPBase.upload_files()
上传多个本地文件到远程服务器
```python
upload_files(self, local_files, remote_path='', upload_mode='overwrite')
```
**参数:**
- local_files: 需要上传的本地文件列表
- remote_path: 本地文件将要上传到的远程文件夹，默认为空
- upload_mode: 远程目标路径下存在和需要上传的文件同名的文件时的上传模式

### FTPBase.upload_folder()
上传本地文件夹到远程服务器
```python
upload_folder(self, local_folder, remote_path='', upload_mode='overwrite')
```
**参数:**
- local_folder: 需要上传的本地文件夹路径
- remote_path: 本地文件将要上传到的远程文件夹，默认为空
- upload_mode: 远程目标路径下存在和需要上传的文件同名的文件时的上传模式

### FTPBase.upload_folders()
上传多个本地文件夹到远程服务器
```python
upload_folders(self, local_folders, remote_path='', upload_mode='overwrite')
```
**参数:**
- local_folders: 需要上传的本地文件夹路径列表
- remote_path: 本地文件将要上传到的远程文件夹，默认为空
- upload_mode: 远程目标路径下存在和需要上传的文件同名的文件时的上传模式

### FTPBase.change_workspace_path()
改变当前连接的Working路径
```python
change_workspace_path(self, new_remote_path)
```
**参数:**
- new_remote_path: 新的远程Working路径

### FTPBase.delete_file()
删除当前连接Working路径下的文件
```python
delete_file(self, remote_file)
```
**参数:**
- remote_file: 将要删除的文件名称

### FTPBase.rename_file()
修改当前连接的Working路径下指定文件的名称
```python
rename_file(self, remote_file, new_name)
```
**参数:**
- remote_file: 将要重命名的远程文件
- new_name: 新的文件名称

### FTPBase.create_directory()
在当前连接的Working路径下创建文件夹
```python
create_directory(self, new_remote_path)
```
**参数:**
- new_remote_path: 将要创建的文件夹名称

### FTPBase.delete_folder()
删除当前连接的Working路径下指定的文件夹
```python
delete_folder(self, remote_path)
```
**参数:**
- remote_path: 将要删除的文件夹名称

## xbot.mobile

### connect()
使用Appium模式，根据连接参数与指定的手机建立连接
```python
connect(appium_url, platform_name, platform_version, device_name, additional_capabilities=None)
```
**参数:**
- appium_url: 指定的Appium服务器地址
- platform_name: 指定的系统名称
- platform_version: 指定的系统版本
- device_name: 指定的设备型号
- additional_capabilities: 添加其他配置项

### connect_by_custom_name()
根据自定义名称连接指定的手机
```python
connect_by_custom_name(custom_name)
```
**参数:**
- custom_name: 自定义手机名称

### MobileSession.find_all()
获取手机中与选择器匹配的全部元素并返回元素列表
```python
find_all(self, selector)
```
**参数:**
- selector: 要查找的选择器

### MobileSession.find()
获取手机中与元素选择器匹配的元素
```python
find(self, selector)
```
**参数:**
- selector: 要查找的选择器

### MobileSession.find_all_by_id()
获取手机中指定resource-id的全部元素并返回元素列表
```python
find_all_by_id(self, id)
```
**参数:**
- id: 元素的resource-id属性值

### MobileSession.find_by_id()
获取手机中指定resource-id的元素
```python
find_by_id(self, id)
```
**参数:**
- id: 元素的resource-id属性值

### MobileSession.find_all_by_accessibility_id()
获取手机中指定accessibility_id的全部元素并返回元素列表
```python
find_all_by_accessibility_id(self, accessibility_id)
```
**参数:**
- accessibility_id: 元素的content-desc属性值

### MobileSession.find_by_accessibility_id()
获取手机中指定accessibility_id的元素
```python
find_by_accessibility_id(self, accessibility_id)
```
**参数:**
- accessibility_id: 元素的content-desc属性值

### MobileSession.find_all_by_label_name()
获取手机中指定label_name的全部元素并返回元素列表
```python
find_all_by_label_name(self, label_name)
```
**参数:**
- label_name: 元素的class属性值/元素的标签名

### MobileSession.find_by_label_name()
获取手机中指定label_name的元素
```python
find_by_label_name(self, label_name)
```
**参数:**
- label_name: 元素的class属性值/元素的标签名

### MobileSession.find_all_by_xpath()
获取手机中指定xpath的全部元素并返回元素列表
```python
find_all_by_xpath(self, xpath)
```
**参数:**
- xpath: 元素的xpath路径

### MobileSession.find_by_xpath()
获取手机中指定xpath的元素
```python
find_by_xpath(self, xpath)
```
**参数:**
- xpath: 元素的xpath路径

### MobileSession.find_all_by_uiautomator_selector()
获取手机中指定uiautomator_selector的全部元素并返回元素列表
```python
find_all_by_uiautomator_selector(self, uiautomator_selector)
```
**参数:**
- uiautomator_selector: 元素的android selector path

### MobileSession.find_by_uiautomator_selector()
获取手机中指定uiautomator_selector的元素
```python
find_by_uiautomator_selector(self, uiautomator_selector)
```
**参数:**
- uiautomator_selector: 元素的android selector path

### MobileSession.contains_element()
当前手机中是否包含与元素选择器匹配的元素
```python
contains_element(self, selector)
```
**参数:**
- selector: 要查找的选择器

### MobileSession.click()
单机手机屏幕指定位置
```python
click(self, point_x, point_y, delay_after=1)
```
**参数:**
- point_x: 目标点的横向坐标
- point_y: 目标点的纵向坐标
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.dblclick()
双击手机屏幕指定位置
```python
dblclick(self, point_x, point_y, delay_after=1)
```
**参数:**
- point_x: 目标点的横向坐标
- point_y: 目标点的纵向坐标
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.longpress()
长按手机屏幕指定位置
```python
dblclick(self, point_x, point_y, delay_after=1)
```
**参数:**
- point_x: 目标点的横向坐标
- point_y: 目标点的纵向坐标
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.swipe()
在手机屏幕上滑动手指
```python
swipe(self, start_point_x, start_point_y, end_point_x, end_point_y, swipe_time=800, delay_after=1)
```
**参数:**
- start_point_x: 滑动起始点横向坐标
- start_point_y: 滑动起始点纵向坐标
- end_point_x: 滑动结束点横向坐标
- end_point_y: 滑动结束点纵向坐标
- swipe_time: 滑动总时间
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.back()
后退
```python
back(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.home()
主页
```python
home(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.switchapp()
切换应用
```python
switchapp(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileSession.getoriention()
获取手机当前的屏幕方向
```python
getoriention(self)
```

### MobileSession.setoriention()
设置手机的屏幕方向
```python
setoriention(self, screenOrientation:int)
```
**参数:**
- screenOrientation: 横屏为 0, 竖屏为 1

### MobileSession.screenshot()
对手机屏幕进行截图并保存
```python
screenshot(self, folder_path, filename=None)
```
**参数:**
- folder_path: 截图保存的路径
- filename: 截图保存时的文件名

### MobileSession.get_page_source()
获取手机当前页面的树结构信息，返回XML结构的字符串
```python
get_page_source(self)
```

### MobileSession.get_clipboard_text()
获取剪贴板文本内容
```python
get_clipboard_text(self)
```

### MobileSession.set_clipboard_text()
设置剪贴板文本内容
```python
set_clipboard_text(self, value)
```
**参数:**
- value: 文本内容

### MobileSession.get_session_detail()
获取手机连接信息详情
```python
get_session_detail(self)
```

### MobileSession.close()
关闭此手机连接
```python
close(self)
```

### MobileElement.click()
单击手机元素
```python
click(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileElement.dblclick()
双击手机元素
```python
dblclick(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileElement.longpress()
长按手机元素
```python
longpress(self, delay_after=1)
```
**参数:**
- delay_after: 执行成功后延迟时间，默认延迟1s

### MobileElement.input()
填写手机输入框
```python
input(self, text: str, append=False, delay_after=1)
```
**参数:**
- text: 需要填写到输入框中的文本内容
- append: 是否追加输入，默认值为False
- delay_after: 执行成功后延迟时间，默认延迟 1s

### MobileElement.get_text()
获取元素的文本内容
```python
get_text(self)
```

### MobileElement.get_attribute()
获取元素的属性值
```python
get_attribute(self, name: str)
```
**参数:**
- name: 元素的属性名

### MobileElement.screenshot()
对元素进行截图并保存
```python
screenshot(self, folder_path, filename=None)
```
**参数:**
- folder_path: 截图保存的路径
- filename: 截图保存时的文件名

### MobileElement.get_bounding()
获取元素的位置信息
```python
get_bounding(self)
```

## xbot.pdf

### extract_text()
提取pdf文件文本
```python
extract_text(path, from_page, to_page, password = None)
```
**参数:**
- path: pdf文件路径
- from_page: 起始页码
- to_page: 终止页码
- password: pdf的文件密码

### extract_images()
提取pdf文件多张图片
```python
extract_images(path, from_page, to_page, save_to_dir,password = None, name_prefix = 'pdf_image')
```
**参数:**
- path: pdf文件路径
- from_page: 起始页码
- to_page: 终止页码
- save_to_dir: 图片保存的文件夹路径
- password: pdf的文件密码
- name_prefix: 导出的图片名称前缀

### extract_pages()
导出pdf文件中的页
```python
extract_pages( path, from_page, to_page, save_to,password = None )
```
**参数:**
- path: pdf文件路径
- from_page: 起始页码
- to_page: 终止页码
- save_to: 保存的文件路径
- password: pdf的文件密码

### merge_pdfs()
合并多个pdf文件
```python
merge_pdfs(paths, save_to , passwords = None)
```
**参数:**
- paths: pdf文件路径列表
- save_to: 保存的文件路径
- passwords: pdf文件各自的密码

## xbot.web

### create()
打开网页
```python
create(url, mode='cef' ,load_timeout=20, stop_if_timeout=False, silent_running=False, executable_path=None, arguments=None)
```
**参数:**
- url: 目标网址
- mode: 浏览器类型
- load_timeout: 等待加载超时时间，默认超时时间20s
- stop_if_timeout: 网页加载超时是否停止加载网页，默认为 False
- silent_running: 是否开启运行时不抢占鼠标键盘，默认为 False
- executable_path: 浏览器执行文件路径，默认为None
- arguments: 命令行参数，默认为None

### get()
根据网址或标题获取网页
```python
get(title=None, url=None, mode='cef', load_timeout=20, use_wildcard=False, stop_if_timeout=False, open_page=False, page_url=None, silent_running=False)
```
**参数:**
- title: 网页标题
- url: 网址
- mode: 浏览器类型
- load_timeout: 等待加载超时时间，默认超时时间20s
- use_wildcard: 是否使用通配符方式匹配，默认为False
- stop_if_timeout: 等待加载超时时间，默认超时时间20s
- open_page: 根据url或title匹配失败时，是否打开新的网页，默认为False
- page_url: open_page=True时，指定打开的网页地址
- silent_running: 是否开启运行时不抢占鼠标键盘，默认为 False

### get_active()
获取当前选中或激活的网页
```python
get_active(mode='cef', load_timeout=20, stop_if_timeout=False, silent_running=False)
```
**参数:**
- mode: 浏览器类型
- load_timeout: 等待加载超时时间，默认超时时间20s
- stop_if_timeout: 等待加载超时时间，默认超时时间20s
- silent_running: 是否开启运行时不抢占鼠标键盘，默认为 False

### get_all()
获取所有网页
```python
get_all(mode='cef', title=None, url=None, use_wildcard=False, silent_running=False)
```
**参数:**
- mode: 浏览器类型
- title: 网页标题
- url: 网址
- use_wildcard: 是否使用通配符方式匹配，默认为False
- silent_running: 是否开启运行时不抢占鼠标键盘，默认为 False

### get_cookies()
获取浏览器Cookie信息
```python
get_cookies(mode='cef' , url=None, name=None, domain=None, path=None)
```
**参数:**
- mode: 浏览器类型
- url: 根据给定的url找到相应的cookie
- name: 根据 cookie 的 name 来筛选cookie
- domain: 根据 cookie 的 domain 来筛选cookie
- path: 根据 cookie 的 path 来筛选cookie

### get_cookies_v2()
获取浏览器Cookie信息，支持 PartitionKey
```python
get_cookies_v2(mode='cef', name=None, url=None, domain=None, path=None, partition_key=None, secure=None, session=None)
```
**参数:**
- mode: 浏览器类型
- name: 根据给定的 name 筛选cookie
- url: 根据给定的 URL 筛选cookie
- domain: 根据 cookie 的 domain 来筛选cookie
- path: 根据 cookie 的 path 来筛选cookie
- partition_key: 根据 cookie 的 partition key 来筛选cookie
- secure: secure参数
- session: session参数

### set_cookie()
设置浏览器Cookie信息
```python
set_cookie(url, mode='cef', name=None ,value=None, sessionCookie=True, expires=100, domain=None, path=None, httpOnly=False, secure=False)
```
**参数:**
- url: 根据给定的 URL 设置cookie
- mode: 浏览器类型
- name: 根据给定的 name 设置cookie
- value: 根据给定的 value 设置cookie
- domain: 根据给定的 domain 设置cookie
- path: 根据给定的 path 设置cookie
- sessionCookie: 默认为 True，设置为会话 cookie
- expires: 持久化 cookie 需要设置有效期
- secure: 设置该 cookie 是否被标记为 Secure
- session: 设置该 cookie 是否被标记为 HttpOnly

### remove_cookie()
获取浏览器Cookie信息移除通过 cookie url、 cookie name 指定的 cookie
```python
remove_cookie(url, name, mode='cef')
```
**参数:**
- url: 将被移除的 cookie url
- name: 将被移除的 cookie 名称
- mode: 浏览器类型

### close_all()
关闭所有网页
```python
close_all(mode='cef' , task_kill=False )
```
**参数:**
- mode: 浏览器类型
- task_kill: 是否终止浏览器进程，默认为 False

### handle_save_dialog()
处理网页下载对话框
```python
handle_save_dialog(file_folder, dialog_result='ok', mode='cef' , *, file_name=None,wait_appear_timeout=20,focus_timeout=600)
```
**参数:**
- file_folder: 文件保存路径
- dialog_result: 点击下载对话框中按钮
- mode: 浏览器类型
- file_name: 保存文件名
- wait_appear_timeout: 等待对话框出现超时时间
- focus_timeout: 焦点超时时间

### handle_upload_dialog()
处理网页上传对话框
```python
handle_upload_dialog(filename, dialog_result='ok', mode='cef' , *, wait_appear_timeout=20)
```
**参数:**
- filename: 文件保存路径
- dialog_result: 点击下载对话框中按钮
- mode: 浏览器类型
- wait_appear_timeout: 等待对话框出现超时时间

### Browser.get_url()
获取网址
```python
get_url(self)
```

### Browser.get_title()
获取标题
```python
get_title(self)
```

### Browser.get_text()
获取网页的文本内容
```python
get_text(self)
```

### Browser.get_html()
获取网页的html
```python
get_html(self)
```

### Browser.activate()
激活目标网页
```python
activate(self)
```

### Browser.navigate()
跳转到新网页
```python
navigate(self, url, load_timeout=20)
```
**参数:**
- url: 新网页地址
- load_timeout: 等待加载超时时间，默认超时时间20s

### Browser.go_back()
网页后退
```python
go_back(self, load_timeout=20)
```
**参数:**
- load_timeout: 等待加载超时时间，默认超时时间20s

### Browser.go_forward()
网页前进
```python
go_forward(self, load_timeout=20)
```
**参数:**
- load_timeout: 等待加载超时时间，默认超时时间20s

### Browser.reload()
网页重新加载
```python
reload(self, ignore_cache=False, load_timeout=20)
```
**参数:**
- ignore_cache: 是否忽略缓存，默认为 False
- load_timeout: 等待加载超时时间，默认超时时间20s

### Browser.stop_load()
网页停止加载
```python
stop_load(self)
```

### Browser.is_load_completed()
判断网页是否加载完成
```python
is_load_completed(self)
```

### Browser.wait_load_completed()
等待网页加载完成
```python
wait_load_completed(self, timeout=20)
```
**参数:**
- timeout: 等待超时时间，默认为20s

### Browser.close()
关闭网页
```python
close(self)
```

### Browser.execute_javascript()
在网页元素上执行JS脚本
```python
execute_javascript(self, code, argument=None)
```
**参数:**
- code: 要执行的JS脚本
- argument: 要传入到JS函数中的参数

### Browser.scroll_to()
鼠标滚动网页
```python
scroll_to(self, location='bottom', behavior='instant', top=0, left=0)
```
**参数:**
- location: 网页要滚动到的位置
- behavior: 网页滚动效果
- top: 滚动到指定位置的纵坐标
- left: 滚动到指定位置的横坐标

### Browser.handle_javascript_dialog()
处理网页对话框
```python
handle_javascript_dialog(self, dialog_result='ok' , text=None, wait_appear_timeout=20)
```
**参数:**
- dialog_result: 点击下载对话框中按钮
- text: 输入网页对话框的内容
- wait_appear_timeout: 等待对话框出现超时时间

### Browser.get_javascript_dialog_text()
获取网页对话框内容
```python
get_javascript_dialog_text(self, wait_appear_timeout=20)
```
**参数:**
- wait_appear_timeout: 等待对话框出现超时时间

### Browser.start_monitor_network()
开始监听网页请求
```python
start_monitor_network(self)
```

### Browser.stop_monitor_network()
停止监听网页请求
```python
stop_monitor_network(self)
```

### Browser.get_responses()
获取网页请求结果
```python
get_responses(self, url, use_wildcard=False,resource_type='All')
```
**参数:**
- url: 资源路径Url
- use_wildcard: 是否使用通配符方式匹配
- resource_type: 要过滤的网页请求结果类型

### Browser.wait_appear()
等待网页元素出现
```python
wait_appear(self, selector_or_element, timeout=20)
```
**参数:**
- selector_or_element: 要查找的选择器
- timeout: 等待网页元素出现超时时间

### Browser.wait_disappear()
等待网页元素消失
```python
wait_disappear(self, selector_or_element, timeout=20)
```
**参数:**
- selector_or_element: 要查找的选择器
- timeout: 等待网页元素出现超时时间

### Browser.find_all()
在当前网页中获取与选择器匹配的相似网页元素列表
```python
find_all(self, selector, timeout=20)
```
**参数:**
- selector: 要查找的选择器
- timeout: 获取网页相似元素列表超时时间

### Browser.find_all_by_css()
在当前网页中获取符合CSS选择器的网页元素列表
```python
find_all_by_css(self, css_selector, timeout=20)
```
**参数:**
- css_selector: CSS选择器
- timeout: 获取网页相似元素列表超时时间

### Browser.find_all_by_xpath()
在当前网页中获取符合Xpath选择器的网页元素列表
```python
find_all_by_xpath(self, xpath_selector, timeout=20)
```
**参数:**
- xpath_selector: xpath字符串语法
- timeout: 获取网页相似元素列表超时时间

### Browser.find()
在当前网页中获取与选择器匹配的网页元素对象
```python
find(self, selector, timeout=20)
```
**参数:**
- selector: 要查找的选择器
- timeout: 获取网页相似元素列表超时时间

### Browser.find_by_css()
在当前网页中获取符合CSS选择器的网页元素对象
```python
find_by_css(self, css_selector, timeout=20)
```
**参数:**
- css_selector: CSS选择器
- timeout: 获取网页相似元素列表超时时间

### Browser.find_by_xpath()
在当前网页中获取符合Xpath选择器的网页元素对象
```python
find_by_xpath(self, xpath_selector, timeout=20)
```
**参数:**
- xpath_selector: xpath字符串语法
- timeout: 获取网页相似元素列表超时时间

### Browser.is_element_displayed()
网页元素是否可见
```python
is_element_displayed(self, selector)
```
**参数:**
- selector: 要查找的选择器

### Browser.extract_table()
获取选择器对应表格数据
```python
extract_table(self, table_selector, *, exclude_thead=False, timeout=20)
```
**参数:**
- table_selector: 要查找的表格选择器
- exclude_thead: 表格数据抓取多页时，只保留第一页抓取结果的表头
- timeout: 获取网页相似元素列表超时时间

### Element.parent()
获取当前元素的父元素
```python
parent(self)
```

### Element.children()
获取当前元素的所有子元素
```python
children(self)
```

### Element.child_at()
获取指定位置的子元素
```python
child_at(self)
```
**参数:**
- index: 子元素的位置索引，从0开始计数

### Element.previous_sibling()
获取上一个并列的兄弟元素
```python
previous_sibling(self)
```

### Element.next_sibling()
获取下一个并列的兄弟元素
```python
next_sibling(self)
```

### Element.click()
单击当前网页元素
```python
click(self, button='left', simulative=True, keys='none', delay_after=1, move_mouse=False, anchor=None)
```
**参数:**
- button: 要点击的鼠标按键
- simulative: 是否模拟人工点击
- keys: 点击鼠标时的键盘辅助按钮
- delay_after: 执行成功后延迟时间
- move_mouse: 是否显示鼠标移动轨迹
- anchor: 锚点

### Element.dblclick()
双击当前网页元素
```python
dblclick(self, simulative=True, delay_after=1, move_mouse=False, anchor=None)
```
**参数:**
- simulative: 是否模拟人工点击
- delay_after: 执行成功后延迟时间
- move_mouse: 是否显示鼠标移动轨迹
- anchor: 锚点

### Element.input()
填写网页输入框
```python
input(self, text: str, simulative=True, append=False, contains_hotkey=False, force_img_ENG=False, send_key_delay=50, focus_timeout=1000, delay_after=1, anchor=None)
```
**参数:**
- text: 需要填写到输入框中的文本内容
- simulative: 是否模拟人工点击
- append: 是否追加输入
- contains_hotkey: 输入内容是否包含快捷键
- send_key_delay: 两次按键之间的时间间隔
- delay_after: 执行成功后延迟时间
- anchor: 锚点
- focus_timeout: 焦点超时时间

### Element.clipboard_input()
通过剪切板填写网页输入框
```python
clipboard_input(self, text: str, append=False, delay_after=1, anchor=None,focus_timeout=1000)
```
**参数:**
- text: 需要填写到输入框中的文本内容
- append: 是否追加输入
- delay_after: 执行成功后延迟时间
- anchor: 锚点
- focus_timeout: 焦点超时时间

### Element.focus()
选中(激活)当前元素
```python
focus(self)
```

### Element.hover()
鼠标悬停在当前元素
```python
hover(self, simulative=True, delay_after=1)
```
**参数:**
- simulative: 是否模拟人工悬停
- delay_after: 执行成功后延迟时间

### Element.get_text()
获取当前网页元素的文本内容
```python
get_text(self)
```

### Element.get_html()
获取当前网页元素的html内容
```python
get_html(self)
```

### Element.get_value()
获取当前网页元素的值
```python
get_value(self)
```

### Element.set_value()
设置当前网页元素的值
```python
set_value(self, value: str)
```
**参数:**
- value: 需要设置到网页元素上的文本值

### Element.check()
设置网页复选框
```python
check(self, mode='check', delay_after=1)
```
**参数:**
- mode: 设置网页复选框的结果
- delay_after: 执行成功后延迟时间

### Element.select()
按选项内容设置单选网页下拉框元素
```python
select(self, item: str, mode='fuzzy', delay_after=1)
```
**参数:**
- item: 要设置的网页下拉框元素的某一项的文本内容
- mode: 查找项的匹配模式
- delay_after: 执行成功后延迟执行时间

### Element.select_multiple()
按选项内容设置单选网页下拉框元素
```python
select_multiple(self, items: typing.List[str], mode='fuzzy', append=False, delay_after=1)
```
**参数:**
- items: 要勾选的网页下拉框元素的列表
- mode: 查找项的匹配模式
- append: 是否追加设置
- delay_after: 执行成功后延迟执行时间

### Element.select_by_index()
按下标设置单选网页下拉框元素
```python
select_by_index(self, index: int, delay_after=1)
```
**参数:**
- index: 要设置的单选网页下拉框元素的位置
- delay_after: 执行成功后延迟执行时间

### Element.select_multiple_by_index()
按下标设置多选网页下拉框元素
```python
select_multiple_by_index(self, indexes: typing.List[int], append=False, delay_after=1)
```
**参数:**
- indexes: 要设置的单选网页下拉框元素的位置列表
- append: 是否追加设置
- delay_after: 执行成功后延迟执行时间

### Element.get_select_options()
获取网页下拉框的值
```python
get_select_options(self)
```

### Element.set_attribute()
设置网页元素属性值
```python
set_attribute(self, name: str, value: str)
```
**参数:**
- name: 元素属性名称
- value: 要设置的元素属性值

### Element.get_attribute()
获取网页元素属性值
```python
get_attribute(self, name: str)
```
**参数:**
- name: 元素属性名称

### Element.get_all_attributes()
获取网页元素全部属性值
```python
get_all_attributes(self)
```

### Element.get_bounding()
获取网页元素的边框属性组合
```python
get_bounding(self, to96dpi=True)
```
**参数:**
- to96dpi: 是否需要将边框属性转换成dpi为96的对应属性值

### Element.extract_table()
获取当前元素所属表格的内容列表
```python
extract_table(self)
```

### Element.screenshot()
对目标元素进行截图, 并将图片进行保存
```python
screenshot(self, folder_path, filename=None)
```
**参数:**
- folder_path: 元素截图后图片需要保存的路径
- filename: 截图后图片保存后的名称

### Element.screenshot_to_clipboard()
对目标元素进行截图, 并将图片保存至剪切板
```python
screenshot_to_clipboard(self)
```

### Element.is_checked()
判断网页复选框元素是否被选中
```python
is_checked(self)
```

## xbot.win32

### get()
通过标题或类名获取窗口对象
```python
get(title, class_name=None, use_wildcard=False)
```
**参数:**
- title: 指定的窗口标题
- class_name: 指定的窗口类名
- use_wildcard: 是否使用通配符进行匹配

### get_by_handle()
通过窗口句柄获取窗口对象
```python
get_by_handle(handle=None)
```
**参数:**
- handle: 指定的窗口句柄

### get_by_selector()
通过选择器获取窗口对象
```python
get_by_selector(selector=None)
```
**参数:**
- selector: 要查找的选择器

### get_desktop()
获取桌面对象
```python
get_desktop()
```

### minimize_all()
最小化全部窗口
```python
minimize_all()
```

### mouse_move()
移动鼠标到指定位置
```python
mouse_move(point_x, point_y, relative_to='screen', move_speed='instant', delay_after=1)
```
**参数:**
- point_x: 指定坐标的横坐标
- point_y: 指定坐标的纵坐标
- relative_to: 指定坐标相对移动位置
- move_speed: 移动鼠标到指定坐标的速度
- delay_after: 执行成功后延迟时间

### send_keys()
模拟键盘输入输入指定键盘按键, 可包含快捷键
```python
send_keys(keys='', send_key_delay, hardware_driver_input, delay_after)
```
**参数:**
- keys: 要模拟输入的键盘按键
- send_key_delay: 两次按键之间的时间间隔
- hardware_driver_input: 是否通过硬件驱动的方式输入
- delay_after: 执行成功后延迟时间

### mouse_click()
模拟鼠标点击, 如鼠标左键单击、左键双击等
```python
mouse_click(button='left', click_type='click', keys='none', delay_after=1)
```
**参数:**
- button: 要点击的鼠标按键
- click_type: 鼠标按键的点击方式
- keys: 点击鼠标时的键盘辅助按钮
- delay_after: 执行成功后延迟时间

### mouse_wheel()
模拟鼠标滚轮滚动, 默认往下滚动
```python
mouse_wheel(wheel_direction='down', wheel_times, keys='none', delay_after=1)
```
**参数:**
- wheel_direction: 鼠标滚轮滚动方向
- wheel_times: 滚动鼠标滚轮次数
- keys: 点击鼠标时的键盘辅助按钮
- delay_after: 执行成功后延迟时间

### get_mouse_position()
获取鼠标相对于桌面/当前选中(激活)的窗的坐标位置
```python
get_mouse_position(relative_to='screen')
```
**参数:**
- relative_to: 鼠标相对于某个对象的位置

### exists()
判断窗口是否存在
```python
exists(window)
```
**参数:**
- window: Win32Window对象

### manual_motion_on()
开启模拟真人操作，一次对多个指令用模拟真人的操作习惯运行
```python
manual_motion_on(motion_move, motion_click)
```
**参数:**
- motion_move: 模拟真人按随机路线和速度移动鼠标
- motion_click: 模拟真人在随机位置点击元素

### manual_motion_off()
结束模拟真人操作
```python
manual_motion_off()
```

### Window.get_detail()
获取窗口详细信息
```python
get_detail(self, operation)
```
**参数:**
- operation: 获取窗口信息

### Window.activate()
激活窗口
```python
activate(self)
```

### Window.set_state()
设置窗口状态
```python
set_state(self, flag)
```
**参数:**
- flag: 窗口的状态

### Window.move()
将窗口移动到指定位置
```python
move(self, x=0, y=0)
```
**参数:**
- x: 指定位置的横坐标
- y: 指定位置的纵坐标

### Window.resize()
设置窗口大小
```python
resize(self, width=1, height=1)
```
**参数:**
- width: 窗口宽度
- height: 窗口高度

### Window.close()
关闭窗口
```python
close(self)
```

### Window.is_active()
判断窗口是否是选中(激活)状态
```python
is_active(self)
```

### Window.wait_active()
等待窗口选中(激活)
```python
wait_active(self, timeout=20)
```
**参数:**
- timeout: 等待窗口选中的超时时间

### Window.wait_exists()
等待窗口出现
```python
wait_exists(self, timeout=20)
```
**参数:**
- timeout: 等待窗口出现超时时间

### Window.wait_close()
等待窗口关闭
```python
wait_close(self, timeout=20)
```
**参数:**
- timeout: 等待窗口关闭超时时间

### Window.find_all()
获取窗口中与选择器匹配的全部元素并返回元素列表
```python
find_all(self, selector, timeout=20)
```
**参数:**
- selector: 要查找的选择器
- timeout: 获取窗口相似元素列表超时时间

### Window.find()
获取窗口中与元素选择器匹配的元素
```python
find(self, selector, timeout=20)
```
**参数:**
- selector: 要查找的选择器
- timeout: 获取窗口相似元素列表超时时间

### Window.wait_appear()
等待元素出现
```python
wait_appear(self, selector_or_element, timeout=20)
```
**参数:**
- selector_or_element: 要查找的选择器
- timeout: 在窗口中等待目标元素出现的超时时间

### Window.wait_disappear()
在当前窗口中等待目标元素或与元素选择器匹配的元素消失
```python
wait_disappear(self, selector_or_element, timeout=20)
```
**参数:**
- selector_or_element: 要查找的选择器
- timeout: 在窗口中等待目标元素消失的超时时间

### Window.contains_element()
当前窗口中是否包含与元素选择器匹配的元素
```python
contains_element(self, selector)
```
**参数:**
- selector: 要查找的选择器

### Window.wait_focus()
等待窗口获取焦点
```python
wait_focus(self, timeout=20)
```
**参数:**
- timeout: 等待窗口获取焦点的超时时间

### Window.wait_focusout()
等待窗口失去焦点
```python
wait_focusout(self, timeout=20)
```
**参数:**
- timeout: 等待窗口失去焦点的超时时间

### Element.parent()
获取当前元素的父元素
```python
parent(self)
```

### Element.children()
获取当前元素的所有子元素
```python
children(self)
```

### Element.child_at()
获取指定位置的子元素
```python
child_at(self)
```
**参数:**
- index: 子元素的位置索引，从0开始计数

### Element.next_sibling()
获取下一个并列的兄弟元素
```python
next_sibling(self)
```

### Element.click()
单击win32元素
```python
click(self, button='left', simulative, keys='none', delay_after, move_mouse=True, anchor=None)
```
**参数:**
- button: 单击时鼠标按下的按键
- simulative: 是否模拟人工点击
- keys: 点击鼠标时的键盘辅助按钮
- delay_after: 执行成功后延迟时间
- move_mouse: 是否显示鼠标移动轨迹
- anchor: 锚点

### Element.dblclick()
双击win32元素
```python
dblclick(self, simulative=True, delay_after=1, move_mouse=True, anchor=None)
```
**参数:**
- simulative: 是否模拟人工点击
- delay_after: 执行成功后延迟时间
- move_mouse: 是否显示鼠标移动轨迹
- anchor: 锚点

### Element.input()
填写win32输入框
```python
input(self, text, simulative, append, contains_hotkey, delay_after, anchor,focus_timeout)
```
**参数:**
- text: 需要填写到输入框中的文本内容
- simulative: 是否模拟人工点击
- append: 是否追加输入
- contains_hotkey: 输入内容是否包含快捷键
- delay_after: 执行成功后延迟时间
- anchor: 锚点
- focus_timeout: 焦点超时时间

### Element.clipboard_input()
使用剪切板填写win32输入框
```python
clipboard_input(self, text: str, append=False, delay_after=1, anchor=None,focus_timeout=1000)
```
**参数:**
- text: 需要填写到输入框中的文本内容
- append: 是否追加输入
- delay_after: 执行成功后延迟时间
- anchor: 锚点
- focus_timeout: 焦点超时时间

### Element.hover()
鼠标悬停在win32软件元素上
```python
hover(self, simulative, delay_after)
```
**参数:**
- simulative: 是否模拟人工点击
- delay_after: 执行成功后延迟时间

### Element.check()
选中或取消选中win32复选框元素
```python
check(self, mode='check', delay_after=1)
```
**参数:**
- mode: win32复选框的设置状态
- delay_after: 执行成功后延迟时间

### Element.select()
设置win32下拉框元素内容
```python
select(self, item , mode , delay_after)
```
**参数:**
- item: 选中项的文本内容
- mode: 对选项文本内容的匹配模式
- delay_after: 执行成功后延迟时间

### Element.select_by_index()
根据目标项的下标设置下拉框内容
```python
select_by_index(self, index: int, delay_after=1)
```
**参数:**
- index: 要选择的目标项的下标
- delay_after: 执行成功后延迟时间

### Element.set_value()
给win32元素设置值
```python
set_value(self, value)
```
**参数:**
- value: 要设置给win32元素的文本值

### Element.get_attribute()
获取win32元素的属性值
```python
get_attribute(self, name: str)
```
**参数:**
- name: win32元素的属性值

### Element.get_all_attributes()
获取win32元素的全部属性值
```python
get_all_attributes(self)
```

### Element.get_text()
获取win32元素的文本内容
```python
get_text(self)
```

### Element.get_value()
获取win32元素的详细信息
```python
get_value(self)
```

### Element.drag_to()
将win32元素拖拽到指定位置
```python
drag_to(self, simulative, behavior , top , left, delay_after)
```
**参数:**
- simulative: 是否模拟人工点击
- behavior: 拖拽方式
- top: 相对于当前元素中心的纵向位移
- left: 相对于当前元素中心的横向位移
- delay_after: 执行成功后延迟时间

### Element.screenshot()
对win32元素进行截图并保存
```python
screenshot(self, folder_path, filename=None)
```
**参数:**
- folder_path: 截图保存的路径
- filename: 截图保存时的文件名

### Element.screenshot_to_clipboard()
对win32元素截图，并将截图添加到剪切板中
```python
screenshot_to_clipboard(self)
```

### Element.get_bounding()
获取win32元素边框信息
```python
get_bounding(self, to96dpi = True)
```
**参数:**
- to96dpi: 是否将获取的到元素边框信息转换为96dpi下的值

### Element.get_all_select_items()
获取win32下拉框元素的全部下拉选项
```python
get_all_select_items(self)
```

### Element.get_selected_item()
获取win32下拉框元素当前选中的全部下拉选项
```python
get_selected_item(self)
```

### Clipboard.set_text()
设置剪切板文本内容
```python
set_text(value)
```
**参数:**
- value: 要设置到剪切板中的文本

### Clipboard.get_text()
获取剪切板文本内容
```python
get_text()
```

### Clipboard.clear()
清空剪切板内容
```python
clear()
```

### Clipboard.set_file()
将文件添加到剪切板
```python
set_file(file_paths)
```
**参数:**
- file_paths: 文件绝对路径列表

### Image.wait_appear()
在当前屏幕中等待与图像库匹配的图片出现
```python
wait_appear(image_selectors , wait_all=False, timeout=20)
```
**参数:**
- image_selectors: 图像选择器
- wait_all: 是否等待全部目标图片出现后再执行
- timeout: 等待目标图片出现的超时时间

### Image.wait_appear_from_window()
在当前激活的窗口中等待与图像选择器匹配的图片出现
```python
wait_appear_from_window(hWnd, image_selectors, wait_all=False, timeout=20)
```
**参数:**
- hWnd: 目标窗口的句柄
- image_selectors: 图像选择器
- wait_all: 是否等待全部目标图片出现后再执行
- timeout: 等待目标图片出现的超时时间

### Image.wait_disappear()
在当前屏幕中等待与图像选择器匹配的图片消失
```python
wait_disappear(image_selectors , wait_all=False, timeout=20)
```
**参数:**
- image_selectors: 图像选择器
- wait_all: 是否等待全部目标图片消失后再执行
- timeout: 等待目标图片消失的超时时间

### Image.wait_disappear_from_window()
在当前激活的窗口中等待与图像选择器匹配的图片消失
```python
wait_disappear_from_window(hWnd, image_selectors, wait_all=False , timeout=20)
```
**参数:**
- hWnd: 目标窗口的句柄
- image_selectors: 图像选择器
- wait_all: 是否等待全部目标图片消失后再执行
- timeout: 等待目标图像消失的超时时间

### Image.hover()
在当前屏幕上查找与图像选择器匹配的图片并将鼠标悬停在上面
```python
hover(image_selectors , anchor=None)
```
**参数:**
- image_selectors: 图像选择器
- anchor: 锚点

### Image.hover_on_window()
在当前屏幕上查找与图像选择器匹配的图片并将鼠标悬停在上面
```python
hover_on_window(hWnd, image_selectors , anchor=None)
```
**参数:**
- hWnd: 目标窗口的句柄
- image_selectors: 图像选择器
- anchor: 锚点

### Image.click()
在这当前屏幕上查找与图像选择器相似的图像并单击
```python
click(image_selectors , anchor=None, button='left', keys='none', move_mouse=True)
```
**参数:**
- image_selectors: 图像选择器
- anchor: 锚点
- button: 单击时鼠标按下的按键
- keys: 点击鼠标时的键盘辅助按钮
- move_mouse: 是否显示鼠标移动轨迹

### Image.click_on_window()
在这当前激活的窗口中查找与图像选择器相似的图像并单击
```python
click_on_window(hWnd, image_selectors, anchor=None, button='left', keys='none', move_mouse=True)
```
**参数:**
- hWnd: 目标窗口的句柄
- image_selectors: 图像选择器
- anchor: 锚点
- button: 单击时鼠标按下的按键
- keys: 点击鼠标时的键盘辅助按钮
- move_mouse: 是否显示鼠标移动轨迹

### Image.dblclick()
在这当前屏幕上查找与图像选择器相似的图像并双击
```python
dblclick(image_selectors , anchor=None, move_mouse=True)
```
**参数:**
- image_selectors: 图像选择器
- anchor: 锚点
- move_mouse: 是否显示鼠标移动轨迹

### Image.dblclick_on_window()
在这当前激活的窗口中查找与图像选择器相似的图像并双击
```python
dblclick_on_window(hWnd, image_selectors, *, anchor=None, move_mouse=True)
```
**参数:**
- hWnd: 目标窗口的句柄
- image_selectors: 图像选择器
- anchor: 锚点
- move_mouse: 是否显示鼠标移动轨迹

### Screenshot.save_screen_to_clipboard()
对屏幕进行截图，并将截图结果添加到剪切板中
```python
save_screen_to_clipboard()
```

### Screenshot.save_screen_to_file()
对屏幕进行截图，并将结果以指定格式保存到指定路径下
```python
save_screen_to_file(image_path, image_format)
```
**参数:**
- image_path: 截图保存完整路径
- image_format: 截图保存的文件格式

### Screenshot.save_window_to_clipboard()
对窗口截图并将图片添加到剪切板, 句柄为0则选择当前激活的窗口
```python
save_window_to_clipboard(hwnd)
```
**参数:**
- hwnd: 目标窗口的句柄

### Screenshot.save_window_to_file()
对窗口截图并将图片保存到本地
```python
save_window_to_file(hwnd, image_path, image_format)
```
**参数:**
- hwnd: 目标窗口的句柄
- image_path: 截图保存完整路径
- image_format: 截图保存的文件格式

### screensaver.open_screen_saver()
唤起屏幕保护
```python
open_screen_saver( settings = None, default_text = None )
```
**参数:**
- settings: 自定义屏保配置json
- default_text: 影刀屏保被唤起时显示的默认文字

### screensaver.append_screen_saver_text()
设置屏保提示
```python
append_screen_saver_text(text, *, settings = None)
```
**参数:**
- text: 设置影刀屏保显示文字
- settings: 对屏保文字进行自定义显示设置的json串

### screensaver.clear()
清空屏保提示
```python
clear()
```

### screensaver.close()
关闭屏幕保护
```python
close()
```

## xbot.word

### create()
创建并返回word对象
```python
create(kind='office', visible=True)
```
**参数:**
- kind: 创建方式
- visible: 用于控制自动化操作是否用户级可见

### open()
打开word文件并返回word对象
```python
open(file_name, kind='office', visible=True, open_password='', edit_password='')
```
**参数:**
- file_name: word文件路径
- kind: 创建方式
- visible: 用于控制自动化操作是否用户级可见
- open_password: 打开密码
- edit_password: 编辑密码

### Document.save()
将工作簿保存为word文件
```python
save(self)
```

### Document.save_as()
将工作簿另存为word文件
```python
save_as(self, filename)
```
**参数:**
- filename: 另存为路径

### Document.close()
关闭工作簿
```python
close(self)
```

### Document.export_to_pdf()
Word导出PDF文件
```python
export_to_pdf(self, pdf_name, export_range = 0, page_from = 0, page_to = 0, overwrite = True)
```
**参数:**
- pdf_name: 要保存的PDF文件绝对路径
- export_range: 要导出的范围
- page_from: 导出指定页面的起始页面
- page_to: 导出指定页面的终止页面
- overwrite: 若导出的PDF文件已存在，是否选择覆盖

### Document.get_selection()
获取Word当前选择区域
```python
get_selection(self)
```

### Document.insert_hyperlink()
插入超链接
```python
insert_hyperlink(self, text, hyperlink_url, newline = False)
```
**参数:**
- text: 超链显示文字
- hyperlink_url: 超链接地址
- newline: 插入超链前是否换行

### Document.insert_table()
插入Word表格
```python
insert_table(self, table_data, table_data_format, grid = True, newline = False)
```
**参数:**
- table_data: 表格数据
- table_data_format: 表格格式内容
- grid: 表格是否显示边框
- newline: 插入超链前是否换行

### Document.read_table_from_document()
读取Word表格
```python
read_table_from_document(self, find_way, table_index, table_content)
```
**参数:**
- find_way: 表格查找方式
- table_index: 表格位置
- table_content: 表格内容

### Document.locate_cursor_to_bookmark()
定位光标到书签处
```python
locate_cursor_to_bookmark(self, bookmark_name, bookmark_cursor_position = 'after_bookmark')
```
**参数:**
- bookmark_name: 书签名
- bookmark_cursor_position: 定位到书签的位置

### Selection.read_text()
读取当前选择区域的文本内容
```python
read_text(self)
```

### Selection.write_text()
在Word中写入文本，写入光标所在位置
```python
write_text(self, text, text_format, newline = False)
```
**参数:**
- text: 写入文本内容
- text_format: 写入文本格式
- newline: 写入文本前是否换行

### Selection.insert_newline()
在word中插入换行符
```python
insert_newline(self)
```

### Selection.insert_picture()
在word中插入图片
```python
insert_picture(self, image_source, image_path, image_scale, newline = False)
```
**参数:**
- image_source: 图片来源
- image_path: 插入图片的路径
- image_scale: 图片缩放百分比
- newline: 写入文本前是否换行

### Selection.replace_text()
在word中替换文本
```python
replace_text(self, search_text, replace_text, replace_all = True, case_sensitive = False)
```
**参数:**
- search_text: 需要查找的文本
- replace_text: 用于替换的文本
- replace_all: 是否全部替换
- case_sensitive: 区分大小写

### Selection.move_cursor()
移动word中的光标
```python
move_cursor(self, move_direction, move_count, press_shift = False)
```
**参数:**
- move_direction: 移动方向
- move_count: 移动单位长度
- press_shift: 移动时是否按下shift键

### Selection.locate_cursor_to_document()
定位光标到word文档开头处和结尾处
```python
locate_cursor_to_document(self, document_cursor_position = 'end_document')
```
**参数:**
- document_cursor_position: 定位位置

### Selection.locate_cursor_to_text()
定位光标到word中指定文本处
```python
locate_cursor_to_text(self, text_content, text_index = 1, text_cursor_position = 'after_text', from_start = True)
```
**参数:**
- text_content: 定位的文本内容
- text_index: 从起点查找到文本的位置
- text_cursor_position: 定位到文本位置
- from_start: 是否从头开始查找

## xbot.xzip

### zip()
压缩文件/文件夹
```python
zip(file_folder_path, zip_file_path, compress_level=5, password=None)
```
**参数:**
- file_folder_path: 待压缩的文件和文件夹
- zip_file_path: 压缩文件路径
- compress_level: 压缩级别
- password: 密码

### unzip()
解压文件/文件夹
```python
unzip(zip_file_path, unzip_dir_path, password=None)
```
**参数:**
- zip_file_path: 压缩文件路径
- unzip_dir_path: 解压目录
- password: 密码
