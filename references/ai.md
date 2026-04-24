# AI 模块

## xbot.ai.BaiduAI

需先配置 api_key 和 secret_key

| 方法 | 说明 |
|------|------|
| `ocr_from_file(image_path)` | 识别文件 |
| `ocr_from_window(hwnd, region)` | 识别窗口 |
| `ocr_from_screen(region)` | 识别屏幕 |

**region**: [x1,y1,x2,y2] 左上右下坐标，None为整屏

## xbot.ai.AliyunAI

| 方法 | 说明 |
|------|------|
| `ocr_from_file(image_path)` | 识别文件 |
| `ocr_from_window(hwnd, region)` | 识别窗口 |
| `ocr_from_screen(region)` | 识别屏幕 |

## xbot.ai.TencentAI

| 方法 | 说明 |
|------|------|
| `ocr_from_file(image_path)` | 识别文件 |
| `ocr_from_window(hwnd, region)` | 识别窗口 |
| `ocr_from_screen(region)` | 识别屏幕 |

## 示例

```python
from xbot import ai

ocr = ai.BaiduAI(api_key='xxx', secret_key='xxx')

# 识别文件
result = ocr.ocr_from_file('D:\\test.png')
print(result)

# 识别窗口
result = ocr.ocr_from_window(0x10412c, None)

# 识别屏幕区域
result = ocr.ocr_from_screen([100, 100, 200, 200])
```
