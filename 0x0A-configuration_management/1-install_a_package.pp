# install flask
package { 'Flask':
  ensure   => 'present',
  provider => 'pip3',
}
