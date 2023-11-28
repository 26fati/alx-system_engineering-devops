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