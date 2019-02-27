# GetTwitterStream

## 概要

TwitterStreamingAPIを呼び出して、Tweetを取得する  
以前、Rubyで作成していたものをPythonで書き直したもの

## Usage

- 必要なモジュールをインストールします

> pip install requests_oauthlib  

- 実行

> python get_twitter_stream.py  

- 取得した結果は、"年月日時.txt" の書式のファイルに書き出される
- 無限ループで取得し続けるので、ctrl-C などで停止する

## 出力形式

出力は、各行に１Tweetで以下の項目をTSVで記述している

- TweetID
- 年月日 時分秒
- ユーザ名
- ユーザID
- ユーザアカウント作成の年月日時分秒
- ユーザのTweet数
- ユーザのFriend数
- ユーザのFollower数
- 該当TweetのReTweet数
- 該当Tweetのいいね数
- 該当Tweetの本文

※ReTweet数、いいね数は、Tweet時には0であり、このプログラムでの収集では0のままである。  
  別途、Tweet情報を取得する際に同一形式を使うことを想定して項目として記載している

## 特記事項

get_twitter_stream.py 内に記載してある  

- API_KEY
- API_SECRET
- ACCESS_TOKEN
- ACCESS_SECRET  

は、Twitterから取得して書き換えないと動作しない
