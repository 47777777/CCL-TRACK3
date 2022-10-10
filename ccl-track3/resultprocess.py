from tqdm import tqdm
'''
由于bart的词表里面有一些词并不包括，我们在训练时忽略了这个问题，导致预测的文本中存在[UNK],因此这样的句子我们并不修改
'''
file_data=''
with open("seq2seq-result.txt", 'r', encoding='utf-8') as f:
    with open("test.src", 'r', encoding='utf-8') as f1:
      with open("test_gector.txt", 'r', encoding='utf-8') as f2:
            datas=f.readlines()
            datas1=f1.readlines()
            datas2=f2.readlines()
            for data,data1,data2 in zip(datas,datas1,datas2):   
                a,b=data[0:-1].split('\t')
                c=data1[0:-1].split('\t')
                c=c[0]
                d=data2[0:-1].split('\t')
                d=d[0]
                b=b.replace("##","")
                b=b.replace(" ","")
               
                if '[UNK]' in b:  
                    b=c

                if float(a)<(-0.45):  #置信度分数，筛掉不好的结果，可以改动
                    b=c

                if b!=c:
                  r=b
                else:
                  r=d

        
                line=c+'\t'+r+'\n'
                file_data+=line  
  
with open("predict.txt", 'w', encoding='utf-8') as f:
  for i in file_data:
    f.write(i)
  f.close()
