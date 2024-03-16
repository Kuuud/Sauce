# 作者(Author)：TonaSmith
# 链接(URL)：https://caoyongzhuo.cn/archives/466
#适用于序号编排的图片如1.png、2.png……

filename="D:\\文档\\imgs.txt"    /*输出目录及文件名*/
randimgs=open(filename,"a")
for numbers in range(1,12):       /*输出序号，这里是从1输出到12*/
    randimgs.write("https://cdn.jsdelivr.net/gh/dogsking/randompicturePC/images/"+str(numbers)+".webp\n")   /*修改此处的图片地址*/
randimgs.close()