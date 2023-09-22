# Welcome to your CDK pipeline project with Python

### 1) Start with Ubuntu instance in AWS. Instance profile with AdministrativeAccess policy.
- `sudo apt update && sudo apt upgrade -y`
- restart ec2 instance
- `sudo apt remove awscli -y`
- `sudo apt autoclean && sudo apt autoremove -y`
- `sudo apt-get install build-essential procps curl file git zsh -y`
- set zsh as default shell
  - `chsh -s $(which zsh)`
  - verify zsh is configured as default
    - `dpkg -l zsh`
    - `grep $USER /etc/passwd`
    - `grep zsh /etc/shells`
- relogin to ec2 instance
- verify current shell is zsh
  - `echo $0`
- install oh-my-zsh
  - https://ohmyz.sh/#install
  - `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- edit `.zshrc`
  - adjust preferred theme (eg `mh`)
  - ensure `plugins=(git)`

#### 2) install node version manager and node lts
- https://github.com/nvm-sh/nvm
- `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash`
- restart shell or try `source ~./zshrc`
- verify nvm is installed
  - `nvm --version`
- install node lts
  - `nvm install --lts`

#### 3) install homebrew
- from https://brew.sh/
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
  - `(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/ubuntu/.zshrc`
  - `eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"`
- verify brew is working
  - `brew doctor`

#### 4)Install aws-cli
- ensure aws-cli is installed
  - `brew install awscli`
  -  `aws s3 ls`

### You can skip all of the above if you are using your laptop (mac) and perform the followings
### 1) Install Node.js 
  - `npm install -g n`
  - `node --version`
  - `sudo n latest`
  - `node --version`

### 2) Install the AWS CDK Toolkit (the cdk command):
  - `npm install -g aws-cdk`
  - `cdk --version`
  - `brew install awscli`

## ------------------------------

#### 1) configure git

- `git config --global user.name "Your Name"`
- `git config --global user.email "your.email@email.com"`
- can also do additional configs like alias

#### 2) setup git 

- `brew install git-remote-codecommit`
- `brew install git-secrets`
  - local repo setup
    - `cd /path/to/my/repo`
    - `git secrets --install`
    - `git secrets --register-aws`
  - global
    - `git secrets --register-aws --global`
    - `git secrets --install ~/.git-templates/git-secrets`
    - `git config --global init.templateDir ~/.git-templates/git-secrets`

#### 3) CDK bootstrap

  - `git clone https://github.com/pnagwekar/cdk-pipeline.git my_pipeline`
  - `cd my_pipeline`
  - `mkdir bootstrap && cd bootstrap`
  - `npx cdk@2 bootstrap --trust 12345678910 aws://12345678910/us-east-1 --cloudformation-execution-policies "arn:aws:iam::aws:policy/AdministratorAccess"`
  - `cd .. && rm -rf bootstrap`


#### 4) install dependencies
  - `source .venv/bin/activate # Enter your isolated python env`
  - `pip install -r requirements.txt # Install required python modules`

#### 5) deploy a pipeline manually once
  - `git add --all`
  - `git commit -m "initial commit"`
  - `git push`
  - `cdk deploy`


