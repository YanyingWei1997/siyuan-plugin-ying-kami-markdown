# YING Kami Markdown 样式

本插件把本机 Typora 的 `kami-work-notes.css` 直接适配到思源 Markdown 所见即所得编辑区。原始 CSS 以只读参考副本保存在 `assets/kami-work-notes.typora.css`，其 SHA-256 为：

```text
d66237ba0ef1aadbd1d0fb5a07dc822ffe6915145e074d3b3ac63461e2c5674c
```

## 思源适配说明

Kami 原文件的纸面变量是 `#fff8ed`。按当前要求，思源正文纸面改为纯白 `#ffffff`；字体、字号、标题层级、链接、列表、标记、波浪下划线和 macOS 代码框均沿用 Kami 原设定。适配层另外消除了思源引用块自带的第二条竖线，并将表格黄色底改为白色与中性灰，以匹配思源的编辑器 DOM。红圈标注不映射到思源。

插件不修改思源工具栏、侧栏、弹窗、设置页和窗口背景，应用外观保持官方 `daylight`。

正文采用响应式宽栏：宽屏最大 `1180px`，窗口缩小时自动保留安全边距。行内代码使用无阴影的平面样式。

## 字体

沿用 Kami 原文件：上图东观体、汇迹正楷、演示魁本楷、霞鹜文楷、Montserrat、Inter、Maple Mono / SF Mono。字体文件不打包，缺失时按原 CSS 回退。

## 自定义标记

- 代码块自定义属性 `code-title=标题`：显示居中代码标题；语言类型仍在右下角。
- 块属性 `decoration=blue-box`：使用 Kami 原版蓝框。

关闭插件即可恢复思源原始 Markdown 样式，不改变笔记数据。
