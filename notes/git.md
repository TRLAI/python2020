# Git基本命令

## git config // 配置命令

```
// 配置全局用户名
git config --global user.name "ZhangSan"
// 配置全局邮箱
git config --global user.email "1@1.com"
// Mac有可能会需要配置
git config --global core.editor vim
```

## git clone  // 克隆仓库

```
// 克隆教学仓库
git clone https://github.com/TRLAI/python2020.git
```

## git status // 查看仓库状态

```
git status
```

## git branch // 分支查看

```
// 查看本地分支
git branch
// 查看本地和远程分支
git branch -a
```

## git checkout // 切换分支，等等

```
// 切换并创建本地的**test**分支
git checkout -b test
// 切换到主分支
git checkout master
```

## git add // 向仓库中添加未被跟踪的文件或文件夹

```
// 添加单个文件**README.md**
git add README.md
// 添加文件夹**test**
git add test/
```

## git commit // 提交

```
// 提交，直接添加提交的信息
git commit -m "提交信息"
// 提交，用编辑器添加提交信息，需要提前设置好编辑器
git commit
```

## git push // 推送提交到远程仓库

```
// 推送提交信息到远程仓库的**master**分支
git push origin master
```

## git pull //从远程仓库下拉代码

```
// 下拉远程**master**分支，并合并到本地当前分支
git pull origin master
```

## git init // 在项目目录下，创建一个空的本地仓库

```
cd workdir
git init
```

## git 删除远程分支

```
git push origin --delete sunjiaqi
```