import pdfkit
import pypandoc
import os

def get_file_name(file_list,outlist):
    print('【当前目录】Markdown文件如下：')
    for each in os.listdir():
        if ".md" in each:
            file_list.append(each)
            print(each)
            filename=each.replace('.md','.pdf')
            outlist.append(filename)
    print('检索完毕')
def convert(input,output):
    pypandoc.convert_file(input, 'html', outputfile='tmp.html')
    html_head_file = open("html_head.txt", "r", encoding='utf-8')
    html_head = html_head_file.read()
    html_head_file.close()
    html_tail = "\n</body>\n</html>"
    html_body_file = open('tmp.html', "r", encoding='utf-8')
    html_body_txt = html_body_file.read()
    html_body_file.close()
    html_body = html_head + html_body_txt + html_tail
    with open('tmp.html', 'w', encoding='utf-8') as f:
        f.write(html_body)
        f.close()
    pdfkit.from_file('tmp.html', output, options={"enable-local-file-access": None})
    if os.path.exists('tmp.html'):
        os.remove('tmp.html')
    print(input+'转换成功！')

filelist=[]
otfilename=[]
get_file_name(filelist,otfilename)
for i in range(len(filelist)):
    convert(filelist[i],otfilename[i])

