# 導入方法   

## 前提 
VSCode、Dockerがインストール済みである

## 目指すこと
APIサーバーをデバッグモードで起動し、取得したjsonデータをブラウザに表示する

## 手順   
1. 当プロジェクトをローカル環境にクローンする   
2. VSCodeに Remote - Containers(ms-vscode-remote.remote-containers) をダウンロードする 
3. VSCodeでクローンした当プロジェクトのフォルダを開く。  
VSCode左のエクスプローラー画面には、「.devcontainer」「fastapi」「mysql」「.gitignore」「README.md」が並んでいることを確認する
4. VSCode画面左下に出ている「>< Dev Container: Python」を押下する
5. 表示されたプルダウン内の「Reopen in Container」を押下する
6. コンテナが作成されたら、上部メニューの「実行」→ 「デバッグの開始」をクリックし、サーバーを起動する   
7. ターミナルに以下の表示が出てサーバーが起動したことを確認する  
```
INFO:     Started server process [296]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
8. サーバー起動したら、ブラウザを開き http://localhost:8000/docs にアクセスし Swagger UI を表示する
9 「POST」の「 /users/ create User」を押下する
10. プルダウンリスト上部の「Try it out」を押下する
11. 表示された json を編集し、任意のユーザー情報を作成する
12. 「Execute」を押下する
13. http://localhost:8000/users にアクセスし、先程作成したユーザー情報がブラウザに表示されることを確認する

