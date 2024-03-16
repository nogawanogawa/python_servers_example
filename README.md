# servers

pythonでいろんなサーバーを立ててみる実験用リポジトリ

## 対象

- REST
- gRPC
- GraphQL

## How to use

### Docker Imageのビルド

```console
docker compose build
```

### 起動

```console
 % docker compose up
[+] Running 3/3
 ✔ Container servers-grpc-1     Recreated                                                                                                                                                                                                                                           0.1s 
 ✔ Container servers-rest-1     Recreated                                                                                                                                                                                                                                           0.2s 
 ✔ Container servers-graphql-1  Recreated                                                                                                                                                                                                                                           0.3s 
Attaching to graphql-1, grpc-1, rest-1
grpc-1     | Python 3.12.2 (main, Mar 12 2024, 08:11:26) [GCC 12.2.0] on linux
grpc-1     | Type "help", "copyright", "credits" or "license" for more information.
rest-1     | Python 3.12.2 (main, Mar 12 2024, 08:11:26) [GCC 12.2.0] on linux
rest-1     | Type "help", "copyright", "credits" or "license" for more information.
graphql-1  | Python 3.12.2 (main, Mar 12 2024, 08:11:26) [GCC 12.2.0] on linux
graphql-1  | Type "help", "copyright", "credits" or "license" for more information.
```

### 使い方

コンテナの中に入る

```console
docker container exec -it <container_id> bash
```

サーバーの起動(REST, GraphQL)

```console
uvicorn server:app --reload &
```

サーバーの起動(gRPC)

```console
python server.py &
```

リクエストの送信

```console
python client.py
Response: 0.7590885162353516
```

