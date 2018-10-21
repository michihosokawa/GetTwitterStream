# GetTwitterStream

## 概要
TwitterStreamingAPIを呼び出して、Tweetを取得する
以前、Rubyで作成していたものをPythonで書き直したもの

## Usage
> python get_twitter_stream.py  

- 取得した結果は、"年月日時.txt" の書式のファイルに書き出される 
- 無限ループで取得し続けるので、ctrl-C などで停止する

## 特記事項
get_twitter_stream.py 内に記載してある  
- API_KEY
- API_SECRET
- ACCESS_TOKEN
- ACCESS_SECRET  
は、それぞれ取得して書き換えること
