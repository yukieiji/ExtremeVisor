# ExtremeVisor
Extreme RolesのアドオンであるExtreme Skinsのバイザーデータ管理用リポジトリ<br>
Extreme Skins以外のMOD(Extreme Skinsのフォーク等も含めて)でこのリポジトリのデータを使用する場合、このリポジトリ自体のライセンス(使用規約)を読み把握した上で各ネームプレートのグループにのライセンス(使用規約、LICENSE.md)に従って下さい<br>
このリポジトリのライセンスは[こちら](https://github.com/yukieiji/ExtremeVisor/blob/main/LICENSE.md)

## 新しいバイザーの追加方法

### ExtremeSkins.Generatorを使用する場合
1. [ここ](https://github.com/yukieiji/ExtremeSkins.Generator/releases/latest)からExtremeSkins.Generatorの最新版をダウンロードする
  - エディションの違い、よくわからないって方はAllinOneをダウンロードして下さい(LightとAllinOneで機能の違いはありません)
    - AllinOne : 容量は大きいが何もしなくてもそのまま利用可能
    - Light : 容量は小さいが別途.NET 6.0 Runtimeのインストールが必要になります
2. ダウンロードしたZipファイルを適当な場所に展開する
3. 展開したフォルダの中にある「ExtremeSkins.Generator.exe」をダブルクリックして起動する
   - 起動しない場合はセキュリティソフトの設定を見直して下さい
4. 画面の「ExtremeVisor」を選択する
5. 必要なファイル等を画面に従って用意、選択するする
   - 画像ファイルの推奨サイズ300×375
6. エクスポートボタンを押す

### 手動でやる場合
1. AmongUs.exeのあるフォルダのExtremeVisorフォルダの下に新しいフォルダを作る(ローマ字推奨、日本語等は使用しない)
2. 以下の名前の画像ファイルを作る、idle.png以外は必要に応じて追加して下さい
   - idle.png : 正面右向き前のレイヤーの画像ファイル(ピクセルサイズ：300×375)
   - flip_idle.png : 正面左向き前のレイヤーの画像ファイル(ピクセルサイズ：300×375)
3. 以下を記入したinfo.jsonを作る(「,」の前に記載、#以降全ては消して下さい)
```
{
    "Author": , #製作者名、ローマ字スネークケースで記入、例"yukiEiji"
    "Name": , #スキンの名、ローマ字スネークケースで記入、例"overLoading"
    "LeftIdle": #true(ある)かfalse(ない)か,
    "Shader": #これがtrue(オン)の時、一部の色が体の色とシンクロします。シンクロしてほしくない場合はfalse(オフ)に,
    "BehindHat": #これがtrue(オン)の時、バイザーがハットの後ろになります,
    "comitHash": "" # 記載しなくて大丈夫
}
```
4. 追加後、ゲームを再起動するとスキンが追加されているはずです

- エラーが出た場合
  - AmongUs.exeのあるフォルダのBepInExの下にLogOutput.txtがあります。正しくロードできているとそのログの途中に以下の様な出力が出ているはずです
    - ```[Info   :Extreme Skins] Visor Loaded:（バイザーの画像名）, from:（ロードしているファイル名）```

## 他のMODのバイザーをExtremeVisor用に変換したい
- [ExtremeSkins.Converter](https://github.com/yukieiji/ExtremeSkins.Converter/releases/latest)を使用することで変換できます

#### 身内内専用のネームプレートを追加して遊ぶ場合は[Impostor](https://github.com/Impostor/Impostor)等のカスタムサーバーの使用をおすすめします

## バイサーを提供していただいた方々
- [猫野和錆](https://twitter.com/neko_wasa)様
- [YJ\*白桜](https://twitter.com/_Sakura_White_)様(ExtremeVisorで使えるようにデータ構造を変更しています(バイザーデータがGNU General Public License v3.0ライセンスのため詳細を記載))-
- [ひなにい](https://twitter.com/__xxhina)様
- アンハッピーセット様
- アドミン様
- からっぱもん様
- おやきもん様
- ラプ様
- クロドル様
- Nyayuta様
