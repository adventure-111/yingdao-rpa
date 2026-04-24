# 影刀RPA 模块索引

> 完整文档：https://www.yingdao.com/yddoc/rpa/zh-CN/

## 模块总览

| 模块 | 说明 | 指令数 |
|------|------|--------|
| **xbot.web** | 网页自动化 | 70 |
| **xbot.win32** | Windows桌面自动化 | 75 |
| **xbot.excel** | Excel操作 | 52 |
| **xbot.mobile** | 移动端自动化 | 38 |
| **xbot_extensions.activity_feishu_bitable** | 飞书多维表格 | 28 |
| **xbot.word** | Word操作 | 19 |
| **xbot.ftp** | FTP文件传输 | 16 |
| **xbot.app** | 数据表格与对话框 | 18 |
| **xbot.ado** | 数据库操作 | 3 |
| **xbot.ai** | AI能力(OCR) | 3 |
| **xbot.pdf** | PDF处理 | 4 |
| **xbot.xzip** | 压缩解压 | 2 |
| **package** | 元素选择器与资源文件 | 6 |

---

## package

元素与资源管理，完整文档：[references/api_summary.md](references/api_summary.md)

| 指令 | 说明 |
|------|------|
| `selector(name)` | 获取元素库中的元素选择器 |
| `image_selector(name)` | 获取图像库中的图像选择器 |
| `resources.get_text(filename, encoding='utf-8')` | 读取文本资源文件 |
| `resources.get_bytes(filename)` | 读取二进制资源文件 |
| `resources.copy_to(filename, dest_filename)` | 复制资源文件到本地 |
| `resources.add_to_clipboard(filenames)` | 添加资源文件到剪切板 |

---

## xbot.web

网页自动化，完整文档：[references/web.md](references/web.md)

### 浏览器操作
| 指令 | 说明 |
|------|------|
| `xbot.web.create(url, mode='cef')` | 创建并打开网页 |
| `xbot.web.get(title, url)` | 获取已打开的网页 |
| `xbot.web.get_active()` | 获取当前激活的网页 |
| `xbot.web.get_all(url)` | 获取所有匹配的网页 |
| `xbot.web.close_all()` | 关闭所有网页 |

### Browser 对象
| 指令 | 说明 |
|------|------|
| `browser.navigate(url)` | 跳转URL |
| `browser.go_back()` | 后退 |
| `browser.go_forward()` | 前进 |
| `browser.reload(ignore_cache)` | 刷新 |
| `browser.get_url()` | 获取当前URL |
| `browser.get_title()` | 获取页面标题 |
| `browser.get_html()` | 获取页面HTML |
| `browser.get_text()` | 获取页面文本 |
| `browser.execute_javascript(code)` | 执行JS代码 |
| `browser.scroll_to(x, y)` | 滚动到位置 |
| `browser.close()` | 关闭网页 |

### 元素查找
| 指令 | 说明 |
|------|------|
| `browser.find(selector)` | 查找单个元素 |
| `browser.find_by_xpath(xpath)` | 按xpath查找 |
| `browser.find_by_css(css)` | 按CSS选择器查找 |
| `browser.find_all(selector)` | 查找所有匹配元素 |
| `browser.find_all_by_xpath(xpath)` | 按xpath查找所有 |
| `browser.find_all_by_css(css)` | 按CSS查找所有 |
| `browser.wait_appear(selector, timeout)` | 等待元素出现 |
| `browser.wait_disappear(selector, timeout)` | 等待元素消失 |
| `browser.is_element_displayed(selector)` | 元素是否可见 |

### Element 对象
| 指令 | 说明 |
|------|------|
| `element.click(button, simulative)` | 点击 |
| `element.dblclick(button)` | 双击 |
| `element.input(text, simulative, append)` | 输入文本 |
| `element.clipboard_input()` | 剪切板输入 |
| `element.hover()` | 悬停 |
| `element.focus()` | 聚焦 |
| `element.get_text()` | 获取文本 |
| `element.get_value()` | 获取输入值 |
| `element.get_attribute(name)` | 获取属性 |
| `element.set_attribute(name, value)` | 设置属性 |
| `element.set_value(value)` | 设置输入值 |
| `element.check(mode)` | 复选框操作 |
| `element.select(text, mode)` | 下拉框选择 |
| `element.select_by_index(index)` | 下拉框按索引选 |
| `element.select_multiple(items)` | 多选下拉框 |
| `element.get_select_options()` | 获取下拉框选项 |
| `element.is_checked()` | 是否选中 |
| `element.get_bounding()` | 获取元素位置尺寸 |
| `element.screenshot(path)` | 截图 |
| `element.screenshot_to_clipboard()` | 截图到剪切板 |
| `element.extract_table()` | 提取表格数据 |

### Cookie与对话框
| 指令 | 说明 |
|------|------|
| `xbot.web.get_cookies(mode, domain)` | 获取Cookie |
| `xbot.web.set_cookie(url, name, value, expires)` | 设置Cookie |
| `xbot.web.remove_cookie(url, name)` | 删除Cookie |
| `browser.handle_javascript_dialog(result, text)` | 处理JS对话框 |
| `xbot.web.handle_save_dialog(file_folder, file_name)` | 处理下载对话框 |
| `xbot.web.handle_upload_dialog(file_path)` | 处理上传对话框 |

---

## xbot.win32

Windows桌面自动化，完整文档：[references/win32.md](references/win32.md)

### 窗口操作
| 指令 | 说明 |
|------|------|
| `xbot.win32.get(title, class_name)` | 获取窗口 |
| `xbot.win32.get_by_handle(hwnd)` | 按句柄获取窗口 |
| `xbot.win32.get_by_selector(selector)` | 按选择器获取窗口 |
| `xbot.win32.get_desktop()` | 获取桌面窗口 |
| `xbot.win32.exists(title, class_name)` | 窗口是否存在 |
| `window.activate()` | 激活窗口 |
| `window.set_state(state)` | 设置窗口状态(maximize/minimize/normal) |
| `window.move(x, y)` | 移动窗口 |
| `window.resize(width, height)` | 调整大小 |
| `window.close()` | 关闭窗口 |
| `window.wait_active(timeout)` | 等待窗口激活 |
| `window.wait_exists(timeout)` | 等待窗口出现 |
| `window.wait_close(timeout)` | 等待窗口关闭 |

### 鼠标键盘
| 指令 | 说明 |
|------|------|
| `xbot.win32.mouse_move(x, y, move_speed)` | 移动鼠标 |
| `xbot.win32.mouse_click(button, click_type)` | 鼠标点击 |
| `xbot.win32.mouse_wheel(direction, times)` | 鼠标滚轮 |
| `xbot.win32.get_mouse_position(relative_to)` | 获取鼠标位置 |
| `xbot.win32.send_keys(keys)` | 发送按键 |

### 元素操作
| 指令 | 说明 |
|------|------|
| `window.find(selector)` | 查找元素 |
| `window.find_all(selector)` | 查找所有元素 |
| `window.wait_appear(selector, timeout)` | 等待元素出现 |
| `element.click(button, simulative)` | 点击 |
| `element.input(text)` | 输入 |
| `element.clipboard_input()` | 剪切板输入 |
| `element.hover()` | 悬停 |
| `element.check(mode)` | 复选框 |
| `element.select(text)` | 下拉框选择 |
| `element.select_by_index(index)` | 按索引选 |
| `element.set_value(value)` | 设置值 |
| `element.get_text()` | 获取文本 |
| `element.get_value()` | 获取值 |
| `element.get_attribute(name)` | 获取属性 |
| `element.get_all_attributes()` | 获取所有属性 |
| `element.drag_to(top, left, simulative)` | 拖拽 |
| `element.screenshot(path)` | 截图 |
| `element.get_bounding()` | 获取位置尺寸 |
| `element.get_all_select_items()` | 获取下拉框选项 |
| `element.get_selected_item()` | 获取选中项 |

### 剪切板
| 指令 | 说明 |
|------|------|
| `xbot.win32.Clipboard.set_text(text)` | 设置文本 |
| `xbot.win32.Clipboard.get_text()` | 获取文本 |
| `xbot.win32.Clipboard.clear()` | 清空 |
| `xbot.win32.Clipboard.set_file(paths)` | 设置文件 |

### 图像识别
| 指令 | 说明 |
|------|------|
| `xbot.win32.Image.wait_appear(image_selectors, timeout)` | 等待图像出现 |
| `xbot.win32.Image.wait_disappear(image_selectors, timeout)` | 等待图像消失 |
| `xbot.win32.Image.hover(image_selectors)` | 图像悬停 |
| `xbot.win32.Image.click(image_selectors, button)` | 图像点击 |
| `xbot.win32.Image.dblclick(image_selectors, button)` | 图像双击 |
| `xbot.win32.Image.wait_appear_from_window(window, image, timeout)` | 从窗口等待图像 |
| `xbot.win32.Image.hover_on_window(window, image)` | 窗口图像悬停 |
| `xbot.win32.Image.click_on_window(window, image, button)` | 窗口图像点击 |

### 截图
| 指令 | 说明 |
|------|------|
| `xbot.win32.Screenshot.save_screen_to_file(path, image_format)` | 屏幕截图 |
| `xbot.win32.Screenshot.save_screen_to_clipboard()` | 屏幕截图到剪切板 |
| `xbot.win32.Screenshot.save_window_to_file(hwnd, path, format)` | 窗口截图 |
| `xbot.win32.Screenshot.save_window_to_clipboard(hwnd)` | 窗口截图到剪切板 |

---

## xbot.excel

Excel操作，完整文档：[references/excel.md](references/excel.md)

### 工作簿操作
| 指令 | 说明 |
|------|------|
| `xbot.excel.create(kind, visible)` | 创建Excel |
| `xbot.excel.open(file_name, kind, visible)` | 打开Excel |
| `xbot.excel.get_active_workbook(kind)` | 获取活动工作簿 |

### WorkBook 对象
| 指令 | 说明 |
|------|------|
| `workbook.get_active_sheet()` | 获取当前sheet |
| `workbook.get_sheet_by_index(index)` | 按索引获取sheet |
| `workbook.get_sheet_by_name(name)` | 按名称获取sheet |
| `workbook.get_all_sheets()` | 获取所有sheet名称 |
| `workbook.create_sheet(name, create_way)` | 创建sheet |
| `workbook.active_sheet_by_index(index)` | 激活sheet |
| `workbook.active_sheet_by_name(name)` | 按名称激活 |
| `workbook.delete_sheet(name)` | 删除sheet |
| `workbook.copy_sheet(name, new_name)` | 复制sheet |
| `workbook.copy_sheet_to_workbook(name, workbook, new_name)` | 复制到另一工作簿 |
| `workbook.rename_sheet(name, new_name)` | 重命名sheet |
| `workbook.save()` | 保存 |
| `workbook.save_as(filename)` | 另存为 |
| `workbook.close()` | 关闭 |
| `workbook.execute_macro(macro)` | 执行宏 |
| `workbook.refresh_data()` | 刷新数据 |
| `workbook.export_to_pdf(name, sheet_name, all_sheets, override)` | 导出PDF |

### WorkSheet 对象
| 指令 | 说明 |
|------|------|
| `sheet.get_cell(row_num, col_name)` | 获取单元格 |
| `sheet.set_cell(row_num, col_name, value)` | 写入单元格 |
| `sheet.get_row(row_num)` | 获取整行 |
| `sheet.set_row(row_num, values, begin_column_name)` | 写入整行 |
| `sheet.get_column(col_name)` | 获取整列 |
| `sheet.set_column(col_name, values, begin_row_num)` | 写入整列 |
| `sheet.get_range(begin_row, begin_col, end_row, end_col)` | 获取区域 |
| `sheet.set_range(row, col, values)` | 写入区域(二维数组) |
| `sheet.append_row(values, begin_column_name)` | 追加行 |
| `sheet.insert_row(row_num, values, begin_column_name)` | 插入行 |
| `sheet.remove_row(row_num)` | 删除行 |
| `sheet.remove_column(col_name)` | 删除列 |
| `sheet.clear()` | 清空sheet |
| `sheet.clear_range(begin_row, begin_col, end_row, end_col)` | 清空区域 |
| `sheet.get_row_count()` | 获取行数 |
| `sheet.get_column_count()` | 获取列数 |
| `sheet.get_first_free_row()` | 获取第一个空闲行 |
| `sheet.get_first_free_column()` | 获取第一个空闲列 |
| `sheet.get_first_free_row_on_column(col)` | 列中第一个空闲行 |
| `sheet.get_first_free_column_on_row(row)` | 行中第一个空闲列 |
| `sheet.select_range(begin_row, begin_col, end_row, end_col)` | 选中区域 |
| `sheet.copy_range(begin_row, begin_col, end_row, end_col)` | 复制区域 |
| `sheet.paste_range(row, col)` | 粘贴 |
| `sheet.paste_range_ex(row, col, paste_type)` | 高级粘贴 |
| `sheet.set_row_hidden(row, hidden)` | 行隐藏 |
| `sheet.set_column_hidden(col, hidden)` | 列隐藏 |
| `sheet.get_name()` | 获取sheet名称 |
| `sheet.get_selected_range()` | 获取选中区域 |

---

## xbot.word

Word操作，完整文档：[references/word.md](references/word.md)

| 指令 | 说明 |
|------|------|
| `xbot.word.create(kind, visible)` | 创建Word |
| `xbot.word.open(file_name, kind, visible, open_password, edit_password)` | 打开Word |
| `doc.save()` | 保存 |
| `doc.save_as(filename)` | 另存为 |
| `doc.close()` | 关闭 |
| `doc.export_to_pdf(path, export_range, page_from, page_to)` | 导出PDF |
| `doc.get_selection()` | 获取选择区域 |
| `doc.insert_hyperlink(text, url)` | 插入超链接 |
| `doc.insert_table(table_data, grid, newline)` | 插入表格 |
| `doc.read_table_from_document()` | 读取文档表格 |
| `doc.locate_cursor_to_bookmark(name)` | 定位到书签 |
| `selection.read_text()` | 读取文本 |
| `selection.write_text(text, newline)` | 写入文本 |
| `selection.insert_newline()` | 插入换行 |
| `selection.insert_picture(image_source, image_path, image_scale, newline)` | 插入图片 |
| `selection.replace_text(search, replace, replace_all, case_sensitive)` | 替换文本 |
| `selection.move_cursor(direction, count, press_shift)` | 移动光标 |
| `selection.locate_cursor_to_document(location)` | 定位光标到文档首尾 |
| `selection.locate_cursor_to_text(text)` | 定位光标到文本 |

---

## xbot.mobile

移动端自动化，完整文档：[references/mobile.md](references/mobile.md)

### 连接
| 指令 | 说明 |
|------|------|
| `xbot.mobile.connect(appium_url, platform_name, platform_version, device_name)` | Appium连接 |
| `xbot.mobile.connect_by_custom_name(name)` | 按设备名连接 |
| `mobile.close()` | 关闭连接 |

### MobileSession
| 指令 | 说明 |
|------|------|
| `mobile.find(selector)` | 查找元素 |
| `mobile.find_all(selector)` | 查找所有 |
| `mobile.find_by_id(id)` | 按ID查找 |
| `mobile.find_all_by_id(id)` | 按ID查找所有 |
| `mobile.find_by_xpath(xpath)` | 按xpath查找 |
| `mobile.find_all_by_xpath(xpath)` | 按xpath查找所有 |
| `mobile.find_by_accessibility_id(id)` | 按accessibility查找 |
| `mobile.find_by_label_name(name)` | 按标签名查找 |
| `mobile.find_by_uiautomator_selector(selector)` | UIAutomator选择器 |
| `mobile.contains_element(selector)` | 是否包含元素 |
| `mobile.click(x, y)` | 点击坐标 |
| `mobile.dblclick(x, y)` | 双击坐标 |
| `mobile.longpress(x, y)` | 长按坐标 |
| `mobile.swipe(start_x, start_y, end_x, end_y, swipe_time)` | 滑动 |
| `mobile.back()` | 返回 |
| `mobile.home()` | 主页 |
| `mobile.switchapp()` | 切换应用 |
| `mobile.getoriention()` | 获取屏幕方向 |
| `mobile.setoriention(orientation)` | 设置屏幕方向 |
| `mobile.screenshot(path, filename)` | 截图 |
| `mobile.get_page_source()` | 获取页面源码 |
| `mobile.get_clipboard_text()` | 获取剪切板文本 |
| `mobile.set_clipboard_text(text)` | 设置剪切板文本 |
| `mobile.get_session_detail()` | 获取连接详情 |

### MobileElement
| 指令 | 说明 |
|------|------|
| `element.click()` | 点击 |
| `element.dblclick()` | 双击 |
| `element.longpress()` | 长按 |
| `element.input(text)` | 输入 |
| `element.get_text()` | 获取文本 |
| `element.get_attribute(name)` | 获取属性 |
| `element.screenshot(path, name)` | 截图 |
| `element.get_bounding()` | 获取位置尺寸 |

---

## xbot.app

数据表格与对话框，完整文档：[references/app.md](references/app.md)

### databook
| 指令 | 说明 |
|------|------|
| `xbot.app.databook.get_row(row_num)` | 获取指定行 |
| `xbot.app.databook.set_row(row_num, values, begin_column_name)` | 写入整行 |
| `xbot.app.databook.append_row(values, begin_column_name)` | 追加行 |
| `xbot.app.databook.insert_row(row_num, values, begin_column_name)` | 插入行 |
| `xbot.app.databook.remove_row(row_num)` | 删除行 |
| `xbot.app.databook.get_cell(row_num, col_name)` | 获取单元格 |
| `xbot.app.databook.set_cell(row_num, col_name, value)` | 写入单元格 |
| `xbot.app.databook.set_column(col_name, values, begin_row_num)` | 写入整列 |
| `xbot.app.databook.get_range(begin_row, begin_col, end_row, end_col)` | 获取区域 |
| `xbot.app.databook.set_range(row, col, values)` | 写入区域 |
| `xbot.app.databook.get_row_count()` | 获取行数 |
| `xbot.app.databook.clear()` | 清空 |

### dialog
| 指令 | 说明 |
|------|------|
| `xbot.app.dialog.show_alert(message, title)` | 消息对话框 |
| `xbot.app.dialog.show_confirm(message, title)` | 确认对话框(返回bool) |
| `xbot.app.dialog.show_message_box(title, message, button, timeout, default_button)` | 消息框 |
| `xbot.app.dialog.show_workbook_dialog(title, message)` | 数据表格对话框 |
| `xbot.app.dialog.show_custom_dialog(settings)` | 自定义对话框 |
| `xbot.app.dialog.show_notifycation(message, placement, level, timeout)` | 通知框 |

---

## xbot.ado

数据库操作，完整文档：[references/other.md](references/other.md)

| 指令 | 说明 |
|------|------|
| `xbot.ado.Database.open(conn_str)` | 连接数据库 |
| `xbot.ado.Database.exec(sql, timeout_seconds)` | 执行SQL |
| `xbot.ado.Database.close()` | 关闭连接 |

---

## xbot.ai

AI能力集成，完整文档：[references/ai.md](references/ai.md)

| 指令 | 说明 |
|------|------|
| `xbot.ai.AliyunAI.ocr_from_file(image_path)` | 阿里云OCR |
| `xbot.ai.BaiduAI.ocr_from_file(image_path)` | 百度OCR |
| `xbot.ai.TencentAI.ocr_from_file(image_path)` | 腾讯OCR |

---

## xbot.pdf

PDF处理，完整文档：[references/other.md](references/other.md)

| 指令 | 说明 |
|------|------|
| `xbot.pdf.extract_text(path, from_page, to_page, password)` | 提取文本 |
| `xbot.pdf.extract_images(path, from_page, to_page, save_to_dir, name_prefix)` | 提取图片 |
| `xbot.pdf.extract_pages(path, from_page, to_page, save_to)` | 提取页面 |
| `xbot.pdf.merge_pdfs(paths, save_to, passwords)` | 合并PDF |

---

## xbot.ftp

FTP文件传输，完整文档：[references/other.md](references/other.md)

| 指令 | 说明 |
|------|------|
| `xbot.ftp.connect(host, username, password)` | 连接FTP |
| `ftp.unlogin()` | 断开连接 |
| `ftp.get_ftp_files(path)` | 获取文件列表 |
| `ftp.download_file(local_path, remote_path)` | 下载文件 |
| `ftp.download_files(local_path, remote_paths)` | 批量下载文件 |
| `ftp.download_folder(local_path, remote_path)` | 下载文件夹 |
| `ftp.upload_file(local_path, remote_path)` | 上传文件 |
| `ftp.upload_files(local_path, remote_paths)` | 批量上传文件 |
| `ftp.upload_folder(local_path, remote_path)` | 上传文件夹 |
| `ftp.change_workspace_path(path)` | 切换工作目录 |
| `ftp.delete_file(path)` | 删除文件 |
| `ftp.rename_file(old, new)` | 重命名 |
| `ftp.create_directory(path)` | 创建目录 |
| `ftp.delete_folder(path)` | 删除文件夹 |

---

## xbot.xzip

压缩解压，完整文档：[references/other.md](references/other.md)

| 指令 | 说明 |
|------|------|
| `xbot.xzip.zip(file_folder_path, zip_file_path, compress_level, password)` | 压缩 |
| `xbot.xzip.unzip(zip_file_path, unzip_dir_path, password)` | 解压 |

---

## xbot_extensions.activity_feishu_bitable

飞书多维表格，完整文档：[references/feishu_bitable.md](references/feishu_bitable.md)

共28个指令，通过 `xbot_visual.process.run(process="xbot_extensions.activity_feishu_bitable.指令名", ...)` 调用。

| 指令分类 | 指令 |
|---------|------|
| 连接 | `create_instance` |
| 数据表 | `get_tables`, `add_table`, `delete_table`, `update_table` |
| 视图 | `get_views`, `add_view`, `delete_view`, `update_view` |
| 字段 | `get_fields`, `add_fields`, `update_fields`, `delete_fields` |
| 记录 | `get_records_by_view`, `get_records_by_view_v2`, `get_record_by_id`, `get_record_by_filter`, `add_record`, `add_records`, `update_record`, `delete_record`, `batch_delete_record`, `batch_get_record` |
| 素材 | `download_media`, `upload_media` |
| 元信息 | `get_meta_info`, `update_meta_info`, `get_wiki_token` |

---

## 指南文档

| 名称 | 地址 |
|------|------|
| 编码版使用说明 | 710947295618007040 |
| 如何调用Python模块 | 710946480648302592 |
| 如何定义和调用函数 | 710945349377404928 |
| 如何安装第三方库 | 710945906455162880 |
