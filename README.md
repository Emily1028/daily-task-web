# 每日任務表產生器（Daily Task Web）

這是一個用 Flask 製作的小工具，可以快速產生「每日任務 Markdown 模板」📋

🛠 適合：
- 想每天規劃任務，但不想每天重複貼格式
- 使用 Obsidian / VSCode / Notion 的人
- 執行實習、接案、自學等每日追蹤

---

## 🚀 Demo
部署在 Render 上之後，你可以打開你的網站看到：

> 點選「產生任務表」即可產出 Markdown，還能直接下載！

---

## 🧰 使用技術
- Python 3.10+
- Flask（Web 應用框架）
- Markdown 格式輸出

---

## 🖥 部署 Render 教學

### 📁 專案結構
```
app.py               # 主程式
requirements.txt     # 套件列表
```

### ✅ Render 設定
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`
- **環境版本**: Python 3.10+

> 注意：Flask 啟動時需綁定到 `0.0.0.0` 並讀取 Render 的 PORT，如下所示：

```python
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)
```

---

## 📄 授權
MIT License — 自由修改使用，不需告知！

---

如果覺得有幫助，幫我按個星星 ⭐ 或留言交流吧！
