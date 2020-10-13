PHP:7.3-FPM (php-product)
    - port: 9000
        * docker-php-ext-install mysqli
        * docker-php-ext-install pdo_mysql
    - Work Directory: /home/sites/site1


APACHE HTTPD (c-httpd01)
    - port 80, 443
    - config /usr/local/apache2/conf/httpd.conf
        * Uncomment mod-proxy, mod_proxy_fcgi
        * Work Directory: /home/sites/site1
        * index by default index.php index.html
        *PHPHANDLER AddHandler "proxy:fcgi://php-product:9000" .php
    

MYSQL: (mysql-product)
    - port: 3304
    - config: /etc/mysql/my.cnf
        * default-authentication-plugin=mysql_native_password
    - databases: /var/lib/mysql -> /Users/bnmac/Documents/Travail/docker/compose/db
    - MYSQL_ROOT_PASSWORD: 123abc
    - MYSQL_DATABASE: db_site
    - MYSQL_USER: siteuser
    - MYSQL_PASSWORD: sitepass


NETWORK:
    - bridge
    - my-network

    
