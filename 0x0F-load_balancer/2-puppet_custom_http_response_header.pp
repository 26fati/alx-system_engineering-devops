# Use Puppet to automate the task of creating a custom HTTP header response
exec { 'insert_header_line':
  command => "sed -i '56i\\tadd_header X-Served-By \$hostname;' /etc/nginx/sites-enabled/default",
  path    => ['/bin', '/usr/bin'],
}
exec {'run':
  command => '/usr/sbin/service nginx restart',
}