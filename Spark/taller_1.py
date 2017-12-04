import json
chatsData = sc.textFile('file:///Users/manuelramoslg/Diplomado-Big-Data-PUC/Spark/chatlogs/*.json')
lines = chatsData.take(4)
print lines
struct_lines = [json.loads(line) for line in lines]
print json.dumps(struct_lines[0], indent=4)
chatsData.count()

def get_field(data, field):
        struct_data = json.loads(data)
        if type(field) != list:
            return struct_data[field]
        else:
            return tuple([struct_data[f] for f in field])

agentNames = chatsData.map(lambda chat: get_field(chat, "agentName"))
agentNames.take(10) # se visualizan 10 nombres

pairs_agent = agentNames.map(lambda agent: (agent,1))
sum_chats_agent = pairs_agent.reduceByKey(lambda a,b: a+b)
sorted_sum_chats = sum_chats_agent.sortBy(lambda x: x[1], ascending=False)
sorted_sum_chats.take(10)

sorted_sum_chats.map(lambda x: x[1]).mean()
accounts = chatsData.map(lambda chat: get_field(chat, ["accountNum", "category"]))

number_per_acc_and_cat = accounts.map(lambda acc: (acc,1)).reduceByKey(lambda a,b: a+b)
filtered_results = number_per_acc_and_cat.filter(lambda x: x[1]>1)
sorted_results = filtered_results.sortBy(lambda x: x[1], ascending=False)
sorted_results.take(10)

messages = chatsData.flatMap( lambda chat: get_field(chat, 'messages'))
messages.cache()
text_messages = messages.map(lambda message: message['text'])
text_messages.take(10)

filt_messages = text_messages.filter( lambda line: 'KBDOC' in line)
filt_messages.take(10)

def get_kbdoc_code(line):
        ind = line.index('KBDOC')
        return line[ind:ind+11]
kbdoc_codes = filt_messages.map(get_kbdoc_code)
kbdoc_codes.take(10)

sorted_sum_codes = kbdoc_codes.map(lambda x:(x,1)).reduceByKey(lambda
a,b:a+b).sortBy(lambda x:x[1], ascending=False)
sorted_sum_codes.take(10)

stopWords = ['a','my','to','is','the','it','for','what','should','on','do','me','by','get','too','how','the']
convs = chatsData.map( lambda chat: get_field(chat, 'messages'))
customerConvs = convs.map(lambda conv: [m['text'] for m in conv if m['sender'] == 'customer'][0])
customerConvs.take(10)

wordsCustomerConvs = customerConvs.flatMap(lambda m: m.split()).filter(lambda w: w.lower() not in stopWords)
countsWordsCustomer = wordsCustomerConvs.map(lambda w: (w,1)).reduceByKey(lambda a,b: a+b).sortBy(lambda x: x[1], ascending=False)
countsWordsCustomer.take(30)

countsWordsCustomer.saveAsTextFile('/Users/manuelramoslg/Diplomado-Big-Data-PUC/Spark/customerWordsConvs.txt')

# Ejecutar en la terminal
hdfs dfs -ls /user/cloudera/customerWordsConvs.txt
!hdfs dfs -ls /user/cloudera/customerWordsConvs.txt
countsWordsCustomer.coalesce(numPartitions=1).saveAsTextFile('/Users/manuelramoslg/Diplomado-Big-Data-PUC/Spark/customerWordsConvsAgg.txt')
