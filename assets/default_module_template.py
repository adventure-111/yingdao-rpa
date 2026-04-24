# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from . import package
from .package import variables as glv


def _do_task():
    """
    业务逻辑函数（供 main 调用）
    """
    print("开始执行任务")

    # --- 示例：读取资源文件 ---
    # data = package.resources.get_text('config.json', encoding='utf-8')

    # --- 示例：元素操作 ---
    # browser = xbot.web.create('https://example.com', mode='cef')
    # try:
    #     browser.find(package.selector('登录按钮')).click()
    # finally:
    #     browser.quit()

    # --- 示例：Excel操作 ---
    # workbook = xbot.excel.open('D:\\data.xlsx', kind='office', visible=True)
    # try:
    #     sheet = workbook.get_sheet_by_name('Sheet1')
    #     value = sheet.get_cell(1, 'A')
    #     print(f"读取到: {value}")
    #     workbook.save()
    # finally:
    #     workbook.close()

    # --- 示例：全局变量 ---
    # glv.set('last_result', 'some_value')
    # saved = glv.get('last_result')

    print("任务执行完成")


def main(args):
    """
    入口函数 - 影刀独立运行或通过"调用模块"指令触发时执行

    参数:
        args: 影刀传递的参数（字典或None）
    """
    try:
        _do_task()
    except Exception as e:
        print(f"执行异常: {e}")
        # 异常处理：根据需要重试或上报
        raise
