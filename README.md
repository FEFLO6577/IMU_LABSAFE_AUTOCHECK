# IMU化学化工学院实验室安全打卡自动脚本

本项目是一个用于 **内蒙古大学（IMU）化学化工学院** 实验室安全每日打卡的自动化脚本。通过 GitHub Actions，脚本可以每天自动运行，完成实验室安全打卡任务。

---

## 功能特性

- **自动化打卡**：每日定时自动完成实验室安全打卡。
- **GitHub Actions 集成**：无需本地运行，通过 GitHub Actions 实现云端自动化。
- **灵活配置**：支持自定义打卡时间和学号密码。
- **跨平台支持**：基于 Selenium 和 Chrome，兼容 Windows、Linux 和 macOS 系统。

---

## 使用说明

### 1. Fork 项目
点击右上角的 `Fork` 按钮，将本项目复制到您的 GitHub 仓库。

### 2. 修改学号和密码
- 打开 `login_script.py` 文件。
- 找到以下代码段，替换为您的学号和密码：
  ```python
  USERNAME = "您的学号"
  PASSWORD = "您的密码"
  ```

### 3. 配置 GitHub Actions
- 确保项目的 GitHub Actions 已启用。
- 打卡时间默认为 **每天 7:00**，如需修改，请编辑 `.github/workflows/main.yml` 文件中的 `cron` 表达式：
  ```yaml
  schedule:
    - cron: '0 23 * * *'  # 每天 UTC 时间 23:00（北京时间 7:00）
  ```

### 4. 运行脚本
- 提交更改后，GitHub Actions 会自动运行脚本。
- 您可以在项目的 `Actions` 选项卡中查看运行日志。

---

## 项目结构

```
IMU_LABSAFE_AUTOCHECK/
├── .github/
│   └── workflows/
│       └── daily_checkin.yml  # GitHub Actions 工作流文件
├── login_script.py            # 打卡脚本主程序
├── requirements.txt           # Python 依赖列表
└── README.md                  # 项目说明文件
```

---

## 依赖环境

- Python 3.8+
- Selenium
- Chrome 浏览器
- Chromedriver

### 安装依赖
运行以下命令安装所需依赖：
```bash
pip install -r requirements.txt
```

---

## 注意事项

1. **隐私保护**：
   - 请勿将您的学号和密码直接提交到公共仓库。建议使用 GitHub Secrets 存储敏感信息。
   - 如需使用 Secrets，请参考 [GitHub Secrets 官方文档](https://docs.github.com/en/actions/security-guides/encrypted-secrets)。

2. **打卡时间**：
   - 默认打卡时间为每天 7:00（北京时间），请根据需求调整 `cron` 表达式。

3. **脚本稳定性**：
   - 如果打卡页面结构发生变化，可能需要更新脚本中的元素定位逻辑。

---

## 常见问题

### 1. 脚本运行失败怎么办？
- 检查 GitHub Actions 日志，确认错误原因。
- 确保学号和密码正确。
- 确保 Chrome 和 Chromedriver 版本匹配。

### 2. 如何修改打卡时间？
编辑 `.github/workflows/main.yml` 文件中的 `cron` 表达式。例如：
- 每天 8:00 打卡：`0 0 * * *`（UTC 时间 0:00，北京时间 8:00）
- 每天 12:00 打卡：`0 4 * * *`（UTC 时间 4:00，北京时间 12:00）

### 3. 如何本地运行脚本？
- 安装 Chrome 浏览器和 Chromedriver。
- 运行以下命令：
  ```bash
  python login_script.py
  ```

---

## 致谢

- 本项目参考自 [trae](www.trae.com.cn)，感谢AI编程软件。
- 感谢各位大佬的改进建议，欢迎提交 Issue 或 Pull Request。

---

## 许可证

本项目基于 [MIT License](LICENSE) 开源。

---

## 支持与反馈

如有任何问题或建议，请提交 [Issue](https://github.com/FEFLO677/IMU_LABSAFE_AUTOCHECK/issues) 或通过邮件联系我。

---

希望这份 `README.md` 文件能帮助用户更好地理解和使用您的项目！如果有其他需求，请随时告诉我！
