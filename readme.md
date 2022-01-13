# 微信电脑版跳一跳小游戏辅助

# 概述
本程序帮助用户完成跳跃动作，但是需要用户手动在本程序弹出的页面中双击鼠标左键方式标记游戏主角将要跳跃的位置

# 运行环境
windows 10 微信电脑版 跳一跳小游戏
# 安装依赖

``python 3.7``


依赖的 python3 模块：
```bash
pip install pywin32
pip install opencv-python
pip install numpy
pip install Pillow
```

# 使用方法
1. 打开微信小程序中的跳一跳小程序
2. 将小程序窗口拖到屏幕边上(露出游戏完整窗口)
3. 进入到开始游戏的画面
4. 打开此程序``python3 jump.py``
5. 等待显示的新的黑白色的游戏窗口画面
6. 使用鼠标双击标记要跳越的新的目的位置，按任意键继续