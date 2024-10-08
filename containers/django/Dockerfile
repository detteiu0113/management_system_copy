# Pythonのイメージを指定
FROM python:3

# PYTHONDONTWRITEBYTECODEとPYTHONUNBUFFEREDはオプション
# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1

# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1

# コンテナのワークディレクトリを/codeに指定
WORKDIR /code

# ローカルのrequirements.txtをコンテナの/codeフォルダ直下に置く
COPY requirements.txt /code/

# コンテナ内でpipをアップグレードした後、pip install -r requirements.txtを実行
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ソースコードをコンテナにコピー
COPY . /code/
COPY ./containers/django/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY ./containers/django/cron.sh /root/script/
RUN chmod +x /usr/local/bin/entrypoint.sh

# cronをインストール
RUN apt-get update && apt-get install -y cron

RUN echo '1 0 1 3 * sh /root/script/cron.sh' > /var/spool/cron/crontabs/root
RUN crontab /var/spool/cron/crontabs/root

# エントリーポイントの設定
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]