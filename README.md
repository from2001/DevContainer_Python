# DevContainer_Python
Dev ContainerでPythonの環境を構築するサンプルです。

## Container 

### 設定ファイル
[.devcontainer/devcontainer.json](.devcontainer/devcontainer.json)

### イメージ
Python 3.11入りDebianのイメージを利用

### インストールされるVS Codeのエクステンション
 - Python Debugger
 - Markdown Preview Mermaid Support
 - Jupyter

### 初回実行
#### 仮想環境構築
```
python -m venv .venv
```

#### 必要パッケージインストール
```
pip install -r requirements.txt
```

### 接続時実行
素数を100個表示
```
python demo.py
```


