<<-DOC
Start a virtualbox image with
    * all supported interpreters installed
    * tox installed
    * this folder mapped read/writable to /vagrant
    * convenient way to ssh into the box

This should work from Windows, macOS and Linux.

To run tests in the box do:
    $ cd </path/to/where/this/file/is>
    $ vagrant up arch
    $ vagrant ssh arch
    $ tox

Prerequisites: https://www.vagrantup.com/ and https://www.virtualbox.org/
DOC

Vagrant.configure("2") do |config|
    config.vm.define :arch do |arch|
        arch.vm.box = "obestwalter/bindlestiff-arch-linux"
        arch.vm.provider "virtualbox" do |vb|
            vb.memory = "2048"
        end
    end
end
