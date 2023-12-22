# kills a process named killmenow
exec { 'killmenow':
  command => 'pkill -TERM killmenow',
}
