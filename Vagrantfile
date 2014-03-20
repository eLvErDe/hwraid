Vagrant.configure('2') do |config|
  config.vm.box = 'debian-7-amd64-plain'

  config.vm.provider :virtualbox do |virtualbox, override|
    override.vm.box_url = 'http://vagrant-boxes.cargomedia.ch/virtualbox/debian-7-amd64-plain.box'
  end

  config.vm.provision 'shell', inline: [
    'sudo apt-get install -y build-essential quilt debhelper libstdc++5',
  ].join(' && ')
end
