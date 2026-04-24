# Mobile 模块

## mobilesession

手机连接和操作

| 方法 | 说明 |
|------|------|
| `connect(name)` | 连接手机 |
| `find(selector)` | 查找元素 |
| `find_all(selector)` | 查找所有元素 |
| `get_device_info()` | 获取设备信息 |
| `screenshot(path)` | 截图 |

## mobileelement

| 方法 | 说明 |
|------|------|
| `click()` | 点击 |
| `double_click()` | 双击 |
| `input(text)` | 输入 |
| `get_text()` | 获取文本 |
| `get_attribute(name)` | 获取属性 |
| `screenshot(path)` | 元素截图 |
| `swipe_up/down/left/right()` | 滑动 |
| `wait(timeout)` | 等待 |

## 示例

```python
import xbot

session = xbot.mobile.connect('我的安卓手机')
element = session.find('登录按钮')
element.click()
session.screenshot('D:\\mobile.png')
```
