#install nginx

exec { 'update':
    command => 'apt_get update',
}

package { 'nginx':
    ensure => 'installed',
}

exec { 'allow utf':
    command => 'ufw allow "Nginx HTTP"',
}

file { '/var/www/html/index.html':
    ensure => 'file',
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  '        rewrite ^/redirect_me https://www.youtube.com/ permanent;',
}

service { 'nginx':
  ensure => running,
}