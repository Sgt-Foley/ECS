#Tailscale 内网穿透

#中转服务器环境配置
{
    apt update && apt upgrade #软件更新
 
    apt install -y wget git openssl curl #下载软件
 
    wget https://go.dev/dl/go1.20.5.linux-amd64.tar.gz #下载go
 
    rm -rf /usr/local/go && tar -C /usr/local -xzf go1.20.5.linux-amd64.tar.gz #解压安装go
 
    export PATH=$PATH:/usr/local/go/bin #环境变量
    go version #检查版本
 
    echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
    source /etc/profile #环境变量
 
    go env -w GO111MODULE=on
    go env -w GOPROXY=https://goproxy.cn,direct #go代理设置
 
    go install tailscale.com/cmd/derper@main #下载tailscale
 
    go build -o /etc/derp/derper #编译derper
 
    ls /etc/derp #检查编译情况
 
    openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes -keyout /etc/derp/derp.myself.com.key -out /etc/derp/derp.myself.com.crt -subj "/CN=derp.myself.com" -addext "subjectAltName=DNS:derp.myself.com" #启动derper
 
    cat > /etc/systemd/system/derp.service <<EOF
    [Unit]
    Description=TS Derper
    After=network.target
    Wants=network.target
    [Service]
    User=root
    Restart=always
    ExecStart=/etc/derp/derper -hostname derp.myself.com -a :33445 -http-port 33446 -certmode manual -certdir /etc/derp
    RestartPreventExitStatus=1
    [Install]
    WantedBy=multi-user.target
    EOF #设置deper服务

    systemctl enable derp
    systemctl start derp #检查连接情况
}

#隐藏中转服务器
{
    curl -fsSL https://tailscale.com/install.sh | sh #下载tailscale

    tailscale up #启动tailscale
 
    nano /etc/systemd/system/derp.service #修改service
 
    --verify-clients #添加参数
 
    systemctl daemon-reload #重新载入服务
 
    systemctl restart derp #重启服务
}