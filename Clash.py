# clash环境配置
{
    # 安装包、country.mmdb文件建议提前下载
    gzip -d clash-linux-amd64.gz #解压对应版本号的clash
    mv clash-linux-amd64 clash #将clash名字改小
    chmod +x clash #赋予文件执行权限
    mv clash /usr/local/bin/clash #移动clash至bin目录
    clash -v #检查是否安装成功
    cd /usr/local/bin #进入clash所在目录
    ./clash #初次运行clash并初始化
    # config.yaml\country.mmdb文件配置
    cd root/.config/clash #进入参数文件目录
    vim config.yaml #运用vim编辑器编辑
    # config.yaml参数文件
    {
        port: 7890 # HTTP端口
        socks-port: 7891 # SOCKS5端口
        allow-lan: true #允许局域网内设备访问
        mode: Rule #规则Rule / Global / Direct
        log-level: info #信息长度info / warning / error / debug / silent
        proxies: #你的梯子订阅内容

        # 可选：访问网址 http://clash.razord.top/#/proxies 进行相关配置
        external-controller: '0.0.0.0:9090' #控制面板端口(需开放对应防火墙端口)
        secret: "password" # 控制面板密码，账号为主机ip地址
    }
    cp config.yaml /etc/clash/ 
    cp Country.mmdb /etc/clash/  # 复制参数至etc目录，不知道是不是有用
    cd /usr/local/bin #进入clash目录
    ./clash #运行clash检查是否配置成功
}

#Clash相关操作
{
    cd /usr/local/bin/    # 进入存放clash目录
    ./clash         # 终端运行当前目录clash
    nohup ./clash > /dev/null 2> /dev/null & # 后台运行clash并生成自动删除的临时日志
    ps -ef|grep clash #查找clash进程
    pkill -9 clash #杀死clash进程(不需要进程号)
    curl -I https://www.google.com/ #测试系统代理
}