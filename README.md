# Zen Music Recommender

## English

Zen Music Recommender is an emotion-aware music recommendation prototype that maps heart-rate input to an emotional state and returns a matching music experience. The project combines ECG-derived emotion modelling, a curated music metadata library, and a lightweight Flask web interface.

### Project Stage

Prototype / proof of concept

### Core Features

- Heart-rate BPM input with validation for realistic user values.
- Emotion mapping for `Happy`, `Sad`, and `Calm` states.
- Music recommendation from a structured JSON library.
- Dynamic playback page with album artwork, BPM display, emotion text, and synchronized visual animation.
- Lightweight feedback popup for checking whether the recommended music matches the user's perceived emotion.

### Methods

- ECG and heart-rate variability feature extraction using NeuroKit2.
- Feature set: `RMSSD`, `SDNN`, `LF_HF`, and average `BPM`.
- Random Forest classifier for emotion prediction.
- Flask routes for input handling, recommendation, result rendering, and playback reset.

### Results Snapshot

- 15 curated music records across 3 emotion classes.
- 5 tracks per emotion class.
- 50 BPM-to-emotion prediction mappings.
- BPM prediction range in the exported mapping: 52 to 131.
- Notebook training output accuracy: 83.33%.

### Repository Notes

The repository is prepared as a public project summary. Private identifiers and local environment details should not be included in public-facing documentation.

The public demo includes a minimal Flask template. Audio and image assets are not included unless their licenses allow redistribution.

### Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

Run smoke tests:

```bash
pip install -r requirements-dev.txt
python -m pytest
```

Additional public-safe demo evidence is documented in `docs/demo-evidence.md`.

## 中文

Zen Music Recommender 是一个情绪感知音乐推荐原型系统。项目将心率 BPM 输入映射到情绪状态，并根据情绪返回匹配的音乐体验。项目结合了 ECG 情绪建模、结构化音乐元数据和轻量级 Flask Web 界面。

### 项目阶段

原型 / 概念验证

### 核心功能

- 支持心率 BPM 输入，并对用户输入范围进行校验。
- 支持 `Happy`、`Sad`、`Calm` 三类情绪映射。
- 基于结构化 JSON 音乐库进行推荐。
- 播放页面展示专辑封面、BPM、情绪文案，并提供同步视觉动画。
- 提供轻量反馈弹窗，用于判断推荐音乐是否匹配用户主观感受。

### 方法

- 使用 NeuroKit2 从 ECG 数据中提取心率和心率变异性特征。
- 特征包括：`RMSSD`、`SDNN`、`LF_HF` 和平均 `BPM`。
- 使用 Random Forest 分类模型进行情绪预测。
- 使用 Flask 实现输入处理、推荐逻辑、结果渲染和播放重置。

### 成果概览

- 音乐库包含 15 条精选音乐记录，覆盖 3 类情绪。
- 每类情绪包含 5 首音乐。
- 导出 50 条 BPM 到情绪的预测映射。
- 预测映射中的 BPM 范围为 52 到 131。
- Notebook 训练输出准确率为 83.33%。

### 仓库说明

本仓库按公开项目展示方式整理。公开文档中不应包含个人身份标识或本地环境细节。

公开 demo 包含一个最小 Flask 模板。音频和图片素材只有在授权允许公开分发时才应加入仓库。

### 本地运行

```bash
pip install -r requirements.txt
python app.py
```

打开 `http://127.0.0.1:5000`。

运行基础测试：

```bash
pip install -r requirements-dev.txt
python -m pytest
```

脱敏后的 demo 证据记录在 `docs/demo-evidence.md`。
