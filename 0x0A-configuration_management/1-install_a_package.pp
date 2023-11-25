# Using Puppet, install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
# Ensure Werkzeug version 2.1.1

package { 'Werkzeug':
ensure => '0.16.1',
provider => 'pip3',
}
