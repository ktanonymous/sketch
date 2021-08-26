#!/bin/bash

# -pオプションは間にスペースを入れると上手く動作しないので注意
# ref: https://dev.mysql.com/doc/refman/5.6/ja/command-line-options.html
mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DEFAULT_DATABASE} --default-character-set=utf8
