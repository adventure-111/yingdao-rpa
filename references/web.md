# Web 模块

## xbot.web

| 方法 | 说明 |
|------|------|
| `create(url, mode='cef', load_timeout=20)` | 打开网页，mode: cef/chrome/ie/edge/360se |
| `get(title=None, url=None, mode='cef')` | 获取已打开的网页 |
| `close(web_object)` | 关闭网页 |

## xbot.web.Browser

| 方法 | 说明 |
|------|------|
| `navigate(url)` | 导航到URL |
| `get_title()` | 获取标题 |
| `get_url()` | 获取URL |
| `reload()` | 刷新 |
| `go_back()` | 返回 |
| `go_forward()` | 前进 |
| `execute_js(script)` | 执行JS |
| `close()` | 关闭 |
| `activate()` | 激活 |

## xbot.web.Element

| 方法 | 说明 |
|------|------|
| `find(selector)` | 查找元素（使用预录制选择器） |
| `find_all(selector)` | 查找所有 |
| `find_by_xpath(xpath)` | 按绝对xpath查找 |
| `wait_for_element(selector, timeout)` | 等待元素出现 |
| `wait_for_all_elements(xpath, timeout)` | 等待所有匹配元素（支持相对xpath） |
| `click()` | 点击 |
| `double_click()` | 双击 |
| `input(text)` | 输入 |
| `get_text()` | 获取文本 |
| `get_attribute(name)` | 获取属性 |
| `hover()` | 悬停 |
| `scroll_into_view()` | 滚动到可见 |
| `wait_for_visible(timeout)` | 等待可见 |
| `get_all_inputs()` | 获取所有输入框 |
| `get_all_links()` | 获取所有链接 |

## xpath 定位方式

### 方式1：find_by_xpath（绝对路径）
```python
browser = web.create('https://www.baidu.com', 'chrome')
browser.find_by_xpath("//input[@id='kw']").input('关键词')
browser.find_by_xpath("//button[@id='chat-submit-button']").click()
```

### 方式2：混合定位 + 容错
```python
# 搜索按钮：用户可见的是 button 元素
try:
    browser.find_by_xpath("//button[@id='chat-submit-button']").click()
except:
    browser.find_by_xpath("//input[@id='su']").click()
```

## 常用xpath表达式参考
| 场景 | xpath表达式 |
|------|------------|
| 按id | `//input[@id='kw']` |
| 按name | `//input[@name='wd']` |
| 按button id | `//button[@id='chat-submit-button']` |
| 按value | `//input[@value='百度一下']` |
| 按class | `//input[@class='s_ipt']` |
| 按placeholder | `//input[@placeholder='搜索']` |
