from datetime import datetime
from flask import Flask, render_template_string, request, send_file
import io

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>每日任務表產生器</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2em; }
        textarea { width: 100%; height: 400px; margin-top: 1em; }
        button { margin-top: 1em; padding: 0.5em 1em; }
    </style>
</head>
<body>
    <h1>每日任務表產生器</h1>
    <form method="post">
        <button type="submit">產生任務表</button>
    </form>
    {% if task_md %}
    <h2>Markdown 預覽：</h2>
    <textarea readonly>{{ task_md }}</textarea>
    <form method="post" action="/download">
        <input type="hidden" name="content" value="{{ task_md }}">
        <button type="submit">下載 Markdown 檔</button>
    </form>
    {% endif %}
</body>
</html>
"""

def generate_daily_task_template(date=None):
    if date is None:
        date = datetime.today().strftime('%Y/%m/%d')

    template = f"""# 每日任務規劃表（{date}）

## 今日重點目標（最多三項）
- [ ] 1. 
- [ ] 2. 
- [ ] 3. 

---

## 任務拆解與時間預估

### 1. 
- [ ] 子任務1（30分鐘）
- [ ] 子任務2（30分鐘）
- [ ] 子任務3（60分鐘）

### 2. 
- [ ] 子任務1（30分鐘）
- [ ] 子任務2（30分鐘）

### 3. 
- [ ] 子任務1（30分鐘）
- [ ] 子任務2（30分鐘）

---

## 行事曆排程（建議使用 Google Calendar 或 Notion 實作）

| 時間段 | 任務內容 |
|--------|----------------|
| 09:00-09:30 | 任務A |
| 09:30-10:00 | 任務B |
| 10:00-11:00 | 任務C |

---

## 自我檢視（下班前）
- [ ] 今天的工作是否都完成？若沒有，原因是什麼？
- [ ] 是否有任務可以提前安排到明天？
- [ ] 今天學到的一件事是什麼？
"""
    return template

@app.route('/', methods=['GET', 'POST'])
def index():
    task_md = None
    if request.method == 'POST':
        task_md = generate_daily_task_template()
    return render_template_string(HTML_TEMPLATE, task_md=task_md)

@app.route('/download', methods=['POST'])
def download():
    content = request.form['content']
    buffer = io.BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="每日任務規劃表.md", mimetype='text/markdown')

if __name__ == '__main__':
    app.run(debug=True)
