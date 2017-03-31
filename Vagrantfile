INTERPRETERS =  [
    "3.6.0",
    "3.5.2",
    "3.4.5",
    "3.3.6",
    "2.7.13",
    "2.6.9",
    "pypy2-5.6.0"
],

PYENV_BIN_PATH = "/home/vagrant/.pyenv/bin"

Vagrant.configure("2") do |config|
    config.vm.define :lin do |lin|
        lin.vm.box = "obestwalter/tox-dev-arch-linux"
        lin.vm.provider "virtualbox" do |vb|
            vb.memory = "2048"
        end
        prepDevenv = <<-HEREDOC
            if [ -d "#{PYENV_BIN_PATH}" ]; then
                #{PYENV_BIN_PATH}/pyenv update
            else
                sudo pacman --noconfirm -S base-devel openssl zlib git xz
                curl pyenv.run | sh
                sed -i '$ a\\export PATH="$HOME/.pyenv/bin:$PATH"' .bashrc
                sed -i '$ a\\eval "$(pyenv init -)"' .bashrc
                sed -i '$ a\\export TMPDIR="#{GUEST_TMP_DIR}"' .bashrc
                sed -i '$ a\\cd #{PROJECTS_MOUNT}' .bashrc
            fi
            export PATH="#{PYENV_BIN_PATH}:$PATH"
            eval "$(pyenv init -)"
            echo #{INTERPRETERS.join(" ")}
            for version in #{INTERPRETERS.join(" ")}; do
                pyenv install -s $version
            done
            pyenv global #{INTERPRETERS.join(" ")}
            pip install -U tox
            pip install -U -e /vagrant
            # pytest fails with ImportMismatchError if we don't tidy up
            find /vagrant -name '*.pyc' -delete
        HEREDOC
        lin.vm.provision "shell",
            name: "prepare devenv",
            inline: prepDevenv,
            privileged: false
    end

    # No automation here yet, just the bare box wating to be configured ...
    config.vm.define :win do |win|
        win.vm.box = "inclusivedesign/windows10-eval"
    end
end
