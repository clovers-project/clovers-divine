<div align="center">

# Clovers Fortune

_✨ 今日运势和塔罗牌占卜合集 ✨_

[![python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![license](https://img.shields.io/github/license/KarisAya/clovers_fortune.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/clovers_fortune.svg)](https://pypi.python.org/pypi/clovers_fortune)
[![pypi download](https://img.shields.io/pypi/dm/clovers_fortune)](https://pypi.python.org/pypi/clovers_fortune)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

</div>

# 安装

```bash
pip install clovers_fortune
```

# 配置

<details>

<summary>在 clovers 配置文件内按需添加下面的配置项</summary>

```toml

```

# 说明

今日运势和 id 绑定

## 今日运势资源

本插件会遍历 `daily_fortune_resorce` 路径下的所有 `.png` `.jpg` `.jpeg` 文件作为插件的今日运势抽签主题
原版主题图片大小为 480\*480，如果需要添加主题图片请注意下面的规则
标题位置中心点是 (140, 99)，标题字号是 45
文本位置中心点是 (140, 297)，文本字号是 25，文本每行 9 字符最高支持 4 行（从右到左竖向排版）

## 塔罗牌资源

注意：资源中塔罗牌[碧蓝档案主题](./fortune/tarot/Blue%20Archive/) 依照原仓库 [GPL-3.0](https://github.com/Perseus037/nonebot_plugin_batarot?tab=GPL-3.0-1-ov-file#readme) 协议开源
其余资源遵循 [MIT](https://github.com/KarisAya/clovers_fortune/blob/main/LICENSE) 协议开源

本插件会认为 `tarot_resource` 路径下的每个文件夹都是一套主题。

建议主题下的文件夹有如下子路径

- MajorArcana 大阿卡纳
- Pentacles 星币
- Swords 宝剑
- Cups 星杯
- Wands 权杖

子路径下即为塔罗牌图片。

下面是图片的命名规则，对后缀名没有要求

```bash
└ MyTheme
  ├ Cups
  │ ├ 圣杯-01.png
  │ ├ 圣杯-02.png
  │ ├ ……
  │ └ 圣杯王后.png
  └ MajorArcana
    ├ 0-愚者.png
    ├ 01-魔术师.png
    ├ ……
    └ 21-世界.png
```

在抽牌时插件会随机一个主题，如果主题内没有对应卡片则会用其他主题的对应卡牌补位。

请注意资源内至少要有一套完整的塔罗牌主题。

# 鸣谢

[nonebot_plugin_fortune](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune)
[nonebot_plugin_tarot](https://github.com/MinatoAquaCrews/nonebot_plugin_tarot)
[nonebot_plugin_batarot](https://github.com/Perseus037/nonebot_plugin_batarot)
