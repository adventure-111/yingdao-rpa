# Win32 模块

## xbot.win32

| 方法 | 说明 |
|------|------|
| `get(title, class_name=None, use_wildcard=False)` | 按标题获取窗口 |
| `get_by_handle(hwnd)` | 按句柄获取窗口 |
| `get_by_selector(selector)` | 按选择器获取窗口 |
| `get_desktop()` | 获取桌面窗口 |

## xbot.win32.Window

| 方法 | 说明 |
|------|------|
| `find(element_name)` | 查找元素 |
| `find_all(element_name)` | 查找所有匹配元素 |
| `activate()` | 激活窗口 |
| `close()` | 关闭窗口 |
| `maximize()` | 最大化 |
| `minimize()` | 最小化 |
| `restore()` | 还原 |
| `hide()` | 隐藏 |
| `show()` | 显示 |
| `set_position(x, y)` | 设置位置 |
| `set_size(width, height)` | 设置大小 |
| `get_position()` | 获取位置 |
| `get_size()` | 获取大小 |
| `get_title()` | 获取标题 |
| `get_handle()` | 获取句柄 |

## xbot.win32.Element

| 方法 | 说明 |
|------|------|
| `click()` | 点击 |
| `double_click()` | 双击 |
| `right_click()` | 右键 |
| `input(text, timeout=5)` | 输入文本 |
| `get_text()` | 获取文本 |
| `get_attribute(name)` | 获取属性 |
| `wait_for_element(timeout=10)` | 等待元素 |
| `scroll_into_view()` | 滚动到可见 |
| `hover()` | 悬停 |
| `get_bounds()` | 获取边界 |

## xbot.win32.Image

| 方法 | 说明 |
|------|------|
| `wait_for_appear(timeout)` | 等待图像出现 |
| `wait_for_disappear(timeout)` | 等待图像消失 |
| `click_on_window(wnd, image)` | 在窗口点击图像 |
| `dblclick_on_window(wnd, image)` | 双击 |
| `move_to(image)` | 移动到图像 |
| `exists()` | 图像是否存在 |

## xbot.win32.Screenshot

| 方法 | 说明 |
|------|------|
| `capture_window(wnd, path)` | 截取窗口 |
| `capture_screen(path, region)` | 截取屏幕 |

## xbot.win32.Clipboard

| 方法 | 说明 |
|------|------|
| `set_text(text)` | 设置文本 |
| `get_text()` | 获取文本 |
| `clear()` | 清空 |

## xbot.win32.screensaver

| 方法 | 说明 |
|------|------|
| `activate()` | 唤起屏保 |
| `deactivate()` | 关闭屏保 |
| `set_text(text)` | 设置屏保文字 |
| `clear_text()` | 清空文字 |

## 示例

```python
from xbot import win32

# 获取窗口并操作
wnd = win32.get('记事本')
element = wnd.find('文本编辑器')
element.click()
element.input('hello')

# 截图
win32.screenshot.capture_screen('D:\\screen.png')
```
