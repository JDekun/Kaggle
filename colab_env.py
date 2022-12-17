#[[Colab]](https://colab.research.google.com/github/JDekun/DCNet/blob/dcnet/fcn/scripts/debug.ipynb?authuser=1) 
#@title [Colab] 构建Kaggle环境 && 下载数据集

'''
自动化代码，当值 colab 断路
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton,60000);
'''
# clearInterval()

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--datasets')
parser.add_argument('--github')
parser.add_argument('--branch')
args = parser.parse_args()

github = args.github
branch = args.branch
datasets = args.datasets

if os.path.exists('/content'):
  # 构建 working input 文件夹
  if not os.path.exists('/content/working'):
    os.mkdir("/content/working")
  if not os.path.exists('/content/input'):
    os.mkdir("/content/input")
  # 导入Kaggle API
  os.chdir('/content')
  os.environ['KAGGLE_CONFIG_DIR'] = '/content/Kaggle' #注意kaggle文件夹包含json文件 

  ######### 下载数据集 #########
  os.chdir('/content/input')
  datasets = datasets.split(",")
  len_mydekun = len(datasets)
  if len_mydekun != 0:
    for i in range(len_mydekun):
      # 下载 kaggle 数据集
      temp = datasets[i]
      name, dataset = temp.split('/')
      dirlist = os.listdir('/content/input')

      if (dataset in dirlist):
        print("您已经下载过'%s'数据集" % dataset)
      else:
        zip = dataset + '.zip'
        os.system("kaggle datasets download -d %s -p %s" % (temp,dataset))
        # 解压数据集并删除压缩包
        os.system("unzip %s/%s -d %s > /dev/null 2>&1" % (dataset,zip,dataset))
        os.system("rm -f %s/%s" % (dataset,zip))

######### 克隆GitHub库 #########
try:
  os.chdir("/kaggle/working/")
except:
  os.chdir("/content/working/")

os.system("git clone -b %s %s > /dev/null 2>&1" % (branch,github))   # 克隆 github 项目
print("All ready !")