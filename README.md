# tinydns2postfix

TinyDNSのゾーンファイルから PostfixをセカンダリMXとして使用するための transportファイルを自動生成するプログラム

python2用

## postfixの設定

### /etc/postfix/main.cf

```
inet_interfaces = all
relay_domains = hash:/etc/postfix/transport
smtpd_recipient_restrictions = permit_mynetworks permit_auth_destination reject_unauth_destination
transport_maps = hash:/etc/postfix/transport
```

## cronジョブの内容

- 1.2.3.4 = セカンダリMXとして使用するサーバのIPアドレス(ゾーンファイル内MXレコード自体に記述のあるもの)
- data = TinyDNSのゾーンファイル（複数指定可）

```
tinydns2postfix.py 1.2.3.4 /path/to/tinydns/data > /etc/postfix/transport && postmap /etc/postfix/transport
```
