VER = "0.0.1 20230414"

CREDIT = '''
=*= Translator Tools =*=
Made by @Sunnyboy971(https://github.com/Sunnyboy971)
'''

LOCALE = "zh-CN"

COMMAND = {
    "main": ["help", "exit", "replace"],
    "replace": ["exit", "mode", "help", "saveas", "preview"]
}

CLI = {
    "na": ["Not Available", "内容暂时不可用。"],
    "sym": [["Fatal", "Error", "Warning", "Info", "Info"], ["致命错误", "错误", "警告", "提示", "信息"]],
    "nae": ["Alternatives not found.", "无可用候选项。"],
    "pre": [["one", "at least one"], ["一个", "至少一个"]],
    "default": ["Default:{}", "默认值：{}"],
    "0ed": ["Using default: ", "将使用默认值："],
    "0e": ["You must choose {} from the list.", "必须从列表中选择{}选项。"],
    "kbi": ["User cancelled the process.", "用户已取消。"],
    "eof": ["EOF received! Exiting...", "收到 EOF 了！正在退出..."],
    "ve": ["Answer with integers please.", "请输入整数以选择。"],
    "or": ["Choice out of range.", "输入超出了范围。"],
    "nmc": ["Multiple choices aren't allowed.", "不允许多选。"],
    "argcmd": ["Args: [? for help] ", "参数：[输入 ? 获取帮助] "]
}

SHARED = {
    "title": ["Main menu", "主菜单"],
    "target": ["Target file:", "目标文件："],
    "cnf": ["Command not found.", "未找到命令。"],
    "unknownerror": ["An unknown error just occurred. Please report the problem at your convience on Github.", "发生未知错误。如有可能，还请您在 Github 上报告问题。"],
    "choice": ["Selection:", "选择："]
}

REPLACE = {
    "title": ["Replace", "替换"],
    "modelist": [["Simple", "Advanced", "Template"], ["简单模式", "高级模式", "批处理模板"]],
    "source": ["String to be replaced:", "待替换字符串："],
    "target": ["Replace to:", "替换为："],
    "replaceall": ["Replace all occurences in the file?", "全部替换吗？"]
}

HELP = {
    "main": [],
    "replace": []
}
