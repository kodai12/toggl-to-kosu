## toggl-to-kosu

### 使い方
1. togglのレポート機能から`Detailed`をクリック=>日付の範囲を選択=>`Download CSV`をクリックし`toggl_to_kosu.csv`というファイル名にリネームし同じディレクトリ上に保存
2. `python toggl_to_kosu.py`を実行
3. `output.csv`というファイルが生成される

### 注意点
- togglのタグ機能でタスクのカテゴリー分けをしているのでカテゴリーは先にタグに登録しておいて毎回タグ付けを忘れないようにする
