
## 基于python的scrapy爬虫，爬取链家网成都地区新房源，并用高德api在地图上可视化显示

1.效果图如下
![image](https://github.com/happyte/buyhouse/blob/master/1.png)
![image](https://github.com/happyte/buyhouse/blob/master/2.png)
![image](https://github.com/happyte/buyhouse/blob/master/3.png)
![image](https://github.com/happyte/buyhouse/blob/master/4.png)


2.工程里面已经有爬取后的rent.csv文件，可以删除，然后执行命令`scrapy crawl fangjia rent.csv -t csv`生成csv文件
3.爬取完成后，执行命令`python -m SimpleHTTPServer 3000`,然后打开`http://localhost:3000/`,点击打开demo.html，导入上面生成的rent.csv文件即可。
