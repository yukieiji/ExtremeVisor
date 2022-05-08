# ExtremeVisor
Extreme RolesのアドオンであるExtreme Skinsのバイザーデータ管理用リポジトリ<br>
Extreme Skins以外のMOD(Extreme Skinsのフォーク等も含めて)でこのリポジトリのデータを使用する場合、このリポジトリ自体のライセンス(使用規約)を読み把握した上で各ネームプレートのグループにのライセンス(使用規約、LICENSE.md)に従って下さい<br>
このリポジトリのライセンスは[こちら](https://github.com/yukieiji/ExtremeNamePlate/blob/main/LICENSE.md)

## 新しいバイザーの追加方法
0. 必要であれば、ExtremeVisorの下に新しいフォルダを作る(フォルダがグループ分けの目安になりますローマ字推奨、日本語等は使用しない)
1. 追加したいネームプレートの画像データ(名前はローマ字推奨、日本語等は使用しない、透過pngファイル)を追加したいグループのフォルダ入れる
2. ゲームを再起動する

- エラーが出た場合
  - AmongUs.exeのあるフォルダのBepInExの下にLogOutput.txtがあります。正しくロードできているとそのログの途中に以下の様な出力が出ているはずです
    - ```[Info   :Extreme Skins] Visor Loaded:（ネームプレートの画像名）, from:（ロードしているファイル名）```

#### 身内内専用のネームプレートを追加して遊ぶ場合は[Impostor](https://github.com/Impostor/Impostor)等のカスタムサーバーの使用をおすすめします
