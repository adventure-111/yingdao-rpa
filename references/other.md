# Other 模块

## xbot.ado

数据库操作

| 方法 | 说明 |
|------|------|
| `Database()` | 创建数据库对象 |
| `open(conn_str)` | 连接数据库 |
| `exec(sql)` | 执行SQL |
| `close()` | 关闭 |

## xbot.ftp.FTPBase

| 方法 | 说明 |
|------|------|
| `connect(host, port, user, password)` | 连接FTP |
| `upload(local_path, remote_path)` | 上传 |
| `download(remote_path, local_path)` | 下载 |
| `list_files(path)` | 列出文件 |
| `delete_file(path)` | 删除文件 |
| `close()` | 关闭 |

## xbot.xzip

| 方法 | 说明 |
|------|------|
| `zip(source, dest)` | 压缩 |
| `unzip(source, dest)` | 解压 |

## xbot.pdf

| 方法 | 说明 |
|------|------|
| `read_text(file_path)` | 读取文本 |
| `extract_images(file_path, dest)` | 提取图片 |
| `export_pages(file_path, dest, pages)` | 导出页面 |

## xbot.logging

| 方法 | 说明 |
|------|------|
| `info(msg)` | 普通日志 |
| `warning(msg)` | 警告日志 |
| `error(msg)` | 错误日志 |

## 示例

```python
from xbot import ado, ftp, xzip, pdf, logging

# 数据库
db = ado.Database()
db.open('连接字符串')
result = db.exec('SELECT * FROM table')
db.close()

# FTP
f = ftp.FTPBase()
f.connect('host', 21, 'user', 'pwd')
f.upload('local.txt', '/remote.txt')

# PDF
text = pdf.read_text('D:\\test.pdf')

# 日志
logging.info('操作开始')
```
